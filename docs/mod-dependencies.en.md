title: Mod Dependencies
description: How to set up mod dependencies for your GTA IV install.
hide: footer

Only install Ultimate ASI Loader if you're here for the first time.

# Ultimate ASI Loader
This tool is used to load `.asi` mods (one of the most common types of GTA IV mods) into your game. It's multipurpose and can be used for many other games, but we will use it for GTA IV.

!!! warning ""
    This tool is compatible with all versions.

    [FusionFix](essential-modding/fusionfix.md) already includes this tool.

???+ note "Installation"
    * Go to the [Releases](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases) page.
    * Download :material-zip-box:`Ultimate-ASI-Loader.zip`.
    ??? question "Why not :material-zip-box:`Ultimate-ASI-Loader_x64.zip`? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-zip-box:`Ultimate-ASI-Loader_x64.zip`.
    * Extract to the game folder.

??? tip "How to use .asi mods?"
    !!! warning ""
        Make sure your mod was built for Ultimate ASI Loader and not [ScriptHook](#scripthook) or [IV-SDK .NET](#iv-sdk-.net).
    
    Extract the mod to either the game folder or :material-folder:==plugins== - either will do.

??? tip "Getting rid of Games for Windows - LIVE (for retail patches)"
    This tool can be used to get rid of [GFWL](../multiplayer/#games-for-windows-live) if you're not interested in [multiplayer](multiplayer.md) and Xbox achievements. This will reduce the amount of hassle you have with your game.

    * Rename the :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll`

??? tip "Modloading"
    This tool can be used for modloading purposes. See [modloading](modloading.md).

# ScriptHook
!!! info ""
    Also known as ScriptHookDotNet and aru's ScriptHook.
!!! warning ""
    Compatible with all versions. See notes below.
This tool is used to run scripts written in any .NET language. Not to be confused with [IV-SDK .NET](#iv-sdk-.net). See your mod's requirements to see whether it was built for ScriptHook or [IV-SDK .NET](#iv-sdk-.net).

???+ note "Installation"
    * Go to [Releases](https://github.com/HazardX/gta4_scripthookdotnet/releases) and download the version for the patch you want.
    * Extract :material-zip-box:`scripthookdotnet_vx_x_x_xb.zip` to your game folder.
    !!! note "Compatibility with 1.0.8.0"
        You may want to use [this version](https://gtaforums.com/topic/946154-release-gtaiv-net-scripthook-v1718-support-for-gta-iv-1080-and-eflc-1130-by-arinc9-zolika1351/) instead for 1.0.8.0 compatibility.
    ??? note "Compatibility with Complete Edition"
        Add this [patch](https://www.lcpdfr.com/downloads/gta4mods/g17media/26726-compatibility-patch-for-gta-iv-complete-edition/) for Complete Edition compatibility ontop. This is limited and you may experience problems.
??? tip "How to use .NET scripts?"
    !!! warning ""
        Make sure that your mod is built for ScriptHook and not for [IV-SDK .NET](#iv-sdk-.net).

    Extract the mod into :material-folder:==scripts==.

# IV-SDK .NET
!!! warning ""
    Only compatible with 1.0.8.0 and 1.0.7.0.
This tool is used to run scripts written in any .NET language. Not to confuse with [ScriptHook](#scripthook). See your mod's requirements to see whether it was built for IV-SDK .NET or [ScriptHook](#scripthook).

???+ note "Installation"
    * Go to the [GTAForums page](https://gtaforums.com/topic/986510-iv-sdk-net/) and download latest version.
    * Extract :material-zip-box:`IV-SDK.NET.vx_x_x.zip` to your game folder. 
??? tip "How to use .NET scripts?"
    !!! warning ""
        Make sure your mod is built for IV-SDK .NET and not [ScriptHook](#scripthook).

    Extract the mod to :material-folder:==IVSDKDotNot\scripts==.

[:material-page-first:Previous page <br>Downgrading</br>](downgrading.md){ .md-button } [Next page:material-page-last: <br>Modloading</br>](modloading.md){ .md-button .md-button--primary }