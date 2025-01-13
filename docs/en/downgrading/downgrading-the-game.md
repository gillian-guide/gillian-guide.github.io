title: Downgrading the game
description: Downgrading the game version and the savefiles back to the retail version.

# Downgrading the game

## Game versions

The following is information about two versions we will focus on and their differences. 1.0.4.0 is for informational purposes only - we will not use it in the scope of this guide.

???+ info "Complete Edition (1.2.0.59)"

    This is the latest version of the game, which you normally receive when installing the game on :material-steam: Steam or :simple-rockstargames: Rockstar Games Launcher. ==This version should be preferred if you want the **best singleplayer campaign experience.**==

    ??? quote "Pros and cons"
        !!! success ""
            :material-plus-box: It works out of the box. No modifications are required to launch the game.<br>
            :material-plus-box: Best support for modern mods made after 2020, such as FusionFix. This ensures getting the most fixes possible when modding.<br>
            :material-plus-box: Includes EFLC.<br>
            :material-plus-box: Supports Steam and Social Club Achievements out of the box.

        !!! danger ""
            :material-minus-box: Rockstar Games Launcher and it's DRM is required, which can be considered bloat for multiple reasons: the game launches for a minute longer and it does not provide anything but achievements to the game, to name two.<br>
            :material-minus-box: Compatibility with old mods is not guaranteed. While some mods work, there are some that do not. They are not critical to fixing the game, though.<br>
            :material-minus-box: Official multiplayer is removed and third-party experience is limited.<br>
            :material-minus-box: No support for GFWL (Xbox Live) achievements.

???+ info "Retail version (1.0.8.0)"

    This is the version of the game that existed before the Complete Edition. ==This version should only be preferred if you want to **play the multiplayer**, use  **specific mods** you have in mind that don't support CE or want to **play without DRM.**==

    ??? quote "Pros and cons"
        !!! success ""
            :material-plus-box: Supports official multiplayer.<br>
            :material-plus-box: DRM can be removed, making this version capable of DRM-free play.<br>
            :material-plus-box: Best support for old mods made before 2020, such as Liberty Tweaks. If you don't know any yourself, don't consider this a point worth noting.<br>
            :material-plus-box: Supports GFWL (Xbox Live) achievements, but at the cost of Steam Achievements.

        !!! danger ""
            :material-minus-box: Limited compatibility with FusionFix, which will reduce how many fixes you actually get.<br>
            :material-minus-box: To make multiplayer work, you have to set up GFWL, which is a lot of hassle. Although a third-party alternative exists.<br>
            :material-minus-box: EFLC support can only be achieved through mods.<br>
            :material-minus-box: Steam Achievements support can only be achieved with mods, which also disable GFWL achievements. No support for Social Club achievements.<br>

??? info "Retail version (1.0.4.0)"

    This version is not going to be useful in the scope of the guide, but since it is a popular version in the community, it should be mentioned - and explained why won't we use it. ==This version should only be preferred for **graphical mods**, which receive no support on this guide.==

    ??? quote "Pros and cons"
        !!! success ""
            :material-plus-box: Best support for graphical mods.<br>
            :material-plus-box: Slightly better average FPS.<br>
            :material-plus-box: DRM can be removed, making this version capable of DRM-free play.<br>
            :material-plus-box: Supports GFWL (Xbox Live) achievements.

        !!! danger ""
            :material-minus-box: Little to none mod support.<br>
            :material-minus-box: Awful framepacing.<br>
            :material-minus-box: No EFLC support.<br>
            :material-minus-box: No support for Steam or Social Club achievements.

---

## Downgrading instructions

!!! question "Which downgrader to choose?"
    - Use ItsClonkAndre's if you want to downgrade to 1.0.4.0 or if you have issues with mine.
    - Use mine for every other case.

=== "[Gillian's GTA IV Downgrade Utility](https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF)"
    I've made my own downgrader for my own purposes as an alternative to ItsClonkAndre's. This downgrader is lightweight in core and doesn't let you do broken downgrades regardless of how you choose to downgrade, thus why I recommend it.

    1. Go to the latest [release page](https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF/releases/latest).
    2. Download :material-zip-box:`GTAIVDowngradeUtilityWPF.zip`.
    3. Extract the archive into any empty folder.
    4. Open :material-file:`GTAIVDowngradeUtilityWPF.exe`.
    5. Press `Open` and select your game folder. Follow the in-app instructions if any pop-ups appear.
    6. Press `Downgrade` to downgrade the game. It will automatically download and install everything.
        - If you are experienced, feel free to change toggles manually. ^^Only use Full downgrading if you absolutely require all the original files.^^
        - If any issues occur, [report them on the Discord server](../../index.md/#navigation).

=== "[ItsClonkAndre's Downgrader](https://gtaforums.com/topic/976691-gta-iv-downgrader/)"
    This downgrader replaces many more files than a typical user really needs, which may result in a slightly inferior experience. It also has an option to downgrade to 1.0.4.0, which my downgrader does not. It also allows you to make incompatible selections, so **read the warnings carefully**.

    1. Create an antivirus exclusion for your game folder. Don't worry, the tool is safe.
    2. Go to the [GTAForums page](https://gtaforums.com/topic/976691-gta-iv-downgrader/) and download the latest version.
    3. Extract the archive, run :material-file:`IVDowngrader.exe` with :fontawesome-solid-shield-halved: ==elevated permissions==.
    4. Follow the instructions in the application. Be sure to read the warnings at mod selection.

!!! warning ""
    - After downgrading, always launch the game via :material-steam: Steam or the `PlayGTAIV.exe` executable.
    - If using the :simple-rockstargames: Rockstar Games Launcher, **do not launch the game via the launcher**.
    - If you already had some [launch options](../additional-setup.md/#launch-options), they have to be moved to :material-file-cog:`commandline.txt` after downgrading.
    - Your game folder can also now be moved elsewhere if you desire so.

???+ question "Games for Windows - LIVE"
    If you wish to play the official multiplayer or get Xbox Live achievements, enable GFWL support when downgrading and, after downgrading, refer to [this page](../../extras/multiplayer.md/#games-for-windows-live) to set GFWL up.

    Don't enable the option if you don't want either though - you will make things harder for yourself. If you had accidentally enabled it, rename :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll`. If you don't have that file - install [Ultimate ASI Loader](../../resources/mod-dependencies/#ultimate-asi-loader) manually.

!!! info "Setup Utility"
    If you happened to come back here later after already using the Setup Utility on the [Optimization](../../optimization.md) or [Additional Setup](../../additional-setup.md) pages, consider re-running it.

---

## Downgrading the savefile

If you've already started playing on the Complete Edition, you may want to downgrade your savefile.

### Instructions

1. First, locate your savefiles in :material-folder: ==Documents\Rockstar Games\GTA IV\Profiles\\(id)\\==. They're named in this format: :material-file:`SGTAxxx`.
2. Upload the one you want to convert to [GTASnP](https://gtasnp.com/).
3. Expand the `Modifications` tab.
4. Pick `1.0.8.0 IV / 1.1.3.0 EFLC and older` in `Downgrade Version`.
5. Pick the slot you want to save your savefile as. You'll download your converted savefile.
6. Move it to :material-folder: ==C:\Users\\(user)\AppData\Local\Rockstar Games\GTA IV\savegames\user_(id)\\==.

---

## Navigation

Proceed with optimization after you are done with downgrading:

[:material-page-first:Previous page <br>Downgrading</br>](index.md){ .md-button } [Next page:material-page-last: <br>Optimization</br>](../optimization.md){ .md-button .md-button--primary }
