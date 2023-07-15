title: Modloading
description: Methods for injecting mods into your GTA IV installation to avoid replacing internal files.
hide: footer

# Modloading
Most mods require replacing internal files with OpenIV. We can get around this by using a modloader - or two!

## What's the difference between them?
While they are different in some ways, you can still use both if you're running 1.0.8.0 or 1.0.7.0. UAL's, for example, can cover what IV Tweaker doesn't support.
???+ question "Comparison"
    | Advantages | IV Tweaker | UAL's |
    | :--------: | :--------: | :---: |
    | 1.0.8.0 and 1.0.7.0 support | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Complete Edition support | :material-cancel: | :material-checkbox-marked-circle: |
    | Can inject .img files | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Can inject other files without overriding | :material-checkbox-marked-circle: | :material-cancel: |
    | Greater variety of supported inject files | :material-checkbox-marked-circle: | :material-cancel: |
    | Greater variety of supported override files | :material-cancel: | :material-checkbox-marked-circle: |
    | Subfolder support | :material-cancel: | :material-checkbox-marked-circle: |
    | A simple .ini for configuration | :material-checkbox-marked-circle: | :material-cancel: |

## IV Tweaker
!!! warning ""
    Supports 1.0.8.0 and 1.0.7.0 only.
This modloader is superior to UAL's in many ways - especially the ability to merge different files and having a simple .ini file for configuration. It also allows to increase limits for various things - like VehicleBudget to avoid the taxi bug.
???+ note "Installation"
    * Go to the bottom of the [page](https://zolika1351.pages.dev/mods/ivtweaker) and download the archive.
    * Extract the :material-zip-box:`IVTweaker_vx.x.zip` to your game folder.

???+ info "Usage"

    ??? "Installing mods"
        To install mods, create a folder with the name of your mod in :material-folder:==modloader==. Then create(with OpenIV) or place an `.img` or other [supported files](https://zolika1351.pages.dev/mods/ivtweaker) in that folder. ==Don't use subfolders. Use different folders for files that can be used for both IV and EFLC DLCs to avoid compatibility issues==.
        ??? warning "Expected folder structure"
            Improved Animations mod will be used for an example.

            * :material-folder:==GTAIV==\
                * :material-folder:==modloader==\
                    * :material-folder:==IVImprovedAnimations==\
                        * :material-file:`IVAnims.img`
                        * :material-file:`WeaponInfo.xml`
                    * :material-folder:==TLADImprovedAnimations==\
                        * :material-file:`TLADAnims.img`
                    * :material-folder:==TBoGTImprovedAnimations==\
                        * :material-file:`TBoGTAnims.img`
                            

    ??? "Configuring the modloader"
        To configure the modloader, edit :material-file-cog:`modloader.ini` in :material-folder:==modloader==. Make sure you set the correct priority so you don't have unwanted mods overriding other mods. Make sure mods that should be be injected to TBoGT or TLAD are disabled for IV (Ep0), mods that are for TBoGT are disabled for TLAD (Ep1), and mods that are for TLAD are disabled for TBoGT(Ep2). If you have issues - experiment with disabling mods.
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

## Ultimate ASI Loader
!!! warning ""
    See [Ultimate ASI Loader](ultimate-asi-loader.md) for installation.

    Supports the Complete Edition.
    
    Can support 1.0.8.0/1.0.7.0 by using latest [ZolikaPatch](/Essential-Modding/ZolikaPatch).
This modloader is not as robust as IV Tweaker, but can replace all kinds of files.

???+ info "Usage"

    ??? "Installing mods"
        * For `.img` mods, create a folder with the name of your mod in :material-folder:==update==. Then create (with OpenIV) or place an `.img` in that folder. ==If your mod has files that can be used for both IV and EFLC DLCs, create :material-folder:`IV`, :material-folder:`TLAD` and :material-folder:`TBoGT` subfolders and place the .img files separately to avoid compatibility issues==.

        * For mods that replace other files, create an identical folder structure to the game's in :material-folder:==update== for the replacement files and place the replacement files in their respective folders. ==Don't use the mod folders.==
        ??? warning "Expected folder structure"
            Improved Animations mod will be used for an example.

            * :material-folder:==GTAIV==\
                * :material-folder:==update==\
                    * :material-folder:==ImprovedAnimations==\
                        * :material-folder:==IV==\
                            * :material-file:`IVAnims.img`
                        * :material-folder:==TLAD==\
                            * :material-file:`TLADAnims.img`
                        * :material-folder:==TBoGT==\
                            * :material-file:`TBoGTAnims.img`
                    * :material-folder:==common==\
                        * :material-folder:==data==\
                            * :material-file:`WeaponInfo.xml`
                    * :material-folder:==TLAD==\
                        * :material-folder:==common==\
                            * :material-folder:==data==\
                                * :material-file:`WeaponInfo.xml`

    ??? "Configuring the modloader"
        Currently, I do not know of any way to configure the modloader to set up a priority or anything else. [Contact me](contact-me.md) if you know a way to.

[:material-page-first:Previous page <br>Ultimate ASI Loader</br>](ultimate-asi-loader.md){ .md-button } [Next page:material-page-last: <br>Essential Modding</br>](essential-modding/index.md){ .md-button .md-button--primary }