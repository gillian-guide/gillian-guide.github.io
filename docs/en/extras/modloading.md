title: Modloading
description: Phew, all original files are still there!

# Modloading

A lot of mods require replacing game files with [OpenIV](openiv.md). We can get around this by using a modloader.

---

## [Fusion Overloader](../../essential-modding/fusionfix.md)

!!! warning "Compatibility"
    Supports both the Complete Edition and 1.0.8.0/1.0.7.0 as long as the latest version of [FusionFix](../../essential-modding/fusionfix.md) is installed.

This modloader works by loading the files from the :material-folder: ==update== folder *instead* of the main game files, avoiding replacing the original files.

---

### Installing mods packaged for Fusion Overloader

They're likely already packaged into an :material-folder: ==update== folder. Just drop that folder into the root folder of the game.

---

### Installing mods with files that go into `.img` archives"

Example: mod requires you to drop a file into the :material-file:`vehicles.img` file.

!!! info "For mods that provide a whole `.img` archive"
    If, say, the mod compiles the whole `vehicles.img` but only replaces one vehicle - you should only package that separate vehicle alone. While you *can* get away with not separating the modified files, you'll ruin compatibility with other mods. So please don't do that.

    If you want to separate modified files, you have to extract the mod's and vanilla archives into separate folders and compare the folders with something like [WinMerge](https://winmerge.org/).

1. Compile all the files that go into `.img`'s into a single `.img` archive (or multiple if your archives exceed `1.5GB` to avoid issues) using [OpenIV](openiv.md).
2. If you have files that should be only injected into TLAD, TBoGT or IV and not the other (i.e. a mod provides separate files for base IV and EFLC), compile a separate `.img` file for each subgame.
3. Create a folder with the name of your mod in the :material-folder: ==update== folder (create one in the game folder if it doesn't exist).
4. Drop your compiled `.img` files into that folder.
5. If you went through step 2, also create folders called :material-folder: ==IV==, :material-folder: ==TLAD== or :material-folder: ==TBoGT== and drop the separate `.img` files there.

!!! tip "Priority"
    If you have multiple mods that replace same files and need a priority system, you can add a number or a symbol (such as !) before it's name.

    Whatever is higher on the folder when sorting by **Name (ascending)** - is higher on priority.

    ??? info "Expected folder structure"
        In this example, Mod 2 is supposed to be higher priority than Mod 1.

        * :material-folder: ==GTAIV==\
            * :material-folder: ==update==\
                * :material-folder: ==1 Mod 2==\
                    *  :material-file:`Mod2.ForEveryGame.img`
                * :material-folder: ==2 Mod 1==\
                    *  :material-file:`Mod1.ForEveryGame.img`
                    * :material-folder: ==IV==\
                        * :material-file:`Mod 1.IVOnly.img`
                    * :material-folder: ==TLAD==\
                        * :material-file:`Mod 1.TLADOnly.img`
                    * :material-folder: ==TBoGT==\
                        * :material-file:`Mod 1.TBoGTOnly.img`

---

### Installing mods with other kind of files

Example: mod requires you to modify :material-file:`gta.dat`.

Example 2: mod requires you to modify :material-file:`playerped.rpf` (copy the vanilla file over first and modify that).

!!! note ""
    By other kind of files I mean literally any replacement files that go into :material-folder: ==pc==, :material-folder: ==common==, :material-folder: ==TLAD== or :material-folder: ==TBoGT==. As long as they're not `.img` files.

    Placing the files in the mod folders won't work.

1. Recreate the folder structure from the vanilla one in :material-folder: ==update==.
2. Place the replacement files exactly as you would in vanilla, just do that in :material-folder: ==update==.
3. If the two mods replace same files, use a comparison tool (I like to use [WinMerge](https://winmerge.org/)) to merge them.

??? info "Expected folder structure"

    * :material-folder: ==GTAIV==\
        * :material-folder: ==update==\
            * :material-folder: ==common==\
                * :material-folder: ==data==\
                    * :material-file:`WeaponInfo.xml`
            * :material-folder: ==TLAD==\
                * :material-folder: ==common==\
                    * :material-folder: ==data==\
                        * :material-file:`WeaponInfo.xml`

---

## [IV Tweaker](https://zolika1351.pages.dev/mods/ivtweaker)

!!! warning "Compatibility"
    Supports 1.0.8.0 and 1.0.7.0 only.

This modloader has a few advantages over Fusion Overloader, such as being able to inject more files than just `.img`'s while still having the originals intact. It also allows to increase limits.

---

### Installation

1. Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivtweaker)
2. Scroll to the bottom and download the archive.
3. Extract the :material-zip-box:`IVTweaker_vx.x.zip` archive into the game folder.

---

### Installing mods

!!! warning "For mods that provide a whole `.img` archive"
    If, say, the mod compiles the whole `vehicles.img` but only replaces one vehicle - you should only package that separate vehicle alone. While you *can* get away with not separating the modified files, you'll ruin compatibility with other mods. So please don't do that.

    If you want to separate modified files, you have to extract the mod's and vanilla archives into separate folders and compare the folders with something like [WinMerge](https://winmerge.org/).

1. Compile all the files that go into `.img`'s into a single `.img` archive (or multiple if your archives exceed `1.5GB` to avoid issues) using [OpenIV](openiv.md).
2. If you have files that should be only injected into TLAD, TBoGT or IV and not the other, compile a separate `.img` file for them.
    - You can also omit the above two steps and just use raw files.
3. Create a folder with the name of your mod in :material-folder: ==modloader==.
4. Drop your compiled `.img` or raw files into that folder.
5. If you had to go through step 3, also create separate folders for IV, TLAD or TBoGT and drop the specific files there.
6. You can add :material-file:`GTAIVOnly`, :material-file:`TLADOnly` or a :material-file:`TBoGTOnly` if you don't need the mod to load in any other subgame. Otherwise, edit :material-file-cog:`modloader.ini` for priority and when the mods should or should not load.

??? warning "Expected folder structure"

    * :material-folder: ==GTAIV==\
        * :material-folder: ==modloader==\
            * :material-folder: ==Mod1==\
                * :material-file:`IVAnims.ForEveryGame.img`
                * :material-file:`WeaponInfo.xml`
            * :material-folder: ==Mod1.TLADOnly==\
                * :material-file:`TLADOnly`
                * :material-file:`TLADAnims.img`
                * :material-file:`WeaponInfo.xml`
            * :material-folder: ==Mod1.TBoGTOnly==\
                * :material-file:`TBoGTOnly`
                * :material-file:`TBoGTAnims.img`

---

### Configuring the modloader

To configure the modloader, edit :material-file-cog:`modloader.ini` in :material-folder: ==modloader==.

- Make sure you set the correct priority so you don't have unwanted mods overriding other mods (higher number - higher priority).
- Make sure mods that should *only* be injected to TBoGT or TLAD are disabled for IV (Ep0), mods that are *only* for TBoGT are disabled for TLAD (Ep1), and mods that are *only* for TLAD are disabled for TBoGT(Ep2).
    - This isn't necessary if you left :material-file:`GTAIVOnly`, :material-file:`TLADOnly` or :material-file:`TBoGTOnly` files in the folders.

??? warning "Expected configuration"
    Improved Animations mod will be used for an example.

    ``` { .ini }
    [DisabledMods]
    IVImprovedAnimations=0
    TLADImprovedAnimations=0
    TBoGTImprovedAnimations=0

    [Priorities]
    IVImprovedAnimations=1
    TLADImprovedAnimations=2
    TBoGTImprovedAnimations=2

    [DisabledForEp0]
    TLADImprovedAnimations=1
    TBoGTImprovedAnimations=1

    [DisabledForEp1]
    TBoGTImprovedAnimations=1

    [DisabledForEp2]
    TLADImprovedAnimations=1
    ```

!!! info "Increasing the limits"
    To increase the limits, edit :material-file-cog:`IVTweaker.ini`.

    You may want to do that if you install mods that, for example, change vehicle textures, since you should increase the vehicle budget limits for those.

---

## Navigation

[:material-page-first:Previous page <br>Extras</br>](index.md){ .md-button }
