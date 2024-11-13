title: Troubleshooting
description: Why game no work

# Troubleshooting

Anyone can have problems modding their favorite games, and GTA IV is extremely prone to them.

---

## Known issues without a solution

I know about these issues, no need to report them to me, unless you know a solution.

- Cutscenes freeze the game up if the game is out-of-focus for too long.
- Car engine sounds occasionally appear and disappear (the solution involves bringing the taxi bug back - lower the traffic budget in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`).
- Social Club achievements cannot be acquired on downgraded versions.
- Night shadows are limited (intended to reduce bugs).

---

## Known issues & solutions

### Boot issues

??? info "Asi Loader Error | Other Visual C++ issues"
    Make sure you installed the [prerequisite software](../../preparation.md#software).

??? info "Error RMN60 on launch"
    Occurs on downgraded versions. Install [ZolikaPatch](../../essential-modding/zolikapatch.md) (your antivirus may have removed it, aswell).

??? info "Error "SecuLauncher: failed to start application [2000]" on launch"
    - Right click :material-file:`GTAIV.exe`, click **Properties**, switch to the **Compatibility** tab and uncheck **Run this program as an administrator**. If it's already unchecked, see the next solution.
    - Make sure you installed the [prerequisite software](../../preparation.md#software).
    - If even that doesn't solve the issue, install [NET 3.5](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net35-sp1).

??? info "Game doesn't even show up"
    - Make sure you don't have any duplicate mods - for example, you may have left FusionFix in both the :material-folder: ==plugins== folder and the game folder. The game won't start in this case.
    - Reboot your PC.
    - Only launch a downgraded version from :material-steam: Steam or using :material-file:`PlayGTAIV.exe`.
    - If using ZolikaPatch and FusionFix together, disable the [incompatible options](../../essential-modding/zolikapatch.md/#incompatible-options).
    - If the problem persists, try deleting/disabling mods one-by-one to see which one is causing the problem. Usually has something to do with `.asi` mods, so start there.

??? info "Game crashes immediately upon booting"
    - Try turning off RivaTuner Statistics (with MSI Afterburner if using that) or any other software of this sort - overlays can mess the game up on boot.
    - On a downgraded version, try installing [ZolikaPatch](../../essential-modding/zolikapatch.md) if you hadn't already.
    - Try deleting `SETTINGS.cfg` from :material-folder: ==C:/Users/(User)/AppData/Local/Rockstar Games/GTA IV/Settings==.
    - If the problem persists, try deleting/disabling mods one-by-one to see which one is causing the problem. Usually has something to do with injectable mods, so start there.

---

### Load screen issues

??? info "Load times are too long"
    - Remove ColAccel if you had installed it outside of the guide.
    - Remove the `-managed` [launch option](../../additional-setup.md/#launch-options).

??? info "Game loads endlessly"
    Set the `-availablevidmem` [launch option](../../additional-setup.md/#launch-options) (with a value of up to 3072.0).

??? info "Game loads directly into the savegame on startup, no menu"
    You can hold ++lshift++ on boot for when you need the menu.

    If you want to completely disable the feature off, change **Skip Menu** to **Off** in `Settings` - `Game` if using FusionFix. If the feature still triggers, set `SkipMenu` to `0` in :material-file-cog:`ZolikaPatch.ini`.

---

### Settings / performance issues

??? info "Game shows wrong VRAM value in settings"
    Set the `-availablevidmem` [launch option](../../additional-setup.md/#launch-options) (with a value of up to 3072.0).

??? info "The game does not start in desired resolution and there is no option to increase it in the settings"
    Set these [launch options](../../additional-setup.md/#launch-options):

    * `-width (horizontal resolution)`
    * `-height (vertical resolution)`
    * `-refreshrate (refresh rate)`

    Example:

    * `-width 1920`
    * `-height 1080`
    * `-refreshrate 60`

    If that still doesn't help, add `d3d9.forceAspectRatio = 16:9` to :material-file-cog:`dxvk.conf`. Change `16:9` with your *[exact](https://stevewadsworth.github.io/calculateAspectRatio/)* aspect ratio if you don't use a 16:9 monitor.

    Also, check for [GPU driver updates](../../preparation.md/#drivers).

??? info "Poor in-game performance"
    - Make sure that [DXVK](../../optimization.md) is installed correctly.
    - Try using [optimal game settings](../../additional-setup.md/#optimal-game-settings).
    - Make sure `Shader Pre-caching` is disabled in the :material-steam: Steam `Settings` - `Downloads` tab if using DXVK.
    - Make sure you don't have overlays such as Rainmeter running in fullscreen, they can tank your performance greatly.
    - Try lowering the graphics settings, in particular:
        - Shadow Quality
        - Night Shadows
        - View/Detail Distance
        - Depth of Field
        - Motion Blur
        - Reflection Quality

??? info "Constant unstable frame timing after a while of playing (i.e. a microstutter every 0.5 seconds)"
    Try disconnecting your gamepad. If the problem goes away, try enabling or disabling Steam Overlay. If the problem persists, try also enabling or disabling Steam Input alongside.

---

### Crash issues

??? info "Game crashes during or shortly after load screen"
    - Make sure you started with a clean install (after pressing Uninstall on Steam, manually wipe the remainders in the folder).
    - If you have added modded cars and saved them near your savehouse, your savefile is corrupted. Change the saved car using this [software](https://x3t-infinity.com/GTAIV_SE).
    - Your savefile may be corrupted. Try temporarily removing your savefiles and start a new game to see if the problem persists.
    - If the problem persists, try deleting/disabling mods one-by-one to see which one is causing the problem. Usually has something to do with script mods, so start there.

??? info "Game randomly crashes mid-game"
    - If using ZolikaPatch and FusionFix together, disable the [incompatible options](../../essential-modding/zolikapatch.md/#incompatible-options).
    - Open :material-file-cog:`ZolikaPatch.ini` and change `HighFPSSpeedupFix` to `0`.
    - If the problem persists, try deleting/disabling mods one-by-one to see which one is causing the problem.

---

### Gameplay issues

??? info "Broken LODs / textures"
    - Set the `-availablevidmem` [launch option](../../additional-setup.md/#launch-options) (with a value of up to 3072.0).
    - Tone down the amount of texture mods you're using - especially stuff like road textures.

??? info "Can't get into helicopter on last mission | Other timing-related issues at high FPS such as arcades being broken"
    - Install [FusionFix](../../essential-modding/fusionfix.md).
    - Some issues can only be omitted by setting a 60 or 30 FPS lock. Can be done in `Settings` - `Graphics` if using FusionFix.

??? info "Softlock on TLAD - Shifting Weight"
    Open :material-file-cog:`ZolikaPatch.ini` and set `HighFPSSpeedupFix` to `0`. You can put it back to `1` after the mission.

??? info "Cannot access internet cafe computers or interact with entertainment assets (pool, bowling)"
    You can do one of the following:

    - Start a new game and forget about your existing save.
    - Remove `LibertyTweaks` files from :material-folder: ==IVSDKDotNet\scripts== (if you don't use **IV-SDK .NET** for anything else, you can remove safely all files and folders starting with `IVSDKDotNet` from the game folder aswell).

??? info ":material-steam: Steam achievements disappeared after downgrading"
    Install [SteamAchievements](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/).

??? info "GFWL / Xbox Live achievements don't work"
    - Remove :material-file:`SteamAchivements.asi` - you can't use both at once.
    - Set `TryToSkipAllErrors` and `VSyncFix` to `0` in :material-file-cog:`ZolikaPatch.ini`.

---

### Multiplayer issues

??? info ""Unable to connect to game session", "Unable to join a game you were kicked from" or joining an empty lobby in GFWL"
    You were either actually kicked by the host, or you're experiencing what's known as kickbug.

    If you're indeed experiencing kickbug, you have to do manual port forwarding for the following ports in your router's settings and your system's firewall (look online for instructions for your specific router or ISP, or contact your ISP):

    * TCP: `3074`, `80`, `88`
    * UDP: `3074`, `80`, `88`

    If you can't perform port forwarding, use a VPN service instead. I recommend [Mullvad VPN](https://mullvad.net/en).

    Alternatively, give up. Seriously, just give up and try other multiplayer methods - some people are just stuck with the kickbug with no way to fight it.

??? info "GFWL overlay doesn't appear"
    - You are using XLiveless (:fontawesome-solid-gears:`xlive.dll`). Rename the file to `dinput8.dll`.
    - GFWL files are missing. You need :material-file:`GTAIV.exe.cdf`, :material-file-cog:`GTAIV.exe.cfg` and `GTAIV.exe.cat`.
    - Try [reinstalling GFWL](../../extras/multiplayer.md/#gfwl-install).

??? info ""This session no longer exists" in GFWL"
    The license key you're using is also used by somebody else who's already in the lobby. Log out and find yourself a different key or re-run the keygen.

??? info "The game asks to sign in to Social Club in GFWL"
    You need [ZolikaPatch](../../essential-modding/zolikapatch.md).

??? info ""The downloadable content required for this autoload is not available" in GFWL"
    Restart the game.

??? info ""You have been disconnected because your computer is running too slowly" in GFWL"
    - Enable `Windowed`, `Borderless` and disable `Block on Focus Loss` in `Settings` - `Game` if using FusionFix.
        - If not using FusionFix, set `BorderlessWindowed` and `DoNotPauseOnMinimize` to `1` in :material-file-cog:`ZolikaPatch.ini` and add `-windowed` to your :material-file-cog:`commandline.txt` instead.

??? info ""The profile could not be signed in to LIVE" in GFWL"
    - Install the [Xbox App](https://www.xbox.com/en-US/apps/xbox-app-for-pc) and sign in to it with the same account you're trying to use for GFWL.
    - Try [reinstalling GFWL](../../extras/multiplayer.md/#gfwl-install).

??? info "Error code: 0x80048821 or "Password contains special characters" in GFWL"
    [Create a new app password](https://account.live.com/proofs/AppPassword) and use that to log in.

??? info "Error code: 0x8007065b in GFWL"
    Only known solution is to use another account to sign in.

??? info "Error code: 0x80151906 in GFWL"
    [Xbox LIVE servers are likely down at the moment](https://support.xbox.com/en-US/xbox-live-status), try again later.

??? info "Error code: 0x8015403A in GFWL"
    Try logging in on the [website](https://account.xbox.com/Account/Signin).

??? info "Error code: 0x80150001 in GFWL"
    GFWL only allows 100 friends maximum on the account. Reduce your number of friends on the account below 100, then try logging in again.

??? info "Getting kicked by the anticheat in GTAC"
    Your files are likely modified - make sure you're using a clean copy from :material-steam: Steam or :simple-rockstargames: Rockstar Games Launcher.

    The only way to find out which file doesn't pass through is to ask somebody with access to server logs (normally, the owner).

---

### Miscellaneous issues

??? info "I'm using the :simple-rockstargames: Rockstar Games Launcher and my files get constantly replaced"
    After downgrading or using the drag-and-drop archive for 1.0.8.0, avoid using the launcher and start the game with :material-file:`PlayGTAIV.exe` instead.

    Otherwise, if you want to use CE, avoid file replacements and use [modloaders](../../extras/modloading.md).

??? info "Game is using the wrong GPU (NVIDIA laptop)"
    Go to the NVIDIA Control Panel, 3D settings, add :material-file:`GTAIV.exe` and select `Max Performance` in `Power Plan Mode`.

??? info "EFLC disappeared after downgrading"
    Make sure you are using [ZolikaPatch](../../essential-modding/zolikapatch.md) and set `LoadDLCs` to `1` in :material-file-cog:`ZolikaPatch.ini`.

??? info ".NET mods don't work on Linux"
    See [Getting ScriptHookDotNet and IV-SDK .NET to work on Linux](mod-dependencies.md/#getting-scripthookdotnet-and-iv-sdk-net-to-work-on-linux)

---

If you know an issue and a solution that I missed, [let me know on the Discord server](../../index.md/#navigation).
