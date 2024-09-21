title: Multiplayer
description: Hello? Anybody there?

# Multiplayer

GTA IV had an amazing multiplayer... and it still does! Rockstar Games has removed the multiplayer from the Complete Edition, but there are still plenty of ways to play even the official multiplayer (which, no, is not shut down). If you're tired of GTA Online and want something more classic, you should definitely check out GTA IV's multiplayer!

---

## Prerequisites and info

- It's recommended to have [ZolikaPatch](../../essential-modding/zolikapatch.md) set up for a better multiplayer experience. Make sure to configure :material-file-cog:`ZolikaPatch.ini` to use multiplayer functions.
- Make sure to have `RecoilFix` set to `0` in :material-file-cog:`GTAIV.EFLC.FusionFix.ini` to avoid being at disadvantage with other players.
    - It is also recommended to use the [GFWLMin patch](https://github.com/SandeMC/GTAIV.EFLC.FusionFix-GFWLMin/releases/latest) for increased stability - ^^but it cuts out singleplayer features.^^
- Additionally, you may want to have [ZMenuIV](trainers.md/#ZMenuIV) for the ability to create and participate in custom gamemodes.
- You can also use [this](https://www.gtainside.com/en/gta4/mods/160558-gta-iv-and-eflc-all-multiplayer-clothes-are-unlocked/) to unlock all multiplayer clothing for customization.
- **Avoid using overhaul, addition or replacement mods**. They will put you, or others, at disadvantage and create instability.

---

## Games for Windows LIVE

!!! note ""
    This section also includes steps to configure GFWL for non-multiplayer use too. If you came here for that, just skip the "Joining/Creating Lobbies" section.
!!! warning "Compatibility"
    This method is only compatible with patches 1.0.7.0 and 1.0.8.0. It's also compatible with older patches, but they'll be put into separate lobbies. [Downgrade](../../downgrading/downgrading.md) if using the Complete Edition.

    Wine does not implement support for GFWL, so this method is not possible on Linux.

The one and only official multiplayer method. And to that end, it's also the one that's most annoying to set up. If you don't want the hassle, check out [GTAConnected](#grand-theft-auto-connected) first.

---

<a id="gfwl-install"></a>

### Installation

!!! note ""
    This step is already taken care of by the downgraders if you chose to configure the install for GFWL. Skip it if you did.

1. Make sure you don't have outdated installations of `GFWL Marketplace` and `LIVE`. Remove them if you do.
2. Download latest [Redistributables](https://community.pcgamingwiki.com/files/file/1012-microsoft-games-for-windows-live/).
3. Extract the archive in any empty folder.
4. Run :material-file-download:`gfwllivesetup.exe` and go through the installation.
5. Install the [Xbox App](https://apps.microsoft.com/detail/9mv0b5hzvk9z) and sign into the Xbox account in it. This is required for signing in later.
!!! question "What's the Marketplace?"
    While you do get the Marketplace, don't bother opening it or trying to make it work. Marketplace is not functional, but still must be installed for GFWL itself to work.

---

### Signing in

!!! warning ""
    GFWL account is the same as a [Microsoft](https://microsoft.com/account) or [Xbox](https://xbox.com/account) account. Create one if you don't already have one.

1. Make sure you don't have :fontawesome-solid-gears:`xlive.dll` in the game folder - rename it to :fontawesome-solid-gears:`dinput8.dll` if you do.
2. Open the game.
3. Press the ++home++ key on your keyboard. You'll be met with the startup screen.
    - If the startup screen did not appear or you're met with an error when opening the game, re-read the instructions from the start.
4. Click `Use Existing LIVE Profile` to get the sign in screen.
5. Uncheck `Save my e-mail address` and `Save my e-mail address and password`.
6. Enter your [Microsoft](https://microsoft.com/account) or [Xbox](https://xbox.com/account) account credentials to sign in.
    - **Check `Sign me in automatically`**. This will allow you to re-enable 2FA on your account, aswell.
    - **If you have a password longer than 16 character or use 2FA,** go to [this website](https://account.live.com/proofs/AppPassword) and use the generated "App password" to sign in.
7. Make yourself a cup of tea or do whatever you want for the next 2-10 minutes. I'm not kidding - it might take that long to log in. ==Don't think it's stuck - it's not.==
8. The game will ask you for an activation key now:

???+ note "Activation"
    We have several ways to activate the game.
    === "Buying a key or game"
        One of the ways to activate the game is to own a GFWL key. Although you'll share it with a lot of other people - it'll still be "yours", so to say.

        First, check if you already own any game with [Legacy (5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) - you may already own one of these games - check if their CD Key works for you.

        After you've made sure you don't have one already, you can:

        - Look for a GFWL key on some marketplaces.
        - Buy one of these Steam games, which are the only ones still selling a GFWL key as of December 2023. This may change in the future. ==Don't worry, you can refund the game after you purchase the key.==

        <iframe src="https://store.steampowered.com/widget/32420/" frameborder="0" width="646" height="190" allowtransparency="true"></iframe>

        <iframe src="https://store.steampowered.com/widget/10460/" frameborder="0" width="646" height="190" allowtransparency="true"></iframe>

        <iframe src="https://store.steampowered.com/widget/20570/4025/" frameborder="0" width="646" height="190" allowtransparency="true"></iframe>

        After buying the game, go to the library, select the game and right click - Manage - CD keys and copy the key somewhere. You can refund it now.
    === "Trying out random keys online"
        This one is pretty self-explanatory - just go around online and look for random GFWL keys - preferably with [Legacy (5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) - they have multiple uses, so you might get lucky. This Discord server might help you:

        [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }
    === "RevIVal's community method"
        The channel with the activation method is `#gfwl-keys` (for promotion and respect reasons, I won't link it here directly), but check out the server itself too, we're welcome to anyone!

        [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }
    After you acquired the key and activated the game (again, this might take another 5-10 minutes, so get yourself a tea or something), you're ready to play!

---

### Joining/Creating Lobbies

Either use the in-game phone's `Multiplayer` - `LIVE` - `Player Match` option to join or create a lobby, or add friends in the ++home++ overlay and join their lobbies instead.

Explanations of menu options:

- ==Quick Match== allows to join a random existing lobby of a *specific* gamemode.
- ==Custom Match== allows to find an existing lobby of *any* gamemode.
- ==Create Match== allows to create a lobby yourself.

If you're looking for people to play with, visit this Discord server:

[:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }

???+ info "Port Forwarding"
    If you are having problems connecting to lobbies (kickbug, joining an empty lobby), you have to do manual port forwarding for the following ports in your router's settings (look online for instructions for your specific router or ISP, or contact your ISP):

    * TCP: `3074`, `80`, `88`
    * UDP: `3074`, `80`, `88`

    If you can't perform port forwarding, use a VPN service instead. I recommend [Mullvad VPN](https://mullvad.net/en).

    Alternatively, give up. Seriously, just give up and try other methods - some people are just stuck with the kickbug with no way to fight it.

---

## [Grand Theft Auto Connected](https://gtaconnected.com/downloads/)

!!! warning "Compatibility"
    See [this](https://wiki.gtaconnected.com/DowngradingIV) if using the Complete Edition.

    GTA Connected only supports ZolikaPatch and ZMenuIV out of mods - other mods are simply not loaded **(though, unless they replace game files, there's no need to remove them).**

    If you want to have Fusion Shaders, you can use [V106](https://github.com/gillian-guide/GTAIVFullDowngradeAssets/releases/download/Base/ShaderFixes.zip) - but this version lacks a lot of things from the latest versions present in FusionFix; it's still better than nothing, though. **Backup the :material-folder: ==shaders== folder before installing.**

Second most popular multiplayer option, as it's the best way to experience GTA IV multiplayer without messing with GFWL while still having many of things intact from the official multiplayer.

### Installation and usage

1. Go to the [GTAConnected](https://gtaconnected.com/downloads/) website.
2. Download the latest **client**.
3. Install :material-file-download:`GTAC-x.x.x.exe` from the :material-zip-box:`GTAC-x.x.x.zip` archive.
4. Open the client.
5. Set the `Game` box to `Grand Theft Auto IV`.
6. In the `Tools` - `Launcher Settings` window, set your nickname. You can also set various settings as desired.
7. In the `Tools` - Game Settings window, set the path to your GTA IV install. You can also set various settings as you wish.
8. To join servers, simply double click on any server on the list.

[:simple-discord: GTAConnected Discord Server](https://discord.gg/YSyasDa){ .md-button .md-button--primary }

---

## [HappinessMP](https://happinessmp.net/)

!!! warning "Compatibility"
    This client is only compatible with the Complete Edition and does not support any custom mods.

    If using FusionFix, only [this version](https://happinessmp.net/files/GTAIV.EFLC.FusionFix.HappinessMP.zip) is allowed.
This client is somewhat similar to GTA Connected in essence, as you can host your own servers with your own scripts, but it aims to be compatible with the Complete Edition and requires Social Club to function rather than 1.0.8.0/1.0.7.0. It also lacks any of the official Rockstar gamemodes.

### Installation and usage

1. Go to the [HappinessMP](https://happinessmp.net/) website.
2. Press the **Download** button.
3. Install :material-file-download:`HappinessMP.exe`.
4. Open the client.
5. In the settings, set your nickname.
6. To join servers, simply click on any server on the list.

[:simple-discord: HappinessMP Discord Server](https://discord.gg/U6w3Yu8jkt){ .md-button .md-button--primary }

---

## Upcoming clients

These clients are currently in development and are not available for play yet. They'll receive their own full-fledged sections when they're freely available for play. Support their development if you can!

---

### XLiveLessNess

This project aims to be a replacement for GFWL. It technically works, but at the same time I couldn't get a lobby with more than just two players working with it just yet. Download the release, drop the files to the game folder, press HOME in-game, set your nickname, check the checkmarks and set the broadcast address to `glitchyscripts.com:1100`. Use the LAN function in-game instead of LIVE.

[:material-gitlab: GitLab](https://gitlab.com/GlitchyScripts/xlivelessness){ .md-button .md-button--primary }

---

## Navigation

[:material-page-first:Previous page <br>Extras</br>](index.md){ .md-button }
