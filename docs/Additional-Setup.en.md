title: Additional Setup
description: Additional setup for your GTA IV installation - after using main optimisation or the drag-and-drop archive.

# Additional Setup
Whether you're here after using the [drag-and-drop archive](Drag-and-Drop-Archive.md) or using the [main optimisation](Main-Optimisation.md), we still need to do some setup for the best experience.

## Launch Options
???+ note "How to set the Launch Options?"
    There are several ways to:
    
    1. Going to the game's Properties menu in :material-steam:Steam and setting them there
    2. Creating a :material-file-cog:`commandline.txt` in the game's folder and editing it
    3. Creating a shortcut for the game and adding the options after the shortcut's path

    We're going to stick with the first two.

The only options you should set are: `-norestrictions -nomemrestrict`

??? warning "If using DXVK or drag-and-drop archive..."
    Add `-windowed` to use Borderless Fullscreen for improved stability. Make sure `BorderlessFullscreen` is enabled in :material-file-cog:`ZolikaPatch.ini` or/and :material-file-cog:`IV.EFLC.FusionFix.ini` for this to work.

    If the game doesn't show correct VRAM amounts (i.e. 512MB), add `-availablevidmem` with your GPU's amount of video memory with a `.0` after it - up to `3072.0`.

    If the game doesn't allow to use correct resolution/refresh rate, add `-width`, `-height` and `-refreshrate` with your monitor's native values.

!!! danger "But other guides use more options!"
    ^^Don't use them^^. They might've helped, back in 2009, when average customer PC's couldn't really handle precaching and other stuff, but nowadays these options only do worse or act as a pure placebo.

??? note "Full list of launch options"
    You can use these options for tweaking, debugging and playing around. The list was sourced from the [PCGW page](https://www.pcgamingwiki.com/wiki/Grand_Theft_Auto_IV#Launch_options)

    | Option | Description | 
    | -----: | :---------- |
    | -help | Lists the available commands. |
    | -adapter | Uses the specified screen adapter. |
    | -autoconfig | Automatically adjusts the graphics settings depending on computer specifications. |
    | -availablevidmem | Sets the amount of available physical video memory. |
    | -benchmark | Launches the game in Benchmark mode and then quits it. |
    | -detailquality | Sets the game's detail distance (0-99). |
    | -disableimposters | Turns off imposter rendering for vehicles. |
    | -forcehighqualitymirrors | ? |
    | -forcer2vb | Forces rendering to Vertex Buffer. |
    | -frameLimit | Sets the setting for VSync. |
    | -framelockinwindow | Forces framelock to work even in a window. |
    | -fullscreen | Forces fullscreen mode. |
    | -fullspecaudio | Forces high-end CPU audio footprint. |
    | -gpucount | Allows to manually set the GPU count if query fails. |
    | -height | Sets the vertical resolution. |
    | -managed | Uses D3D runtime managed resources. |
    | -memrestrict | Restricts the amount of available memory the game can use. |
    | -minspecaudio | Forces low-end CPU audio footprint. |
    | -no_3GB | Disables 3GB memory support on 32-bit OSes which have been set to allow games and applications to use that much memory. |
    | -noBlockOnLostFocus | Prevents the game from blocking window updates during focus loss. |
    | -noprecache | Disables precaching of resources. |
    | -nomemrestrict | Disables memory restrictions. |
    | -nominimize | Disables the ability to restore the game from minimize and altering resolutions (reduces system memory footprint). |
    | -norestrictions | Disables restrictions on graphics settings. |
    | -noswapdelay | Disables sleep delay before Present (disables the hard present stalls fix). |
    | -notimefix | Disables Time Fix. |
    | -novblank | Disables vertical blanking for V-Sync. |
    | -percentvidmem | Percentage of video memory to be made available for the game. |
    | -refreshrate | Sets the refresh rate (values set must be supported by the monitor used). |
    | -reserve | Sets the amount of memory to be used by other programs. |
    | -reservedApp | Sets the amount of memory to be left available within application space. |
    | -renderquality | Adjusts anisotropic filtering (0-4). |
    | -safemode | Sets the game's graphics to the lowest setting possible. |
    | -shadowdensity | Adjusts night shadows (0-16). |
    | -shadowquality | Sets the shadow quality (0-4). |
    | -stereo | Enables stereo audio support. |
    | -texturequality | Sets the game's texture quality (0-2). |
    | -unmanaged | Uses application managed resources. |
    | -usedirectinput | Allows DirectInput support alongside XInput support. |
    | -viewdistance | Sets the game's view distance (0-99). |
    | -windowed | Forces windowed mode. |
    | -width | Sets the horizontal resolution. |

## Optimal Game Settings
![GTA IV Settings](gta4settings.jpg){ align=right }
???+ note
    These options are optimal for most people. If your PC is weaker - feel free to lower them. If your PC is stronger - feel free to set them higher, but don't blame me for the problems.
??? info "Console Settings"
    These settings were set on console versions of the game, and the game is most optimized for them. They're included for the sake of a complete list.
| Setting | Optimal Setting | Console Setting | Description | 
| :-----: | :-------------: | :-----------: | :---------: |
| Video Mode | Your native resolution(max option, usually) | 1280x720 on Xbox 360; 1152x640 on PlayStation 3; both ran at 20-30 FPS | This setting controls your monitor resolution or, if the `-windowed' launch option is set, the size of the game window. |
| Aspect Ratio | Auto | Auto | This setting controls the aspect ratio of the screen relative to the resolution of your monitor. |
| Texture Quality | High | Medium | This setting controls the resolution of all textures. |
| Reflection Resolution | Very High | Medium | This setting controls the resolution of reflections - mainly car reflections (but if you're using [FusionFix](/Essential-Modding/FusionFix/) or [Shader Fixes](/Essential-Modding/Shader-Fixes/), it won't affect the resolution) |
| Water Quality | Medium or Very High | Medium | This setting controls the density and intensity of waves in water, as well as water samples. Medium is reccomended due to being less extreme and more realistic. It does not affect the resolution of water's reflection. |
| Shadow Quality | High | Medium | This setting controls the resolution, as well as the render distance, of shadows. Medium and Low rely on static shadows much more than High. Very High consumes ~20 FPS |
| Night Shadows | High or Very High | Off | This setting controls the resolution of dynamic shadows off cars' headlights. [FusionFix](/Essential-Modding/FusionFix/) allows to enhance it by adding dynamic shadows to most objects. |
| Texture Filter Quality | Anisotropic 16x | Anisotropic 1x | This setting controls anisotropic filtering. |
| View Distance | Between 21 and 70 | 21 | This setting controls main LOD render distance for stuff like buildings and vehicles. Setting the option above 70 is known to produce instability and artefacts, as well as negatively impact the framerate |
| Detail Distance | Between 10 and 70 | 10 | This setting controls secondary LOD render distance for secondary props(such as trashcans). Setting the option above 70 may produce instability and artefacts |
| Vehicle Density | Preference - preferably below 90 | 33 | This setting controls the density of traffic. Setting the option too high might prove travelling by car too troublesome, especially with unstable traffic AI that can occasionally create random blocks even on straight roads and bridges |
| Definition | Off | Off | This setting controls Depth of Field and Motion Blur - however, it is also known to have issues with blurred image on PC and effects that simply don't scale up in resolution - use [FusionFix](/Essential-Modding/FusionFix/) or [Shader Fixes](/Essential-Modding/Shader-Fixes/) to solve the problem |
| VSync | Off | On | This setting controls Vertical Synchronisation. We're using the one bundled with DXVK instead for it's much better framepacing, aswell as [FusionFix](/Essential-Modding/FusionFix/)'s FPS limiter |

??? info "What's :material-file-cog:`stream.ini`?"
    Other guides commonly use :material-file-cog:`stream.ini` and change the values in there from `2048000` to `4096000`. From [PCGW users' observations](https://www.pcgamingwiki.com/w/index.php?title=Topic:X1jmh4mc3t6mv3hv&topic_showPostId=xb5gbd4mggke2ets#flow-post-xb5gbd4mggke2ets), aswell as my own's - this provides no benefit whatsoever and is likely placebo.