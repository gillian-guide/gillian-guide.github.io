title: Downgrading the game
description: Downgrading the game version and the savefiles back to the retail version.

# Downgrading the game

## Downgrading process

??? question "Which downgrader to choose"
    It depends vaguely on your goals. If you want something as simple as pressing two buttons - go with mine. If you want something more in-depth - go with ItsClockAndre's.

    * :material-plus-minus: means "Partially" or "Not as good".

    | Advantages | Gillian's | ItsClockAndre's |
    | :--------: | :-------: | :-------------: |
    | Downgrading to 1.0.8.0 and 1.0.7.0 | :material-checkbox-marked-circle: |  :material-checkbox-marked-circle: |
    | Downgrading to 1.0.4.0 | :material-cancel: | :material-checkbox-marked-circle: |
    | Simplicity | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Lightweight | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Optional [GFWL](../multiplayer/#games-for-windows-live) support | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Radio downgrading | :material-plus-minus: | :material-checkbox-marked-circle: |

=== "[Gillian's GTA IV Downgrade Utility](https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF)"
    I've made my own downgrader for my own purposes. I don't intend this to be a replacement to Clonk's, nor in any way necessarily superior - simply my own alternative. Though, it does offer a few benefits - it attempts to keep the mods up-to-date and doesn't let you do "stupid" downgrades with the toggles logic. You can also just open it, select your folder and press `Downgrade` without toggling anything else.

    ???+ note "Usage"
        - Go to the [Releases](https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF/releases/latest) page.
        - Download :material-zip-box:`GTAIVDowngradeUtilityWPF.zip`.
        - Unpack the archive in any desired folder.
        - Open the tool.
        - Select your game folder.
        - Toggle anything if your heart desires to. Defaults are fine, but you may want to disable the GFWL toggle.
        - Press `Downgrade` to, well, downgrade. It will automatically download and install everything.

=== "[ItsClockAndre's Downgrader](https://gtaforums.com/topic/976691-gta-iv-downgrader/)"
    This downgrader is online-based and only downloads what you choose to download. It replaces more files than Zolika1351's downgrader, making it harder to restore an installation if you haven't made a backup, but it also makes this downgrader closer to a true retail version. This downgrader may bundle outdated files. This downgrader also has an option to downgrade to 1.0.4.0.

    ???+ note "Installation"
        - Create an antivirus exclusion for your game folder (optional, but highly recommended).
        - Go to the [GTAForums page](https://gtaforums.com/topic/976691-gta-iv-downgrader/) and download the latest version.
        - Extract the archive, run :material-file:`IVDowngrader.exe` with :fontawesome-solid-shield-halved:==administrator rights==.
        ??? info "Offline mode"
            You can set up downgrader up for offline use instead. Download the files from [here](https://mega.nz/folder/Fn0Q3LhY#_0t1VZQFuQX22lMxRZNB1A) and extract them into the :material-folder:==Downgrader\\Data\\Temp==. Run :material-file:`LaunchInOfflineMode.exe` instead.
        - Follow the instructions in the application. Be sure to read the warnings at mod selection.
        - If setting up for GFWL support, see [multiplayer](../multiplayer/#games-for-windows-live). If not, make sure the `xliveless` mod is enabled.
        !!! info ""
            If you somehow missed this step, set up [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) to get rid of GFWL.

!!! warning ""
    [Launch options](additional-setup.md) need to be moved to :material-file-cog:`commandline.txt` after downgrading.

    After downgrading, always launch the game using :material-file:`PlayGTAIV.exe` or `Play` button on Steam. Additionally, your game folder can be moved elsewhere if you desire so.

## Downgrading the savefile

If you've already started playing on the Complete Edition, you may want to downgrade your savefile to retail version.

???+ note "Instructions"
    - First, locate your savefiles in :material-folder:==Documents\Rockstar Games\GTA IV\Profiles\(id)\\==. They're named :material-file:`SGTAxxx`.
    - Upload the one you want to convert to [GTASnP](https://gtasnp.com/).
    - Expand the `Modifications` tab.
    - Pick `1.0.8.0 IV / 1.1.3.0 EFLC and older` in `Downgrade Version`.
    - Pick the slot you want to save your savefile as. You'll download your converted savefile.
    - Place it at :material-folder:==C:\Users\(user)\AppData\Local\Rockstar Games\GTA IV\savegames\user_(id)\\==.

[:material-page-first:Previous page <br>Additional Setup</br>](additional-setup.md){ .md-button } [Next page:material-page-last: <br>Mod Dependencies</br>](mod-dependencies.md){ .md-button .md-button--primary }
