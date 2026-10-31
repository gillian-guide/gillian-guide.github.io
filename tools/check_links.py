#!/usr/bin/env python3
"""Check the links of the built site.

Zensical validates the links it can resolve while building, but it cannot see
the generated output, it does not verify anchors of pages that are assembled
from multiple languages, and it never touches external URLs. This script walks
the generated HTML and verifies:

* internal links, including directory URLs (``/foo/`` -> ``foo/index.html``),
* anchors (``/foo/#bar`` -> ``id="bar"`` on the target page),
* assets referenced from ``href``/``src`` attributes,
* optionally, external ``http(s)`` links (``--external``).

Run it after ``zensical-i18n build``::

    python tools/check_links.py
    python tools/check_links.py --external
    python tools/check_links.py --only-external --external

Exits non-zero when a problem is found, so it can run in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

# Attributes that point at another document or asset
LINK_ATTRIBUTES = frozenset({"href", "src"})

# Schemes that are not links to check
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:", "irc:", "magnet:")

# Status codes that mean "the server refused to talk to a bot", not "gone"
SOFT_STATUS = frozenset({401, 403, 429})

USER_AGENT = "gillian-guide-link-check/1.0 (+https://gillian-guide.github.io/)"

ID_RE = re.compile(
    rb"""\s(?:id|name)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"']+))"""
)


@dataclass
class Reference:
    """A link found in a page of the site."""

    page: Path
    attribute: str
    url: str
    line: int


@dataclass
class Report:
    """Collected findings of a check."""

    internal_checked: int = 0
    external_checked: int = 0
    broken: list[tuple[Reference, str]] = field(default_factory=list)
    external_failed: dict[str, list[tuple[Reference, str]]] = field(
        default_factory=dict
    )
    external_blocked: dict[str, list[tuple[Reference, str]]] = field(
        default_factory=dict
    )


# ``rel`` values of <link> elements that do not point at a fetcheable resource
SKIP_REL = frozenset({
    "canonical", "alternate", "author", "license", "next", "prev", "me",
    "dns-prefetch", "preconnect", "search", "sitemap",
})


class Extractor(HTMLParser):
    """Collect ``href`` and ``src`` attributes with their line numbers."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.found: list[tuple[str, str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: (value or "").strip() for name, value in attrs}
        if tag == "link":
            rel = values.get("rel", "").lower()
            if rel in SKIP_REL:
                return
        for name in LINK_ATTRIBUTES:
            value = values.get(name)
            if value:
                self.found.append((name, value, self.getpos()[0]))

    handle_startendtag = handle_starttag


def read_ids(path: Path) -> set[str]:
    """Return the anchor targets of an HTML file."""
    try:
        data = path.read_bytes()
    except OSError:
        return set()
    found = set()
    for match in ID_RE.finditer(data):
        value = next(group for group in match.groups() if group is not None)
        found.add(value.decode("utf-8", "replace"))
    return found


def public_path(page: Path, site: Path) -> str:
    """Return the URL path a page is served at."""
    relative = page.relative_to(site).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def resolve_file(site: Path, path: str) -> Path | None:
    """Map a URL path of the site to the file that serves it."""
    relative = path.lstrip("/")
    if relative.endswith("/") or not relative:
        candidate = site / relative / "index.html"
        return candidate if candidate.is_file() else None
    direct = site / relative
    if direct.is_file():
        return direct
    if (with_suffix := site / (relative + ".html")).is_file():
        return with_suffix
    nested = site / relative / "index.html"
    if nested.is_file():
        return nested
    return None


def split_url(url: str) -> tuple[str, str]:
    """Return path and fragment of a URL, percent-decoded."""
    path, _, fragment = url.partition("#")
    path = path.partition("?")[0]
    return urllib.parse.unquote(path), urllib.parse.unquote(fragment)


def check_internal(ref: Reference, site: Path, ids: dict[Path, set[str]],
                   report: Report) -> None:
    """Check a single reference that points into the site."""
    page_path = public_path(ref.page, site)
    target = urllib.parse.urljoin(page_path, ref.url)
    parsed = urllib.parse.urlsplit(target)
    path, anchor = split_url(parsed.path + ("#" + parsed.fragment if parsed.fragment else ""))
    report.internal_checked += 1

    if not path:
        path = page_path

    resolved = resolve_file(site, path)
    if resolved is None:
        report.broken.append((ref, f"target not found: {parsed.path or path}"))
        return

    if not anchor or resolved.suffix != ".html":
        return

    if resolved not in ids:
        ids[resolved] = read_ids(resolved)
    if anchor not in ids[resolved]:
        report.broken.append(
            (ref, f"missing anchor #{anchor} in {resolved.relative_to(site).as_posix()}")
        )


def fetch(url: str, timeout: float) -> tuple[int | None, str]:
    """Request a URL, returning its status code and an error message."""
    request = urllib.request.Request(url, method="GET", headers={
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    })
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, ""
    except urllib.error.HTTPError as error:
        return error.code, error.reason or ""
    except Exception as error:  # noqa: BLE001 - report, never crash the run
        return None, str(error)


def check_external(refs: list[Reference], timeout: float, workers: int,
                   report: Report) -> None:
    """Check every external URL once, remembering the pages that use it."""
    by_url: dict[str, list[Reference]] = {}
    for ref in refs:
        by_url.setdefault(ref.url, []).append(ref)

    def run(url: str) -> tuple[str, int | None, str]:
        return (url, *fetch(url, timeout))

    with ThreadPoolExecutor(max_workers=workers) as pool:
        for url, status, message in pool.map(run, sorted(by_url)):
            report.external_checked += 1
            pages = by_url[url]
            if status is not None and 200 <= status < 400:
                continue
            entry = (f"HTTP {status}" if status else message, pages)
            if status in SOFT_STATUS:
                report.external_blocked[url] = [(p, entry[0]) for p in pages]
            else:
                report.external_failed[url] = [(p, entry[0]) for p in pages]


def iter_pages(site: Path) -> list[Path]:
    """Return every HTML file of the site."""
    return sorted(site.rglob("*.html"))


def relative(ref: Reference, site: Path) -> str:
    """Short page name for the report."""
    return ref.page.relative_to(site).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--site", type=Path, default=Path("site"),
                        help="directory with the built site (default: site)")
    parser.add_argument("--external", action="store_true",
                        help="also check external http(s) links")
    parser.add_argument("--only-external", action="store_true",
                        help="skip internal checks, implies --external")
    parser.add_argument("--timeout", type=float, default=15.0,
                        help="timeout of a single external request in seconds")
    parser.add_argument("--workers", type=int, default=8,
                        help="concurrent external requests (default: 8)")
    parser.add_argument("--ignore", type=Path, action="append", default=[],
                        help="file with URLs to ignore, one per line")
    parser.add_argument("--max-report", type=int, default=50,
                        help="maximum entries per section (default: 50)")
    args = parser.parse_args()

    site: Path = args.site
    if not site.is_dir():
        print(f"error: no built site at {site} - run zensical-i18n build first",
              file=sys.stderr)
        return 2

    ignored = set()
    for path in args.ignore:
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ignored.add(line)

    report = Report()
    ids: dict[Path, set[str]] = {}
    external: list[Reference] = []

    pages = iter_pages(site)
    for page in pages:
        extractor = Extractor()
        try:
            extractor.feed(page.read_text(encoding="utf-8", errors="replace"))
        except Exception as error:  # noqa: BLE001 - malformed page is worth reporting
            report.broken.append(
                (Reference(page, "html", "", 0), f"could not parse: {error}")
            )
            continue

        for attribute, value, line in extractor.found:
            if value.startswith(SKIP_SCHEMES) or value.startswith("#"):
                if value.startswith("#") and value != "#":
                    ref = Reference(page, attribute, value, line)
                    if not args.only_external:
                        check_internal(ref, site, ids, report)
                continue
            if any(value.startswith(scheme) for scheme in ignored):
                continue
            scheme = urllib.parse.urlsplit(value).scheme
            if value.startswith("//"):
                external.append(Reference(page, attribute, "https:" + value, line))
            elif scheme in ("http", "https"):
                external.append(Reference(page, attribute, value, line))
            elif not scheme and not args.only_external:
                check_internal(Reference(page, attribute, value, line),
                               site, ids, report)

    if args.external or args.only_external:
        check_external(external, args.timeout, args.workers, report)

    show = args.max_report

    if not args.only_external:
        print(f"internal: {report.internal_checked} references in {len(pages)} pages")
        if report.broken:
            print(f"  {len(report.broken)} broken:")
            for ref, reason in report.broken[:show]:
                print(f"    {relative(ref, site)}:{ref.line}  {ref.url}  ({reason})")
            if len(report.broken) > show:
                print(f"    ... and {len(report.broken) - show} more")

    if args.external or args.only_external:
        print(f"external: {report.external_checked} unique URLs")
        for label, entries in (("failing", report.external_failed),
                               ("blocked (not counted as broken)",
                                report.external_blocked)):
            if not entries:
                continue
            print(f"  {len(entries)} {label}:")
            for url, pages_used in list(entries.items())[:show]:
                status = pages_used[0][1]
                where = pages_used[0][0]
                print(f"    {status}  {url}")
                print(f"      from {relative(where, site)}"
                      + (f" (+{len(pages_used) - 1} more pages)"
                         if len(pages_used) > 1 else ""))
            if len(entries) > show:
                print(f"    ... and {len(entries) - show} more")

    failed = bool(report.broken) or bool(report.external_failed)
    print("result:", "FAILED" if failed else "ok")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
