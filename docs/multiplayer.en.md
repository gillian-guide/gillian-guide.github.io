title: Multiplayer
description: Experience GTA IV Multiplayer!

# Multiplayer
GTA IV had an amazing multiplayer... and it still does! At least for people who [downgrade](downgrading.md), as Rockstar Games has removed the multiplayer from the Complete Edition. If you're tired of GTA Online and want something more classic, you should definitely check out GTA IV's multiplayer!
!!! warning ""
    Current multiplayer methods require [downgrading](downgrading.md).

    It's extremely recommended to have [ZolikaPatch](essential-modding/zolikapatch.md) set up for a better multiplayer experience. Make sure to configure :material-file-cog:`ZolikaPatch.ini` to use multiplayer functions and set `DoNotPauseOnMinimize` to `1`. [ItsClockAndre's Downgrader](../downgrading/#itsclockandres-downgrader) already takes care of that if you chose to configure your install for GFWL.

    Make sure to have `RecoilFix` set to `0` in :material-file-cog:`GTAIV.EFLC.FusionFix.ini` to avoid being at disadvantage with other players.

    Additionally, you may want to have [ZMenuIV](../extras/trainers/#ZMenuIV) for the ability to create and participate in [custom gamemodes](https://grandtheftrevivalforums.com/thread/9/all-community-game-mode-rules).

    You can also use [this](https://www.gtainside.com/en/gta4/mods/160558-gta-iv-and-eflc-all-multiplayer-clothes-are-unlocked/) to unlock all multiplayer clothing for customization.

    Avoid using overhaul, addition or replacement [mods](extras/mods.md).

## Games for Windows - LIVE
!!! note ""
    This section also includes steps to configure GFWL for non-mulitplayer use too, if you came here from other pages. Just skip the "Joining/Creating Lobbies" part.
!!! warning "Compatibility"
    This method is only compatible with patches 1.0.7.0 and 1.0.8.0. It's also compatible with older patches, but they'll be put into separate lobbies. [Downgrade](downgrading.md) if using the Complete Edition.
The classic multiplayer method, the one that started it all. And the one that is obnoxiously annoying to set up. Most communities stick to it at the moment.

### Usage
???+ info "Installation"
    !!! note ""
        This step is already taken care of by [ItsClockAndre's downgrader](../downgrading/#itsclockandres-downgrader) if you chose to configure the install for GFWL. Skip it if you did.

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
    === "Buying another GFWL game"
        Unironically, this is the easiest way. Don't worry - you can refund the game later, so no money is wasted. I recommend `FlatOut: Ultimate Carnage`, but any other GFWL game with [Legacy (Per-Title 5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) will do.

        <iframe src="https://store.steampowered.com/widget/12360/943/" frameborder="0" width="646" height="190"></iframe>

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
    This method is only compatible with patches 1.0.7.0 and 1.0.8.0. [Downgrade](downgrading.md) if using the Complete Edition.
This is not as faithful as the original multiplayer, but it is currently one of the best ways to experience GTA IV multiplayer without messing with GFWL.
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
??? tip "Setting up a server"
    !!! warning ""
        Only do any of this if you're experienced with hosting servers.
    * Download the server from the [GTA Connected](https://gtaconnected.com/downloads/) website.
    * Extract the `GTAC-Server-Winxx-x.x.x.zip` to a folder of your choice.
    * Configure the :material-file-cog:`server.xml` as needed. Use [this page](https://wiki.gtaconnected.com/ServerConfiguration) for instructions.
    * Run :material-file:`Server.exe` or the :material-file:`Server` if your server is on Linux.

## Upcoming clients
These clients are currently in development and are not available for play yet. They'll receive their own full-fledged sections when they're freely available for play. Support their development if you can!
### HappinessMP
This client aims to provide a highly flexible multiplayer experience, similar to [SA:MP](https://www.sa-mp.com/), along with support for original game modes such as Deathmatch. It will require the Complete Edition and rely on Social Club to function.

[:simple-discord: HappinessMP Discord Server](https://discord.gg/U6w3Yu8jkt){ .md-button .md-button--primary } [:material-web: HappinessMP's website](https://happinessmp.net/){ .md-button .md-button--primary }

### Liberty City Online
This client also aims to provide a highly flexible multiplayer experience, similar to [SA:MP](https://www.sa-mp.com/), along with support for original game modes such as Deathmatch. However, it will require the 1.0.8.0 and 1.0.7.0 patches instead.

[:material-web: Liberty City Online's website](https://lc-online.net/){ .md-button .md-button--primary }

[:material-page-first:Previous page <br>Extras</br>](extras/index.md){ .md-button } [Next page:material-page-last: <br>Trainers</br>](extras/trainers.md){ .md-button .md-button--primary }