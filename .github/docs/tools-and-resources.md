# Tools & Resources

This document provides a list of tools and resources to assist you in making high-quality contributions.

## Choose a reliable text editor

The tool you use to edit and create content is crucial. Choose one that suits your needs.

If you're unsure, consider using [Visual Studio Code](https://code.visualstudio.com/).

## Implement a linter

To minimize errors, consider using a linter specifically for `markdown` files, such as [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

> Note: The linter can utilize the `.markdownlint.json` file to observe any disabled or modified rules.

## Visual Studio Code extensions

Here's a curated list of useful extensions for [Visual Studio Code](https://code.visualstudio.com/):

- [Zensical Studio](https://marketplace.visualstudio.com/items?itemName=zensical.zensical-studio): A linter for Zensical markdown files and all kinds of necessary tools in one.
- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces): Highlights unnecessary spaces.
- [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml): Provides TOML file support.

When you first open the project in **VSC**, you will be prompted to install these extensions automaticlaly.

## Repository tools

The `tools` folder contains scripts that keep the content healthy:

- `tools/check_links.py` checks the built site for broken internal links, missing anchors and dead external URLs.
- `tools/normalize_links.py` rewrites relative links in the Markdown sources to file-relative paths, so they resolve the same way in every language.

Both are described in [Setting up your local development environment](setting-up-your-local-development-environment.md#checking-links).

## Useful Resources

Below are some resources that you might find useful for understanding the toolset:

- [Zensical](https://zensical.org/)
- [Zensical documentation](https://zensical.org/docs/)
- [zensical-i18n](https://github.com/hsandmann/zensical-i18n)
- [Markdown Guide](https://www.markdownguide.org/)
- [Markdown Rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md)
