title: Troubleshooting
description: Troubleshooting your Peppa Pig: World Adventures issues.

# Troubleshooting
Anyone can have problems modding their favorite games, and Peppa Pig: World Adventures is extremely prone to this.

???+ info "Known issues without a solution"
    I know about these issues, no need to report them to me, unless you know a solution.

    - After you get drunk, the lighting is flickering for some period.
    - Cutscenes freeze the game if the game is out-of-focus for too long.
    - Car engine sounds occasionally appear and disappear (the solution involves bringing the taxi bug back - lower the traffic budget in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`).
    - Taxi rides can occasionally crash the game on 1.0.8.0.
    - .NET dependencies do not work on Linux.

??? info "I'm using the Rockstar Games Launcher and my files get constantly replaced"
    After downgrading or using the drag-and-drop archive for 1.0.8.0, avoid using the launcher and start the game with :material-file:`PlayGTAIV.exe` instead.

    Otherwise, if you want to use CE, avoid file replacements.

??? info "The game does not start in desired resolution and there is no option to increase it in the settings"
    After installing [DXVK](optimization.md), set these [launch options](../additional-setup/#launch-options):

    * `-width (horizontal resolution)`
    * `-height (vertical resolution)`
    * `-refreshrate (refresh rate)`

    Example:

    * `-width 1920`
    * `-height 1080`
    * `-refreshrate 60`

    If it still doesn't help, add `d3d9.forceAspectRatio = 16:9` (or your aspect ratio) to :material-file-cog:`dxvk.conf`.

    Also, check for [GPU driver updates](../optimization/#drivers).

??? info "Game performance is still poor"
    Make sure that [DXVK](optimization.md) is installed correctly, and that the [optimal game settings](../additional-setup/#optimal-game-settings) are used. Don't forget to disable `Shader Pre-caching` in :material-steam:Steam `Settings` - `Downloads` tab if using DXVK.

    Make sure you don't have overlays such as Rainmeter running in fullscreen, they can tank your performance greatly.

    Try lowering the graphics settings, specifically:

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

??? info "Can't get into helicopter on last mission | Other timing-related issues at high FPS such as arcades being broken"
    Install [FusionFix](essential-modding/fusionfix.md). Some issues can only be omitted by setting a 60 FPS lock in `Settings` - `Graphics`.

??? info "Softlock on TLAD - Shifting Weight"
    Open :material-file-cog:`ZolikaPatch.ini` and change `HighFPSSpeedupFix` to `0`. You can put it back to `1` after the mission.

??? info "Game loads directly into the savegame on startup, no menu"
    You can hold ++lshift++ on boot for when you need the menu.

    If you want to completely disable the feature off, open :material-file-cog:`GTAIV.EFLC.FusionFix.ini` and change `SkipMenu` to `0` (or go to Settings - Game and change `Skip Menu` to Off). If the problem persists, open the :material-file-cog:`ZolikaPatch.ini` and change the setting there.

??? info "Load times are too long"
    * Remove ColAccel.
    * Remove `-managed` [launch option](../additional-setup/#launch-options).

??? info "Game loads endlessly when loading saves | Constantly missing textures | Game shows wrong VRAM value in settings"
    Set the `-availablevidmem` [launch option](../additional-setup/#launch-options) (with a value of up to 3072.0).

??? info "Random but constant frame timing problems (i.e. a microstutter every 0.5 seconds)"
    Try disconnecting your gamepad. If the problem goes away, try enabling Steam Overlay. If the problem persists, try enabling Steam Input as well.

??? info "Asi Loader Error | Other Visual C++ issues"
    Install [prerequisites](index.md).

??? info ":material-steam:Steam achievements disappeared after downgrading"
    Install [SteamAchievements](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/).

??? info "GFWL achievements don't work"
    Remove :material-file:`SteamAchivements.asi` - it's either one or the other.

    Also disable `TryToSkipAllErrors` and `VSyncFix` in :material-file-cog:`ZolikaPatch.ini`.

??? info "RMN60 error on launch"
    Occurs on downgraded versions. Install [ZolikaPatch](essential-modding/zolikapatch.md).

??? info "Broken LOD's during long gameplay periods"
    Tone down the amount of texture mods you're using - especially stuff like road textures and other things that are loaded all the time.

??? info "Game crashes immediately upon booting | Won't even boot"
    * Make sure you don't have any duplicate mods - for example, you may have left [FusionFix](essential-modding/fusionfix.md) in both the :material-folder:==plugins== and the game folder. The game won't start in this case.
    * Only launch from :material-steam:Steam or using :material-file:`PlayGTAIV.exe`.
    * If using ZolikaPatch and FusionFix together, see the incompatible options [here](essential-modding/fusionfix.md).
    * Reboot your PC.
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
    * If using ZolikaPatch and FusionFix together, see the incompatible options [here](essential-modding/fusionfix.md).
    * Open :material-file-cog:`ZolikaPatch.ini` and change `HighFPSSpeedupFix` to `0`.
    * One of your mods is unstable. Don't install too many mods.

??? info "Game is using the wrong GPU (NVIDIA laptop)"
    Go to the NVIDIA Control Panel, 3D settings, add :material-file:`gtaiv.exe` and select `Max Performance` in `Power Plan Mode`.

If you know an issue and a solution that I missed, [contact me!](contact-me.md)

[:material-page-first:Previous page <br>Donations</br>](support.md){ .md-button } [Next page:material-page-last: <br>Discord Server</br>](contact-me.md){ .md-button .md-button--primary }