title: FusionFix & Shader Fixes
description: One of the must-have mods for your GTA IV install that fixes a lot of things graphics and physics related

# FusionFix & Shader Fixes
!!! warning "Compatibility"
    This mod is only officially supported on the Complete Edition, but with taking several things in account, you can also use it with the 1.0.8.0 and 1.0.7.0 patches.
This project aims to fix or address some issues in Grand Theft Auto IV. You can read the changelog [here](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/tree/master#coregameplay-changelog). It also bundles [Shader Fixes](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection) with toggles to many of it's options.

???+ info "Shader Fixes"
    This project aims to fix and restore broken and missing shaders on the PC port (everything from [here](https://libertycity-ru.translate.goog/gta-4/articles/4346-gta-iv-complete-edition-xbox-protiv-pc.html?_x_tr_sl=ru&_x_tr_tl=en&_x_tr_hl=pt-BR) and more). You can read the changelog [here](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/blob/main/README.md#feature-list).

## Installation { data-search-exclude }
=== "1.0.8.0"
    !!! warning "Compatibility"
        Official support may hinder the GFWL experience. If you want to use GFWL, install the mod first, then apply [GFWL patch](https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL) ontop.
    * Go to the [Releases](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases) page.
    * Download the latest release.
    * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.zip` into the game folder.
    * Rename the :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll` if downgraded and not using GFWL. Replace if needed.
    !!! tip ""
        You can move files from the :material-folder:==plugins== to the game folder for convenience.
    !!! warning "If using ZolikaPatch..."
        Open :material-file-cog:`ZolikaPatch.ini` and disable the following options:

        - BuildingAlphaFix
        - EmissiveLerpFix
        - BikePhoneAnimsFix
        - BorderlessWindowed
        - CutsceneFixes
        - HighFPSBikePhysicsFix
        - HighFPSSpeedupFix
        - ReversingLightFix
        - OutOfCommissionFix
        - SkipIntro
        - SkipMenu

        Note that this doesn't break or actually disable anything, as these features are reimplemented by FusionFix.
=== "1.2.0.59"
    * Go to the [Releases](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases) page.
    * Download the latest release.
    * Extract :material-zip-box:`GTAIV.EFLC.FusionFix.zip` into the game folder.
    !!! tip ""
        You can move files from the :material-folder:==plugins== to the game folder for convenience.
!!! warning "Updating"
    If you're updating the mod, do not extract :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. Just take note if there are any new options that differ from your existing ones, carry them over in that case.

!!! tip "Performance impact"
    By itself, FusionFix does not impact performance. However, several options *can* increase the performance impact - change the options if you want to minimize the impact. Options are sorted by the more impacting options and descending.
    - SSAA 2x
    - Shadow Filter (PCSS)
    - Shadow Quality
    - Night Shadows
    - Depth of Field
    - Distant Blur
    - Motion Blur
    - View/Detail Distance
    - Reflection Quality
    - Console Shadows

!!! tip "Modloading"
    This mod can be used for modloading purposes. See [modloading](extras/modloading.md) for more details.

## Configuration
You can edit :material-file-cog:`GTAIV.EFLC.FusionFix.ini` or :material-file-cog:`GTAIV.EFLC.FusionFix.cfg` if you need to edit the file outside of the game for some reason. See [the list of non-ingame options](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix?tab=readme-ov-file#details) if you need to tweak them.

[:material-page-first:Previous page <br>Essential Modding</br>](index.md){ .md-button } [Next page:material-page-last: <br>ZolikaPatch</br>](zolikapatch.md){ .md-button .md-button--primary }