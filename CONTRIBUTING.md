# Contributing to Gillian's GTA IV Modding Guide

First and foremost, thank you for considering a contribution to Gillian's GTA IV Modding Guide! Your knowledge, expertise, and dedication will help us enhance this guide, benefiting the entire modding community.

## Getting Started

Before diving in, here's a summary of what you should know:

### Table of Contents

- [Reporting bugs and issues](#reporting-bugs-and-issues)
- [Suggesting enhancements](#suggesting-enhancements)
- To contribute yourself, refer to:
    - [Coding style guide](#coding-style-guide)
    - [Pull Request process](#pull-request-process)
    - [Setting up your local development environment](.github/docs/setting-up-your-local-development-environment.md)
    - [Tools & Resources](.github/docs/tools-and-resources.md)

---

## Reporting bugs and Issues

If you've identified a bug or issue:

1. **Check existing issues**: Before creating a new issue, please check [existing issues](https://github.com/gillian-guide/gillian-guide.github.io/issues) to avoid duplicates. Also, check if it was reported on the [Discord server](https://discord.gg/zwmsQqExbQ).
2. **Create a new issue**: If your issue hasn't been reported, open a [new issue on GitHub](https://github.com/gillian-guide/gillian-guide.github.io/issues/new) or create a ticket on the [Discord server](https://discord.gg/zwmsQqExbQ), providing as much detail as possible.

## Suggesting enhancements

I'm always looking for ways to improve the guide. If you have a suggestion:

1. **Suggest it on the Discord server**: Share your ideas on the [Discord server](https://discord.gg/zwmsQqExbQ).
2. **Provide Details**: Ensure your proposal is detailed, explaining both the benefits and any potential challenges.

## Coding style guide

This project uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), a framework that converts `markdown` files into a static documentation website. Learn more about [markdown](https://www.markdownguide.org/).

For clarity, adhere to the default [markdown rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md). The [Tools & Resources](.github/docs/tools-and-resources.md) can assist you.

- Some of these rules can be bypassed in the `.markdownlint.json` file, but only when absolutely necessary. Here is the complete list of currently changed rules:
    - [MD007 - Unordered list indentation](https://github.com/DavidAnson/markdownlint/blob/main/doc/md007.md): Changed to 4 due to Material requiring it for some styling.
    - [MD013 - Line length](https://github.com/DavidAnson/markdownlint/blob/main/doc/md013.md): Disabled due to Material handling it automatically.
    - [MD033 - Inline HTML](https://github.com/DavidAnson/markdownlint/blob/main/doc/md033.md): `<div>` was allowed due to Material requiring divs for grid cards. `<br>` is allowed to occasionally requiring to force a newline without creating spacing. `<a>` is allowed for the `README.md`. `<h2>` and `<h3>` are allowed to be able to create a header without it appearing in the table of contents. `<iframe>` is allowed for YouTube embeds.
    - [MD041 - First line in a file should be a top-level heading](https://github.com/DavidAnson/markdownlint/blob/main/doc/md041.md): Disabled due to Material requiring the title and description be the top item in the file.
    - [MD046 - Code block style](https://github.com/DavidAnson/markdownlint/blob/main/doc/md046.md): Disabled due to using fenced, but it occasionally treats Material snippets as a codeblock.

Furthermore, this project also uses [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n/) for multi-language support. All the suggested changes must include a Russian version of the page alongside the English one. If you're unable to translate the page yourself, create a Draft Pull Request and request for somebody else to translate your page.

- If you wish to add a new language, create a new folder with your language code, copy the files from the other folders, translate *all* the `markdown` files and follow the documentation on the i18n repository.

## Pull Request process

If you're ready to contribute:

1. **Fork & Clone**: Fork the repository and clone it to your local machine.
2. **Branch**: Always create and work in a new branch, naming it appropriately.
3. **Commit & Push**: Commit your changes and push them to your fork.
4. **Open a Pull Request**: Return to this repository and create a new pull request, detailing your changes and motivations.

---

Thank you once again for your interest in contributing! Together, we can make Gillian's GTA IV Modding Guide the premier resource for the community.
