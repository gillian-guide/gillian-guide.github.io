title: Downgrading
description: Methods for downgrading your GTA IV installation from the Complete Edition to retail patches


# Downgrading
You may want to downgrade your game to 1.0.8.0 or older retail patches, mainly for mod compatibility. The Complete Edition supports a much smaller number of mods, and mainly doesn't support [ZolikaPatch](essential-modding/zolikapatch.md), Liberty Tweaks and [IV Tweaker](../extras/modloading/#iv-tweaker). 

However, we have several downgraders to choose from.

### Notes
!!! info ""
	1. 1.2.0.59 is the Complete Edition, also known as the latest [:material-steam:Steam](https://store.steampowered.com/app/12210/) or [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv) version. It removes support for multiplayer and Games for Windows - LIVE, while adding the Rockstar Games Launcher (and it's DRM) and the Social Club overlay (with it's achievements). ==The amount of supported mods is also much more limited in this version - most mods are built for 1.0.8.0 and 1.0.7.0.==
	2. 1.0.8.0 is the latest retail patch, with ZolikaPatch and multiplayer support. ==This version is better for mod compatibility.==
    3. 1.0.4.0 is an older retail patch with full ENB compatibility, as well as old shadow algorithm - considered better by some of the community.
!!! warning ""
    After downgrading, always launch the game using :material-file:`PlayGTAIV.exe` or `Play` button on Steam. Additionally, your game folder can be moved elsewhere if you desire so.

## Which downgrader to choose?
It depends vaguely on your goals. If you want something as simple as a drag&drop archive - go with Zolika1351's. If you want something more in-depth - go with ItsClockAndre's.

???+ question "Comparison"
    * :material-plus-minus: means "Partially" or "Not as good".

    | Advantages | Zolika1351's | ItsClockAndre's |
    | :--------: | :----------: | :-------------: |
    | Downgrading to 1.0.8.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Downgrading to 1.0.7.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Downgrading to 1.0.4.0 | :material-cancel: | :material-checkbox-marked-circle: |
    | Simplicity | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Lightweight | :material-checkbox-marked-circle: | :material-plus-minus: |
    | The ability to select optional mods | :material-plus-minus: | :material-checkbox-marked-circle: |
    | Optional [GFWL](../multiplayer/#games-for-windows-live) support | :material-cancel: | :material-checkbox-marked-circle: |
    | Radio downgrader as a part of downgrading | :material-cancel: | :material-checkbox-marked-circle: |
    | Savefile conversion as a part of downgrading | :material-cancel: | :material-checkbox-marked-circle: |

## Zolika1351's Downgrader
This downgrader is very lightweight and replaces a minimal amount of files(which strays this downgrade from a true retail version), but also doesn't bundle a radio downgrader or a way to downgrade to 1.0.4.0. It bundles [ZolikaPatch](essential-modding/zolikapatch.md).md and [IV Tweaker](../extras/modloading/#iv-tweaker), and has optional support for a ported version of [FusionFix](essential-modding/fusionfix.md). It is not compatible at all with [Games for Windows - LIVE](../multiplayer/#games-for-windows-live), however.

???+ note "Installation"
    * Create an antivirus exclusion for your game folder. (Optional, but highly recommended).
    * Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch/downgrading).
    * Download the downgrade archive (version for 1.0.7.0 is lower).
    * Extract the contents of the :material-zip-box:`IV_Downgrade_10x0_vxx.zip` into the game folder, replacing everything if prompted.
    * Run :material-file-download:`vcredist_x86.exe` and let it install.
    * Run the game.
    * If everything works fine, you can also install one of the optional mods listed below (it is not recommended to install both; [FusionFix](essential-modding/fusionfix.md) is preferred).

## ItsClockAndre's Downgrader
This downgrader is online-based and only downloads what you choose to download. It replaces more files than Zolika1351's downgrader, making it harder to restore an installation if you haven't made a backup, but it also makes this downgrader closer to a true retail version. This downgrader may also not be as up to date as Zolika1351's. This downgrader also has an option to downgrade to 1.0.4.0.

???+ note "Installation"
    * Create an antivirus exclusion for your game folder. (Optional, but highly recommended).
    * Go to the [GTAForums page](https://gtaforums.com/topic/976691-gta-iv-downgrader/) and download the latest version.
    * Extract the archive, run :material-file:`IVDowngrader.exe` with :fontawesome-solid-shield-halved:==admin rights==.
    ??? info "Offline mode"
        You can set up downgrader up for offline use instead. Download the files from [here](https://mega.nz/folder/Fn0Q3LhY#_0t1VZQFuQX22lMxRZNB1A) and extract them into the :material-folder:==Downgrader\\Data\\Temp==. Run :material-file:`LaunchInOfflineMode.exe` instead.
    * Follow the instructions in the application. Be sure to read the warnings at mod selection.
    * If setting up for GFWL support, see [multiplayer](../multiplayer/#games-for-windows-live). If not, make sure the `xliveless` mod is enabled.
    !!! info ""
        If you somehow missed this step, set up [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) to get rid of GFWL.

## Radio Downgrader
!!! note ""
    This downgrader can be used on both Complete Edition and downgraded versions. Read notes below.

    This downgrader is already a part of [ItsClockAndre's Downgrader](#itsclockandres-downgrader) if you didn't skip the radio downgrading stage - you can skip this part in that case.
Over 50 radio station tracks were removed from the game in April 2018 due to expired licenses. We can restore them, however.
???+ note "Installation"
    * Get latest [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) for the modloader (also get latest [ZolikaPatch](essential-modding/zolikapatch.md) if you're using downgraded copies; we can get around this, read the note later)
    * Go to the [Various GTA Downgraders website](http://downgraders.rockstarvision.com/) and scroll to the bottom of the page.
    * Download the Radio downgrader for GTA IV.
    * Extract the :material-zip-box:`IVCE_RADIO_DOWNGRADER.rar` into the game folder (excl. :material-folder:`... new vladivostok` folders).
    * Run :material-file-download:`install.bat` and wait until the console closes itself.
    * Now extract the contents of either the :material-folder:`with new vladivostok` or :material-folder:`without new vladivostok` into the game folder.
    ???+ question "What's the difference?"
        Rockstar added new tracks to Vladivostok to replace the cut ones. :material-folder:`with new vladivostok` keeps these alongside the restored cut ones, while :material-folder:`without new vladivostok` cuts them out, only keeping the restored ones.
    ???+ tip "Addons"
        There are serveral addons - see them [here](https://www.nexusmods.com/gta4/mods/234?tab=files)
    ??? question "How to get around using Ultimate ASI Loader?"
        Move the contents of the :material-folder:`update` folder to the game folder, replacing files when prompted.

## Downgrading the savefile
If you've already started playing on the Complete Edition, you may want to downgrade your savefile to retail version.

* First, locate your savefiles in :material-folder:==Documents\Rockstar Games\GTA IV\Profiles\(id)\\==. They're named :material-file:`SGTAxxx`.
* Upload the one you want to convert to [GTASnP](https://gtasnp.com/).
* Expand the `Modifications` tab.
* Pick `1.0.8.0 IV / 1.1.3.0 EFLC and older` in `Downgrade Version`.
* Pick the slot you want to save your savefile as. You'll download your converted savefile.
* Place it at :material-folder:==C:\Users\(user)\AppData\Local\Rockstar Games\GTA IV\savegames\user_(id)\\==.

[:material-page-first:Previous page <br>Additional Setup</br>](additional-setup.md){ .md-button } [Next page:material-page-last: <br>Mod Dependencies</br>](mod-dependencies.md){ .md-button .md-button--primary }