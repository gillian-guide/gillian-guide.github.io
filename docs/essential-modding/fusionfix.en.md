title: FusionFix
description: One of the must-have mods for your GTA IV install

# FusionFix
!!! warning "Compatibility" 
    This mod is only officially supported on the Complete Edition, but thanks to the efforts of Zolika1351, you can also use it with the 1.0.8.0 and 1.0.7.0 patches.
This project aims to fix or address some issues in Grand Theft Auto IV. You can read the changelog [here](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/blob/master/readme.md). It also bundles [Shader Fixes](shader-fixes.md) along with toggles to enable/disable its [FXAA](../../additional-setup/#optimal-game-settings), [Console-like Gamma](assets/console-gamma.png) and Depth of Field.

## Installation { data-search-exclude }
=== "1.0.8.0"
    * Get the latest [ZolikaPatch](zolikapatch.md) and [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader).
    !!! note ""
        [Zolika1351's Downgrader](../../downgrading/#zolika1351s-downgrader) already takes care of that.
    * Download Zolika1351's fork of FusionFix [here](https://github.com/Zolika1351/GTAIV.EFLC.FusionFix/).
    * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.preCE.zip` into the game folder.
    !!! tip ""
        Optionally, if the official release is more up-to-date, you can update the files from the :material-folder:==update== - simply download the latest [release](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases) and extract only the :material-folder:==update==.
=== "1.2.0.59"
    * Go to the [Releases](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases) page.
    * Download the latest release.
    * Extract the :material-zip-box:`GTAIV.EFLC.FusionFix.zip` into the game folder.
!!! tip ""
    You can move files from the :material-folder:==plugins== to the game folder for convenience.
## Configuration
Open :material-file-cog:`GTAIV.EFLC.FusionFix.ini` (located in :material-folder:==plugins== by default) and configure the file as needed.

??? abstract "Full list of options"
    !!! warning ""
        This list is based on the latest version of FusionFix. If you're using the legacy or other outdated version, you may be missing some of these options.

        The options are either `0` for disabled and `1` for enabled unless otherwise noted.
    
    * `SkipIntro` allows to skip the game's normally unskippable intro video. This setting has an in-game toggle in Settings - Game. ==Default is `1`.==
    * `SkipMenu` allows to skip game's menu, loading into the savefile immediately upon launching the game. You can hold ++lshift++ to stop at the menu. This setting has an in-game toggle in Settings - Game. ==Default is `1`.==
    * `BorderlessWindowed` launches the game in Borderless Windowed mode instead of Exclusive Fullscreen, which the game uses by default (`-windowed` [launch option](../../additional-setup/#launch-options) must be set for this to work). This setting has an in-game toggle in Settings - Game. ==Default is `1`.==
    * `RecoilFix` enables weapon recoil on keyboard&mouse controls, which is only present on gamepads due to an oversight. ==Default is `1`.==
    * `DefinitonFix` fixes the behavior where the game ignores the Definition [setting](../../additional-setup/#optimal-game-settings) in cutscenes. ==Default is `1`.==
    * `EmissiveShaderFix` fixes broken emissive shaders present in the PC port. ==Default is `1`.==
    * `AimingZoomFix` fixes inverted zoom control in TBoGT and allows to remember last zoom multiplier. The options are `0` for disabled, `1` for an xbox-like fix, `2` to also enable the fix in IV and TLAD, `-1` to disable the feature. ==Default is `1`.==
    * `FlickeringShadowsFix` disables player's shadow from headlights to avoid flickering shadows. ==Default is `1`.==
    * `ExtraDynamicShadows` allows to restore missing dynamic shadows, up to forcing all objects to cast a shadow. The options are `0` for disabled, `1` for restoring some missing ,shadows, `2` for adding vegetation shadows and `3` for forcing all shadows. ==Default is `1`.==
    * `DynamicShadowForTrees` makes tree shadows dynamic. ==Default is `1`.==
    * `FpsLimitPreset` controls the FPS limiter preset. Toggle from the in-game Settings - Display tab instead - recommended to limit to 60 FPS to avoid [timing-related issues](https://www.pcgamingwiki.com/wiki/Grand_Theft_Auto_IV#Timing-related_issues). ==Default is `0`.==
    * `FrameLimitType` controls the type of the framerate lock. The options are `1` for a real-time lock (thread-lock) and `2` for an accurate lock (sleep-yield) that uses less resources. ==Default is `2`.==
    * `FpsLimit` allows you to set a custom framerate lock. Set your desired framerate as an option. To toggle it in-game, change the "FPS limiter" setting in Settings - Display to `Default`. ==Default is `0`.==
    * `CutsceneFpsLimit` allows you to set a custom framerate lock for cutscenes. It's recommended to set this option to 32 - [read this issue](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/issues/58) for context. Do not set this option above 60 FPS to avoid zoom-ins. ==Default is `60`.==
    * `ScriptCutsceneFovLimit` allows you to set a FOV limit for scripted cutscenes. This is needed because scripted cutscenes [changing the FOV based on your framerate](https://youtu.be/NzKw7ijHG10). ==Default is `20`.==
    * `ScriptCutsceneFpsLimit` is a proper fix for the issue above (toggle the `ScriptCutsceneFovLimit` off) that locks the framerate instead. ==This option is hidden by default.==
    * `FXAA` allows you to toggle [Shader Fixes](shader-fixes.md)' [FXAA](../../additional-setup/#optimal-game-settings). This setting has an in-game toggle in Settings - Graphics. ==Default is `1`.==
    * `ConsoleGamma` allows to toggle [Shader Fixes](shader-fixes.md)' [Console-like Gamma](assets/console-gamma.png). This setting has an in-game toggle in Settings - Display. ==Default is `0`.==
    * `DefaultCameraAngleInTLAD` allows to force the original [IV camera angle](assets/enabled.png) in [TLAD](assets/disabled.png). ==Default is `0`.==
    * `PedDeathAnimFixFromTBoGT` enables an additional ped death animation when you perform a counter attack after a dodge. [Enabled](https://imgur.com/EYsiGPe) vs [Disabled](https://imgur.com/CR3LEdR). ==Default is `1`.== 
    * `DisableCameraCenteringInCover` allows you to disable camera centering when entering a corner of cover. [Enabled](https://imgur.com/93CKToM) vs [Disabled](https://imgur.com/q6i6KOX). ==Default is `1`.== 
    * `MouseFix` removes the mouse deadzone. ==Default is `1`.== 
    * `ScreenFilter` changes the timecyc between Default, IV, TLAD and TBoGT. Use the in-game toggle in Settings - Screen instead. ==Default is `5`.== 
    * `DepthOfField` toggles Depth of Field. Use the in-game toggle in Settings - Screen instead. ==Default is `1`.==
    * `VehicleBudget` allows you to change the vehicle budget. This option comes from the built-in [RIL.Budgeted](https://gtaforums.com/topic/744584-reliv-rilbudgeted-population-budget-adjustertaxi-bug-fix/). Only change this option if you've encountered the [taxi bug](assets/taxi-bug.png). The value should be the size of your :material-file:`vehicles.img` in bytes(e.g. 200000000). ==Default is `0`.==
    * `PedBudget` allows to change the ped budget. This option comes from the built-in [RIL.Budgeted](https://gtaforums.com/topic/744584-reliv-rilbudgeted-population-budget-adjustertaxi-bug-fix/). Only change this option if you're unable to encounter modded peds. ==This option is hidden by default.==

[:material-page-first:Previous page <br>ZolikaPatch</br>](zolikapatch.md){ .md-button } [Next page:material-page-last: <br>Shader Fixes</br>](shader-fixes.md){ .md-button .md-button--primary }