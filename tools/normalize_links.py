#!/usr/bin/env python3
"""Rewrite relative links in the Markdown sources so they are file-relative.

Zensical resolves a relative link against the file that contains it, and then
emits the URL relative to the page, which adds one level because of the
trailing slash of directory URLs. Several pages of this guide were written
against the URL instead of the file - a root-level page linking ``../foo.md``
instead of ``foo.md`` - which works on the English site only because the
browser clamps excess ``..`` segments at the site root. Under ``/ru/`` the same
link escapes the language and silently drops readers into English.

This script rewrites every relative link to the shortest path from its own
file, which is what Zensical validates and what renders correctly in every
language. Links that cannot be resolved are reported and left alone.

Usage::

    python tools/normalize_links.py --dry-run   # show what would change
    python tools/normalize_links.py             # rewrite the sources
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from pathlib import Path

# Markdown links and images: [text](target) and ![alt](target)
LINK_RE = re.compile(r"(\]\(\s*)([^)\s]+)")

# Target schemes and prefixes that are never rewritten
SKIP_PREFIX = ("http://", "https://", "//", "#", "mailto:", "tel:", "data:")


def split_target(target: str) -> tuple[str, str]:
    """Split a link target into path and the ``#anchor`` suffix."""
    path, sep, fragment = target.partition("#")
    return path, (sep + fragment)


def resolve(relative_file: str, path: str) -> str | None:
    """Resolve a link path against a file, clamping at the language root."""
    parts: list[str] = []
    for segment in (posixpath.dirname(relative_file) + "/" + path).split("/"):
        if segment in ("", "."):
            continue
        if segment == "..":
            if parts:
                parts.pop()
            # A missing parent means the link climbs above the docs directory;
            # clamp it, which is what the browser does at the site root too.
            continue
        parts.append(segment)
    return "/".join(parts) if parts else None


def target_exists(resolved: str, docs: Path, language: Path, default: Path) -> bool:
    """Whether a resolved path exists in the language, fallback or shared tree."""
    candidates = [resolved, resolved + ".md", resolved.rstrip("/") + "/index.md"]
    for base in (language, default, docs):
        for candidate in candidates:
            if (base / candidate).exists():
                return True
    return False


def rewrite_file(path: Path, root: Path, docs: Path, default: Path,
                 dry_run: bool) -> list[str]:
    """Rewrite the relative links of one file, returning the changes made."""
    relative = path.relative_to(root).as_posix()
    with path.open(encoding="utf-8", newline="") as handle:
        text = handle.read()
    changes: list[str] = []
    in_fence = False
    output: list[str] = []

    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence or "](" not in line:
            output.append(line)
            continue

        def replace(match: re.Match[str]) -> str:
            target = match.group(2)
            if target.startswith(SKIP_PREFIX) or target.startswith("{"):
                return match.group(0)
            if target.startswith("/"):
                changes.append(f"{relative}: absolute link left as is: {target}")
                return match.group(0)
            link_path, suffix = split_target(target)
            if not link_path:
                return match.group(0)
            resolved = resolve(relative, link_path)
            if resolved is None:
                changes.append(f"{relative}: cannot resolve: {target}")
                return match.group(0)
            if not target_exists(resolved, docs, root, default):
                changes.append(f"{relative}: missing target: {target}")
                return match.group(0)
            new_path = posixpath.relpath(resolved, posixpath.dirname(relative) or ".")
            if new_path == link_path:
                return match.group(0)
            changes.append(f"{relative}: {link_path} -> {new_path}")
            return match.group(1) + new_path + suffix

        output.append(LINK_RE.sub(replace, line))

    if not dry_run and any(" -> " in change for change in changes):
        path.write_text("\n".join(output), encoding="utf-8", newline="")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--docs", type=Path, default=Path("docs"),
                        help="documentation directory (default: docs)")
    parser.add_argument("--dry-run", action="store_true",
                        help="report the changes without writing files")
    args = parser.parse_args()

    problems = 0
    rewrites = 0
    default = args.docs / "en"
    if not default.is_dir():
        default = next(p for p in sorted(args.docs.iterdir()) if p.is_dir())
    for root in sorted(p for p in args.docs.iterdir() if p.is_dir()):
        for page in sorted(root.rglob("*.md")):
            for change in rewrite_file(page, root, args.docs, default, args.dry_run):
                print(change)
                if " -> " in change:
                    rewrites += 1
                else:
                    problems += 1

    verb = "would rewrite" if args.dry_run else "rewrote"
    print(f"\n{verb} {rewrites} links, {problems} problems left alone")
    return 0


if __name__ == "__main__":
    sys.exit(main())
