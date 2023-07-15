title: Ultimate ASI Loader
description: How to set up Ultimate ASI Loader for your GTA IV install.
hide: footer

# Ultimate ASI Loader
This tool is used to load `.asi` mods (one of the most common types of GTA IV mods) into your game. It's multipurpose and can be used for many other games, but we're going to use it for GTA IV.

!!! warning ""
    [FusionFix](essential-modding/fusionfix.md) already includes this tool.

???+ note "Installation"
    * Go to the [Releases](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases) page.
    * Download :material-zip-box:`Ultimate-ASI-Loader.zip`.
    ??? question "Why not :material-zip-box:`Ultimate-ASI-Loader_x64.zip`? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-zip-box:`Ultimate-ASI-Loader_x64.zip`.
    * Extract to the game folder.

??? tip "Getting rid of Games for Windows - LIVE (for retail patches)"
    This tool can be used to get rid of [GFWL](../multiplayer/#games-for-windows-live) if you're not interested in [multiplayer](multiplayer.md) and Xbox achievements. This will reduce the amount of hassle you have with your game.

    * Rename the :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll`

??? tip "Modloading"
    This tool can be used for modloading purposes. See [modloading](modloading.md).

[:material-page-first:Previous page <br>Downgrading</br>](downgrading.md){ .md-button } [Next page:material-page-last: <br>Modloading</br>](modloading.md){ .md-button .md-button--primary }