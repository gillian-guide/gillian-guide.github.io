# Mod Dependencies

---

## [Ultimate ASI Loader](<https://github.com/ThirteenAG/Ultimate-ASI-Loader>)

UAL is used to load `.asi` mods (one of the most common types of GTA IV mods) into the game. It's multipurpose and can be used for many other games, but we will use it for GTA IV.

> [!NOTE]
>
> **Compatibility**
>
> Ultimate ASI Loader is compatible with all game versions.

### Installation

1. Go to the latest [release page](<https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases/latest>).
2. Download `Ultimate-ASI-Loader.zip` (**not `Ultimate-ASI-Loader_x64.zip`**).
3. Extract the archive into the game folder.

> [!WARNING]
>
> **If using Linux...**
>
> Add `WINEDLLOVERRIDES="dinput8=n,b" %command%` to your Launch options:
>
> - **Steam**: Right click the game in your library, press `Properties...` and paste the line in the `Launch options` field.
> - **Rockstar Games Launcher**: Open the game page in your library, open settings and paste the line in the `Launcher arguments` field.
> - **Windows shortcut**: Right click on the game shortcut, click `Properties` and paste the line in `Target` field.

> [!TIP]
>
> **Getting rid of Games for Windows - LIVE (for retail patches)**
>
> This tool can be used to get rid of GFWL if you're not interested in official [GFWL multiplayer](<https://gillian-guide.github.io/extras/multiplayer/#games-for-windows-live>) and Xbox Live achievements. This will reduce the amount of hassle and setup you have to do.
>
> - Rename the `dinput8.dll` to `xlive.dll`

> [!TIP]
>
> **Modloading**
>
> Ultimate ASI Loader can be used for modloading purposes. See [modloading](<https://gillian-guide.github.io/extras/modloading/index.md>) for more details.

---

## [ScriptHookDotNet](<https://github.com/HazardX/gta4_scripthookdotnet/>)

> [!WARNING]
>
> **Compatibility**
>
> - Compatible with all game versions.
> - See [Getting ScriptHookDotNet and IV-SDK .NET to work on Linux](<#getting-scripthookdotnet-and-iv-sdk-net-to-work-on-linux>) if running Linux.

ScriptHookDotNet is used to run scripts written in any .NET language. Not to be confused with [IV-SDK .NET](<#iv-sdk-net>).

### Installation

1. Go to the latest [release page](<https://github.com/Tomasak/gta4_scripthookdotnet/releases>).
2. Download `scripthookdotnet_vx_x_x_x.zip`.
3. Extract the archive into the game folder.

1. Go to the latest [release page for ScriptHook](<https://github.com/themonthofjune/IV.1080.ScriptHook/releases>).
2. Download `ScriptHook.zip`.
3. Extract the `ScriptHook.zip` archive into the game folder.
4. Go to the latest [release page for ScriptHookDotNet](<https://github.com/ClonkAndre/gta4_scripthookdotnet/releases/tag/v1.7.2.0>).
5. Download `ScriptHookDotNet.asi`.
6. Move the file into the game folder.

---

## [IV-SDK .NET](<https://gtaforums.com/topic/986510-iv-sdk-net/>)

> [!WARNING]
>
> **Compatibility**
>
> - Only compatible with 1.0.8.0 and 1.0.7.0. [Downgrade](<https://gillian-guide.github.io/downgrading/downgrading-the-game/index.md>) if using Complete Edition.
> - See [Getting ScriptHookDotNet and IV-SDK .NET to work on Linux](<#getting-scripthookdotnet-and-iv-sdk-net-to-work-on-linux>) if running Linux.

IV-SDK .NET is used to run scripts written in any .NET language. Not to be confused with [ScriptHookDotNet](<#scripthookdotnet>).

### Installation

1. Go to the latest [release page](<https://github.com/ClonkAndre/IV-SDK-DotNet/releases/latest>).
2. Download `IV-SDK.NET.vx_x_x.zip`.
3. Extract the archive into the game folder.

> [!TIP]
>
> **Clonk's Coding Library**
>
> Some mods may require extensions from [Clonk's Coding Library](<https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/>).
>
> #### Installation
>
> - Go to the latest [release page](<https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/releases/latest>).
> - Download `ClonkCodingLib.GTAIV.vx_x.zip`.
> - Extract the archive into the game folder.

---

## Getting ScriptHookDotNet and IV-SDK .NET to work on Linux

By default, neither of those two will run on Linux. This can be fixed, however. These instructions will assume you are an experienced Linux user, so if you don't get something - look it up online.

### Instructions

1. In the `Compatibility` tab of the game in Steam, temporarily change Proton version to one of Proton 4.11-4.13 versions
2. Find your GTA IV's prefix folder, usually located at <mark>~/.steam/Steam/steamapps/compatdata/12210/pfx</mark>, and delete it
3. Launch the game once, you will get a Rockstar Games Launcher error, just close it, we only need this for the prefix folder to generate again
4. Install [Protontricks](<https://github.com/Matoking/protontricks>) (If using Lutris (or any other form of managing GTA IV outside of Steam), use Winetricks instead)
5. Open a terminal and run the following command to install .NET in the GTA IV prefix:

   ```bash
   protontricks 12210 -q dotnet472
   ```

   If you installed Protontricks through Flatpak (which you do if you're running Steam via Flatpak as well), run this instead:

   ```bash
   flatpak run com.github.Matoking.protontricks 12210 -q dotnet472
   ```
6. Wait until .NET installs (may take from 5 to 30 minutes)
7. Change the game's Proton version back to your usual one (highly recommended to be using [Proton-GE](<https://github.com/GloriousEggroll/proton-ge-custom/releases>) (can be installed using [ProtonUp-Qt](<https://davidotek.github.io/protonup-qt/>)) which can improve stability and allows the use of Independence FM)
8. When you launch the game, you may get some .NET errors, but the mods should be working fine.

Credit goes to Roigo and minidrwho for figuring out the actual solution.

> [!TIP]
>
> **Alternative method, if the instructions above do not work**
>
> These steps come from a system where the method above fails - in particular, Proton 4.11-4.13 refuses to work.
>
> 1. Find your GTA IV's prefix folder, usually located at <mark>~/.steam/Steam/steamapps/compatdata/12210/pfx</mark>, and delete it
> 2. In the `Compatibility` tab of the game in Steam, set Proton to a [GE-Proton](<https://github.com/GloriousEggroll/proton-ge-custom/releases>) release - GE-Proton 11-1 was used. Install it with [ProtonUp-Qt](<https://davidotek.github.io/protonup-qt/>) if you don't have it.
> 3. Create an empty <mark>pfx</mark> folder inside <mark>compatdata/12210</mark> again.
> 4. Launch the game once, so the prefix is generated and updated. It may crash right after the loading screen at this point - that is expected and does not affect the following steps.
> 5. Open a terminal and run the following command to install .NET in the GTA IV prefix:
>
>    ```bash
>    protontricks 12210 -q dotnet472
>    ```
>
>    If you installed Protontricks through Flatpak (which you do if you're running Steam via Flatpak as well), run this instead:
>
>    ```bash
>    flatpak run com.github.Matoking.protontricks 12210 -q dotnet472
>    ```
> 6. Wait until .NET installs (may take from 5 to 30 minutes)
> 7. Change the game's Proton version back to Proton Experimental.
> 8. Launch the game. A `rundll` error appears twice - dismiss it with `No` both times.
> 9. ScriptHookDotNet now works, the game does not crash and the console is available.
>
> Credit goes to EzequielGhR, who reported this method in [issue \#60](<https://github.com/gillian-guide/gillian-guide.github.io/issues/60>).
