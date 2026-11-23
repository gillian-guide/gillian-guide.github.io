# Downgrading the game

## Game versions

The following is information about two versions we will focus on and their differences. 1.0.4.0 is for informational purposes only - we will not use it in the scope of this guide.

> [!NOTE]
>
> **Complete Edition (1.2.0.59)**
>
> This is the latest version of the game, which you normally receive when installing the game on Steam or Rockstar Games Launcher. <mark>This version should be preferred if you want the <strong>best singleplayer campaign experience.</strong></mark>
>
> > **Pros and cons**
> >
> > > It works out of the box. No modifications are required to launch the game.  
> > > Best support for modern mods made after 2020, such as FusionFix. This ensures getting the most fixes possible when modding.  
> > > Includes EFLC.  
> > > Supports Steam and Social Club Achievements out of the box.
> >
> > > Rockstar Games Launcher and it's DRM is required, which can be considered bloat for multiple reasons: the game launches for a minute longer and it does not provide anything but achievements to the game, to name two.  
> > > Compatibility with old mods is not guaranteed. While some mods work, there are some that do not. They are not critical to fixing the game, though.  
> > > Official multiplayer is removed and third-party experience is limited.  
> > > No support for GFWL (Xbox Live) achievements.

> [!NOTE]
>
> **Retail version (1.0.8.0)**
>
> This is the version of the game that existed before the Complete Edition. <mark>This version should only be preferred if you want to <strong>play the multiplayer</strong>, use  <strong>specific mods</strong> you have in mind that don't support <abbr title="Complete Edition, a.k.a. 1.2.0.59 or Steam and RGL version">CE</abbr> or want to <strong>play without DRM.</strong></mark>
>
> > **Pros and cons**
> >
> > > Supports official multiplayer.  
> > > DRM can be removed, making this version capable of DRM-free play.  
> > > Best support for old mods made before 2020, such as Liberty Tweaks. If you don't know any yourself, don't consider this a point worth noting.  
> > > Supports GFWL (Xbox Live) achievements, but at the cost of Steam Achievements.
> >
> > > Limited compatibility with FusionFix, which will reduce how many fixes you actually get.  
> > > To make multiplayer work, you have to set up GFWL, which is a lot of hassle. Although a third-party alternative exists.  
> > > EFLC support can only be achieved through mods.  
> > > Steam Achievements support can only be achieved with mods, which also disable GFWL achievements. No support for Social Club achievements.

> [!NOTE]
>
> **Retail version (1.0.4.0)**
>
> This version is not going to be useful in the scope of the guide, but since it is a popular version in the community, it should be mentioned - and explained why won't we use it. <mark>This version should only be preferred for <strong>graphical mods</strong>, which receive no support on this guide.</mark>
>
> > **Pros and cons**
> >
> > > Best support for graphical mods.  
> > > Slightly better average FPS.  
> > > DRM can be removed, making this version capable of DRM-free play.  
> > > Supports GFWL (Xbox Live) achievements.
> >
> > > Little to none mod support.  
> > > Awful framepacing.  
> > > No EFLC support.  
> > > No support for Steam or Social Club achievements.

---

## Downgrading instructions

> [!NOTE]
>
> **Which downgrader to choose?**
>
> - Use ItsClonkAndre's if you want to downgrade to 1.0.4.0 or if you have issues with mine.
> - Use mine for every other case.

I've made my own downgrader for my own purposes as an alternative to ItsClonkAndre's. This downgrader is lightweight in core and doesn't let you do broken downgrades regardless of how you choose to downgrade, thus why I recommend it.

1. Go to the latest [release page](<https://github.com/gillian-guide/GTAIVDowngradeUtilityWPF/releases/latest>).
2. Download `GTAIVDowngradeUtilityWPF.zip`.
3. Extract the archive into any empty folder.
4. Open `GTAIVDowngradeUtilityWPF.exe`.
5. Press `Open` and select your game folder. Follow the in-app instructions if any pop-ups appear.
6. Press `Downgrade` to downgrade the game. It will automatically download and install everything.

   - If you are experienced, feel free to change toggles manually. Only use Full downgrading if you absolutely require all the original files.
   - If any issues occur, [report them on the Discord server](<https://gillian-guide.github.io/#navigation>).

This downgrader replaces many more files than a typical user really needs, which may result in a slightly inferior experience. It also has an option to downgrade to 1.0.4.0, which my downgrader does not. It also allows you to make incompatible selections, so **read the warnings carefully**.

1. Create an antivirus exclusion for your game folder. Don't worry, the tool is safe.
2. Go to the [GTAForums page](<https://gtaforums.com/topic/976691-gta-iv-downgrader/>) and download the latest version.
3. Extract the archive, run `IVDowngrader.exe` with <mark>elevated permissions</mark>.
4. Follow the instructions in the application. Be sure to read the warnings at mod selection.

> [!WARNING]
>
> - After downgrading, always launch the game via Steam or the `PlayGTAIV.exe` executable.
> - If using the Rockstar Games Launcher, **do not launch the game via the launcher**.
> - If you already had some [launch options](<https://gillian-guide.github.io/additional-setup/#launch-options>), they have to be moved to `commandline.txt` after downgrading.
> - Your game folder can also now be moved elsewhere if you desire so.

> [!NOTE]
>
> **Games for Windows - LIVE**
>
> If you wish to play the official multiplayer or get Xbox Live achievements, enable GFWL support when downgrading and, after downgrading, refer to [this page](<https://gillian-guide.github.io/extras/multiplayer/#games-for-windows-live>) to set GFWL up.
>
> Don't enable the option if you don't want either though - you will make things harder for yourself. If you had accidentally enabled it, rename `dinput8.dll` to `xlive.dll`. If you don't have that file - install [Ultimate ASI Loader](<https://gillian-guide.github.io/resources/mod-dependencies#ultimate-asi-loader>) manually.

> [!NOTE]
>
> **Setup Utility**
>
> If you happened to come back here later after already using the Setup Utility on the [Optimization](<https://gillian-guide.github.io/optimization/index.md>) or [Additional Setup](<https://gillian-guide.github.io/additional-setup/index.md>) pages, consider re-running it.

---

## Downgrading the savefile

If you've already started playing on the Complete Edition, you may want to downgrade your savefile.

### Instructions

1. First, locate your savefiles in <mark>Documents\Rockstar Games\GTA IV\Profiles\(id)\</mark>. They're named in this format: `SGTAxxx`.
2. Upload the one you want to convert to [GTASnP](<https://gtasnp.com/>).
3. Expand the `Modifications` tab.
4. Pick `1.0.8.0 IV / 1.1.3.0 EFLC and older` in `Downgrade Version`.
5. Pick the slot you want to save your savefile as. You'll download your converted savefile.
6. Move it to <mark>C:\Users\(user)\AppData\Local\Rockstar Games\GTA IV\savegames\user_(id)\</mark>.

---

## Navigation

Proceed with optimization after you are done with downgrading:
