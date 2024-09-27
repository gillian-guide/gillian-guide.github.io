title: Mod Dependencies
description: Why can't all the mods use UAL it would make everyone's life easier

# Mod Dependencies

---

## [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader)

 UAL is used to load `.asi` mods (one of the most common types of GTA IV mods) into the game. It's multipurpose and can be used for many other games, but we will use it for GTA IV.

!!! info "Compatibility"
    Ultimate ASI Loader is compatible with all game versions.

<h3>Installation</h3>

1. Go to the latest [release page](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases/latest).
2. Download :material-zip-box: `Ultimate-ASI-Loader.zip` (**not :material-zip-box:`Ultimate-ASI-Loader_x64.zip`**).
3. Extract the archive into the game folder.

!!! warning "If using Linux..."
    Add `WINEDLLOVERRIDES="dinput8=n,b" %command%` to your Launch options:

    - **:material-steam: Steam**: Right click the game in your library, press `Properties...` and paste the line in the `Launch options` field.
    - **:simple-rockstargames: Rockstar Games Launcher**: Open the game page in your library, open settings and paste the line in the `Launcher arguments` field.
    - **Windows shortcut**: Right click on the game shortcut, click `Properties` and paste the line in `Target` field.

!!! tip "Getting rid of Games for Windows - LIVE (for retail patches)"
    This tool can be used to get rid of GFWL if you're not interested in official [GFWL multiplayer](../../multiplayer.md/#games-for-windows-live) and Xbox Live achievements. This will reduce the amount of hassle and setup you have to do.

    - Rename the :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll`

!!! tip "Modloading"
    Ultimate ASI Loader can be used for modloading purposes. See [modloading](extras/modloading.md) for more details.

---

## [ScriptHookDotNet](https://github.com/HazardX/gta4_scripthookdotnet/)

!!! warning "Compatibility"
    - Compatible with all game versions.
    - See [Getting ScriptHookDotNet and IV-SDK .NET to work on Linux](#getting-scripthookdotnet-and-iv-sdk-net-to-work-on-linux) if running Linux.

ScriptHookDotNet is used to run scripts written in any .NET language. Not to be confused with [IV-SDK .NET](#iv-sdk-net).

<h3>Installation</h3>

=== "1.2.0.59"
    1. Go to the latest [release page](https://github.com/Tomasak/gta4_scripthookdotnet/releases).
    2. Download :material-zip-box:`scripthookdotnet_vx_x_x_x.zip`.
    3. Extract the archive into the game folder.
=== "1.0.8.0 to 1.0.5.0"
    1. Go to the [GTAForums page](https://gtaforums.com/topic/946154-release-gtaiv-net-scripthook-v1718-support-for-gta-iv-1080-and-eflc-1130-by-arinc9-zolika1351/).
    2. Click on **DOWNLOAD the GTAIV .Net Script Hook for GTA IV** to download the archive.
    3. Extract the :material-zip-box:`scripthookdotnet_v1_7_1_8.zip` archive into the game folder.
=== "1.0.4.0 to 1.0.1.0"
    1. Go to the [v1.7.1.7a release](https://github.com/HazardX/gta4_scripthookdotnet/releases/tag/v1.7.1.7a).
    2. Download :material-zip-box:`scripthookdotnet_v1_7_1_7a.zip`.
    3. Extract the archive into the game folder.

---

## [IV-SDK .NET](https://gtaforums.com/topic/986510-iv-sdk-net/)

!!! warning "Compatibility"
    - Only compatible with 1.0.8.0 and 1.0.7.0. [Downgrade](../downgrading/downgrading-the-game.md) if using Complete Edition.
    - See [Getting ScriptHookDotNet and IV-SDK .NET to work on Linux](#getting-scripthookdotnet-and-iv-sdk-net-to-work-on-linux) if running Linux.

IV-SDK .NET is used to run scripts written in any .NET language. Not to be confused with [ScriptHookDotNet](#scripthookdotnet).

<h3>Installation</h3>

1. Go to the latest [release page](https://github.com/ClonkAndre/IV-SDK-DotNet/releases/latest).
2. Download :material-zip-box:`IV-SDK.NET.vx_x_x.zip`.
3. Extract the archive into the game folder.

???+ tip "Clonk's Coding Library"
    Some mods may require extensions from [Clonk's Coding Library](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/).

    <h4>Installation</h4>

    * Go to the latest [release page](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/releases/latest).
    * Download :material-zip-box:`ClonkCodingLib.GTAIV.vx_x.zip`.
    * Extract the archive into the game folder.

---

## Getting ScriptHookDotNet and IV-SDK .NET to work on Linux

By default, neither of those two will run on Linux. That can be fixed, however. These instructions will assume you are an experienced Linux user, so if you don't get something - Google it.

<h3>Instructions</h3>

1. Set up Proton-GE.
2. Go to Proton-GE's gamefixes directory (location's different if using Flatpak):

    ```text
    ~/.local/share/Steam/compatibilitytools.d/GE-Proton9-10/protonfixes/gamefixes-steam/
    ```

3. Open `12210.py` in a text editor and add the following line at the end of the file:

    ```text
    util.protontricks('dotnet472')
    ```

4. Force the game to use Proton-GE.
5. Run the game and wait until .NET installs (may take from 5 to 30 minutes).
