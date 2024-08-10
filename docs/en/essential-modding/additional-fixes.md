title: Additional Fixes (List)
description: There's more??

# Additional Fixes (List)

Following mods are fixes that I'd personally consider essential, as they don't have any downsides or incompatibilities to them.

!!! warning ""
    [FusionFix](../essential-modding/fusionfix.md) is required for most mods. **This page will assume you have it installed and will not remind you of it.**

---

## [Luis' Helmet Reflections Fix](https://www.gtainside.com/en/gta4/skins/125863-luis-s-helmet-reflections-fix/)

This mod fixes the bleak reflection on TBoGT player model's helmet.

<h3>Installation</h3>

1. Download this [archive](https://drive.google.com/file/d/14uB8cRR7DXYXc4HPCxoGd3J78nc1zBK8/view?usp=sharing).
2. Extract the :material-folder: ==update== folder from the archive into the game folder.

---

## [Liberty Ferry Terminal - Waiting Sign Fix & Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/)

These mods by donnits fix minor issues on the map.

<h3>Installation</h3>

1. Download this [archive](https://drive.google.com/file/d/1LnT29wamuxJp1Xo074b50IU8gLDJjRxL/view?usp=sharing).
2. Extract the :material-folder: ==update== folder from the archive into the game folder.

---

## [Responsive Plus](https://gtaforums.com/topic/931069-iveflc-responsive-plus/) - `cargrp.dat` and `carcols.dat` fixes

These fix some oversights in the original files that prevent some cars from spawning as intended.

<h3>Installation</h3>

1. Download this [archive](https://drive.google.com/file/d/1s0upbkeDpH9zJ03ELXrcOItMZw17xvVC/view?usp=sharing).
2. Extract the :material-folder: ==update== folder from the archive into the game folder.

---

## [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/)

This mod fixes an incorrect suit in Perseus, as you end up buying a different one from the one displayed.

<h3>Installation</h3>

1. Download this [archive](https://drive.google.com/file/d/19HKJfv_nwLJQxlkiQMnoNqRAymgwAElq/view?usp=sharing).
2. Extract the :material-folder: ==update== folder from the archive into the game folder.

---

## [Default Pistol Iron Sight Fix](https://www.nexusmods.com/gta4/mods/15)

This mod fixes an oversight in the pistol's model where the iron sight doesn't make any sense.

<h3>Installation</h3>

1. Download this [archive](https://drive.google.com/file/d/1xVV-towntlO8uZX5N1Ftt83zGljKIamf/view?usp=sharing).
2. Extract the :material-folder: ==update== folder from the archive into the game folder.

---

## [Menu Art Fix](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072165611)

This mod fixes the lower-resolution backgrounds in EFLC menus and removes the Social Club text.

<h3>Installation</h3>

TBA (original download link got nuked)

---

## [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/)

This mod fixes the IV Bikers voicelines in EFLC.

<h3>Installation</h3>

1. Go to the [GTAForums page](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/).
2. Press the **Download** link.
3. Extract the :material-file:`BYeah.dat16` file to :material-folder: ==GTAIV/TLAD/pc/audio/config/==.
4. If the **radio was downgraded by the guide**, add the following after `<game content="ascii">ex:/pc/audio/config/epx_game.dat</game>` in the :material-file:`e1_audio.xml` file in the :material-folder: ==GTAIV/update/TLAD/== folder and an :material-file:`e2_audio.xml` file in :material-folder: ==GTAIV/update/TboGT/==:

```text
    <game content="ascii">platform:/audio/config/BYeah.dat</game>
```

- If the **radio was not downgraded by the guide**, copy the same-named files from the vanilla :material-folder: ==GTAIV/update/TLAD|TBoGT/== folders to the :material-folder: ==update== folder and do the same steps as above.

---

## [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes)

This mod fixes green-ish textures on some character models.

<h3>Installation</h3>

1. Download this [archive](https://drive.google.com/file/d/1R--bkDVJIEk_ZzScJNuLQn7B6yCIuQwv/view?usp=sharing).
2. Extract the :material-folder: ==update== folder from the archive into the game folder.
3. Extract the other folders into any empty folder.
4. Copy the :material-file:`playerped.rpf` archive from :material-folder: ==GTAIV/pc/models/cdimages/== to :material-folder: ==GTAIV/**update**/pc/models/cdimages/==.
5. Copy the :material-file:`playerped.rpf` archive from :material-folder: ==GTAIV/TBoGT/pc/models/cdimages/== to :material-folder: ==GTAIV/**update**/TBoGT/pc/models/cdimages/==.
6. Open the copied archives with [OpenIV](../../resources/openiv.md/#editing-existing-archives-installing-mods-to-game-files).
7. Copy the files from :material-folder: ==IV - playerped.rpf== to the archive you copied in step 4.
8. Copy the files from :material-folder: ==TBoGT - playerped.rpf== to the archive you copied in step 5.

---

## [Luis' Bag Texture Fix](https://www.gtainside.com/en/gta4/skins/136118-luis-s-bag-texture-fix/)

This mod adds missing normal and specular maps and improves texture quality on TBoGT player model's bag.

<h3>Installation</h3>

1. Download the mod.
2. Extract the archive into any empty folder.
3. Copy the :material-file:`playerped.rpf` archive from :material-folder: ==GTAIV/TBoGT/pc/models/cdimages/== to :material-folder: ==GTAIV/**update**/TBoGT/pc/models/cdimages/==.
    - Skip this step if you had already done it earlier with other mods.
4. Open the copied archive with [OpenIV](../../resources/openiv.md/#editing-existing-archives-installing-mods-to-game-files).
5. Using the files from the mod, replace the :material-file:`suse_002_u.wdr` and :material-file:`suse_002_a_uni.wdr` in the archive.

---

## [Johnny's Shoe Texture Fix](https://www.gtainside.com/en/gta4/skins/125196-johnny-s-shoe-texture-fix/)

This mod adds missing normal and specular maps to the TLAD player model's shoes.

<h3>Installation</h3>

1. Download the mod.
2. Extract the archive into any empty folder.
3. Copy the :material-file:`playerped.rpf` archive from :material-folder: ==GTAIV/TLAD/pc/models/cdimages/== to :material-folder: ==GTAIV/**update**/TLAD/pc/models/cdimages/==.
4. Open the copied archive with [OpenIV](../../resources/openiv.md/#editing-existing-archives-installing-mods-to-game-files).
5. Using the file from the mod, replace the :material-file:`feet_000_u.wdr` in the archive.

---

## [Reduced Trafic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/)

This mod changes the pitch of the traffic screech in Algonquin to match the real-life levels you'd usually hear in Times Square.

<h3>Installation</h3>

1. Download the mod.
2. Extract the archive into any empty folder.
3. Copy the :material-file:`resident.rpf` archive from :material-folder: ==GTAIV/pc/audio/sfx/== to :material-folder: ==GTAIV/**update**/pc/audio/sfx/==.
4. Open the copied archive with [OpenIV](../../resources/openiv.md/#editing-existing-archives-installing-mods-to-game-files).
5. Using the file from the mod, replace the :material-file:`AMB_RESIDENT` file in the :material-folder: ==RESIDENT== folder inside the archive.

---

## `.img` limits

You may want to manually merge some `.img` mods together using [OpenIV](../../resources/openiv.md/#creating-archives) to avoid going over the limit.

You can see how far you are on the limits if you set `ExtraInfo` to `1` in FusionFix's :material-file-cog:`GTAIV.EFLC.FusionFix.ini` - it'll give the number on bottom of the screen in settings.

---

## Navigation

[:material-page-first:Previous page <br>Various Fixes</br>](various-fixes.md){ .md-button } [Next page:material-page-last: <br>Recommended Enhancements</br>](../../enhancements.md){ .md-button .md-button--primary }
