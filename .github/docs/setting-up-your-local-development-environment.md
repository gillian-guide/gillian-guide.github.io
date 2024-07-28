# Setting up your local development environment

This section will guide you through setting up your environment for local development.

## Prerequisites

Before proceeding, ensure your system meets the following requirements:

- **Python**: Version 3.8.1 or higher. [Download Python](https://www.python.org/)
- **Linux System** (Recommended): While not mandatory, using a Linux system or the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/fr-fr/windows/wsl/install) simplifies library installation and allows for easier previews.

## Dependency Installation

### System Libraries

Install the required system libraries using the command below:

```bash
sudo apt install libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
```

> **Note**: If not using a Debian-based system, similar packages should be available on other package managers (such as `pacman`) aswell.

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

> **Note**: If you need to add a new python extension for some reason, remember to update the [`.github/workflows/deploy.yml`](../workflows/deploy.yml) file.

## Useful Commands

### Running the website locally

To serve the website locally, use the following command:

```bash
mkdocs serve
```

> **Note**: If you wish to use a port or IP other than the default, specify it using the `-a` option:

```bash
mkdocs serve -a ip:port
```

### Building the website

To build a static website, use the following command:

```bash
mkdocs build
```
