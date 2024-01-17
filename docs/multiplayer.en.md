title: Multiplayer
description: Experience GTA IV Multiplayer!

# Multiplayer
GTA IV had an amazing multiplayer... and it still does! Rockstar Games has removed the multiplayer from the Complete Edition, but there's HappinessMP for CE, and you can always [downgrade](downgrading.md) to have the original experience. If you're tired of GTA Online and want something more classic, you should definitely check out GTA IV's multiplayer!
!!! warning ""
    Most multiplayer methods require [downgrading](downgrading.md).

    It's recommended to have [ZolikaPatch](essential-modding/zolikapatch.md) set up for a better multiplayer experience. Make sure to configure :material-file-cog:`ZolikaPatch.ini` to use multiplayer functions and set `DoNotPauseOnMinimize` to `1`.

    Make sure to have `RecoilFix` set to `0` in :material-file-cog:`GTAIV.EFLC.FusionFix.ini` to avoid being at disadvantage with other players.

    Additionally, you may want to have [ZMenuIV](../extras/trainers/#ZMenuIV) for the ability to create and participate in [custom gamemodes](https://grandtheftrevivalforums.com/thread/9/all-community-game-mode-rules).

    You can also use [this](https://www.gtainside.com/en/gta4/mods/160558-gta-iv-and-eflc-all-multiplayer-clothes-are-unlocked/) to unlock all multiplayer clothing for customization.

    Avoid using overhaul, addition or replacement [mods](extras/mods.md).

## Games for Windows - LIVE
!!! note ""
    This section also includes steps to configure GFWL for non-multiplayer use too, if you came here from other pages. Just skip the "Joining/Creating Lobbies" part.
!!! warning "Compatibility"
    This method is only compatible with patches 1.0.7.0 and 1.0.8.0. It's also compatible with older patches, but they'll be put into separate lobbies. [Downgrade](downgrading.md) if using the Complete Edition.
The classic multiplayer method, the one that started it all. And the one that is obnoxiously annoying to set up. Most communities stick to it at the moment.

### Usage
???+ info "Installation"
    !!! note ""
        This step is already taken care of by [ItsClockAndre's downgrader](downgrading.md) if you chose to configure the install for GFWL. Skip it if you did.

    * Make sure you don't have an outdated installation of GFWL Marketplace and LIVE. Remove them if you do.
    * Install [Microsoft Visual C++ 2005 Redistributable **x86**](https://www.microsoft.com/en-us/download/details.aspx?id=26347).
    * Download latest [GFWL Redistributables](https://community.pcgamingwiki.com/files/file/1012-microsoft-games-for-windows-live/).
    * Install :material-file-download:`gfwllivesetup.exe`, :material-file-download:`wllogin_64.msi` and :material-file-download:`xliveredist.msi`.
    !!! question "What's the Marketplace?"
        While you do get the Marketplace, don't bother opening it or trying to make it work. Marketplace is not functional, but still must be installed for GFWL itself to work.
???+ info "Signing in"
    !!! warning ""
        This is using the same account as your [Microsoft](https://microsoft.com/account) or [Xbox](https://xbox.com/account) account. Create one if you don't already have one.

        [Disable 2FA completely on the account](https://account.microsoft.com/security) to be able to sign in. You can turn it back on after you're signed in and set to sign in automatically.

    * Make sure you don't have :fontawesome-solid-gears:`xlive.dll` in the game folder - rename it to :fontawesome-solid-gears:`dinput8.dll` if you do.
    * Open the game.
    * Press the ++home++ key on your keyboard. You'll be met with the startup screen.
    !!! note ""
        If the startup screen did not appear or you're met with an error when opening the game, re-read the instructions from the start.
    * Click `Use Existing LIVE Profile` to get the sign in screen.
    * Uncheck `Save my e-mail address` and `Save my e-mail address and password`.
    * Enter your [Microsoft](https://microsoft.com/account) or [Xbox](https://xbox.com/account) account credentials to sign in.  ==Check `Sign me in automatically` for convenience and to be able to turn 2FA back on.==
    * Make yourself a cup of tea or do whatever you want for the next 5-10 minutes. I'm not kidding - it might take that long to log in. ==Don't think it's stuck - it's not.==
    * See the next part for activation.
???+ tip "Activation"
    We now have several ways to activate the game.
    === "Buying a GFWL key or game"
        One of the ways to activate the game is to own a GFWL key. Although you'll share it with a lot of other people - it'll still be "yours", so to say.

        First, check if you already own any game with [Legacy (Per-Title 5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) - you may already own one of these games - check if their CD Key works for you.

        After you've made sure you don't have one already, you can look for a GFWL key on some marketplaces or such. Or, you can buy one of these two Steam games, that are the only ones that still sell a GFWL key as of December 2023. That might change in the future. Don't worry, you can refund the game after you've acquired the key.

        <iframe src="https://store.steampowered.com/widget/32420/" frameborder="0" width="646" height="190"></iframe>

        <iframe src="https://store.steampowered.com/widget/10460/" frameborder="0" width="646" height="190"></iframe>

        After buying the game, go to the library, select the game and right click - Manage - CD keys and copy the key somewhere. You can refund it now.
    === "Trying out random GFWL keys online"
        This one is pretty self-explanatory - just go around online and look for random GFWL keys - preferably with [Legacy (Per-Title 5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) - they have multiple uses, so you might get lucky. These two Discord servers might help you:

        [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary } [:simple-discord: Games For Windows Live Hub](https://discord.gg/d97u73k2TV){ .md-button .md-button--primary }
    === "RevIVal's community method"
        The channel with the activation method is `#gfwl-keys` (for promotion and respect reasons, I won't link it here directly), but check out the server itself too, we're welcome to anyone!

        [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }
    After you acquired the key and activated the game(again, this might take another 5-10 minutes, so get yourself a tea or something), you're ready to play!
???+ tip "Joining/Creating Lobbies"
    Either use the in-game phone's Multiplayer - LIVE - Player Match option to join or create a lobby, or add friends in the ++home++ overlay and join their lobbies instead.

    - Explanations of menu options:
        * ==Quick Match== allows to join a random existing lobby of a *specific* gamemode.
        * ==Custom Match== allows to find an existing lobby of *any* gamemode.
        * ==Create Match== allows to create a lobby yourself.

    If you're looking for people to play with, visit this Discord server:

    [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }
???+ warning "Port Forwarding"
    If you are having problems connecting to lobbies (kickbug, joining an empty lobby), you may be having problems with automatic port forwarding (UPnP). Set up port forwarding for the following ports in your router's settings (look online for instructions for your specific router or ISP, or contact your ISP):

    * TCP: `3074`, `80`, `88`
    * UDP: `3074`, `80`, `88`

    If you can't perform port forwarding, use a VPN service instead. I recommend [Mullvad VPN](https://mullvad.net/en) (I'm not paid for this).

## Grand Theft Auto Connected
!!! warning "Compatibility"
    This client is only compatible with patches 1.0.6.0, 1.0.7.0 and 1.0.8.0. [Downgrade](downgrading.md) if using the Complete Edition.

    GTA Connected only supports ZolikaPatch and ZMenuIV out of mods - other mods are not allowed. If you want to have Fusion Shaders, you can use [V109](https://github.com/Parallellines0451/GTAIV.EFLC.FusionShaders/releases/tag/V109) or [V106](https://github.com/Parallellines0451/GTAIV.EFLC.FusionShaders/releases/tag/V106) - but they lack a lot of things from the latest versions.
Second most popular multiplayer option, as it's the best way to experience GTA IV multiplayer without messing with GFWL while still having many of it's things intact.
### Usage
???+ info "Installation"
    * Go to the [GTA Connected](https://gtaconnected.com/downloads/) website.
    * Download the latest ==client==.
    * Install the :material-file-download:`GTAC-x.x.x.exe` from the :material-zip-box:`GTAC-x.x.x.zip`.
???+ tip "Configuration"
    * Set the `Game` box to `Grand Theft Auto IV`.
    * In the Tools - Launcher Settings window, set your nickname. You can also set various settings as you wish.
    * In the Tools - Game Settings window, set the path to your GTA IV install. You can also set various settings as you wish.
???+ tip "Joining servers"
    Once you're done with the configuration, it's as simple as double-clicking on any server in the list. You'll be presented with the game's main menu - just hit Play.

[:material-web: GTAConnected website](https://gtaconnected.com/){ .md-button .md-button--primary } [:simple-discord: GTAConnected Discord Server](https://discord.gg/YSyasDa){ .md-button .md-button--primary }

## HappinessMP
!!! warning "Compatibility"
    This client is only compatible with the Complete Edition and does not support any mods at the moment - even Ultimate ASI Loader.
This client is somewhat similar to GTA Connected in essence, as you can host your own servers with your own scripts, but it aims to be compatible with the Complete Edition and requires Social Club to function rather than 1.0.8.0/1.0.7.0. It also lacks any of the official Rockstar gamemodes.
### Usage
???+ info "Installation"
    * Go to the [HappinessMP](https://happinessmp.net/) website.
    * Click the ==Download== button.
    * Install the :material-file-download:`HappinessMP.exe`.
???+ tip "Playing"
    Set your nickname and chat key in the Settings. After that, just click on any server you want in the server to join.

[:simple-discord: HappinessMP Discord Server](https://discord.gg/U6w3Yu8jkt){ .md-button .md-button--primary } [:material-web: HappinessMP's website](https://happinessmp.net/){ .md-button .md-button--primary }


## Upcoming clients
These clients are currently in development and are not available for play yet. They'll receive their own full-fledged sections when they're freely available for play. Support their development if you can!

### XLiveLessNess
This project aims to be a replacement for GFWL. It technically works, but at the same time I couldn't get a lobby with more than just two players working with it just yet. Download the release, drop the files to the game folder, press HOME in-game, set your nickname, check the checkmarks and set the broadcast address to `glitchyscripts.com:1100`. Use the LAN function in-game instead of LIVE.

[:material-gitlab: GitLab](https://gitlab.com/GlitchyScripts/xlivelessness){ .md-button .md-button--primary }

### Liberty City Online
This client also aims to provide a highly flexible multiplayer experience, similar to [SA:MP](https://www.sa-mp.com/), along with support for original game modes such as Deathmatch. However, it will require the 1.0.8.0 and 1.0.7.0 patches instead.

[:material-web: Liberty City Online's website](https://lc-online.net/){ .md-button .md-button--primary }

[:material-page-first:Previous page <br>Extras</br>](extras/index.md){ .md-button } [Next page:material-page-last: <br>Trainers</br>](extras/trainers.md){ .md-button .md-button--primary }