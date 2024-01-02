title: Downgrading
description: Methods for downgrading your GTA IV installation from the Complete Edition to retail patches

# Downgrading
You may want to downgrade your game to 1.0.8.0 or older retail patches, mainly for mod compatibility. The Complete Edition supports a much smaller number of mods, and mainly doesn't support [ZolikaPatch](essential-modding/zolikapatch.md), Liberty Tweaks and [IV Tweaker](../extras/modloading/#iv-tweaker). 

Go through each big section to complete the downgrading or only the [Downgrading the radio](#downgrading-the-radio) section if you're only interested in doing that.

## Downgrading the game
### Notes
!!! info ""
	1. 1.2.0.59 is the Complete Edition, also known as the latest [:material-steam:Steam](https://store.steampowered.com/app/12210/) or [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv) version. It removes support for multiplayer and Games for Windows - LIVE, while adding the Rockstar Games Launcher (and it's DRM) and the Social Club overlay (with it's achievements). ==The amount of supported mods is also much more limited in this version - most mods are built for 1.0.8.0 and 1.0.7.0.==
	2. 1.0.8.0 is the latest retail patch, with ZolikaPatch and multiplayer support. ==This version is better for mod compatibility.==
    3. 1.0.4.0 is an older retail patch with full ENB compatibility, as well as old shadow algorithm - considered better by some of the community. A lot of things listed on the guide won't work with 1.0.4.0 however - and I don't provide support for it.

### Which downgrader to choose?
It depends vaguely on your goals. If you want something as simple as a drag&drop archive - go with mine or Zolika1351's. If you want something more in-depth - go with ItsClockAndre's.

???+ question "Comparison"
    * :material-plus-minus: means "Partially" or "Not as good".

    | Advantages | Gillian's | Zolika1351's | ItsClockAndre's |
    | :--------: | :-------: | :----------: | :-------------: |
    | Downgrading to 1.0.8.0 and 1.0.7.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Downgrading to 1.0.4.0 | :material-cancel: | :material-cancel: | :material-checkbox-marked-circle: |
    | Simplicity | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Lightweight | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Optional [GFWL](../multiplayer/#games-for-windows-live) support | :material-checkbox-marked-circle: | :material-cancel: | :material-checkbox-marked-circle: |
    | Radio downgrading | :material-plus-minus: | :material-cancel: | :material-checkbox-marked-circle: |

=== "[Gillian's GTA IV Downgrade Utility](https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF)"
    I've made my own downgrader for my own purposes. I don't intend this to be a replacement to the other two, nor in any way necessarily superior - simply my own alternative. Though, it does offer a few benefits - it attempts to keep the mods up-to-date and doesn't let you do "stupid" downgrades with the toggles logic. You can also just open it, select your folder and press `Downgrade` without toggling anything else.

    ???+ note "Usage"
        * Go to the [Releases](https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF/releases/latest) page.
        * Download :material-zip-box:`GTAIVDowngradeUtilityWPF.zip`.
        * Unpack the archive in any desired folder.
        * Open the tool.
        * Select your game folder.
        * Toggle anything if your heart desires to. Defaults are fine, but you may want to disable the GFWL toggle.
        * Press `Backup` if you want to have a backup. It will be stored in :material-folder:==backup== in your game folder.
        * Press `Install redistributables` to download and install Visual C++, DirectX and GFWL redistributables.
        * Press `Downgrade` to, well, downgrade.

        Tool will hang when using `Downgrade` or `Install redistributables`, this is normal. Unless it closes. Then it's not - submit a GitHub Issue with the log.

=== "[Zolika1351's Downgrader (ZolikaPatch)](https://zolika1351.pages.dev/mods/ivpatch)"
    This downgrader is very lightweight and replaces a minimal amount of files (which strays this downgrade from a true retail version), but also doesn't bundle a radio downgrader or a way to downgrade to 1.0.4.0. It automatically handles all dependencies and downgrades the mods you already had installed. It is not compatible at all with [Games for Windows - LIVE](../multiplayer/#games-for-windows-live), however.

    ???+ note "Installation"
        * Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch).
        * Scroll to the bottom of the page and download the latest version.
        * Extract :material-zip-box:`ZolikaPatch_vx_x.zip` into the game folder.
        * You will be prompted to downgrade when opening the game, press Yes. It'll automatically handle everything.
        ??? note "Downgrading to 1.0.7.0"
            This tool is only intended to downgrade to 1.0.8.0. For 1.0.7.0, instead, follow these instructions:

            * Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivmenu/downgrading).
            * Scroll to the bottom and download the 1.0.7.0 archive.
            * Extract the contents of the :material-zip-box:`IV_Downgrade_1070_vxx.zip` into the game folder, replacing everything if prompted.
            * Run :material-file-download:`vcredist_x86.exe` and let it install.

=== "[ItsClockAndre's Downgrader](https://gtaforums.com/topic/976691-gta-iv-downgrader/)"
    This downgrader is online-based and only downloads what you choose to download. It replaces more files than Zolika1351's downgrader, making it harder to restore an installation if you haven't made a backup, but it also makes this downgrader closer to a true retail version. This downgrader may bundle outdated files. This downgrader also has an option to downgrade to 1.0.4.0.

    ???+ note "Installation"
        * Create an antivirus exclusion for your game folder (optional, but highly recommended).
        * Go to the [GTAForums page](https://gtaforums.com/topic/976691-gta-iv-downgrader/) and download the latest version.
        * Extract the archive, run :material-file:`IVDowngrader.exe` with :fontawesome-solid-shield-halved:==administrator rights==.
        ??? info "Offline mode"
            You can set up downgrader up for offline use instead. Download the files from [here](https://mega.nz/folder/Fn0Q3LhY#_0t1VZQFuQX22lMxRZNB1A) and extract them into the :material-folder:==Downgrader\\Data\\Temp==. Run :material-file:`LaunchInOfflineMode.exe` instead.
        * Follow the instructions in the application. Be sure to read the warnings at mod selection.
        * If setting up for GFWL support, see [multiplayer](../multiplayer/#games-for-windows-live). If not, make sure the `xliveless` mod is enabled.
        !!! info ""
            If you somehow missed this step, set up [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) to get rid of GFWL.

!!! warning ""
    [Launch options](additional-setup.md) need to be moved to :material-file-cog:`commandline.txt` after downgrading.

    After downgrading, always launch the game using :material-file:`PlayGTAIV.exe` or `Play` button on Steam. Additionally, your game folder can be moved elsewhere if you desire so.

## Downgrading the radio
Over 50 radio station tracks were removed from the game in April 2018 due to expired licenses. We can restore them, however.
???+ note "Installation"
    * Go to the [Various GTA Downgraders website](http://downgraders.rockstarvision.com/) and scroll to the bottom of the page.
    * Download the Radio Restoration mod for GTAIV CE.
    * Extract the :material-zip-box:`GTAIVCERADIORESTOREINSTALLER.zip` into any empty folder.
    * Run :material-file-download:`IVCERadioRestorer.exe` and follow the in-app instructions. Pick to install [FusionFix](essential-modding/fusionfix.md) if you didn't install it beforehand (install manually on older patches).
    ???+ question "What's the difference between only pre-cut Vladivostok and pre-+post-cut?"
        Rockstar added new tracks to Vladivostok to replace the cut ones. Pre-+post-cut keeps these alongside the restored cut ones, while only pre-cut songs cuts them out, only keeping the restored ones.
    ???+ tip "Addons"
        There are serveral addons - see them [here](https://www.nexusmods.com/gta4/mods/234?tab=files)

## Downgrading the savefile
!!! note ""
    You don't need to go through this stage if you used [ZolikaPatch](essential-modding/zolikapatch.md) with it's downgrader.

If you've already started playing on the Complete Edition, you may want to downgrade your savefile to retail version.

???+ note "Instructions"
    * First, locate your savefiles in :material-folder:==Documents\Rockstar Games\GTA IV\Profiles\(id)\\==. They're named :material-file:`SGTAxxx`.
    * Upload the one you want to convert to [GTASnP](https://gtasnp.com/).
    * Expand the `Modifications` tab.
    * Pick `1.0.8.0 IV / 1.1.3.0 EFLC and older` in `Downgrade Version`.
    * Pick the slot you want to save your savefile as. You'll download your converted savefile.
    * Place it at :material-folder:==C:\Users\(user)\AppData\Local\Rockstar Games\GTA IV\savegames\user_(id)\\==.

[:material-page-first:Previous page <br>Additional Setup</br>](additional-setup.md){ .md-button } [Next page:material-page-last: <br>Mod Dependencies</br>](mod-dependencies.md){ .md-button .md-button--primary }