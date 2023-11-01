title: FusionFix & Shader Fixes
description: One of the must-have mods for your GTA IV install

# FusionFix & Shader Fixes
!!! warning "Compatibility"
    This mod is only officially supported on the Complete Edition, but with taking several things in account, you can also use it with the 1.0.8.0 and 1.0.7.0 patches.
This project aims to fix or address some issues in Grand Theft Auto IV. You can read the changelog [here](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/tree/master#coregameplay-changelog). It also bundles [Shader Fixes](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection) with toggles to many of it's options.

???+ info "Shader Fixes"
    This project aims to fix and restore broken and missing shaders on the PC port (everything from [here](https://libertycity-ru.translate.goog/gta-4/articles/4346-gta-iv-complete-edition-xbox-protiv-pc.html?_x_tr_sl=ru&_x_tr_tl=en&_x_tr_hl=pt-BR)). You can read the changelog [here](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/blob/main/README.md#feature-list).

## Installation { data-search-exclude }
=== "1.0.8.0"
    === "Official"
        !!! warning "Compatibility"
            Official support is lacking support for Zolika1351's Extra Options mod.
        * Go to the [Releases](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases) page.
        * Download the latest release.
        * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.zip` into the game folder.
        * Rename the :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll` if not using GFWL. Replace if needed.
        !!! tip ""
            You can move files from the :material-folder:==plugins== to the game folder for convenience.
    === "Zolika1351's fork"
        !!! warning "Notice"
            This fork, nor any other Zolika1351's mods will not be updated anymore. See [this post](https://zolika1351.pages.dev/posts/saying-goodbye) for context.

            It is provided only in the case you want to use Zolika1351's Extra Options. Use the Official version otherwise.
        * Go to the Zolika1351's fork of FusionFix [Releases](https://github.com/Zolika1351/GTAIV.EFLC.FusionFix/releases/).
        * Download the latest release.
        * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.preCE.zip` into the game folder.
=== "1.2.0.59"
    * Go to the [Releases](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases) page.
    * Download the latest release.
    * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.zip` into the game folder.
    !!! tip ""
        You can move files from the :material-folder:==plugins== to the game folder for convenience.
!!! warning "Updating"
    If you're updating the mod, do not extract :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. Just take note if there are any new options that differ from your existing ones, carry them over in that case.

## Configuration
Open :material-file-cog:`GTAIV.EFLC.FusionFix.ini` (located in :material-folder:==plugins== by default) and configure the file as needed.

??? abstract "Full list of options"
    !!! warning ""
        This list is based on the latest version of FusionFix. If you're using the legacy or other outdated version, you may be missing some of these options.

        The options are either `0` for disabled and `1` for enabled unless otherwise noted.

    * `SkipIntro` allows to skip the game's normally unskippable intro video. This setting has an in-game toggle in `Settings` - `Game`. ==Default is `1`.==
    * `SkipMenu` allows to skip game's menu, loading into the savefile immediately upon launching the game. You can hold ++lshift++ to stop at the menu. This setting has an in-game toggle in `Settings` - `Game`. ==Default is `1`.==
    * `BorderlessWindowed` launches the game in Borderless Windowed mode instead of Exclusive Fullscreen, which the game uses by default (`-windowed` [launch option](../../additional-setup/#launch-options) must be set for this to work). This setting has an in-game toggle in `Settings` - `Game`. ==Default is `1`.==
    * `RecoilFix` enables weapon recoil on keyboard&mouse controls, which is only present on gamepads due to an oversight. ==Default is `1`.==
    * `AimingZoomFix` fixes inverted zoom control in TBoGT and allows to remember last zoom multiplier. The options are `0` for disabled, `1` for an xbox-like fix, `2` to also enable the fix in IV and TLAD, `-1` to disable the feature. ==Default is `1`.==
    * `FlickeringShadowsFix` disables player's shadow from headlights to avoid flickering. ==Default is `1`.==
    * `ExtraDynamicShadows` allows to restore missing dynamic shadows, up to forcing all objects to cast a shadow. The options are `0` for disabled, `1` for restoring some missing ,shadows, `2` for adding vegetation shadows and `3` for forcing all shadows. ==Default is `1`.==
    * `DynamicShadowForTrees` adds dynamic shadows to vegetation. ==Default is `1`.==
    * `FixCascadedShadowMapResolution` fixes the resolution of cascaded shadowmaps. ==Default is `1`.==
    * `FrameLimitType` controls the type of the framerate lock. The options are `1` for a real-time lock (thread-lock) and `2` for an accurate lock (sleep-yield) that uses less resources. ==Default is `2`.==
    * `FpsLimit` allows you to set a custom framerate lock. Set your desired framerate as an option. To toggle it in-game, change the `FPS Limiter` setting in `Settings` - `Graphics` to `Default`. ==Default is `0`.==
    * `CutsceneFpsLimit` allows you to set a custom framerate lock for cutscenes. It's recommended to set this option to 32 - [read this issue](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/issues/58) for context. ==Default is `0`.==
    * `ScriptCutsceneFovLimit` allows you to set a FOV limit for scripted cutscenes. This is needed because scripted cutscenes [changing the FOV based on your framerate](https://youtu.be/NzKw7ijHG10). ==Default is `30`.==
    * `ScriptCutsceneFpsLimit` is an alternative fix for the issue above (change the `ScriptCutsceneFovLimit` to 0) that locks the framerate instead. ==This option is hidden by default.==
    * `DefaultCameraAngleInTLAD` allows to force the original [IV camera angle](assets/enabled.png) in [TLAD](assets/disabled.png). ==Default is `0`.==
    * `PedDeathAnimFixFromTBoGT` enables an additional ped death animation when you perform a counter attack after a dodge. [Enabled](https://imgur.com/EYsiGPe) vs [Disabled](https://imgur.com/CR3LEdR). ==Default is `1`.==
    * `DisableCameraCenteringInCover` allows you to disable camera centering when entering a corner of cover. [Enabled](https://imgur.com/93CKToM) vs [Disabled](https://imgur.com/q6i6KOX). ==Default is `1`.==
    * `MouseFix` removes the mouse deadzone. ==Default is `1`.==
    * `FixRainDrops` fixes the black water droplets on the screen and restores the refraction effect from console version. ==Default is `1`.==
    * `RainDropsBlur` controls the type of refraction from the `FixRainDrops` option. ==Default is `2`.==
    * `VehicleBudget` allows you to change the vehicle budget. This option comes from the built-in [RIL.Budgeted](https://gtaforums.com/topic/744584-reliv-rilbudgeted-population-budget-adjustertaxi-bug-fix/). Only change this option if you've encountered the [taxi bug](assets/taxi-bug.png). The value should be the size of your :material-file:`vehicles.img` in bytes(e.g. 200000000). ==Default is `0`.==
    * `PedBudget` allows to change the ped budget. This option comes from the built-in [RIL.Budgeted](https://gtaforums.com/topic/744584-reliv-rilbudgeted-population-budget-adjustertaxi-bug-fix/). Only change this option if you're unable to encounter modded peds.

[:material-page-first:Previous page <br>ZolikaPatch</br>](zolikapatch.md){ .md-button } [Next page:material-page-last: <br>Multiplayer</br>](../multiplayer.md){ .md-button .md-button--primary }