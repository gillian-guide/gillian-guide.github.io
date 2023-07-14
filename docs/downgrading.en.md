title: Downgrading
description: Methods for downgrading your GTA IV installation from the Complete Edition to retail patches.

# Downgrading
You may want to downgrade your game to 1.0.8.0 or older retail patches, mainly for mod compatibility. The Complete Edition supports a much smaller number of mods, and mainly doesn't support [ZolikaPatch](Essential-Modding/ZolikaPatch) and [IV Tweaker](modloading.md/#iv-tweaker). 

However, we have several downgraders to choose from.

### Notes
!!! info ""
	1. 1.2.0.59 is the Complete Edition, also known as the latest [:material-steam:Steam](https://store.steampowered.com/app/12210/) or [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv) version. It removes support for multiplayer and Games for Windows - LIVE, while adding the Rockstar Games Launcher (and it's DRM) and the Social Club overlay (with it's achievements). The amount of supported mods is also much more limited in this version - most mods are built for 1.0.8.0 and 1.0.7.0.
	2. 1.0.8.0 is the latest retail patch, with ZolikaPatch and multiplayer support. This version is better for mod compatibility.
    3. 1.0.4.0 is an older retail patch with full ENB compatibility, as well as old shadow algorithm - considered better by some of the community.

## Which downgrade to choose?
That depends vaguely on your goals.
| Advantages | Zolika1351's | ItsClockAndre's |
| :------: | :----------: | :-------------: |
| Downgrading to 1.0.8.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
| Downgrading to 1.0.7.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
| Downgrading to 1.0.4.0 | :material-cancel: | :material-checkbox-marked-circle: |
| Simplicity | :material-checkbox-marked-circle: | :material-plus-minus: |
| The ability to select optional mods | :material-plus-minus: | :material-checkbox-marked-circle: |
| Optional Games for Windows - LIVE support | :material-cancel: | :material-checkbox-marked-circle: |
| Lightweight | :material-checkbox-marked-circle: | :material-cancel: |
| Avoids replacing internal files | :material-checkbox-marked-circle: | :material-cancel: |
| Radio downgrader as a part of downgrading | :material-cancel: | :material-checkbox-marked-circle: |
| Savefile conversion as a part of downgrading | :material-cancel: | :material-checkbox-marked-circle: |
| Support for latest [FusionFix](Essential-Modding/FusionFix) | :material-checkbox-marked-circle: | :material-cancel: |

## Zolika1351's Downgrader
This downgrader is very lightweight, replaces a minimal amount of files, but also doesn't bundle a radio downgrader or a way to downgrade to 1.0.4.0. It bundles [ZolikaPatch](Essential-Modding/ZolikaPatch) and [IV Tweaker](modloading.md/#iv-tweaker), and has optional support for a ported version of [FusionFix](Essential-Modding/FusionFix).

### Installation
- Instructions:
    * Create an antivirus exclusion for your game folder. (Optional, but highly recommended).
    * Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch/downgrading).
    * Download the downgrade archive (version for 1.0.7.0 is lower).
    * Extract the contents of the :material-zip-box:`IV_Downgrade_10x0_vxx.zip` into your game folder, replacing everything if prompted.
    * Run :material-file-download:`vcredist_x86.exe` and let it install.
    * Run the game.
    * If everything works fine, you can also install one of the optional mods listed below (it is not recommended to install both; [FusionFix](Essential-Modding/FusionFix) is preferred).

## ItsClockAndre's Downgrader
This downgrader is online-based and only downloads what you choose to download. It replaces more files than Zolika1351's downgrader, making it harder to restore an installation if you didn't make a backup. This downgrader also has an option to downgrade to 1.0.4.0.

### Installation
- Instructions:
    * Create an antivirus exclusion for your game folder. (Optional, but highly recommended).
    * Go to the [GTAForums page](https://gtaforums.com/topic/976691-gta-iv-downgrader/) and download the latest version.
    * Extract the archive, run :material-file:`IVDowngrader.exe`.
    ??? info "Offline mode"
        You can set up downgrader up for offline use instead. Download the files from [here](https://mega.nz/folder/Fn0Q3LhY#_0t1VZQFuQX22lMxRZNB1A) and extract them to the :material-folder:==Downgrader\\Data\\Temp==. Run :material-file:`LaunchInOfflineMode.exe` instead.
    * Follow the instructions in the application. Be sure to read the warnings at mod selection.
    * If setting up for GFWL support, make sure to check [multiplayer](multiplayer.md). If not, make sure the `xliveless` mod is enabled.
    !!! info ""
        If you somehow missed this step, download the latest [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases) and rename :material-file:`dinput8.dll` to `xlive.dll`