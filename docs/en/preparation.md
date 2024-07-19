title: Preparation
description: Getting ready for playing and modding GTA IV

# Preparation

To mod the game, we first need to get your system ready for modding and install the game. We will also go over basic instructions, terminology and mod dependencies you may need later.

## Enabling File Extensions

Not seeing file extensions can cause some confusion when looking at all the files you need to use when modding. File extensions are not turned on by default in Windows, so if you haven't turned them on yet - do it now:

1. Open **File Explorer**
2. Select the **View** tab at the top
3. Hover the mouse over **Show** section and enable **File name extensions** from the submenu.
![File name extensions in Explorer](assets/fileextensions.webp){: style="height:60%;width:60%";}

## Software

Some software should be installed before you can play and mod the game:

- You need to have an archivator installed. I recommend **[NanaZip](https://apps.microsoft.com/detail/9n8g7tscl18r?rtc=1&hl=en-us&gl=us)** or **[7-Zip](https://www.7-zip.org/ "Official 7-Zip website")**.
- [Microsoft Visual C++ Redistributables](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/ "VC++ Runtimes All-in-One") (extract and run :material-file-download:`install_all.bat`).
- [Microsoft DirectX 9 (June 2010)](https://www.microsoft.com/en-us/download/details.aspx?id=8109 "Microsoft's official redistributables").

## Drivers

It is highly recommended to have latest drivers installed for best performance and stability. Select your GPU vendor on the selector for instructions.

!!! tip "Installing drivers"
    === "NVIDIA"
        - Go to the [official website](https://www.nvidia.com/en-us/software/nvidia-app/).
        - Press `Download Beta` and open the downloaded executable.
        - Follow the in-app instructions to install the driver.
    === "AMD"
        - Go to the [official website](https://www.amd.com/en/support).
        - Press `Download Windows Drivers` and open the downloaded executable.
        - Follow the in-app instructions to install the driver.
            - Select `Optional` drivers over `Recommended` to get the latest drivers.
            - Select `Minimal Install` over `Full Install` if you don't need the extra features of the Adrenaline app.
    === "Intel"
        - Go to the [official website](https://www.intel.com/content/www/us/en/support/detect.html).
        - Press `Download now` and open the downloaded executable.
        - Follow the displayed instructions to install the drivers. Ignore warnings about OEM drivers.

## Terminology

- **Game**, **Installation** or **Root folder** typically refers to the location where :material-file:`GTAIV.exe` is located, which is at:
    - :material-steam:**Steam**: :material-folder:==Steam\steamapps\common\Grand Theft Auto IV\GTAIV==
    - :simple-rockstargames: **Rockstar Games Launcher**: :material-folder:==Rockstar Games\Grand Theft Auto IV==
- **CE** or **Complete Edition** refers to the latest official version of the game, **1.2.0.59**.
- **Retail version** normally refers to a disc version of a game, but this guide is referring to the pre-CE version of the game, **1.0.8.0**.
- **EFLC** refers to the "Episodes from Liberty City".
- **UAL**, **ASI Loader**, :material-file:`dinput8.dll` typically refer to **Ultimate ASI Loader** which is used to load :material-file:`*.asi` mods.
- **GFWL** is an abbreviation for **Games for Windows Live**. GFWL is a proprietary service made by Microsoft, which allows for multiplayer and DRM protection. **XLiveless** (sometimes known as :material-file:`xlive.dll`) removes GFWL. GFWL is not used in CE.

## Game versions

There are many versions of the game - but for the purposes of the guide, we will only focus on the two most important ones:

### Complete Edition (1.2.0.59)

This is the latest version of the game, which you normally receive when installing the game on :material-steam:Steam or :simple-rockstargames: Rockstar Games Launcher. ==This version should be preferred if you want the **best singleplayer campaign experience.**==

??? quote "Pros and cons"
    !!! success ""
        :material-plus-box: It works out of the box. No modifications are required to launch the game.<br>
        :material-plus-box: Best support for modern mods made after 2020, such as FusionFix. This ensures getting the most fixes possible when modding.<br>
        :material-plus-box: Includes EFLC.<br>
        :material-plus-box: Supports Steam and Social Club Achievements out of the box.

    !!! danger ""
        :material-minus-box: Rockstar Games Launcher and it's DRM is required, which can be considered bloat for multiple reasons: the game launches for a minute longer and it does not provide anything but achievements to the game, to name two.<br>
        :material-minus-box: Compatibility with old mods is not guaranteed. While some mods work, there are some that do not. They are not critical to fixing the game, though.<br>
        :material-minus-box: Official multiplayer is removed and third-party experience is limited.<br>
        :material-minus-box: Some songs were removed from the radio due to licensing. They can be restored with mods.

### Retail version (1.0.8.0)

This is the version of the game that existed before the Complete Edition. ==This version should only be preferred if you want to **play the multiplayer**, use  **specific mods** you have in mind that don't support CE or want to **play without DRM.**== Instructions on how to downgrade to this version of the game will show up later.

??? quote "Pros and cons"
    !!! success ""
        :material-plus-box: Supports official multiplayer.<br>
        :material-plus-box: DRM can be removed, making this the only version capable of DRM-free play.<br>
        :material-plus-box: Best support for old mods made before 2020. If you don't know any yourself, don't consider this a point worth noting.<br>
        :material-plus-box: Supports a few more QoL mods Complete Edition doesn't, such as Liberty Tweaks.<br>
        :material-plus-box: Supports GFWL (Xbox Live) achievements, but at the cost of Steam Achievements.

    !!! danger ""
        :material-minus-box: Limited compatibility with FusionFix, which will reduce how many fixes you actually get.<br>
        :material-minus-box: To make multiplayer work, you have to set up GFWL, which is a lot of hassle. Although a third-party alternative exists.<br>
        :material-minus-box: EFLC support can only be achieved through mods.<br>
        :material-minus-box: Steam Achievements (which can only be achieved with mods) and GFWL achievements do not work at the same time. No support for Social Club achievements.<br>
        :material-minus-box: Some songs were removed from the radio due to licensing. They can be restored with mods.

## Modding the game

!!! warning ""
    **If you had previously modded the game or installed a modpack, it is highly recommended that you first uninstall the game from your launcher, then delete any leftovers that stayed in the root folder.**

    **The game should not be located in :material-folder:`Desktop` or :material-folder:`Documents` or other default system folders to avoid issues.** If not using :material-steam:Steam, it should also not be located in :material-folder:`C:\Program Files` or :material-folder:`C:\Program Files (x86)`.

<div class="grid cards" markdown>

- If you have **no need for the in-depth guides and only want the best singleplayer-only campaign experience:**

     [Next page:material-page-last: <br>Drag-and-Drop Archive</br>](drag-and-drop-archive.md){ .md-button .md-button--primary }

- If you wish to go through the guide **step-by-step** yourself, start with optimization:

     [Next page:material-page-last: <br>Optimization</br>](optimization.md){ .md-button .md-button--primary }

</div>
