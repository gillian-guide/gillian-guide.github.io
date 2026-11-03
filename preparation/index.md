# Preparation

To mod the game, we first need to get your system ready for modding and install the game. We will also go over basic instructions, terminology and mod dependencies you may need later.

---

## Enabling File Extensions

Not seeing file extensions can cause some confusion when looking at all the files you need to use when modding. File extensions are not turned on by default in Windows, so if you haven't turned them on yet - do it now:

1. Open **File Explorer**
2. Select the **View** tab at the top
3. Hover the mouse over **Show** section and enable **File name extensions** from the submenu. [![File name extensions in Explorer](<https://gillian-guide.github.io/assets/fileextensions.webp>)](<https://gillian-guide.github.io/assets/fileextensions.webp>)

---

## Software

Some software should be installed before you can play and mod the game:

- You need to have an archivator installed. I recommend **[NanaZip](<https://apps.microsoft.com/detail/9n8g7tscl18r?rtc=1&amp;hl=en-us&amp;gl=us>)** or **[7-Zip](<https://www.7-zip.org>)**.
- [Microsoft Visual C++ Redistributables](<https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/>) (extract the archive and run `install_all.bat`).
- [Microsoft DirectX 9 (June 2010)](<https://www.microsoft.com/en-us/download/details.aspx?id=8109>).

---

## Drivers

It is highly recommended to have latest drivers installed for best performance and stability. Select your GPU vendor on the selector for instructions.

- Go to the [official website](<https://www.nvidia.com/en-us/software/nvidia-app/>).
- Press `Download Now` and open the downloaded executable.
- In the app, go to the `Drivers` tab.
- Press `Download` in top right, then `Install`.
- Follow the in-app instructions to install the driver.

  - Use `Express Installation` unless you have your own specifics.

- Go to the [official website](<https://www.amd.com/en/support>).
- Press `Download Windows Drivers` and open the downloaded executable.
- Follow the in-app instructions to install the driver.

  - Select `Optional` drivers over `Recommended` to get the latest drivers.
  - Select `Minimal Install` over `Full Install` if you don't need the extra features of the Adrenalin app.

- Go to the [official website](<https://www.intel.com/content/www/us/en/support/detect.html>).
- Press `Download now` and open the downloaded executable.
- Follow the displayed instructions to install the drivers. Ignore warnings about OEM drivers.

---

## Terminology and tips

- **Game**, **Installation** or **Root folder** typically refers to the location where `GTAIV.exe` is located, which is at:

  - **Steam**: <mark>Steam\steamapps\common\Grand Theft Auto IV\GTAIV</mark>
  - **Rockstar Games Launcher**: <mark>Rockstar Games\Grand Theft Auto IV</mark>
- **When told to extract a folder**, extract the folder itself, not the contents (unless told otherwise).
- **GFWL** is an abbreviation for **Games for Windows LIVE**. GFWL is a proprietary service made by Microsoft, which allows for multiplayer and DRM protection. **XLiveless** (sometimes known as `xlive.dll`) removes GFWL. GFWL is not used in Complete Edition, thus it always means a downgraded version.

---

## Modding the game

> [!WARNING]
>
> **Game installation**
>
> - **If you had previously modded the game or installed a modpack, it is highly recommended that you first uninstall the game from your launcher, then delete any leftovers that stayed in the root folder, as launchers don't remove those.**
> - **The game should not be located in `Desktop` or `Documents` or other default system folders to avoid issues.** If not using Steam, it should also not be located in <mark>C:\Program Files</mark> or <mark>C:\Program Files (x86)</mark>.

I recommend opening the [troubleshooting](<https://gillian-guide.github.io/resources/troubleshooting/index.md>) page on a separate tab to consult during the guide if you encounter issues.

If the above is met, continue with one of the following pages:

- If you have **no need for the in-depth guides and only want the best singleplayer-only campaign experience:**
- If you wish to go through the guide **step-by-step** yourself, start with downgrading:
