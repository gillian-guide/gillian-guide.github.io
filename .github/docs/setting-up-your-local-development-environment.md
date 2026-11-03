# Setting up your local development environment

This section will guide you through setting up your environment for local development.

## Prerequisites

Before proceeding, ensure your system meets the following requirements:

- **Python**: Version 3.11 or higher. [Download Python](https://www.python.org/)
- **Linux System** (Recommended): While not mandatory, using a Linux system or the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) simplifies installation and allows for easier previews.

## Dependency Installation

The website is built with [Zensical](https://zensical.org/), together with [zensical-i18n](https://github.com/hsandmann/zensical-i18n) for the English/Russian localization. Both are Python packages, so no additional system libraries are required.

### Python

1. Create a Python virtual environment:
    1. In an empty folder, create a new virtual environment:`python -m venv \path\to\new\virtual\environment`
    2. Activate the virtual environment:
        - **Windows**: `path\to\venv\Scripts\activate.bat`.
        - **Linux**: `source path\to\venv\bin\activate`.
2. Install the necessary Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

> **Note**: If you need to add a new Python package for some reason, remember to update the [`.github/workflows/deploy.yml`](../workflows/deploy.yml) file.

## Useful Commands

### Running the website locally

The site is built by the `zensical-i18n` wrapper, which builds every language. To serve the website locally, use one of the following commands:

```bash
# Serve the English (default) version
zensical-i18n serve

# Serve the Russian version
zensical-i18n serve --lang ru
```

> **Note**: If you wish to use a port or IP other than the default, specify it using the `-a` option:

```bash
zensical-i18n serve -a ip:port
```

> **Note for Windows users**: `zensical-i18n` currently fails on Windows with `invariant: Id(Format(Path(Backslash)))`, because Zensical rejects the `docs_dir` that the wrapper generates from a Windows path. Build and preview from WSL instead.

### Building the website

To build the static website into the `site` folder, use the following command:

```bash
zensical-i18n build
```

English is written to the root of the `site` folder, Russian to `site/ru`. To rebuild a single language while leaving the others untouched, pass `--lang`:

```bash
zensical-i18n build --lang ru
```

### Checking links

Build the website first, then run the link checker against the generated files:

```bash
# Internal links, anchors and assets
python tools/check_links.py

# Additionally probe every external http(s) link
python tools/check_links.py --external
```

The checker splits its findings into **broken** links, which fail the run, and links it **could not verify** — `401`, `403` and `429` answers, timeouts, DNS and TLS errors. Those say nothing about the link itself, so they are reported but never fail the run.

The [links workflow](../workflows/links.yml) runs the internal check on every push and the external probe weekly. It writes both reports into the job summary and, when it finds broken links, opens — or comments on — the "Broken links found by the links workflow" issue, so the result is visible without a red build.

> **Note**: The guide links between pages with paths relative to the Markdown file, not to the URL of the page. A root-level page links `resources/credits.md`, a page in `resources/` links `../extras/modloading.md`. Writing URL-relative paths (`../../foo.md`) works on the English site because the browser clamps excess `..` segments, but escapes into English from `/ru/`. `tools/normalize_links.py` rewrites such links to their file-relative form:

```bash
python tools/normalize_links.py --dry-run   # review the changes
python tools/normalize_links.py             # apply them
```

### Filtering instant previews

Instant previews are enabled by a Markdown extension, which marks every internal link that matches its `targets`. The theme reveals a preview after a short delay; the delay is set in CSS in [`extra.css`](../../docs/assets/stylesheets/extra.css), so adjust it there if previews feel too eager or too slow.
