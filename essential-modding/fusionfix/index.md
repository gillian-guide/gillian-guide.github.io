# [FusionFix](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix>)

This project aims to fix or address most **graphical and gameplay issues** and introduces new graphics options. You can read the changelog on the [repository](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/tree/master#coregameplay-changelog>).

---

## Demo

---

## Installation

1. Go to the latest [release page](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest>).
2. Download the `GTAIV.EFLC.FusionFix.zip` archive.
3. Extract the archive into the game folder.

   - Consider re-running the Setup Utility if you used it on the [Optimization](<https://gillian-guide.github.io/optimization/index.md>) or [Additional Setup](<https://gillian-guide.github.io/additional-setup/index.md>) pages.
   - See the [optimal graphics settings for FusionFix](<https://gillian-guide.github.io/additional-setup/#__tabbed_2_2>).

> [!NOTE]
>
> **Missing fixes**
>
> Installing FusionFix on 1.0.8.0 compromises on some fixes, and you won't receive any official support from Fusion Team shall any issues arise. Keep that in mind.

1. Go to the latest [release page](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest>).
2. Download `GTAIV.EFLC.FusionFix.zip`.
3. Extract the archive into the game folder.
4. Move the files out of the <mark>plugins</mark> folder into the game folder (don't ask me why, this tends to improve stability).

   - Rename `dinput8.dll` to `xlive.dll` **if not using GFWL**. Replace if needed.
   - Consider re-running the Setup Utility if you used it on the [Optimization](<https://gillian-guide.github.io/optimization/index.md>) or [Additional Setup](<https://gillian-guide.github.io/additional-setup/index.md>) pages.
   - See the [optimal graphics settings for FusionFix](<https://gillian-guide.github.io/additional-setup/#__tabbed_2_2>).
   - **Do not enable `Check For Fusion Fix Updates`.**

> [!TIP]
>
> **If using GFWL for multiplayer...**
>
> Apply this [patch](<https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL/releases/latest>) on top.
>
> If **only playing multiplayer**, consider the multiplayer-only [patch](<https://github.com/SandeMC/GTAIV.EFLC.FusionFix-GFWLMin/releases/latest>) for increased stability instead.

### Additional steps for Linux users

1. Install [Protontricks](<https://github.com/Matoking/protontricks>)
2. Open a terminal and run the following command in the GTA IV prefix:

   ```bash
   protontricks 12210 -q d3dx9_43
   ```

   If you installed Protontricks through Flatpak (which you do if you're running Steam via Flatpak as well), run this instead:, run this:

   ```bash
   flatpak run com.github.Matoking.protontricks 12210 -q d3dx9_43
   ```
3. Wait until DirectX installs (may take a few minutes).

> [!TIP]
>
> **Modloading**
>
> This mod can be used for modloading purposes. See [Fusion Overloader](<https://gillian-guide.github.io/extras/modloading/#fusion-overloader>) for more details.

---

## Configuration

Most of options are available in the in-game settings.

You can edit `GTAIV.EFLC.FusionFix.ini` or `GTAIV.EFLC.FusionFix.cfg` if you need to edit the settings outside of the game for some reason. See [the list of non-ingame options](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix?tab=readme-ov-file#details>) if you need to tweak them.

---

## Navigation

- If your **game is downgraded**, continue with OpenPreCEPatch:
- If it isn't, continue with Various Fixes instead:
