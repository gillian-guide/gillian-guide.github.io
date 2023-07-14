title: Modloading
description: Methods for injecting mods into your GTA IV installation to avoid replacing internal files.

# Modloading
Most mods require replacing internal files with OpenIV. We can get around that by using a modloader - or two!

# What's the difference between them?
While they're different in some ways, you can still use both of them if you're using 1.0.8.0 or 1.0.7.0.

| Advantages | IV Tweaker | UAL's |
| :--------: | :--------: | :---: |
| 1.0.8.0 and 1.0.7.0 support | :material-checkbox-marked-circle: | :material-plus-minus: |
| Complete Edition support | :material-cancel: | :material-checkbox-marked-circle: |
| Can inject .img files | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
| Can inject other files without overriding | :material-checkbox-marked-circle: | :material-cancel: |
| Bigger variety of supported inject files | :material-checkbox-marked-circle: | :material-cancel: |
| Bigger variety of supported override files | :material-cancel: | :material-checkbox-marked-circle: |
| Subfolder support | :material-cancel: | :material-checkbox-marked-circle: |
| A simple .ini for configuration | :material-checkbox-marked-circle: | :material-cancel: |

## IV Tweaker
!!! warning ""
    Only supports 1.0.8.0 and 1.0.7.0.
This modloader is in many ways superior to UAL's - mainly, being able to merge different files and having a simple .ini file for configuration. It also allows to increase limits for various thing - such as VehicleBudget to avoid the taxi bug.

- Installation:
    * Go to the bottom of the [page](https://zolika1351.pages.dev/mods/ivtweaker) and download the archive.
    * Extract the :material-zip-box:`IVTweaker_vx.x.zip` to your game folder.
    * You're done!

- Usage:
    * To increase the limits, edit :material-file-cog`IVTweaker.ini` - you may want to do this when you install mods that change vehicle textures, for example, as you may encounter the taxi bug.
    * To install mods, create a folder with your mod's name in :material-folder:==modloader==. After that, create(with OpenIV) or place an `.img` or other [supported files](https://zolika1351.pages.dev/mods/ivtweaker) into that folder. ==Do not use subfolders. Use different folders for files that can apply to both IV and EFLC DLC's to avoid compatibility issues==.
    * To configure the modloader, edit :material-file-cog:`modloader.ini` in :material-folder:==modloader==. Make sure to set a correct priority so you don't have unwanted mods taking priority of other ones. Make sure mods that are supposed to be injected to TBoGT or TLAD are disabled for IV (Ep0), mods that are for TBoGT are disabled for TLAD (Ep1) and mods that are for TLAD are disabled for TBoGT(Ep2)

## Ultimate ASI Loader's
!!! warning ""
    Supports Complete Edition.
    
    Already included with [FusionFix](/Essential-Modding/FusionFix).
    
    Can support 1.0.8.0/1.0.7.0 by renaming to `xlive.dll` and using latest [ZolikaPatch](/Essential-Modding/ZolikaPatch).
This modloader is not as robust as IV Tweaker, but can replace all kinds of files.

- Installation:
    * Go to the [Releases](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases) page.
    * Download :material-zip-box:`Ultimate-ASI-Loader.zip`
    ??? question "Why not :material-zip-box:`Ultimate-ASI-Loader_x64.zip`? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-zip-box:`Ultimate-ASI-Loader_x64.zip`.
    * Extract to game folder.
- Usage:
    * For `.img` mods, create a folder with your mod's name in :material-folder:==update==. After that, create(with OpenIV) or place an `.img` into that folder. ==If your mod has files that can apply to both IV and EFLC DLC's, create :material-folder:`IV`, :material-folder:`TLAD` and :material-folder:`TBoGT` subfolders and place the .img files separately to avoid compatibility issues==.
    * For mods that replace other files, create an identical to game's folder structure in :material-folder:==update== and place the replacement files in their corresponding folders. ==Do not use the mod folders.==