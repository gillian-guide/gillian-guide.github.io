title: Drag-and-Drop Archive
description: A complete ready-to-play modpack for the best singleplayer-only GTA IV campaign experience

# Drag-and-Drop Archive { data-search-exclude }

The Drag-and-Drop Archive (also known as Gillian's Modpack) is a complete ready-to-play modpack for the best singleplayer-only GTA IV campaign experience. All you have to do to install it is just drop the files into the game folder and do a few extras - thus the name.

!!! warning ""
    Make sure the **prerequisites are met** and **preparation was done**. If you missed one of the steps, you may encounter issues using this archive and won't receive support.

    [:material-page-first:Introduction: Prerequisites</br>](index.md/#prerequisites){ .md-button } [:material-page-first:Preparation</br>](preparation.md){ .md-button }

---

## Demo

TBA

---

## Installation { data-search-exclude }

!!! question "Which game version to pick?"
    The following selector is for the game version - see [here](../downgrading/downgrading-the-game.md/#game-versions) for their base differences. The mods in the archives are mostly identical, but **1.0.8.0 includes more Quality of Life changes at the cost of some fixes from FusionFix and removes the Rockstar Games Launcher DRM, while 1.2.0.59 is considered to be more stable.**

=== "1.2.0.59"
    Last updated: **[09.03.2024](#changelog)**

    !!! warning ""
        - **This archive does NOT provide the best possible performance - the goal is first and foremost to provide the best vanilla-faithful experience.** If you just want the best performance - mod the game manually.
        - Do not attempt to install this version on a downgraded copy.
        - If using Linux, skip steps 3-6 and [apply launch options manually](additional-setup.md/#launch-options).

    1. [Download the archive](https://drive.google.com/file/d/1tMwlvFiTE1tNuq8C4v2MNoDVXlCbLfoY/view?usp=sharing).
    2. Extract the :material-zip-box:`1.2 archive.7z` archive into the game folder (the one that includes :material-file:`GTAIV.exe`).
    3. Launch :material-file-download:`GTAIVSetupUtilityWPF.exe`. It may require you to install [.NET 6 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-6.0.32-windows-x64-installer).
    4. Press `Open`, select the same game folder.
    5. Press `Install DXVK` and then `Setup launch options`. Don't touch the toggles unless you are confident in what you are doing.
    6. After pressing `Setup launch options` and pressing `OK` you will have launch options in your clipboard, so do one of the following:
        - **:material-steam: Steam**: Right click the game in your library, press `Properties...` and paste the contents in the `Launch options` field.
        - **:simple-rockstargames: Rockstar Games Launcher**: Open the game page in your library, open settings and paste the contents in the `Launcher arguments` field.
        - **Something else**: Right click on the game shortcut, click `Properties` and paste the contents at the end of the `Target` field.
    6. You are ready to play!
        - Launch the game via :material-steam: Steam, :simple-rockstargames: Rockstar Games Launcher or the `PlayGTAIV.exe` executable.
        - **If using Linux**, add `WINEDLLOVERRIDES="dinput8=n,b" %command%` to launch options.
        - It's preferable to start **a new savefile**. Existing savefiles can work, but you may encounter issues.
        - If you want **more mods, check out [additional mods](#additional-mods)**.

    !!! info "Updating"
        If you're updating the archive, delete the :material-folder: ==update== folder and remove all :material-file:`.asi` files (but don't touch other ones) from the :material-folder: ==plugins== folder first.

=== "1.0.8.0"
    Last updated: **[21.05.2024](#changelog)**

    !!! warning ""
        - **This archive does NOT provide the best possible performance - the goal is first and foremost to provide the best vanilla-faithful experience.** If you just want the best performance - mod the game manually.
        - Do not downgrade the game on your own. The archive already includes a downgrader.
        - If using Linux, skip steps 3-5 and [apply launch options manually](additional-setup.md/#launch-options).

    1. [Download the archive](https://www.mediafire.com/file/cx6dct4npfqtc5z/1.0_archive.7z/file).
    2. Extract the :material-zip-box:`1.0 archive.7z` archive into the game folder (the one that includes :material-file:`GTAIV.exe`).
    3. Launch :material-file-download:`GTAIVSetupUtilityWPF.exe`.
    4. Press `Open`, select the same game folder.
    5. Press `Install DXVK` and then `Setup launch options`. Don't touch the toggles unless you are confident in what you are doing.
    6. You are ready to play!
        - Launch the game via :material-steam: Steam or the `PlayGTAIV.exe` executable.
        - **If using the :simple-rockstargames: Rockstar Games Launcher**, do not launch the game via the launcher and delete :material-file:`SteamAchievements.asi`.
        - **If using Linux**, see [Getting ScriptHookDotNet and IV-SDK .NET to work on Linux](../resources/mod-dependencies.md/#getting-scripthookdotnet-and-iv-sdk-net-to-work-on-linux) (or delete files & folders starting with `IVSDKDotNet`).
        - It's preferable to start **a new savefile**. Existing savefiles can work, but you may encounter issues. Also, if you already started the game on 1.2.0.59, you have to [downgrade the savefile](../downgrading/downgrading-the-game.md/#downgrading-the-savefile).
        - If you want **more mods, check out [additional mods](#additional-mods)**.

    !!! info "Updating"
        If you're updating the archive, delete :material-folder: ==update== and :material-folder: ==modloader== (if exists) folders and remove all :material-file:`.asi` files (but don't touch other ones) from the game folder first.

??? bug "The game doesn't boot | The game is behaving strangely | The game is crashing randomly"
    See [troubleshooting](../resources/troubleshooting.md).

    Disable mods one by one to see the culprit by deleting folders/files in the :material-folder: ==update== folder or the :material-file:`.asi` files.

    Report the issue on the [Discord server](../index.md/#navigation).

---

## Navigation

<div class="grid cards" markdown>

- After installing the archive, **apply optimal graphics settings**:

    [Next page:material-page-last: <br>Additional Setup: Optimal graphics settings</br>](additional-setup.md/#optimal-graphics-settings){ .md-button .md-button--primary }

- **If using Linux,** also apply Launch Options manually:

    [Next page:material-page-last: <br>Additional Setup: Launch options</br>](additional-setup.md/#launch-options){ .md-button .md-button--primary }

</div>

---

## Modlist { data-search-exclude }

### Shared mods { data-search-exclude }

All mods in the following list are present in both archives with identical versions:

| Mod | Developer(s) | Details |
| :-: | :--------: | :-----: |
| [Radio Downgrader](http://downgraders.rockstarvision.com/) | Tomasak and others | A simple-to-perform radio downgrade.<br>Addon used: [Restored original TBoGT Menu Vocals](https://www.nexusmods.com/gta4/mods/234/?tab=files&category=archived).</br> |
| [FusionFix~2.5.6~](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/) | ThirteenAG, Fusion Team and others | The most essential mod: it contains a lot of fixes, improvements, new settings and also acts as a modloader.<br>==Some fixes are missing in 1.0.8.0 support.==</br> |
| [Various Fixes~1.8.1~](https://gtaforums.com/topic/975211-various-fixes/) | Attramet and others | A large collection of map fixes of various scale - mostly broken map textures. |
| [Trilogy Characters Fixes](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/) | TheYoshiPunch, (Japan) GTA Love and others | Aims to fix the inconsistency of characters between base GTA IV and EFLC. |
| [Improved Animations Pack~1.3~](https://gtaforums.com/topic/958625-improved-animations-pack/) | B Dawg | Fixes some weapon animation issues, such as delayed fire. |
| [IV Fixes and Improvements](https://gtaforums.com/topic/909155-iv-fixes-improvements/) | Zolika1351 and others | A collection of minor fixes and improvements - see the changelog on the page.<br>Only the old `.img` improvements are used - and some are cut due to their precendece in Various Fixes and other mods.</br> |
| [`carcols` and `cargrp` Fixes](https://drive.google.com/file/d/13OgDDm0xakbdRONPlrnN5zRfshdAgwhd/view?usp=sharing) | iiCriminnaaL | Several files from [Responsive Plus](https://gtaforums.com/topic/931069-iveflc-responsive-plus/) that fix some oversights in the original files that prevent some cars from spawning as intended. |
| [Restored Pedestrians](https://gtaforums.com/topic/981864-restored-pedestrians/) | Attramet | Restores pedestrians that were either unused or only present in the betas. |
| [Various Pedestrians Actions](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Attramet | Adds, corrects and completes unfinished actions for pedestrians. |
| [Restored Trees Position](https://gtaforums.com/topic/984591-restored-trees-position/) | Attramet | Restores trees that were present in the betas but removed in the final release, either accidentally or due to performance concerns. |
| [More Visible Interiors](https://gtaforums.com/topic/974099-more-visible-interiors/) | Attramet | Makes interiors more visible from the outside, although comes with a downside of potential pop-in. |
| [Higher Resolution Miscellaneous Pack~1.1~](https://www.nexusmods.com/gta4/mods/357/) | Ash_735 | Improves the texture quality of minor assets. |
| [Project Glass](https://discord.gg/gZvZmFt2p7) | DayL | Adds cubemap reflections to what otherwise is just transparent glass.|
| [Vehicle Pack~2.0~](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736) | Ash_735 | Improves the texture quality of all vehicles in the game. Some textures are upscaled, some are taken from Max Payne 3 and GTA V. |
| [Dodgy Doc - Higher Quality](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Improves the quality of the Dodgy Doc in the Have a Heart mission. |
| [High Quality Pigeons](https://www.gtainside.com/gta4/mods/166924-high-quality-pigeons/) | Supreme Dear Leader | Improves the model and texture quality for pigeons. |
| [Resized Blista Compact](https://www.gtainside.com/en/gta4/cars/188730-resized-blista-compact/) | Thundersmacker | Resizes the Blista Compact to match the real life counterpart (Honda CR-X).  |
| [Fixed LCPD Buffalo](https://www.gtainside.com/en/gta4/cars/181342-fixed-lcpd-buffalo/) | Ooboy | Fixes the police Buffalo model and texture bugs. |
| [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | B Dawg | Fixes green-ish textures on some character models. |
| [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | _ys | Fixes an incorrect suit in Perseus, as you end up buying a different one from the one displayed. |
| [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | B Dawg | Fixes the IV Bikers voicelines in EFLC. |
| [Default Pistol Iron Sight Fix](https://www.nexusmods.com/gta4/mods/15) | grasscid | Fixes an oversight in the pistol's model where the iron sight doesn't make any sense. |
| [Liberty Ferry Terminal - Waiting Room Sign Fix](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Fixes broken UV map on "Waiting Room" sign texture. |
| [Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Edits the UV map on the sign to include an unused texture. |
| [Luis' Helmet Reflections Fix](https://www.gtainside.com/en/gta4/skins/125863-luis-s-helmet-reflections-fix/) | 6135 | Fixes the bleak reflection on TBoGT player model's helmet. |
| [Luis' Bag Texture Fix](https://www.gtainside.com/en/gta4/skins/136118-luis-s-bag-texture-fix/) | 6135 | Adds missing normal and specular maps and improves texture quality on TBoGT player model's bag. |
| [Johnny's Shoe Texture Fix](https://www.gtainside.com/en/gta4/skins/125196-johnny-s-shoe-texture-fix/) | 6135 | Adds missing normal and specular maps to the TLAD player model's shoes. |
| [Reduced Traffic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | GladiTek | Changes the pitch of the traffic screech in Algonquin to match the real-life levels you'd usually hear in Times Square. |
| [Menu Art Fix](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072165611) | _ys | Fixes the lower-resolution backgrounds in EFLC menus and removes the Social Club text. |
| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) and [Higher Res Radio Logos Menu](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871) | Ash_735 | Increases the quality of UI radio icons, as they are highly inconsistent with other UI assets in the game. |

### Separate mods { data-search-exclude }

The mods or their specific versions in the following list are present in only one of the archives due to incompatibility with the other version.

=== "1.2.0.59"
    | Mod | Developer(s) | Details |
    | :-: | :----------: | :-----: |
    | [Console Visuals~1.6~](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | nastyyaboi and others | Ports select console visuals to the PC version. <br>Only Fusion Console Vegetation, Console Peds and Console Select Menu are included in the archive. See [Additional Mods](#additional-mods) for more.</br> |
    | [Project2DFX](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv) | ThirteenAG | Improves distant lights at night. <br>==Can be disabled by deleting the `IVLodLights` files in the :material-folder: `plugins` folder.==</br> |
    | [Xbox Rain Droplets](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Adds nice water droplets on the screen. <br>==Can be disabled by deleting the `GTAIV.XboxRainDroplets` files in the :material-folder: `plugins` folder.==</br> |
=== "1.0.8.0"
    | Mod | Developer(s) | Details |
    | :-: | :----------: | :-----: |
    | Downgrade to 1.0.8.0 | Gillian (files belong to Rockstar) |  A simple downgrade to 1.0.8.0 without replacing too many files. |
    | [ZolikaPatch IV~7.65~](https://zolika1351.pages.dev/mods/ivpatch) | Zolika1351 | Adds a lot of minor fixes exclusive to 1.0.8.0. |
    | [Console Visuals~1.6~](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | nastyyaboi and others | Ports select console visuals to the PC version. <br>Only Fusion Console Vegetation and Console Peds are included in the archive. See [Additional Mods](#additional-mods) for more.</br> |
    | [Liberty Tweaks~1.4.1~](https://gtaforums.com/topic/991160-liberty-tweaks/) | catsmackaroo, ItsClockAndre and others | Aims to improve various aspects of the game and it's general Quality of Life. Highly configurable.<br>==Allows to quicksave using the ++f9++ key and has a lot of various gameplay features - if you're not a fan of the defaults, you can modify things to your taste in :material-file-cog:`LibertyTweaks.ini` located in :material-folder: `IVSDKDotNet\scripts\`==</br> |
    | [Project Thunder](https://gtaforums.com/topic/982902-project-thunder/) | ItsClockAndre | Improves how thunder appears in-game, with actual lighting and improved atmosphere. Highly configurable. |
    | [VAmbience](https://gtaforums.com/topic/981402-vambience/) | ItsClockAndre | Adds background noise to the game, such as driving and shooting, alike to GTA V. Highly configurable. |
    | [Xbox Rain Droplets](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Adds nice water droplets on the screen.<br>==Can be disabled by deleting the `GTAIV.XboxRainDroplets` files.==</br> |
    | [Steam Achievements~v2~](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/) | Zolika1351 | Allows to get :material-steam: Steam achievements on older patches. |

---

## Additional Mods { data-search-exclude }

These mods are not included by default, but are easy to install ontop of the archive. Any other mods not mentioned in this list are not supported.

=== "1.2.0.59"
    | Mod | Developer(s) | Details |
    | :-: | :----------: | :-----: |
    | [Console Visuals Addons](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo and others | This project ports select console visuals to the PC version. <br>Installation: Extract the desired addons into the game folder.</br> |
    [Enhanced Snow Mod Repack](https://drive.google.com/file/d/11PFXrFnvB8JEKVajseL2GIWRd6MdLBBy/view?usp=drive_link) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_, Lover of Winter, Straysify, gdanbo, Attramet and Gillian | [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Realistic Winter Trees](https://www.gtainside.com/en/gta4/mods/177373-realistic-winter-trees/), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) and [Beta Winter Pedestrians](https://gtaforums.com/topic/987173-beta-winter-pedestrians/) bundled for Fusion Overloader with my own custom tweaks.<br>Installation: Backup the :material-folder: ==update== folder. Extract the :material-folder: ==update== folder from the archive into the game folder, replacing files when prompted. Disable/remove FusionFix's `GTATrees.img` and Console Visuals' `FusionConsolevegetation.img`. Set Screen Filter to `TBoGT`. Don't play DLC's.</br> |
    | [UHD Vanilla Map and Radar](https://nexusmods.com/gta4/mods/456) | Valentyn_L | A high-resolution map for 1440p and 4K monitor users (may not look great on a 1080p or lower resolution monitor).<br>Installation: Extract the archive into the game folder.</br> |
    | [Aura](https://gtaforums.com/topic/989259-aura/) | catsmackaroo, nastyyaboi, ItsClockAndre and cubabori | A vanilla+ graphics mod, building upon the vanilla look.<br>Installation: Extract the archive into the :material-folder: ==update== folder.</br> |
    | [Improved Vanilla Timecyc](https://www.gtainside.com/gta4/mods/189357-improved-vanilla-timecyc-v1-1/) | pidarasnahui516 | Another vanilla+ timecyc mod.<br>Installation: Extract the :material-folder: ==Main Files\\pc\\== folder from the archive into the :material-folder: ==update== folder.</br> |
=== "1.0.8.0"
    | Mod | Developer(s) | Details |
    | :-: | :----------: | :-----: |
    | Liberty Tweaks options | catsmackaroo, ItsClockAndre and others | Features many options that severely change the gameplay - if you're not a fan of the defaults, you can modify things to your taste in :material-file-cog:`LibertyTweaks.ini` located in :material-folder: ==IVSDKDotNet\scripts\\==. |
    | [Console Visuals Addons](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | nastyyaboi and others | Collection of ported assets from the console version. <br>Installation: Extract the desired addons into the game folder. Plugins will not work on 1.0.8.0.</br> |
    | [Snow Mod](https://github.com/akifle47/Snow/releases/latest) | AssaultKifle47 | A lightweight snow mod based on shaders rather than textures. |
    | [Addons for the Snow Mod](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_, Lover of Winter, Straysify, gdanbo, Attramet and Gillian | [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Realistic Winter Trees](https://www.gtainside.com/en/gta4/mods/177373-realistic-winter-trees/), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) and [Beta Winter Pedestrians](https://gtaforums.com/topic/987173-beta-winter-pedestrians/) bundled as addons for AssaultKifle47's Snow Mod.<br>Installation: Backup the :material-folder: ==update== folder. Extract the :material-folder: ==update== folder from the archive into the game folder, replacing files when prompted. Disable/remove FusionFix's `GTATrees.img` and Console Visuals' `FusionConsolevegetation.img`. Set Screen Filter to `TBoGT`. Don't play DLC's.</br> |
    | [UHD Vanilla Map and Radar](https://nexusmods.com/gta4/mods/456) | Valentyn_L | A high-resolution map for 1440p and 4K monitor users (may not look great on a 1080p or lower resolution monitor).<br>Installation: Extract the archive into the game folder.</br> |
    | [Aura](https://gtaforums.com/topic/989259-aura/) | catsmackaroo, nastyyaboi, ItsClockAndre and cubabori | A vanilla+ graphics mod, building upon the vanilla look.<br>Installation: Extract the archive into the :material-folder: ==update== folder.</br> |
    | [Improved Vanilla Timecyc](https://www.gtainside.com/gta4/mods/189357-improved-vanilla-timecyc-v1-1/) | pidarasnahui516 | Another vanilla+ timecyc mod.<br>Installation: Extract the :material-folder: ==Main Files\\pc\\== folder from the archive into the :material-folder: ==update== folder.</br> |
    | [IV-Presence](https://gtaforums.com/topic/975850-iv-presence/) | ItsClockAndre | Adds a Discord Rich Presence (custom activity status).<br>Installation: Open the archive, open the material-folder: ==For GTA IV 1070 and 1080== folder in it and extract the :fontawesome-solid-gears:`discord-rpc.dll` and :material-file:`IVPresence.asi` files into the game folder. If you have issues, also extract :material-file:`IVPresenceDependenciesChecker.exe` with it's config, launch it and see what dependencies are you lacking.</br> |

---

## Changelog { data-search-exclude }

=== "1.2.0.59"
    !!! info "Latest version"
        - 09.03.2024:
            - Updated More Visible Interiors, Xbox Rain Droplets.
            - *Actually* fixed Three Leaf Clover for once.
    ??? quote "Old changes"
        - 07.03.2024:
            - Updated FusionFix, Console Visuals, Higher Resolution Misc Pack.
        - 28.01.2024:
            - Updated FusionFix.
        - 14.01.2024:
            - Updated FusionFix.
        - 13.01.2024:
            - Updated FusionFix.
            - Fixed weapon animation issues.
            - Fixed broken head wearables in base IV.
            - Removed more duplicate files from Minor Mods.
        - 04.01.2024:
            - Updated Radio Downgrader, FusionFix, Project2DFX, Xbox Rain Droplets, Various Fixes, More Visible Interiors, Restored Trees Position.
            - Repackaged most mods - should solve a few issues and make less unnecessary changes.
            - Removed Improved Weapon Spec in favor of Higher Resolution Miscellaneous Pack.
            - Added Restored Pedestrians, Various Pedestrians Actions.
        - 18.12.2023:
            - Updated FusionFix.
            - Removed Vanilla Road Texture Enhancement by DayL.
            - Removed Xbox One/Series S+X Buttons (in favor of FusionFix's implementation).
        - 12.12.2023 (hotfix):
            - Fixed TBoGT crash on load.
                - Manual steps: add `DISABLE_FILE common:/data/newchar.ide` to :material-folder: ==/update/TBoGT/:material-file:`content.dat`==
        - 10.12.2023:
            - Updated FusionFix.
            - Fixed the missing NPC in Three Leaf Clover mission.
        - 27.11.2023:
            - Updated FusionFix, Various Fixes and Console Visuals.
        - 01.11.2023:
            - Updated FusionFix.
            - Added Higher Resolution Miscellaneous Pack.
            - Removed some Console Visuals addons, moved to Additional Mods.
        - 21.09.2023:
            - Updated Various Fixes.
            - Replaced Setup Utility with the rewritten one.
        - 15.09.2023:
            - Updated FusionFix, Radio Downgrader (this reduces the archive size a lot), Setup Utility.
            - Added IV Bikers in Episodes voice sets fix.
        - 08.09.2023:
            - Updated Various Fixes.
            - Added missing files that were missing for reasons we'll never know.
        - 07.09.2023:
            - Updated FusionFix.
            - Added Reduced Traffic Screech and High Quality Pigeons.
        - 06.09.2023:
            - Updated FusionFix - with it, Shader Fixes.
            - Included Setup Utility.
            - Removed Traffic Cops in the Toolbooths - FusionFix now includes it.
            - Removed DXVK, you can now install it automatically via :material-file-download:`GTAIVSetupUtility.exe`.
        - 28.08.2023:
            - Fixed Dodgy Doc HQ mod to actually be used.
            - Added `dxvk.gplAsyncCache = true` to :material-file-cog:`dxvk.conf`.
        - 26.08.2023:
            - Updated Project Glass.
            - Added community's fixes to Various Fixes.
            - Returned more up-to-date Shader Fixes files, as I accidentally overwrote them last update.
        - 22.08.2023:
            - Updated FusionFix, Xbox One/Series S+X Buttons.
            - Added Menu Art Fix.
        - 18.08.2023:
            - Updated Various Fixes files.
            - Fixed a model issue with Angels of Death's clubhouse in TLAD.
        - 17.08.2023:
            - Updated Project Glass.
            - Added More Visible Interiors.
            - Slightly tweaked configuration files.
        - 12.08.2023:
            - Fixed known crash and softlock issues in TLAD and TBoGT.
            - Restored TBoGT menu soundtrack.
        - 11.08.2023:
            - Updated Shader Fixes (manually built).
            - Slightly tweaked vehicle budget.
            - Changed Niko's hair files to fix the visual issues.
        - 10.08.2023:
            - Updated Project Glass.
        - 07.08.2023:
            - Updated FusionFix.
        - 03.08.2023:
            - Added Restored Trees Position.
        - 02.08.2023:
            - Updated FusionFix, Trilogy Characters Fixes, Console Visuals.
        - 25.07.2023:
            - Updated Fix Collection.
            - Minor .ini tweaks.
        - 23.07.2023:
            - Added Road Texture Enhancement, Project Glass(+lighthing for bus stops), Dodgy Doc - Higher Quality, Rescaled Blista Compact, Player Outfit Texture Fixes, LCPD Buffalo Fix, Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Fixed Suit Display and borrowed a few fixes from Responsive Plus.
            - Fixed priority for mods.
            - Repackage mods to reduce folder bloat.
        - 20.07.2023:
            - Updated FusionFix.
            - Changed dxvk to dxvk-gplasync.
        - 19.07.2023:
            - Updated FusionFix and Shader Fixes.
            - Added the Radio Downgrader, GTA Online QUB3D Background, Traffic Cops in the Toolbooths, Xbox Rain Droplets, Fixed Pistol Sights.
            - Added Dualsense buttons to optionals.
            - Removed Pedestrians with Unused Clothing Restored and Varied Alderney State Trooper Ped due to potential incompatibilities.
        - 13.07.2023:
            - Fixed disappearing assets in Roman's taxi office.
            - Changed FPS limit in cutscenes to 32.
        - 12.07.2023:
            - Added (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec.
            - Removed TBoGT Texture Quality Fix as Various Fixes already contains the fix.
        - 10.07.2023:
            - Changed Niko's hair file, now has no visual problems.
        - 09.07.2023:
            - Removed IV Fixes and Improvements.
            - Added Various Fixes.
        - 08.07.2023:
            - Updated FusionFix, Shader Fixes.
            - Changed DXVK config.
            - Removed dxgi.dll.
            - Repacked some mods.
        - 02.07.2023:
            - Repacked mods in a more convenient format.
        - 01.07.2023:
            - Updated Shader Fixes.
            - Repacked some old mods for Fusion Overloader.
        - 30.06.2023:
            - Updated mods.
        - 27.06.2023:
            - Updated mods.
        - 26.06.2023:
            - Created the archive.
=== "1.0.8.0"
    !!! info "Latest version"
        - 21.05.2024:
            - Reuploaded the archive to Mediafire because Google is a bitch.
            - Updated IVSDKDotNet and Liberty Tweaks (slightly reconfigured it aswell).
    ??? quote "Old changes"
        - 09.03.2024:
            - Updated More Visible Interiors, Liberty Tweaks (fixes crashes when entering/exiting a vehicle).
            - Removed Project2DFX due to breaking with fixed coronas on 1.0.8.0.
            - *Actually* fixed Three Leaf Clover for once.
            - Fixed the issue where the game wouldn't launch.
        - 07.03.2024:
            - Updated FusionFix, Liberty Tweaks, Console Visuals, Higher Resolution Misc Pack.
        - 28.01.2024:
            - Updated FusionFix.
        - 14.01.2024:
            - Updated FusionFix.
        - 13.01.2024:
            - Updated FusionFix.
            - Fixed weapon animation issues.
            - Fixed broken head wearables in base IV.
            - Removed more duplicate files from Minor Mods.
            - Disabled more problematic ZolikaPatch options.
        - 04.01.2024:
            - Updated Radio Downgrader, FusionFix, Various Fixes, More Visible Interiors, Restored Trees Position, Restored Pedestrians, Various Pedestrians Actions.
            - Repackaged most mods - should solve a few issues and make less unnecessary changes.
            - Retired IV Tweaker in favor of Fusion Overloader - one less injectable is, imo, better for the stability.
            - Removed Improved Weapon Spec in favor of Higher Resolution Miscellaneous Pack.
        - 22.12.2023:
            - Updated IVSDK .NET, Clonk's Coding Library and Liberty Tweaks. Should probably result in better stability and less issues with Liberty Tweaks.
        - 18.12.2023:
            - Updated FusionFix.
            - Disabled Vanilla Road Texture Enhancement by DayL.
            - Removed Dualshock, Dualsense and Xbox One/Series S+X Buttons mods in favor of FusionFix's implementation.
        - 12.12.2023:
            - Attempt to fix Three Leaf Clover issues again. Not a hotfix because I apparently was missing Characters Fixes files.
        - 10.12.2023:
            - Updated FusionFix.
            - Fixed the missing NPC in Three Leaf Clover mission.
        - 27.11.2023:
            - Updated FusionFix, Various Fixes and Console Visuals.
        - 03.11.2023:
            - Fixed an issue with downgrading
            - Fixed incorrect folder name.
            - Disabled the incompatible and redundant options from :material-file-cog:`ZolikaPatch.ini`.
        - 01.11.2023:
            - Updated FusionFix.
            - Added Higher Resolution Miscellaneous Pack.
            - Removed some Console Visuals addons, moved to Additional Mods.
            - Removed Extra Options due to incompatibility with FusionFix 2.0.
        - 04.10.2023 (hotfix):
            - Fixed an issue with downgrading that resulted in corruption of game settings.
        - 27.09.2023:
            - Updated Setup Utility, ZolikaPatch, IV Tweaker, Liberty Tweaks.
            - Added Extra Options.
        - 21.09.2023:
            - Updated Various Fixes.
            - Replaced Setup Utility with the rewritten one.
        - 16.09.2023 (hotfix):
            - Removed the :material-file:`IVMenuAPI.asi` that was bundled accidentally.
        - 15.09.2023:
            - Updated FusionFix, ZolikaPatch, IV Tweaker, IV Fixes and Improvements, Liberty Tweaks, Radio Downgrader (this reduces the archive size a lot), Setup Utility.
            - Added IV Bikers in Episodes voice sets fix.
        - 08.09.2023:
            - Updated Various Fixes (should fix savefile damage).
            - Added VAmbience.
        - 07.09.2023:
            - Updated FusionFix.
            - Added Reduced Traffic Screech and High Quality Pigeons.
        - 06.09.2023:
            - Updated ZolikaPatch, FusionFix.
            - Included Setup Utility.
            - Removed Traffic Cops in the Toolbooths - FusionFix now includes it.
            - Removed DXVK and commandline.txt, you can now install them automatically via :material-file-download:`GTAIVSetupUtility.exe`.
        - 28.08.2023:
            - Fixed the infinite loading on Three Leaf Clover mission (needs a better solution - at the moment, there's a missing NPC model in the cutscene due to this).
            - Fixed Dodgy Doc HQ mod to actually be used.
            - Added `dxvk.gplAsyncCache = true` to :material-file-cog:`dxvk.conf`.
            - Removed Better Wardrobes.
        - 26.08.2023:
            - Updated FusionFix, Project Glass, Xbox One/Series S+X Buttons.
            - Added Menu Art Fix.
            - Repacked Various Fixes, aswell as adding community's fixes to it.
        - 18.08.2023:
            - Updated Various Fixes.
            - Fixed a model issue with Angels of Death's clubhouse in TLAD.
        - 17.08.2023:
            - Updated Project Glass.
            - Added More Visible Interiors.
            - Slightly tweaked configuration files.
        - 12.08.2023:
            - Fixed known crash and softlock issues in TLAD and TBoGT.
            - Restored TBoGT menu soundtrack.
        - 11.08.2023:
            - Updated FusionFix, Shader Fixes (manually built).
            - Fixed crash issues (IV Tweaker from up-to-date downgrader was not up-to-date).
            - Slightly tweaked vehicle budget.
            - Changed Niko's hair files to fix the visual issues.
        - 10.08.2023:
            - Updated the Downgrader, ZolikaPatch and Project Glass.
        - 07.08.2023:
            - Updated FusionFix.
        - 03.08.2023:
            - Updated Console Visuals.
            - Added Restored Trees Position.
            - Rearranged some files to avoid incompatibility issues.
        - 02.08.2023:
            - Updated FusionFix, Trilogy Characters Fixes - also repacked it slightly.
        - 25.07.2023:
            - Updated Fix Collection.
            - Added Project Thunder, Restored Pedestrians, Various Pedestrian Actions.
            - Minor .ini tweaks.
        - 24.07.2023:
            - Repackage mods to reduce folder bloat.
            - Added Road Texture Enhancement, Project Glass(+lighthing for bus stops), Dodgy Doc - Higher Quality, Rescaled Blista Compact, Player Outfit Texture Fixes, LCPD Buffalo Fix, Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Fixed Suit Display and borrowed a few fixes from Responsive Plus (dubbed Fix Collection later)
        - 20.07.2023:
            - Updated FusionFix.
            - Changed dxvk to dxvk-gplasync.
        - 19.07.2023:
            - Updated the Downgrader, ZolikaPatch, IV Tweaker, FusionFix, Shader Fixes.
            - Added Radio Downgrader, GTA Online QUB3D Background, Better Wardrobes, Traffic Cops in the Toolbooths, Xbox Rain Droplets, Fixed Pistol Sights.
            - Added Dualsense buttons to optionals.
            - Removed Pedestrians with Unused Clothing Restored and Varied Alderney State Trooper Ped due to potential incompatibilities.
        - 15.07.2023:
            - Added Liberty Tweaks.
        - 13.07.2023:
            - Fixed disappearing assets in Roman's taxi office.
            - Changed FPS limit in cutscenes to 32.
        - 12.07.2023:
            - Updated ZolikaPatch.
            - Added (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec.
            - Moved Various Fixes to update folder due to compatibility issues.
            - Removed TBoGT Texture Quality Fix as Various Fixes already contains this fix fix.
            - Removed TBoGT Vehicle Fix from modloader as FusionFix already contains the fix.
            - Removed IVPresence.
        - 11.07.2023:
            - Fixed the main game crash problem.
        - 10.07.2023:
            - Updated the downgrader.
            - Added FusionFix 1.60 port by Zolika.
            - Fixed TLAD crash, changed Niko's hair file, now has no visual problems.
        - 09.07.2023:
            - Changed the downgrader - now bundled with the archive.
            - Removed IV Fixes and Improvements.
            - Added Various Fixes.
            - Added Dualshock buttons to optionals.
        - 08.07.2023:
            - Updated Shader Fixes.
            - Removed Simple Traffic Loader.
            - Mods completely repacked to use modloader instead.
        - 01.07.2023:
            - Updated Shader Fixes.
            - Repacked some mods.
        - 30.06.2023:
            - Updated Shader Fixes.
        - 26.06.2023:
            - Created the archive.
