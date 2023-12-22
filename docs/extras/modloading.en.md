title: Modloading
description: Methods for injecting mods into your GTA IV installation to avoid replacing internal files

# Modloading
A lot of mods require replacing internal files with [OpenIV](openiv.md). We can get around this by using a modloader.

## What's the difference between them?
While they are different in some ways, you can still use both if you're running 1.0.8.0 or 1.0.7.0. Fusion Overloader, for example, can cover what IV Tweaker doesn't support. Personally, I prefer loading in the `.img` mods via IV Tweaker for ease of configuration and any other files via Fusion Overloader.

## Fusion Overloader
!!! warning "Compatibility"
    Supports both the Complete Edition and 1.0.8.0/1.0.7.0 as long as the latest version of [FusionFix](../essential-modding/fusionfix.md) is installed.

    Although it is possible to only install [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader) (and latest [ZolikaPatch](../essential-modding/zolikapatch.md) on older patches) and omit FusionFix, you may be missing some extra features FusionFix implements for it.
This modloader is not as robust as IV Tweaker, but can replace all kinds of files. It works by loading the files from the :material-folder:==update== *instead* of the main game files. avoiding removing the original files.

???+ info "Usage"

    !!! "Installing mods packaged for Fusion Overloader"
        They're likely already packaged into an :material-folder:==update==. Just drop that folder into the root folder of the game.

    ??? "Installing mods with files that go into `.img` archives"
        !!! warning "Note"
            While you *can* get away with not compiling the separate files (if, say, the mod compiles the whole `vehicles.img` but only replaces one vehicle), you'll ruin any compatibility with other mods. So please don't do that.

        1. Compile all the files that go into `.img`'s into a single `.img` archive (or multiple if your archives exceed `1.5GB` to avoid issues) using [OpenIV](openiv.md).
        1.1. If the mod combines these files with vanilla game files and there's no way to get them separately, extract both the mod's `.img` and the vanilla `.img` and use any comparison tool (I like to use [WinMerge](https://winmerge.org/)) to find the differing files. Go back to 1. after you do that.
        1.2. If you have files that should be only injected into TLAD, TBoGT or IV and not the other, compile a separate `.img` file for them.
        2. Create a folder with the name of your mod in :material-folder:==update== (create the folder if it doesn't exist).
        3. Drop your compiled `.img` files into that folder.
        3.1. If you had to go through 1.2, also create folders called :material-folder:==IV==, :material-folder:==TLAD== or :material-folder:==TBoGT== and drop the specific `.img` files there.
        4. If you have multiple mods that replace similar files, you can set a priority by making sure it shows up higher when sorting by names, ascending. You can do that by adding a number or a symbol (such as !) before it's name.

    ??? "Installing mods with other kind of files"
        !!! warning "Note"
            By other kind of files I mean literally any replacement files that go into :material-folder:==pc==, :material-folder:==common==, :material-folder:==TLAD== or :material-folder:==TBoGT==. As long as they're not `.img` files.

            Placing the files in the mod folders won't work. At the time of writing this, at least.
        1. Recreate the folder structure from the vanilla one in :material-folder:==update==.
        2. Place the replacement files exactly as you would in vanilla, just do that in :material-folder:==update==.
        3. If the two mods replace same files, use a comparison tool (I like to use [WinMerge](https://winmerge.org/)) to merge them.

    ??? warning "Expected folder structure"
        In this example, Mod 2 is supposed to be higher priority than Mod 1.

        * :material-folder:==GTAIV==\
            * :material-folder:==update==\
                * :material-folder:==1 Mod 2==\
                    *  :material-file:`Mod2.ForEveryGame.img`
                * :material-folder:==2 Mod 1==\
                    *  :material-file:`Mod1.ForEveryGame.img`
                    * :material-folder:==IV==\
                        * :material-file:`Mod 1.IVOnly.img`
                    * :material-folder:==TLAD==\
                        * :material-file:`Mod 1.TLADOnly.img`
                    * :material-folder:==TBoGT==\
                        * :material-file:`Mod 2.TBoGTOnly.img`
                * :material-folder:==common==\
                    * :material-folder:==data==\
                        * :material-file:`WeaponInfo.xml`
                * :material-folder:==TLAD==\
                    * :material-folder:==common==\
                        * :material-folder:==data==\
                            * :material-file:`WeaponInfo.xml`

## IV Tweaker
!!! warning "Compatibility"
    Supports 1.0.8.0 and 1.0.7.0 only. [Downgrade](../downgrading.md) if using the Complete Edition.
This modloader has a few advantages, such as being able to inject more files than just `.img`'s while still having the originals intact. It also allows to increase limits.

???+ note "Installation"
    * Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivtweaker)
    * Scroll to the bottom and download the archive.
    * Extract the :material-zip-box:`IVTweaker_vx.x.zip` into the game folder.

???+ info "Usage"

    ??? "Installing mods"
        !!! warning "Note"
            While you *can* get away with not compiling the separate files (if, say, the mod compiles the whole `vehicles.img` but only replaces one vehicle), you'll ruin any compatibility with other mods. So please don't do that.

        1. Compile all the files that go into `.img`'s into a single `.img` archive (or multiple if your archives exceed `1.5GB` to avoid issues) using [OpenIV](openiv.md).
        1.1. If the mod combines these files with vanilla game files and there's no way to get them separately, extract both the mod's `.img` and the vanilla `.img` and use any comparison tool (I like to use [WinMerge](https://winmerge.org/)) to find the differing files. Go back to 1. after you do that.
        1.2. If you have files that should be only injected into TLAD, TBoGT or IV and not the other, compile a separate `.img` file for them.
        1.3. You can also omit this and use raw files.
        2. Create a folder with the name of your mod in :material-folder:==modloader== (create the folder if it doesn't exist).
        3. Drop your compiled `.img` files into that folder.
        3.1. If you had to go through 1.2, also create separate folders for IV, TLAD or TBoGT and drop the specific files there.
        4. You can add :material-file:`GTAIVOnly`, :material-file:`TLADOnly` or a :material-file:`TBoGTOnly` if you don't need the mod to load in any other DLC. Otherwise, edit :material-file-cog:`modloader.ini` for priority and when the mods should or should not load.

        ??? warning "Expected folder structure"
            * :material-folder:==GTAIV==\
                * :material-folder:==modloader==\
                    * :material-folder:==Mod1==\
                        * :material-file:`IVAnims.ForEveryGame.img`
                        * :material-file:`WeaponInfo.xml`
                    * :material-folder:==Mod1.TLADOnly==\
                        * :material-file:`TLADOnly`
                        * :material-file:`TLADAnims.img`
                        * :material-file:`WeaponInfo.xml`
                    * :material-folder:==Mod1.TBoGTOnly==\
                        * :material-file:`TBoGTOnly`
                        * :material-file:`TBoGTAnims.img`

    ??? "Configuring the modloader"
        To configure the modloader, edit :material-file-cog:`modloader.ini` in :material-folder:==modloader==. Make sure you set the correct priority so you don't have unwanted mods overriding other mods(higher number - higher priority). Make sure mods that should be be injected to TBoGT or TLAD are disabled for IV (Ep0), mods that are for TBoGT are disabled for TLAD (Ep1), and mods that are for TLAD are disabled for TBoGT(Ep2). ==This isn't necessary if you left :material-file:`GTAIVOnly`, :material-file:`TLADOnly` or :material-file:`TBoGTOnly` files.== If you have issues - experiment with disabling mods.
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
    ??? "Increasing the limits"
        To increase the limits, edit :material-file-cog:`IVTweaker.ini` - you may want to do this if you install mods that, for example, change vehicle textures as you may encounter the taxi bug.

[:material-page-first:Previous page <br>OpenIV</br>](openiv.md){ .md-button } [Next page:material-page-last: <br>Mods</br>](mods.md){ .md-button .md-button--primary }