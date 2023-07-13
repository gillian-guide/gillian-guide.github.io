You can pick an archive depending on your desired version - be it 1.2.0.43 or 1.0.8.0. However, the modlist is mostly the same - you can see and compare it [below](#modlist)

### Notes
1. 1.2.0.43 is Complete Edition, a.k.a. latest :material-steam: Steam version.
2. 1.0.8.0 is the latest :material-disc: retail patch, with support for ZolikaPatch and multiplayer. However, this drag-and-drop archive does NOT include any support for multiplayer whatsoever. See [downgrading](downgrading.md) and [multiplayer](multiplayer.md) sections instead.

## Installation

=== "1.2.0.43"
	[:material-download-circle: Download](https://drive.google.com/file/d/1eJ4cbVhJ4tnTGJByh_Lf4eS5SS2ShmHO/view){ .md-button .md-button--primary }

	Download the archive and then simply extract the contents into your game folder. After installation, go through [additional optimisation](Additional-Optimisation.md).
	!!! warning
		The archive must be installed on-top of a clean, unmodded Complete Edition install downloaded from :material-steam:[Steam](https://store.steampowered.com/app/12210/). Any other way to install it will not be supported.
	??? info "Updating"
		If you're updating the archive instead after installing it previously, delete :material-folder:`update` first.
	??? warning "If the game does not start"
		Your PC does not support DXVK - remove :fontawesome-solid-gears:`d3d9.dll` from the game folder or try async 1.10.3 from additional mods.
=== "1.0.8.0"
	[:material-download-circle: Download](https://drive.google.com/file/d/1O1qD8ocbJ_fnERTvvVzyw6_bsw-k_evo/view){ .md-button .md-button--primary }
	
	Download the archive and then simply extract the contents into your game folder. After installation, go through [additional optimisation](Additional-Optimisation.md).
	!!! warning
		The archive must be installed on-top of a clean, unmodded Complete Edition install downloaded from :material-steam:[Steam](https://store.steampowered.com/app/12210/). If you're using the Rockstar Games Launcher version, avoid booting the game from the launcher itself, but rather use :material-file:`PlayGTAIV.exe` - the game files will be replaced otherwise. Any other way to install it will not be supported.
	??? info "Updating"
		If you're updating the archive instead after installing it previously, delete :material-folder:`update` and :material-folder:`modloader` first.
	??? warning "If the game does not start"
		Try to install :material-file-download:`vcredist_x86.exe` that's in your game folder.

		Alternatively, your PC does not support DXVK - remove :fontawesome-solid-gears:`d3d9.dll` from the game folder or try async 1.10.3 from [additional mods](#Additional_Mods).

=== 1.2.0.43
## Modlist
| Mod name | Details |
| :------: | :-----: |
| [https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/](FusionFix by ThirteenAG)| The main mod of the pack, it contains a bunch of fixes and also acts as a modloader together with Ultimate ASI Loader. <br>Version - 1.60</br> |
| Mod 2       | Mod 2 details |
| Mod 3    | Mod 3 details |

## Changelog
- The archive frequently updates, below is the list of it's changes:
	* 12.07.2023 - Added following mods: (newer) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos In-Game, Improved Weapon Spec. Moved Various Fixes to update folder for compatibility concerns. Removed TBoGT Texture Quality Fix as Various Fixes already includes the fix. Removed TBoGT Vehicle Fix from modloader as FusionFix already includes the fix. Removed IVPresence. Updated ZolikaPatch.
	* 11.07.2023 - Fixed the main game crash issue.
	* 10.07.2023 - Updated the downgrader. Added FusionFix 1.60 port by Zolika. Later: Fixed TLAD crash, changed Niko's hair file, now has no visual problems.
	* 09.07.2023 - Changed the downgrader - now bundled with the archive. IV Fixes and Improvements removed. Various Fixes added. Added Dualshock buttons(optional)
	* 08.07.2023 - Updated Shader Fixes. Removed Simple Traffic Loader. Fully repacked the mods to use the modloader instead.
	* 01.07.2023 - Updated Shader Fixes, some mods repacked.
	* 30.06.2023 - Updated Shader Fixes.
	* 26.06.2023 - Created the archive.