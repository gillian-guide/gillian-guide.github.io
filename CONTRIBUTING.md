# 📖 Contributing to Gillian's GTA IV Modding Guide

First and foremost, thank you for considering a contribution to Gillian's GTA IV Modding Guide! 🎉 Your knowledge, expertise, and dedication will help us enhance this guide, benefiting the entire modding community.

## 🚀 Getting Started

Before diving in, here's a summary of what you should know:

### Table of Contents

- [🐛 Reporting Bugs and Issues](#-reporting-bugs-and-issues)
- [✨ Suggesting Enhancements](#-suggesting-enhancements)
- To start developing this guide, refer to:
  - [📜 Coding Style Guide](#-coding-style-guide)
  - [🌍 Pull Request Process](#-pull-request-process)
  - [🌀 Setting Up Your Local Development Environment](.github/docs/setting-up-your-local-development-environment.md)
  - [🔧 Tools & Resources](.github/docs/tools-and-resources.md)

---

## 🐛 Reporting Bugs and Issues

If you've identified a bug or issue:

1. **Check Existing Issues**: Before creating a new issue, please check [existing issues](https://github.com/gillian-guide/gillian-guide.github.io/issues) to avoid duplicates. Also, check on the [Discord server](https://discord.gg/zwmsQqExbQ), and don't forget to consult the [Troubleshooting page](https://gillian-guide.github.io/troubleshooting/) beforehand.
2. **Create a New Issue**: If your bug hasn't been reported, open a [new issue on GitHub](https://github.com/gillian-guide/gillian-guide.github.io/issues/new) or create a ticket on the [Discord server](https://discord.gg/zwmsQqExbQ), providing as much detail as possible.

## ✨ Suggesting Enhancements

We are always looking for ways to improve. If you have a suggestion:

1. **Open a Discussion or Issue**: Share your ideas on the [Discord server](https://discord.gg/zwmsQqExbQ).
2. **Provide Details**: Ensure your proposal is detailed, explaining both the benefits and any potential challenges.

## 📜 Coding Style Guide

This project uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), a framework that converts `markdown` files into a static documentation website. Learn more about [markdown](https://www.markdownguide.org/).

For clarity, adhere to the default [markdown rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md). The [🔧 Tools & Resources](.github/docs/tools-and-resources.md) can assist you.

- Some of these rules can be bypassed in the `.markdownlint.json` file, but only when absolutely necessary. Here is the complete list of currently disabled rules:
  - [MD013 - Line length](https://github.com/DavidAnson/markdownlint/blob/main/doc/md013.md)
  - [MD033 - Inline HTML](https://github.com/DavidAnson/markdownlint/blob/main/doc/md033.md#md033---inline-html)
- When including an emoji in a title, you might encounter the [MD051 - Link fragments should be valid](https://github.com/DavidAnson/markdownlint/blob/main/doc/md051.md#md051---link-fragments-should-be-valid) error. To resolve this, simply exclude the emoji from your link. For example: `#-my-car` would target `🚗 My Car`.

Furthermore, this project also uses [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n/) for multi-language support. All the suggested changes must include a Russian version of the page alongside the English one (by creating `file.en.md` and a `file.ru.md` together). If you're unable to translate the page yourself, create a Draft Pull Request and request for somebody else to translate your page.
- If you wish to add a new language, translate *all* the `markdown` files and follow the documentation on the i18n repository. However, please, before that, create a Pull Request converting the suffix docs structure to the [folder docs structure](https://ultrabug.github.io/mkdocs-static-i18n/getting-started/quick-start/#the-folder-docs-structure).

## 🌍 Pull Request Process

If you're ready to contribute:

1. **Fork & Clone**: Fork the repository and clone it to your local machine.
2. **Branch**: Always create and work in a new branch, naming it appropriately.
3. **Commit & Push**: Commit your changes and push them to your fork.
4. **Open a Pull Request**: Return to this repository and create a new pull request, detailing your changes and motivations.

---

Thank you once again for your interest in contributing! Together, we can make Gillian's GTA IV Modding Guide the premier resource for the community.
