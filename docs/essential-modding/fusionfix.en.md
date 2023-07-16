title: FusionFix
description: One of the essential must-use mods for your GTA IV install
hide: footer

# FusionFix
!!! warning "Compatibility" 
    This mod is only officially supported on the Complete Edition, but thanks to the efforts of Zolika1351, you can also use it with the 1.0.8.0 and 1.0.7.0 patches. Alternatively, you can use the old version, which still supports the 1.0.8.0 and 1.0.7.0 patches.
This project aims to fix or address some issues in Grand Theft Auto IV. You can view the changelog [here](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/blob/master/readme.md).

## Installation
=== "1.0.8.0"
    === "Latest version"
        - Instructions:
            * Get latest [ZolikaPatch](ZolikaPatch.md) and [Ultimate ASI Loader](../ultimate-asi-loader.md).
            !!! note ""
                [Zolika1351's Downgrader](../downgrading/#zolika1351s-downgrader) already takes care of that.
            * Download FusionFix from optional mods [here](https://zolika1351.pages.dev/mods/ivpatch/downgrading).
            * Extract :material-zip-box:`FusionFix_1070-1080_New.zip` to your game folder.
    === "Legacy version"
        - Instructions:
            * Get [Release 1.10](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/tag/v1.10) of FusionFix.
            * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.zip` to your game folder.
=== "1.2.0.59"
    - Instructions
        * Go to the [Releases](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix) page.
        * Download the latest release.
        * Extract the :material-zip-box:`GTAIV.EFLC.FusionFix.zip` to your game folder.
!!! tip ""
    You can move files from :material-folder:==plugins== folder to the game folder for convenience.
## Configuration
!!! warning ""
    This list leans on the latest version of FusionFix. If you're using the Legacy or any other outdated version, you may lack some of these options.
Open :material-file-cog:`GTAIV.EFLC.FusionFix.ini` (by default located in :material-folder:==plugins==) and configure the file as needed.

??? abstract "List of options"
    !!! warning ""
        The options are either `0` for disabled and `1` for enabled unless stated otherwise.
    * `SkipIntro` allows to skip game's, normally unskippable, intro video. ==Default is `1`.==
    * `SkipMenu` allows to skip game's menu, loading into the savefile immediately upon launching the game. ==Default is `1`.==
    * `BorderlessWindowed` launches the game in Borderless Windowed mode in favor of Exclusive Fullscreen that the game uses by default (`-windowed` [launch option](../additional-setup/#launch-options) must be set for this to work). ==Default is `1`.==
    * `RecoilFix` enables recoil on keyboard, which is, due to an overlook, only present on gamepads. ==Default is `1`.==
    * `DefinitonFix` fixes blurness that appears from using the Definition [setting](../additional-setup/#optimal-game-settings). ==Default is `1`.==
    * `EmissiveShaderFix` fixes broken emissive shaders present in the PC port. ==Default is `1`.==
    * `AimingZoomFix` fixes reversed zooming control in TBoGT, aswell as remembering last zoom multiplier. The options are `0` for disabled, `1` for an xbox-like fix, `2` to also enable the fix in IV and TLAD, `-1` to disable the feature. ==Default is `1`.==
    * `FlickeringShadowsFix` disables player's shadow from headlights to avoid flickering shadows. ==Default is `1`.==
    * `ExtraDynamicShadows` allows to restore missing dynamic shadows, up to forcing all objects to emit a shadow. The options are `0` for disabled, `1` for restoring some missing ,shadows, `2` for adding vegetation shadows and `3` for forcing all shadows. ==Default is `1`.==
    * `DynamicShadowForTrees` makes tree shadows dynamic. ==Default is `0`.==
    * `FpsLimitPreset` controls the FPS limiter preset. Toggle from in-game settings' Screen tab instead - reccomended to limit to 60 FPS to avoid [timing-related issues](https://www.pcgamingwiki.com/wiki/Grand_Theft_Auto_IV#Timing-related_issues). ==Default is `0`.==
    * `FrameLimitType` controls the type of the framerate lock. The options are `1` for realtime lock (thread-lock) and `2` for accurate lock (sleep-yield) that uses less resources. ==Default is `2`.==
    * `FpsLimit` allows to set a custom framerate lock. Set your desired framerate as an option. To toggle it in-game, change the "FPS limiter" setting in Settings - Game to `Default`. ==Default is `0`.==
    * `CutsceneFpsLimit` allows to set a custom framerate lock for cutscenes. It's recommended to set this option to 32 - [read this issue](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/issues/58) for context. Do not set this option above 60 FPS to avoid zoom-ins. ==Default is `60`.==
    * `ScriptCutsceneFovLimit` allows to set a FOV limit for scripted cutscenes. This is needed due to cutscenes [changing the FOV based on your framerate](https://youtu.be/NzKw7ijHG10).  ==Default is `20`.==
    * `ScriptCutsceneFpsLimit` is a proper fix for the issue above (toggle the `ScriptCutsceneFovLimit` off) that locks the framerate instead. ==This option is hidden by default.==
    * `FXAA` allows to toggle [Shader Fixes](shader-fixes.md)' [FXAA](../additional-setup/#optimal-game-settings). This setting has an in-game toggle in Settings - Graphics. ==Default is `1`.==
    * `ConsoleGamma` allows to toggle [Shader Fixes](shader-fixes.md)' [Console-like gamma](assets/console-gamma.png) ==Default is `0`.==
    * `DefaultCameraAngleInTLAD` allows to force the original [IV camera angle](assets/enabled.png) in [TLAD](assets/disabled.png). ==Default is `0`.==
    * `PedDeathAnimFixFromTBoGT` enables an additional death animation when you perform a counter attack after a dodge. [Enabled](https://imgur.com/EYsiGPe) vs [Disabled](https://imgur.com/CR3LEdR). ==Default is `1`.== 
    * `DisableCameraCenteringInCover` allows to disable the camera centering when getting to a corner of covering. [Enabled](https://imgur.com/93CKToM) vs [Disabled](https://imgur.com/q6i6KOX). ==Default is `1`.== 
    * `MouseFix` removes the mouse deadzone. ==Default is `1`.== 
    * `ScreenFilter` changes the timecyc between Default, IV, TLAD and TBoGT. Use the in-game toggle in Settings - Screen instead. ==Default is `5`.== 
    * `VehicleBudget` allows to change the vehicle budget. This option comes from the integrated [RIL.Budgeted](https://gtaforums.com/topic/744584-reliv-rilbudgeted-population-budget-adjustertaxi-bug-fix/). Only change this option if you're encountering the [taxi bug](assets/taxi-bug.png). The value should be the size of your :material-file:`vehicles.img` file in bytes(e.g. 200000000). ==Default is `0`.==
    * `PedBudget` allows to change the ped budget. This option comes from the integrated [RIL.Budgeted](https://gtaforums.com/topic/744584-reliv-rilbudgeted-population-budget-adjustertaxi-bug-fix/). Only change this option if you're unable to encounter modded peds. ==This option is hidden by default.==