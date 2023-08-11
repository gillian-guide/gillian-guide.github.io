title: Troubleshooting
description: Troubleshooting your GTA IV issues.

# Troubleshooting
Anyone can have problems modding their favorite games, and GTA IV is extremely prone to this.
??? info "I'm using the Rockstar Games Launcher and can't install mods!"
    After downgrading or using the drag-and-drop archive, avoid using the launcher and start the game with :material-file:`PlayGTAIV.exe` instead.

??? info "The game does not start in desired resolution and there is no option to increase it in the settings"
    After installing [DXVK](optimization.md), set these [launch options](../additional-setup/#launch-options):

    * `-width (horizontal resolution)`
    * `-height (vertical resolution)`
    * `-refreshrate (refresh rate)`

    Example:

    * `-width 1920`
    * `-height 1080`
    * `-refreshrate 60`

    Also, check for [GPU driver updates](../optimization/#drivers).

??? info "Game performance is still poor"
    Make sure that [DXVK](optimization.md) is installed correctly, and that the [optimal game settings](../additional-setup/#optimal-game-settings) are used.

??? info "Load times got even longer"
    Remove ColAccel. It doesn't work properly for some people for some reason.

??? info "Can't get into helicopter on last mission | Other timing-related issues at high FPS"
    Install [FusionFix](essential-modding/fusionfix.md) and enable the `FPS limiter` in Settings - Display and set it to 60 FPS.

??? info "Game loads directly into the savegame on startup, no menu"
    You can hold ++lshift++ on boot for when you need the menu.
    
    If you want to completely disable the feature off, open :material-file-cog:`GTAIV.EFLC.FusionFix.ini` and change `SkipMenu` to `0` (or go to Settings - Game and change `Skip Menu` to Off). If the problem persists, open the :material-file-cog:`ZolikaPatch.ini` and change the setting there.

??? info "Game loads endlessly when loading saves | Constantly missing textures | Game shows wrong VRAM value in settings"
    Set the `-availablevidmem` [launch option](../additional-setup/#launch-options) (with a value of up to 3072.0).

??? info "Random but constant frame timing problems (i.e. a microstutter every 0.5 seconds)"
    Try disconnecting your gamepad. If the problem goes away, try enabling Steam Overlay. If the problem persists, try enabling Steam Input as well.

??? info "Asi Loader Error | Other Visual C++ issues"
    Install [prerequisites](index.md).

??? info ":material-steam:Steam Achievements don't work after downgrading"
    You have probably set up your install to be [GFWL](../multiplayer/#games-for-windows-live)-compatible - the script will not work in this case.

??? info "RMN60 error on launch"
    Reinstall [ZolikaPatch](essential-modding/zolikapatch.md). Your antivirus is likely at fault - disable it or add the game folder to exceptions.

??? info "Game crashes"
    Make sure you started with a clean install. After installing any mods, make sure your game is working properly by starting it at least once in game to pinpoint the problematic mod.

??? info "Game crashes immediately upon booting | Won't even boot"
    * Reboot your PC.
    * Make sure you don't have any duplicate mods - for example, you may have left [FusionFix](essential-modding/fusionfix.md) in both the :material-folder:==plugins== and the game folder. The game won't start in this case.
    * Only launch from :material-steam:Steam or using :material-file:`PlayGTAIV.exe`.
    * If you have downgraded to 1.0.4.0, delete :material-file-cog:`settings.cfg` in :material-folder:==C:/Users/(PC Name)/AppData/Local/Rockstar Games/GTA IV/Settings==.
    * Make sure MSI Afterburner and/or RivaTuner Statistics and any other software of this sort is not running - overlays mess the game up on boot.
    * Install [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) (and set it up to get rid of GFWL) and [ZolikaPatch](essential-modding/zolikapatch.md).
    * If the problem persists, try deleting or disabling each mod to see which one is causing the problem.

??? info "Game crashes during or after load"
    * Make sure you started with a clean install (after pressing Uninstall on Steam, manually wipe the remainders in the folder).
    * A corrupted save file can be a problem if you were playing on a newer version before downgrading. This can be fixed by [downgrading your savefile](../downgrading/#downgrading-the-savefile).
    * If you have added modded cars and saved them near your savehouse, your savefile may be corrupted. Change the saved car using this [software](https://x3t-infinity.com/GTAIV_SE).
    * If the problem persists, try deleting or disabling each mod to see which one is causing the problem.

??? info "Game randomly crashes mid-game"
    One of your mods is unstable. Don't install too many mods.

??? info "Game is using the wrong GPU (NVIDIA laptop)"
    Go to the NVIDIA Control Panel, 3D settings, add :material-file:`gtaiv.exe` and select `Max Performance` in `Power Plan Mode`.

If you know an issue and a solution that I missed, [contact me!](contact-me.md)

[:material-page-first:Previous page <br>Credits</br>](credits.md){ .md-button } [Next page:material-page-last: <br>Discord Server</br>](contact-me.md){ .md-button .md-button--primary }