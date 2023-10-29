# 🌀 Setting Up Your Local Development Environment

This section will guide you through setting up your environment for local development.

## Prerequisites

Before proceeding, ensure your system meets the following requirements:

- **Python**: Version 3.8.1 or higher. [Download Python](https://www.python.org/)
- **Linux System** (Recommended): While not mandatory, using a Linux system or the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/fr-fr/windows/wsl/install) simplifies library installation.

## Dependency Installation

### System Libraries

Install the required system libraries using the command below:

```bash
sudo apt install libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
```

### Python Libraries

Install the necessary Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

> **Note**: If you need to add a new python extension for some reason, remember to update the [`.github/workflows/deploy.yml`](../workflows/deploy.yml) file.

## Useful Commands

### Running the Website Locally

To serve the website locally, use the following command:

```bash
mkdocs serve
```

> **Note**: If you wish to use a port other than the default `8000`, specify it using the `-a` option:

```bash
mkdocs serve -a localhost:8080
```
