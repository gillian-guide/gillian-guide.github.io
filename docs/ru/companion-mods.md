title: Companion Mods
description: How many mods does this game have

# Companion Mods

!!! question "А где русский ёпта"
    Следующие части гайда не будут переведены на русский из-за отсутствия желания и времени, хотя по желанию кто-нибудь может выпустить PR на гитхабе с переводом всех последующих частей. Сори

This page includes mods that are either fixes, enhancements, or whatever else - something that's not a huge must-have mod on it's own, but can be used to enhance the experience in one way or another. They're separated in 3 groups - [Fixes](#fixes), [Enhancements](#enhancements) and [Miscellaneous](#miscellaneous). Don't look for mods to add into the Drag-and-Drop Archive here - the archive already includes all the mods I deem needed, and the additional mods for it can be found [there](../drag-and-drop-archive.md/#additional-mods) as well.

!!! warning ""
    [FusionFix](../essential-modding/fusionfix.md) is required for most mods. **This page will assume you have it installed and will not remind you of it.**

!!! warning "For Linux users"
    When installing mods, be careful and take note when filenames have different casing (e.g. `weaponinfo.xml` and `weaponInfo.xml`). Make sure to merge them accordingly.

???+ tip "How to install the mods?"
    Depends on the mod! There's 6 different types, usually:

    - Type 1: basic `.asi` mods that don't require a special mod loader: those go into a :material-folder: ==plugins== folder or simply into the root folder;
    - Type 2: mods packaged for Fusion Overloader. They come with an :material-folder: ==update== folder - you simply extract that into the game folder. However, if there's merge conflicts, you will have to manually merge those files using something like [WinMerge](https://winmerge.org/downloads/?lang=en);
    - Type 3: mods made for :material-file:`playerped.rpf`. Installation instructions for these can be read on [this page](../extras/modloading.md/#installing-mods-with-other-kind-of-files);
    - Type 4: mods with loose files that are meant to go into an :material-file:`.img`. Installation instructions for these can be read on [this page](../extras/modloading.md/#installing-mods-with-files-that-go-into-img-archives);
    - Type 5: mods with loose files that are meant to go into folders like :material-folder: ==common/data/==. Installation instructions for these can be read on [this page](../extras/modloading.md/#installing-mods-with-other-kind-of-files);
    - Type 6: script mods that require a special mod loader (either ScriptHookDotNet or IVSDKDotNet): install the [required modloader](../resources/mod-dependencies.md/#scripthookdotnet), then the mod per installation instructions

    The type tends to be easily recognizable and once you start installing the mods, it should be easy enough to figure it out. If you're finding it hard to do so (or the mod is some other kind entirely), feel free to ask for support on my [Discord server](https://discord.gg/zwmsQqExbQ) on the dedicated #community-modding channel.

    You should keep in mind, however, that not all the mods on the list are 100% compatible with each other. The intention is for *you* to pick what mods to use between the two conflicting ones, if they aren't merge-able (such as two different popcycle mods).

---

## Fixes

These mods fix some aspect of the game without adding or changing something drastically.

| Mod | Developer(s) | Details |
| :-: | :----------: | :-----: |
| [Grass and Procedural Props Fix](https://www.nexusmods.com/gta4/mods/1230) | iammrmikeman | Fixes up the capacity for procedural grass and props so that it doesn't just disappear over some time of playing. |
| [Improved Animations Pack](https://gtaforums.com/topic/958625-improved-animations-pack/#comments) | B Dawg and C1aude_III | Fixes various issues with the weapon animations. |
| [Broker Bridge and Electric Wires Appearance Fix](https://www.gtainside.com/en/gta4/mods/214695-broker-bridge-and-electric-wires-appearance-fix/) | yarrabandi | Improved shaders for the Broker Bridge. |
| [Clean Getaway - Destination Fix](https://gtaforums.com/topic/989680-attramets-workshop/page/3/#comment-1072596471) | Attramet | Changes the destination on the mission 'Clean Getaway' to be more accurate to the dialogue. |
| [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | B Dawg | Fixes green-ish textures on some character models. |
| [Track Jackets Fix](https://www.nexusmods.com/gta4/mods/773) | Niikowo | Fixes the shading on track jacket textures to match the green track jacket. |
| [Puffer Jacket Logo](https://www.nexusmods.com/gta4/mods/542) | erwasabo | Adds the missing logo to one of the Puffer jackets. |
| [No More Hand Seams for Niko](https://www.gtainside.com/en/gta4/skins/192418-no-more-hand-seams-for-niko/) | BrynnaDaRosa | Fixes the hand texture seams in Niko's model. Addons used: [TBoGT Niko In-Game Hands Fix](https://discord.com/channels/452421215076876288/461150059552178176/1535212054997241896), [TLAD Niko In-Game Hands Fix](https://discord.com/channels/1129805289307242577/1494424154097586206/1538900507618451587); both by Pingwinek1234 |
| [Ray Boccino Shirt Fix](https://www.nexusmods.com/gta4/mods/959) | DeathWrench | Fixes Ray Boccino's poor textures. |
| [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | _ys | Fixes an incorrect suit in Perseus, as you end up buying a different one from the one displayed. |
| [Schottler Parked Vehicles Fix](https://www.moddb.com/mods/schottler-parked-vehicles-fix) | Callistonian | Fixes wrongly parked vehicles in Schottler area. |
| [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | B Dawg | Fixes the IV Bikers voicelines in EFLC. |
| [Pistol Iron Sight Fix](https://drive.google.com/file/d/1YJLc7dsrDiEQEgzfv4Mn6UmMjQcVBcmg/view?usp=sharing) | Gillian (me) | Fixes an oversight in the pistol's model where the iron sight doesn't make any sense. |
| [Liberty Ferry Terminal - Waiting Room Sign Fix](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Fixes broken UV map on "Waiting Room" sign texture. |
| [Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Edits the UV map on the sign to include an unused texture. |
| [EFLC Vehicle Addon Pack For GTA IV](https://gtaforums.com/topic/972433-eflc-vehicle-addon-pack-for-gta-iv-with-proper-audio-and-naming/) | 7urbo1ag | **ONLY OPTIONALS**: Aims to further fix the inconsistency between base GTA IV and EFLC. Used: Fixed Infernus Exit Animations, Correct Extras on Gracie's Fetzler in 'Blog This...', Fixed ZombieB Colors in 'Was it Worth It' |
| [Steam Achievements](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/) | Zolika1351 | Allows to get :material-steam: Steam achievements on **older patches**. |
| [CloudFixIV](https://discord.com/channels/452421215076876288/461150059552178176/1541206795769356488) | Chunk | Fixes some issues related to ImGui and cloud rendering. **Only relevant to IVSDKDotNet users.** |

---

## Enhancements

These mods enhance some aspect of the game that already exists or just makes sense to exist.

| Mod | Developer(s) | Details |
| :-: | :----------: | :-----: |
| [Liberty Tweaks](https://gtaforums.com/topic/991160-liberty-tweaks/) | catsmackaroo, ItsClonkAndre and others | Aims to improve various aspects of the game and it's general Quality of Life. Highly configurable. **1.0.8.0 only.** Addon available: [Armored Cops with EFLC heads from Characters Fixes by Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1540680532780916757)<br>==Allows to quicksave using the ++f9++ key and has a lot of various gameplay features - if you're not a fan of the defaults, you can modify things to your taste in :material-file-cog:`LibertyTweaks.ini` located in :material-folder: `IVSDKDotNet\scripts\`==</br> |
| [Trilogy Characters Fixes](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/) | TheYoshiPunch, (Japan) GTA Love and others | Aims to fix the inconsistency of characters between base GTA IV and EFLC. [Custom version with community fixes and community addons](https://www.mediafire.com/file/bo3uxpvozs6mgfx/7_Characters_Fixes.7z/file), which include: [Mitch The Cop TLAD Model by Pingwinek123](https://www.nexusmods.com/gta4/mods/963), [Johnny K Eye Color V~1.2~ by nipahtard](https://www.nexusmods.com/gta4/mods/1110), [Brucie Kibbutz TBoGT Model for IV by nipahtard](https://www.nexusmods.com/gta4/mods/988) |
| [Animated Weapons](https://www.nexusmods.com/gta4/mods/641?tab=description) | ImpossibleEchoes, Spartan112 | Adds detailed weapon animations to every animation. **May conflict with other mods**. |
| [More Visible Interiors](https://gtaforums.com/topic/974099-more-visible-interiors/) | Attramet | Makes interiors more visible from the outside, although comes with a downside of potential pop-in. |
| [Higher Resolution Miscellaneous Pack](https://www.nexusmods.com/gta4/mods/357/) | Ash_735 | Improves the texture quality of minor assets. |
| [HQ Map](https://www.nexusmods.com/gta4/mods/356?tab=description) | Alkimical | A high resolution version of the pause menu map. **Should only be used on 1440p and higher resolutions - doesn't look smooth on lower resolutions.** |
| [UHD Vanilla Map and Radar](https://www.nexusmods.com/gta4/mods/456) | ValentynL | Alternative version of a high resolution of a pause menu map.  **Should only be used on 1440p and higher resolutions - doesn't look smooth on lower resolutions. Also, may cause stability issues.** |
| [HD HUD and Reticle](https://www.nexusmods.com/gta4/mods/455) | ValentynL | A high resolution version of the HUD and the aiming reticle. **Should only be used on 1440p and higher resolutions - doesn't look smooth on lower resolutions. Also, may cause stability issues.** |
| [Project Glass](https://discord.gg/gZvZmFt2p7) | DayL | Adds cubemap reflections to what otherwise is just transparent glass. |
| [Vehicle Pack](https://www.nexusmods.com/gta4/mods/282?tab=files) | Ash_735 | Improves the texture quality of all vehicles in the game. Some textures are upscaled, some are taken from Max Payne 3 and GTA V. |
| [LibertyCityPlates](https://www.nexusmods.com/gta4/mods/875?tab=description) | Ash_735 | Makes license plates unique for every vehicle. |
| [Potential Grim](https://gtaforums.com/topic/945227-iveflc-potential-grim/) | Lord Criminal | Adds more ped variety, corrects some ped behaviours and adds progressive gang relationships. Community addon: [Optimized biker textures from Hardcore Lost MC by B Dawg](https://gtaforums.com/topic/945227-iveflc-potential-grim/?do=findComment&comment=1072426693). **This mod may be hard to install, even in the Drag-and-Drop Archive it's severely cut - beware.** |
| [BetterRaceIV](https://github.com/LotsofEds/BetterRaceIV) | ServalEd | Makes the racing AI opponents better at racing. **1.0.8.0 only.** |
| [New game parameters for transport and traffic](https://www.nexusmods.com/gta4/mods/616?tab=description) | Ushan27 | Increases and improves vehicle and ped variety in different regions. |
| [Fidelity Popcycle](https://www.nexusmods.com/gta4/mods/405?tab=description) | Chunk | A vanilla-friendly popcycle that makes the city life more varied and realistic. |
| [Bullet Penetration - Minimal Edition](https://gtaforums.com/topic/989496-bullet-penetration/) | Internet Rob | Allows bullets to penetrate glass like they do with car windshields. |
| [Yes Way On The Subway](https://www.gtainside.de/en/gta4/mods/200052-yes-way-on-the-subway-kill-jim-early/) | ServalEd | Removes invincibility from the target in the mission 'No Way On The Subway'. |
| [Escuela of the Sleep](https://www.nexusmods.com/gta4/mods/507?tab=description) | ServalEd | Makes the 'Escuela of the Street' mission faster by making the driver ignore traffic laws. |
| [Johnny K Eye Color V](https://www.nexusmods.com/gta4/mods/1110) | nipahtard | Better textures for Johnny in TLAD and TBoGT, ported from GTA V. |
| [Artwork Joni](https://www.nexusmods.com/gta4/mods/975) | BrynnaDaRosa | Joni's model redone to match her artwork, because the in-game model is hideous. |
| [Dodgy Doc - Higher Quality](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Improves the quality of the Dodgy Doc in the Have a Heart mission. |
| [High Quality Pigeons](https://www.gtainside.de/gta4/mods/166924-high-quality-pigeons/) | Supreme Dear Leader | Improves the model and texture quality for pigeons. [Textures downscaled by Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1538872350928408737). |
| [Improved Spyde Jacket](https://www.gtainside.com/en/gta4/skins/213587-improved-spyde-jacket/) | Lukakion | Improves the track jacket's model to be higher poly and fixes the normal maps. |
| [Plane Flight Path Improvements](https://www.gtagaming.com/plane-flight-path-improvements-f33591.html) | C4PT41N BOMB4RD | Makes the plane flight paths more realistic. |
| [Replaced Esperanto by Roman's Taxi in Cab Depot](https://gtaforums.com/topic/989680-attramets-workshop/) | Attramet | Replaces the Esperanto in Roman's Cab Depot with his own taxis. |
| [Reduced Traffic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | GladiTek | Changes the pitch of the traffic screech in Algonquin to match the real-life levels you'd usually hear in Times Square. |
| [Stevie Car Theft Photo-Fixes](https://www.gtainside.com/en/gta4/mods/212547-stevie-car-theft-photo-fixes/) | AXL163 | Re-does some of Stevie's Car Theft photos to match final/modded look of the game and vehicles. |
| [Menu Art Fix](https://drive.google.com/file/d/1g1AtEBNV2ElitGECGBD14Y0EsDN6XXR_/view?usp=drive_link) | _ys | Fixes the lower-resolution backgrounds in EFLC menus. |
| [GTA V's fxdecals](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Replaces some decals with faithful higher resolution counterparts from GTA V. |
| [TBoGT timecyc with DoF and Bloom](https://gtaforums.com/topic/934545-fusion-fix/page/149/#comment-1072589037) | Magic_Al | Enables DoF and Bloom in TBoGT (which are disabled by Rockstar's design). |
| Increased LODs in `visualSettings.dat` | Gillian | Changes some values of `visualSettings.dat` to use GTA Vs LOD values. |
| [Consistent Pump Shotgun](https://drive.google.com/file/d/1AaYVYhaRVW9pA5dzTcsAEj_EgjeV2ST5/view?usp=sharing) | Haxogone, me, Ash_735 | Slight file shift to use the TLAD's gameplay and prop model for pump shotgun in IV and TBoGT. |
| [Fixed Combat Shotgun Icon](https://www.gtainside.com/gta4/mods/116711-fixed-combat-shotgun-icon) | DavSte | Changed Combat Shotgun icon to resemble the in-game model. I don't like because it looks too busy compared to other icons. |
| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) and [Higher Res Radio Logos Menu](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871) | Ash_735 | Increases the quality of UI radio icons, as they are highly inconsistent with other UI assets in the game. |

---

## Miscellaneous

These mods don't enhance or fix anything necessarily - they're mods that *will* alter the experience in some way or add on top of it. Some of these are really nice to have but just didn't feel like they were a fit for the previous two groups, so there's that.

| Mod | Developer(s) | Details |
| :-: | :----------: | :-----: |
| [Console Visuals](https://github.com/Tomasak/Console-Visuals/) | Tomasak, nastyyaboi, Ash_735, Attramet, brokensymmetry and Parallellines | Ports select console visuals to the PC version. |
| [Console Select Menu](https://github.com/gennariarmando/iv-console-select-menu/) | _AG | Replaces the episode selector with a console-like menu which, in my opinion, looks better. **1.2.0.59 only**. [Manual build of a more up-to-date version](https://www.mediafire.com/file/1aiyfmcy74otkbj/ConsoleSelectMenuIV.asi/file). |
| [Liberty Loadout](https://www.nexusmods.com/gta4/mods/1226) | Delusional94 | GTA V-like weapon and radio wheel. **1.2.0.59 only**. |
| [Liberty Shoulder](https://www.nexusmods.com/gta4/mods/1229) | Delusional94 | Shoulder swapping without any extras. **1.2.0.59 only**. |
| [Correction of physical parameters of transport](https://www.nexusmods.com/gta4/mods/714) | Ushan27 | Modified driving parameters to make driving feel more controllable without changing the system drastically. You can read the details on the page. |
| [Restored Pedestrians](https://gtaforums.com/topic/981864-restored-pedestrians/) | Attramet | Restores pedestrians that were either unused or only present in the betas. |
| [Various Pedestrians Actions](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Attramet | Adds, corrects and completes unfinished actions for pedestrians. |
| [Restored Vegetation](https://gtaforums.com/topic/984591-restored-trees-position/) | Attramet | Restores vegetation that was present in the betas but removed in the final release, either as an oversight or due to performance concerns. |
| [Restored Graffiti](https://gtaforums.com/topic/1005785-restored-graffiti/) | Attramet | Restores graffiti, which were completely cut out in the final build of the game. |
| [Xbox Rain Droplets](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Adds nice water droplets on the screen. |
| [Project Thunder](https://gtaforums.com/topic/982902-project-thunder/) | ItsClonkAndre | Improves how thunder appears in-game, with actual lighting and improved atmosphere. Highly configurable. **1.0.8.0 only**. |
| [VAmbience](https://gtaforums.com/topic/981402-vambience/) | ItsClonkAndre | Adds background noise to the game, such as driving and shooting, alike to GTA V. Highly configurable. **1.0.8.0 only**. |
| [Props Restoration](https://gtaforums.com/topic/1004764-props-restoration/) | Attramet | Restores pre-release, beta and unused props to the map. |
| [Beta-Inspired Bank of Liberty](https://gtaforums.com/topic/1002675-interior-mod-beta-inspired-bank-of-liberty/) | Scott1 | Restores the interior of the Bank of Liberty to the state, similar to the one seen in Trailer 1 (mainly, the ceiling has a Dome now). |
| [Resized Blista Compact](https://www.gtainside.de/en/gta4/cars/188730-resized-blista-compact/) | Thundersmacker | Resizes the Blista Compact to match the real life counterpart (Honda CR-X). |
| [Restored Motorcycle Helmets](https://www.nexusmods.com/gta4/mods/1006?file_id=2604) | Attramet | Restores cut motorcycle helmets. [Merged with Project Glass and Characters Fixes by Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1539243333136683099). |
| [TV Restoration](https://gtaforums.com/topic/977025-tv-restoration/) | Attramet | Highest quality TV videos. |
| [Beta Radio](https://gtaforums.com/topic/1007007-iv-beta-radio/) | MrFinger | Restores 136 songs removed from GTA IV and EFLC. |
| [Addons for the Snow Mod](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_, Straysify, gdanbo and ThirteenAG | Parts of [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) and [Project2DFX](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest) bundled as addons for FusionFix's Snow Mode. |
| [IV-Presence](https://gtaforums.com/topic/975850-iv-presence/) | ItsClonkAndre | Adds a Discord Rich Presence (custom activity status). **1.0.8.0 only** |

---

The following mods are less recommended due to various degrees of instability, struggles of installation or personal distaste towards them (as in, they don't fully fit my vision of a vanilla-faithful GTA IV setup). If you like what you're seeing, however, you may attempt to install them.

| Mod | Developer(s) | Details |
| :-: | :----------: | :-----: |
| [Solitude](https://www.nexusmods.com/gta4/mods/417) | Chunk | A vanilla+ timecycle mod. |
| [DayL's Natural Timecycle](https://www.nexusmods.com/gta4/mods/396) | DayL | A natural timecycle mod. |
| [Revamped Visuals](https://libertycity.net/files/gta-4/217259-revamped-visuals-3-0.html) | Lukakion | Another vanilla+ timecycle mod. |
| [Project Birds](https://gtaforums.com/topic/980018-project-birds) | Internet Rob | Adds birds to the skies. |
| [Liberty Rush](https://gtaforums.com/topic/979688-liberty-rush/) | Internet Rob, ItsClonkAndre, donnits, Datalvarezguy | Adds dozens of improvements, restored content, new traffic scenarios etc. |
| [The Actual Complete Edition](https://gtaforums.com/topic/967792-grand-theft-auto-iv-the-actual-complete-edition/) | C1aude_III | This projects puts huge effort at merging IV and EFLC from weapons, vehicles and assets to the whole map. **Hard to install and highly conflicting with other mods**. |
| [TACE.lite](https://www.nexusmods.com/gta4/mods/774) | Snake Swagger | A lighter version of the above that only merges the weapons and vehicles. |
| [Liberty Alive](https://gtaforums.com/topic/992467-liberty-alive/#comments) | nabo45 | Adds a lot of interiors to the world. |
| [Enhanced Minor Characters](https://gtaforums.com/topic/978737-grand-theft-auto-iv-enhanced-minor-characters/) | Datalvarezguy | Replaces vanilla peds in some missions with author's visions for the characters. |
| [Hi-Res Characters](https://www.gtainside.de/en/gta4/mods/176255-hi-res-characters-update-v1-1-upscaled-mod/) | Primusideus | Upscaled and higher resolution character textures. |
| [The Hardcore Lost MC](https://gtaforums.com/topic/908470-iveflc-the-hardcore-lost-mc/) | iiCriminnaaL | Enhances the TLAD experience, changes bikers' appearance and AI. |
| [Outfit Enhancements](https://gtaforums.com/topic/908611-outfit-enhancements/) | iiCriminnaaL | Several simple enhancements for some clothing. |

---

## Recommended load order and `.img` limits

Please use the following load order (put the number before the folder names) after installing the mods above:

1. Minor Mods (any other mod you don't see below is considered minor - their order doesn't matter that much but they should be loaded on top)
2. Potential Grim
3. Restored mods
4. Higher Resolution Miscellaneous Pack
5. Vehicle Mods (Vehicle Pack, Resized Blista etc.)
6. Characters Fixes
7. Console Visuals
8. Project Glass
9. More Visible Interiors
10. FusionFix (leave it at the default folder name for ease of updating)
11. Various Fixes (leave it at the default folder name for ease of updating)

You may want to manually merge some `.img` mods together using [OpenIV](../resources/openiv.md/#creating-archives) to avoid going over the limit.

You can see how far you are on the limits if you set `ExtraInfo` to `1` in FusionFix's :material-file-cog:`GTAIV.EFLC.FusionFix.ini` - it'll give the number on bottom of the screen in settings - **but only on 1.2.0.58**. If you are using an older version, you can only tell if you went over the limit by going into TBoGT and seeing whether traffic spawns (if it doesn't - you're over the limit and it's a sign to merge some mods).

---

## Workshops

These workshops might have some extra mods or tools you may be interested in:

[Attramet's Workshop](https://gtaforums.com/topic/989680-attramets-workshop/){ .md-button}  [ItsClonkAndre's](https://gtaforums.com/topic/988909-itsclonkandres-workshop/){ .md-button}

[Zolika1351's Zone](https://zolika1351.pages.dev/){ .md-button} [Donnit's Bakery](https://gtaforums.com/topic/974798-donnits-bakery/){ .md-button}

[:simple-discord: DayL's Modding Community](https://discord.gg/gZvZmFt2p7){ .md-button} [Internet Rob's](https://gtaforums.com/topic/984476-internet-robs-workshop){ .md-button}

---

<h3>Workshops</h3>

These workshops might have some extra mods or tools you may be interested in:

[Attramet's Workshop](https://gtaforums.com/topic/989680-attramets-workshop/){ .md-button}  [ItsClonkAndre's](https://gtaforums.com/topic/988909-itsclonkandres-workshop/){ .md-button}

[Zolika1351's Zone](https://zolika1351.pages.dev/){ .md-button} [Donnit's Bakery](https://gtaforums.com/topic/974798-donnits-bakery/){ .md-button}

[:simple-discord: DayL's Modding Community](https://discord.gg/gZvZmFt2p7){ .md-button} [Internet Rob's](https://gtaforums.com/topic/984476-internet-robs-workshop){ .md-button}

---

<h3>Making mods</h3>

If you're interested in making mods yourself, visit this Discord server:

[:simple-discord: GTA IV Modding](https://discord.gg/p6RU4xJ){ .md-button .md-button--primary }

---

<h3>Want some mod to be listed?</h3>

Mention it on the Mod Suggestions thread on my Discord server:

[:simple-discord: My Discord server](https://discord.gg/zwmsQqExbQ){ .md-button .md-button--primary }

---

## Afterword

Thanks for using **my** guide for modding GTA IV!

I sincerely hope that I have helped you achieve the perfect state of the game. This guide takes some time to maintain, and it couldn't have been done without all the great mods, so please consider chipping in for some authors: [Credits](../resources/credits.md).

If you want more guides or modpacks like that, check out [Similar Guides & Resources](../resources/similar-guides-modpacks.md).

Additional resources and tools can be found on the [Extras](../extras/index.md) page and the Resources sections on the left.

---

<h3>Navigation</h3>

[:material-page-first:Previous page <br>Essential Modding</br>](../essential-modding/index.md){ .md-button }
