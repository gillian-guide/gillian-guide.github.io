title: Drag-and-Drop Archive
description: A complete ready-to-play drag-and-drop archive for your desired GTA IV version
hide: footer


# Drag-and-Drop Archive
You can choose an archive depending on the version you want - be it 1.2.0.59 or 1.0.8.0(a downgrader is included if you're using the [:material-steam:Steam](https://store.steampowered.com/app/12210/) or [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv) version). However, the modlist for this pack alone is mostly the same - you can see and compare it [below](#modlist). You'll mainly be lacking [ZolikaPatch](essential-modding/zolikapatch.md) and Liberty Tweaks.

### Notes
!!! info ""
	1. 1.2.0.59 is the Complete Edition, also known as the latest [:material-steam:Steam](https://store.steampowered.com/app/12210/) or [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv) version. It removes support for multiplayer and Games for Windows - LIVE, while adding the Rockstar Games Launcher (and it's DRM) and the Social Club overlay (with it's achievements). The amount of supported mods is also much more limited in this version - most mods are built for 1.0.8.0 and 1.0.7.0.
	2. 1.0.8.0 is the latest retail patch, with [ZolikaPatch](essential-modding/zolikapatch.md) and [multiplayer](multiplayer.md) support. However, this drag-and-drop archive does NOT include any support for Games for Windows - LIVE whatsoever. See the [downgrading](downgrading.md) and [multiplayer](multiplayer.md) sections instead. This version is better for mod compatibility.

!!! warning ""
	A potential new huge update is coming soon.

## Installation

=== "1.0.8.0"
	[:material-download-circle: Download](https://drive.google.com/file/d/1O1qD8ocbJ_fnERTvvVzyw6_bsw-k_evo/view){ .md-button .md-button--primary }
	
	Download the archive and then simply extract the contents to your game folder. After installation, go through [additional setup](additional-setup.md).
	!!! warning
		The archive must be installed on top of a clean, unmodded [:material-steam:Steam](https://store.steampowered.com/app/12210/) Complete Edition installation. 
		
		If you are using the [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv) version, do not start the game from the launcher itself, use :material-file:`PlayGTAIV.exe` instead - otherwise the game files will be replaced.
		
		Other installation methods are not supported.
		
		In addition, I will not support any additional modifications to the files other than the instructions already listed.
	??? info "Updating"
		If you're updating after installing the archive instead, delete :material-folder:==update== and :material-folder:==modloader== first.
	??? warning "If the game does not start"
		Try to install :material-file-download:`vcredist_x86.exe` that's in your game folder.

		Alternatively, your PC may not support DXVK - remove :fontawesome-solid-gears:`d3d9.dll` from the game folder or try async 1.10.3 from [additional mods](#additional-mods).
	??? warning "My game is behaving strangely/my game is crashing randomly"
		Disable mods one by one to see the culprit by editing :material-file-edit:`modloader.ini` in :material-folder:==modloader== or deleting mods in :material-folder:==update==. [Let me know if you find the problem](contact-me.md).
=== "1.2.0.59"
	[:material-download-circle: Download](https://drive.google.com/file/d/1eJ4cbVhJ4tnTGJByh_Lf4eS5SS2ShmHO/view){ .md-button .md-button--primary }

	Download the archive and then simply extract the contents into your game folder. After installation, go through [additional setup](additional-setup.md).
	!!! warning
		The archive must be installed on top of a clean, unmodded [:material-steam:Steam](https://store.steampowered.com/app/12210/) Complete Edition installation.
		
		Other installation methods are not supported.
		
		In addition, I will not support any additional modifications to the files other than the instructions already listed.
	??? info "Updating"
		If you're updating after installing the archive instead, delete :material-folder:==update== first.
	??? warning "If the game does not start"
		Your PC may not support DXVK - remove :fontawesome-solid-gears:`d3d9.dll` from the game folder or try async 1.10.3 from [additional mods](#additional-mods).
	??? warning "My game is behaving strangely/my game is crashing randomly"
		Disable mods one by one to see the culprit by deleting mods in :material-folder:==update==. [Let me know if you find the problem.](contact-me.md)

## Modlist
=== "1.0.8.0"
	| Mod name | Details |
	| :------: | :-----: |
	| [Downgrader~v16~ by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch/downgrading)| A simple drag&drop downgrade to 1.0.8.0 with [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader), ZolikaPatch, SteamAchievements and IV Tweaker included. |
	| [ZolikaPatch IV~7.56~ by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| First main mod in the pack: adds a lot of fixes and improvements - and the game won't boot without it. |
	| [IV Tweaker~2.2~ by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| Main modloader in the pack, also allows to increase limits for other mods. |
	| [Steam Achievements~v2~ by Zolika1351](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/)| Allows you to get :material-steam:Steam achievements on older patches. |
	| [FusionFix~1.60~ by ThirteenAG and others](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Second main mod in the pack: it contains a bunch of fixes and also acts as a modloader together with ultimate-asi-loader.md.<br>[Ported by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch/downgrading)</br> |
	| [Shader Fixes Collection~V106~ by Parallellines0451 and others](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection)| A collection of numerous shader fixes, from simple scaling to restoring console files. |
	| [DXVK~2.2~](https://github.com/doitsujin/dxvk)| Translates DirectX 9 API to Vulkan - main [optimization](optimization.md) method. ==Remove :fontawesome-solid-gears:`d3d9.dll` and change :material-file-cog:`dxvk.conf` options to Proton launch options instead if you're using Linux(or just remove the file).== |
	| [Liberty Tweaks~1.1~ by The Westside Minions & The GTA IV Modding Community](https://gtaforums.com/topic/991160-liberty-tweaks/)| A highly configurable quality-of-life mod. |
	| [Various Fixes~1.5~ by Attramet and others](https://gtaforums.com/topic/975211-various-fixes/)| A large collection of fixes of various scale - mostly broken map textures. |
	| [IV Fixes and Improvements~3.3~ by Zolika1351 and others](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| A collection of minor fixes and improvements - see the changelog on the page. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Fixes broken UV map on "Waiting Room" sign texture. |
	| [Sugar Chomps - Separate Signs by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Edits the UV map on the sign to include an unused texture. |
	| [Pedestrians with Unused Clothes Restored by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds unused clothing to some pedestrians. |
	| [Varied Alderney State Trooper Ped by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds diversity to police troppers. |
	| [Characters Fixes~2023-06-09~ by TheYoshiPunch, (Japan) GTA Love and others](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/)| A large collection of fixes for inconsistencies between character appearances in IV and EFLC - plus, a few fixes just for the models themselves.<br>Addon used: Niko's Original GTAIV Hair</br> |
	| [Project2DFX~4.3~ by ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Adds nice lights in the distance at night. ==Can be disabled by deleting the `IVLodLights` files.== |
	| [Console Visuals~1.2~ by nastyyaboi and others](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Collection of ported visuals from the console version - from timecyc, to animations.<br>Used addons: Console Clothing, Console Fences, Console Trees(PC Leaves)</br> |
	| [Improved Animations Pack~1.3~ by B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Fixes some weapon animation issues such as delayed fire. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Upscaled and ported vehicle textures from GTA V and Max Payne 3. |
	| [Xbox One/Series S+X Buttons by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| More modern textures for the controller buttons. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) and [Higher Res Radio Logos Menu by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)| High resolution textures of radio logos. |
	| [Improved Weapon Spec by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=107165200)| Higher resolution specular maps for weapons. |
=== "1.2.0.59"
	| Mod name | Details |
	| :------: | :-----: |
	| [FusionFix~1.60~ by ThirteenAG and others](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| The main mod of the pack, it contains a bunch of fixes and also acts as a modloader together with [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader). |
	| [Shader Fixes Collection~V106~ by Parallellines0451 and others](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection)| A collection of numerous shader fixes, from simple scaling to restoring console files. |
	| [DXVK~2.2~](https://github.com/doitsujin/dxvk)| Translates DirectX 9 API to Vulkan - main [optimization](optimization.md) method. ==Remove :fontawesome-solid-gears:`d3d9.dll` and change :material-file-cog:`dxvk.conf` options to Proton launch options instead if you're using Linux(or just remove the file).== |
	| [Various Fixes~1.5~ by Attramet and others](https://gtaforums.com/topic/975211-various-fixes/)| A large collection of fixes of various scale - mostly broken map textures. |
	| [IV Fixes and Improvements~3.3~ by Zolika1351 and others](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| A collection of minor fixes and improvements - see the changelog on the page. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Fixes broken UV map on "Waiting Room" sign texture. |
	| [Sugar Chomps - Separate Signs by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Edits the UV map on the sign to include an unused texture. |
	| [Pedestrians with Unused Clothes Restored by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds unused clothing for some pedestrians. |
	| [Varied Alderney State Trooper Ped by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds diversity to police troppers. |
	| [Characters Fixes~2023-06-09~ by TheYoshiPunch, (Japan) GTA Love and others](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/)| A large collection of fixes for inconsistencies between character appearances in IV and EFLC - plus, a few fixes just for the models themselves.<br>Addon used: Niko's Original GTAIV Hair<br>[Manually ported.](https://drive.google.com/file/d/19LA4e31Ibux3QpXo2PxHsjGu1xROtTG9/view?usp=drive_link)</br></br> |
	| [Project2DFX~4.5~ by ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Adds nice lights in the distance at night. ==Can be disabled by deleting the `IVLodLights` files.== |
	| [Console Visuals~1.2~ by nastyyaboi and others](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Collection of ported visuals from the console version - from timecyc, to animations.<br>Used addons: Console Clothing, Console Fences, Console Trees(PC Leaves)</br> |
	| [Improved Animations Pack~1.3~ by B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Fixes some weapon animation issues such as delayed fire. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Upscaled and ported vehicle textures from GTA V and Max Payne 3.<br>[Manually ported.](https://drive.google.com/file/d/1rMgtpkMBoyoaaFwYTl1bPV5eWEJwXQ4q/view?usp=drive_link)</br> |
	| [Xbox One/Series S+X Buttons by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| More modern textures for the controller buttons. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) and [Higher Res Radio Logos Menu by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)| High resolution textures of radio logos. |
	| [Improved Weapon Spec by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=107165200)| Higher resolution specular maps for weapons. |

## Additional Mods
These mods are not included by default, but do not require any additional steps to install over the archive
=== "1.0.8.0"
	| Mod name | Details |
	| :------: | :-----: |
	| Liberty Tweaks options |`Improved AI` and `Remove Weapons on Death` have been disabled - you can toggle them back in :material-file-cog:`LibertyTweaks.ini` located in :material-folder:==IVSDKDotNet\scripts==. You can also tweak your FOV in there, aswell as change keybinds for quicksaving and holstering weapons (++f9++ and ++h++ by default) |
	| [ColAccel by ThirteenAG](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Speeds up loading times by several times, ==but can cause memory problems and does not cache moments from the story (like the burnt garage)==. [Can be used in combination with ZolikaPatch's FastLoading option](https://streamable.com/slqqsl). <br>Installation: download version ==1.4==, extract :material-file:`IV.EFLC.ColAccel.asi` into :material-folder:==plugins== or into the game folder</br> |
	| [DXVK-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3)| If you have an ancient GPU (like the GTX 600 series) and DXVK from the main archive doesn't work, use this version as a replacement.<br>Installation: From the archive, extract :fontawesome-solid-gears:`d3d9.dll` from :material-folder:==x32== into the game folder.</br> |
	| [Radio Downgrader](http://downgraders.rockstarvision.com/)| Brings back removed tracks - which were deleted in 2018 due to licensing issues - to the game.<br>Installation: unzip the archive into the folder with the game, open :fontawesome-solid-gears:`install.bat`, then after the console closes itself - extract the :material-folder:==update== from the desired version of vladivostok (:material-folder:==with new vladivostok== and :material-folder:==without new vladivostok== - without will not have new tracks that appeared after the cut).</br> |
	| [Dualshock 4 button textures by tehherb](https://www.gtagaming.com/360-to-ps4-controller-icons-f30380.html)| Replaces the Xbox 360 button textures with Dualshock 4 buttons.<br>Installation: In :material-folder:==modloader== edit :material-file-edit:`modloader.ini` to change `PlaystationButtons=1` to `0` at the beginning of the file, and `XboxButtons=0` to `1`.</br> |
=== "1.2.0.59"
	| Mod name | Details |
	| :------: | :-----: |
	| [ColAccel by ThirteenAG](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Speeds up loading times by several times, ==but can cause memory problems and does not cache moments from the story (like the burnt garage)==.<br>Installation: download version ==1.5==, extract :material-file:`IV.EFLC.ColAccel.asi` into :material-folder:==plugins== or into the game folder.</br> |
	| [DXVK-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3)| If you have an ancient GPU (like the GTX 600 series) and DXVK from the main archive doesn't work, use this version as a replacement.<br>Installation: From the archive, extract :fontawesome-solid-gears:`d3d9.dll` from :material-folder:==x32== into the game folder.</br> |
	| [Radio Downgrader](http://downgraders.rockstarvision.com/)| Brings back removed tracks - which were deleted in 2018 due to licensing issues - to the game.<br>Installation: unzip the archive into the folder with the game, open :fontawesome-solid-gears:`install.bat`, then after the console closes itself - extract the :material-folder:==update== from the desired version of vladivostok (:material-folder:==with new vladivostok== and :material-folder:==without new vladivostok== - without will not have new tracks that appeared after the cut)</br> |
	| [Dualshock 4 button textures by tehherb](https://www.gtagaming.com/360-to-ps4-controller-icons-f30380.html)| Replaces the Xbox 360 button textures with Dualshock 4 buttons.<br>Installation: in the :material-folder:==update/pc/textures==, replace :material-file:`360_buttons.wtd`.</br> |

## Changelog
=== "1.0.8.0"
	- The archive is updated frequently, below is the list of changes:
		* 15.07.2023 - Added Liberty Tweaks.
		* 13.07.2023 - Fixed disappearing assets in Roman's taxi office. Changed FPS limit in cutscenes to 32.
		* 12.07.2023 - Added the following mods: (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec. Moved Various Fixes to update folder due to compatibility issues. Removed TBoGT Texture Quality Fix as Various Fixes already contains this fix fix. Removed TBoGT Vehicle Fix from modloader as FusionFix already contains the fix. Removed IVPresence. Updated ZolikaPatch.
		* 11.07.2023 - Fixed the main game crash problem.
		* 10.07.2023 - Updated the downgrader. Added FusionFix 1.60 port by Zolika. Later: Fixed TLAD crash, changed Niko's hair file, now has no visual problems.
		* 09.07.2023 - Changed the downgrader - now bundled with the archive. Removed IV Fixes and Improvements. Added Various Fixes. Added Dualshock buttons(optional).
		* 08.07.2023 - Updated Shader Fixes. Removed Simple Traffic Loader. Mods completely repacked to use modloader instead.
		* 01.07.2023 - Updated Shader Fixes, repacked some mods.
		* 30.06.2023 - Updated Shader Fixes.
		* 26.06.2023 - Created the archive.
=== "1.2.0.59"
	- The archive is updated frequently, below is the list of changes:
		* 13.07.2023 - Fixed disappearing assets in Roman's taxi office. Changed FPS limit in cutscenes to 32.
		* 12.07.2023 - Added the following mods: (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec. Removed TBoGT Texture Quality Fix as Various Fixes already contains the fix.
		* 10.07.2023 - Changed Niko's hair file, now has no visual problems.
		* 09.07.2023 - Removed IV Fixes and Improvements. Added Various Fixes.
		* 08.07.2023 - Updated FusionFix, Shader Fixes, changed DXVK config, removed dxgi.dll and repacked some mods.
		* 02.07.2023 - Repacked mods in a more convenient format.
		* 01.07.2023 - Updated Shader Fixes. Ported mods from older versions.
		* 30.06.2023 - Updated mods.
		* 27.06.2023 - Updated mods.
		* 26.06.2023 - Created the archive.

[:material-page-first:Previous page <br>Introduction</br>](index.md){ .md-button } [Next page:material-page-last: <br>Additional Setup</br>](additional-setup.md){ .md-button .md-button--primary }