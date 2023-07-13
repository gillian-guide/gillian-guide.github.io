You can pick an archive depending on your desired version - be it 1.2.0.59 or 1.0.8.0. However, the modlist is mostly the same - you can see and compare it [below](#modlist).

### Notes
1. 1.2.0.59 is Complete Edition, a.k.a. latest :material-steam: Steam version.
2. 1.0.8.0 is the latest :material-disc: retail patch, with support for ZolikaPatch and multiplayer. However, this drag-and-drop archive does NOT include any support for multiplayer whatsoever. See [downgrading](downgrading.md) and [multiplayer](multiplayer.md) sections instead.
3. If you're using the Rockstar Games Launcher version, stick to the 1.0.8.0 archive and read it's warning.

## Installation

=== "1.2.0.59"
	[:material-download-circle: Download](https://drive.google.com/file/d/1eJ4cbVhJ4tnTGJByh_Lf4eS5SS2ShmHO/view){ .md-button .md-button--primary }

	Download the archive and then simply extract the contents into your game folder. After installation, go through [additional optimisation](Additional-Optimisation.md).
	!!! warning
		The archive must be installed on-top of a clean, unmodded :material-steam:[Steam](https://store.steampowered.com/app/12210/) Complete Edition install. 
		
		Any other way to install it will not be supported.
		
		In addition to that, I won't support any extra modifications to the files other than already listed instructions.
	??? info "Updating"
		If you're updating the archive instead after installing it previously, delete :material-folder:`update` first.
	??? warning "If the game does not start"
		Your PC may not support DXVK - remove :fontawesome-solid-gears:`d3d9.dll` from the game folder or try async 1.10.3 from additional mods.
	??? warning "My game is acting weird/my game randomly crashes"
		Disable mods one-by-one to see the culprit by deleting mods in :material-folder:`update`. Let me know of the issue if you find it.
=== "1.0.8.0"
	[:material-download-circle: Download](https://drive.google.com/file/d/1O1qD8ocbJ_fnERTvvVzyw6_bsw-k_evo/view){ .md-button .md-button--primary }
	
	Download the archive and then simply extract the contents into your game folder. After installation, go through [additional optimisation](Additional-Optimisation.md).
	!!! warning
		The archive must be installed on-top of a clean, unmodded :material-steam:[Steam](https://store.steampowered.com/app/12210/) Complete Edition install. 
		
		If you're using the Rockstar Games Launcher version, avoid booting the game from the launcher itself, but rather use :material-file:`PlayGTAIV.exe` - the game files will be replaced otherwise. 
		
		Any other way to install it will not be supported.
		
		In addition to that, I won't support any extra modifications to the files other than already listed instructions.
	??? info "Updating"
		If you're updating the archive instead after installing it previously, delete :material-folder:`update` and :material-folder:`modloader` first.
	??? warning "If the game does not start"
		Try to install :material-file-download:`vcredist_x86.exe` that's in your game folder.

		Alternatively, your PC may not support DXVK - remove :fontawesome-solid-gears:`d3d9.dll` from the game folder or try async 1.10.3 from [additional mods](#Additional_Mods).
	??? warning "My game is acting weird/my game randomly crashes"
		Disable mods one-by-one to see the culprit by editing :material-file-edit:`modloader.ini` in :material-folder:`modloader` or deleting mods in :material-folder:`update`. Let me know of the issue if you find it.
		
## Modlist
=== "1.2.0.59"
	| Mod name | Details |
	| :------: | :-----: |
	| [FusionFix~1.60~ by ThirteenAG and others](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| The main mod of the pack, it contains a bunch of fixes and also acts as a modloader together with Ultimate ASI Loader. |
	| [Shader Fixes Collection~V106~ by Parallellines0451 and others](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection)| A collection of numerous shader fixes, from simple scaling to restoring console files. |
	| [DXVK~2.2~](https://github.com/doitsujin/dxvk)| Translates DirectX 9 API to Vulkan - main optimisation method. |
	| [Various Fixes~1.5~ by Attramet and others](https://gtaforums.com/topic/975211-various-fixes/)| A large collection of fixes of various scale - mostly broken map textures. |
	| [IV Fixes and Improvements~3.3~ by Zolika1351 and others](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| A collection of minor fixes and improvements - changelog's on the page. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Fixes broken UV map on "Waiting Room" sign texture. |
	| [Sugar Chomps - Separate Signs by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Edits the UV-map on the sign to include an unused texture. |
	| [Pedestrians with Unused Clothes Restored by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds unused clothes for some pedestrians. |
	| [Varied Alderney State Trooper Ped by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds diversity to police troppers. |
	| [Characters Fixes~2023-06-09~ by TheYoshiPunch, (Japan) GTA Love and others](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/)| A large collection of fixes for inconsistencies between character appearances in IV and EFLC - plus, a few fixes just for the models themselves.<br>Addon used: Niko's Original GTAIV Hair<br>[Manually ported.](https://drive.google.com/file/d/19LA4e31Ibux3QpXo2PxHsjGu1xROtTG9/view?usp=drive_link)</br></br> |
	| [Project2DFX~4.5~ by ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Adds nice lights in the distance at night. ==Can be disabled by deleting IVLodLights files.== |
	| [Console Visuals~1.2~ by nastyyaboi and others](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Collection of ported visuals from the console version - from timecyc, to animations.<br>Used addons: Console Clothing, Console Fences, Console Trees(PC Leaves)</br> |
	| [Improved Animations Pack~3.0~ by B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Fixes some weapon animation issues such as delayed fire. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Upscaled and ported vehicle textures from GTA V and Max Payne 3.<br>[Manually ported.](https://drive.google.com/file/d/1rMgtpkMBoyoaaFwYTl1bPV5eWEJwXQ4q/view?usp=drive_link)</br> |
	| [Xbox One/Series S+X Buttons by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| More modern textures for the controller buttons. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) and <br>[Higher Res Radio Logos Menu by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)</br>| High resolution textures of radio logos. |
	| [Improved Weapon Spec by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| Higher resolution specular maps for weapons. |
=== "1.0.8.0"
	| Mod name | Details |
	| :------: | :-----: |
	| [Downgrader~v16~ by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch/downgrading)| A simple drag&drop downgrade to 1.0.8.0 with Ultimate ASI Loader(also known as xliveless), ZolikaPatch, and IV Tweaker included. |
	| [ZolikaPatch IV~7.56~ by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| First main mod in the pack: adds a lot of fixes and improvements - and the game won't boot without this mod, either. |
	| [IV Tweaker~2.2~ by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| Main modloader in the pack, also allows to increase limits for other mods. |
	| [FusionFix~1.60~ by ThirteenAG and others](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Second main mod of the pack: it contains a bunch of fixes and also acts as a modloader together with Ultimate ASI Loader.<br>[Ported by Zolika1351](https://zolika1351.pages.dev/mods/ivpatch/downgrading)</br> |
	| [Shader Fixes Collection~V106~ by Parallellines0451 and others](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection)| A collection of numerous shader fixes, from simple scaling to restoring console files. |
	| [DXVK~2.2~](https://github.com/doitsujin/dxvk)| Translates DirectX 9 API to Vulkan - main optimisation method. |
	| [Various Fixes~1.5~ by Attramet and others](https://gtaforums.com/topic/975211-various-fixes/)| A large collection of fixes of various scale - mostly broken map textures. |
	| [IV Fixes and Improvements~3.3~ by Zolika1351 and others](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| A collection of minor fixes and improvements - changelog's on the page. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Fixes broken UV map on "Waiting Room" sign texture. |
	| [Sugar Chomps - Separate Signs by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Edits the UV-map on the sign to include an unused texture. |
	| [Pedestrians with Unused Clothes Restored by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds unused clothes for some pedestrians. |
	| [Varied Alderney State Trooper Ped by donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Adds diversity to police troppers. |
	| [Characters Fixes~2023-06-09~ by TheYoshiPunch, (Japan) GTA Love and others](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/)| A large collection of fixes for inconsistencies between character appearances in IV and EFLC - plus, a few fixes just for the models themselves.<br>Addon used: Niko's Original GTAIV Hair</br> |
	| [Project2DFX~4.5~ by ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Adds nice lights in the distance at night. ==Can be disabled by deleting IVLodLights files.== |
	| [Console Visuals~1.2~ by nastyyaboi and others](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Collection of ported visuals from the console version - from timecyc, to animations.<br>Used addons: Console Clothing, Console Fences, Console Trees(PC Leaves)</br> |
	| [Improved Animations Pack~3.0~ by B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Fixes some weapon animation issues such as delayed fire. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Upscaled and ported vehicle textures from GTA V and Max Payne 3. |
	| [Xbox One/Series S+X Buttons by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| More modern textures for the controller buttons. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) and <br>[Higher Res Radio Logos Menu by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)</br>| High resolution textures of radio logos. |
	| [Improved Weapon Spec by Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| Higher resolution specular maps for weapons. |

## Changelog
=== "1.2.0.59"
	- The archive frequently updates, below is the list of it's changes:
		* 12.07.2023 - Added following mods: (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec. Removed TBoGT Texture Quality Fix as Various Fixes already includes the fix.
		* 10.07.2023 - Changed Niko's hair file, now has no visual problems.
		* 09.07.2023 - IV Fixes and Improvements removed. Various Fixes added.
		* 08.07.2023 - Updated FusionFix, Shader Fixes, changed DXVK config, removed dxgi.dll and repacked some mods.
		* 02.07.2023 - Repacked mods in a more convenient format.
		* 01.07.2023 - Updated Shader Fixes. Ported mods from older versions.
		* 30.06.2023 - Updated mods.
		* 27.06.2023 - Updated mods.
		* 26.06.2023 - Created the archive.
=== "1.0.8.0"
	- The archive frequently updates, below is the list of it's changes:
		* 12.07.2023 - Added following mods: (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec. Moved Various Fixes to update folder for compatibility concerns. Removed TBoGT Texture Quality Fix as Various Fixes already includes the fix. Removed TBoGT Vehicle Fix from modloader as FusionFix already includes the fix. Removed IVPresence. Updated ZolikaPatch.
		* 11.07.2023 - Fixed the main game crash issue.
		* 10.07.2023 - Updated the downgrader. Added FusionFix 1.60 port by Zolika. Later: Fixed TLAD crash, changed Niko's hair file, now has no visual problems.
		* 09.07.2023 - Changed the downgrader - now bundled with the archive. IV Fixes and Improvements removed. Various Fixes added. Added Dualshock buttons(optional)
		* 08.07.2023 - Updated Shader Fixes. Removed Simple Traffic Loader. Fully repacked the mods to use the modloader instead.
		* 01.07.2023 - Updated Shader Fixes, some mods repacked.
		* 30.06.2023 - Updated Shader Fixes.
		* 26.06.2023 - Created the archive.