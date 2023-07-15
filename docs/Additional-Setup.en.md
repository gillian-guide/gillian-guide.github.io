title: Additional Setup
description: Additional setup for your GTA IV installation - after performing the optimization or the drag-and-drop archive.
hide: footer


# Additional Setup
Whether you're here after using the [drag-and-drop archive](Drag-and-Drop-Archive.md) or performing the [optimization](optimization.md), we still need to do some setup for the best experience.

## Launch Options
???+ note "How to set the Launch Options?"
    There are several ways to:
    
    1. Go to the game's Properties menu in :material-steam:Steam and set them there;
    2. Create a :material-file-cog:`commandline.txt` in the game folder and edit it;
    3. Create a shortcut for the game and add the options after the path of the shortcut.

    We'll stick with the first two.

The only options you need to set are: `-norestrictions -nomemrestrict`

??? warning "When using DXVK or drag-and-drop archive..."
    Add `-windowed` to use borderless fullscreen for better stability. Make sure `BorderlessWindowed` is enabled in :material-file-cog:`ZolikaPatch.ini` or/and :material-file-cog:`IV.EFLC.FusionFix.ini` for this to work.

    If the game doesn't show the correct amount of VRAM in the graphics settings (e.g. 512MB), add `-availablevidmem` with the amount of video memory of your GPU with a `.0` after it - up to `3072.0`.

    If the game doesn't allow you to use the correct resolution/refresh rate, add `-width`, `-height` and `-refreshrate` with your monitor's native values.

!!! danger "But other guides use more options!"
    ^^Don't use them^^. They might have helped back in 2009 when the average customer PC's couldn't really handle precaching and other stuff, but nowadays these options just make things worse or act as a pure placebo.

??? abstract "Full list of launch options"
    You can use these options for tweaking, debugging and playing around. The list is taken from the [PCGW page](https://www.pcgamingwiki.com/wiki/Grand_Theft_Auto_IV#Launch_options)

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
    | -frameLimit | Sets the setting for V-Sync. |
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
![GTA IV Settings](gta4settings.jpg){: style="height:25%;width:25%"; align=right}
!!! note ""
    These settings are optimal for most people. If your PC is weaker - feel free to lower them. If your PC is stronger - feel free to increase them, but don't blame me for the issues.
??? info "Console Settings"
    These settings were set on console versions of the game, and the game is most optimized for them. They are included for having a complete list.
| Setting | Optimal Setting | Console Setting | Description | 
| :-----: | :-------------: | :-----------: | :---------: |
| Video Mode | Your native resolution(max option, usually) | 1280x720 on Xbox 360; 1152x640 on PlayStation 3; both ran at 20-30 FPS | This setting controls your monitor resolution or, if the `-windowed' launch option is set, the size of the game window. |
| Aspect Ratio | Auto | Auto | This setting controls the aspect ratio of the screen relative to the resolution of your monitor. |
| Texture Quality | High | Medium | This setting controls the resolution of all textures. |
| Reflection Resolution | Very High | Medium | This setting controls the resolution of reflections - mainly car reflections (but if you are using [FusionFix](/Essential-Modding/FusionFix/) or [Shader Fixes](/Essential-Modding/Shader-Fixes/), it will not affect the resolution). |
| Water Quality | Medium or Very High | Medium | This setting controls the density and intensity of waves in water and water samples. Medium is recommended because it is less extreme and more realistic. It does not affect the resolution of water reflections. |
| Shadow Quality | High | Medium | This setting controls the resolution and render distance of shadows. Medium and Low rely much more on static shadows than High. Very High consumes ~20 FPS. |
| Night Shadows | Medium or Very High | Off | This setting controls the resolution of dynamic shadows from car headlights. [FusionFix](/Essential-Modding/FusionFix/) allows you to enhance it by adding dynamic shadows to most objects. Both [FusionFix](/Essential-Modding/FusionFix/) and [Shader Fixes](/Essential-Modding/Shader-Fixes/) fix the artefacts that come from options above Medium. |
| Texture Filter Quality | Anisotropic 16x | Tri-Linear | This setting controls the anisotropic filtering. |
| View Distance | Between 21 and 70 | 21 | This setting controls the main LOD render distance for things like buildings and vehicles. Setting it above 70 is known to cause instability and artifacts, as well as a negative impact on framerate. |
| Detail Distance | Between 10 and 70 | 10 | This setting controls the secondary LOD render distance for secondary props (such as trash cans). Setting it higher than 70 can cause instability and artifacts. |
| Vehicle Density | Preference - preferably below 90 | 33 | This setting controls the traffic density. Setting it too high can make driving too much of a hassle, especially with the unstable traffic AI, which can occasionally create random blocks even on straight roads and bridges. |
| Definition | Off | Off | This setting controls depth of field and motion blur - however, it is also known to cause problems with blurred images on PC and effects that simply do not scale up in resolution - use [FusionFix](/Essential-Modding/FusionFix/) or [Shader Fixes](/Essential-Modding/Shader-Fixes/) to solve this problem |
| FXAA | On | - | This setting controls FXAA (a simple method of Anti-Aliasing) - use [FusionFix](/Essential-Modding/FusionFix/) for it to exist, or [Shader Fixes](/Essential-Modding/Shader-Fixes/) to have FXAA at all times. |
| VSync | Off | On | This setting controls the vertical synchronization. We'll use the one bundled with [DXVK](Optimization.md) instead, as it has much better frame timing, as well as [FusionFix](/Essential-Modding/FusionFix/)'s FPS limiter |

??? question "What is :material-file-cog:`stream.ini`?"
    Other guides often use :material-file-cog:`stream.ini` and change the values in there from `2048000` to `4096000`. From [PCGW users' observations](https://www.pcgamingwiki.com/w/index.php?title=Topic:X1jmh4mc3t6mv3hv&topic_showPostId=xb5gbd4mggke2ets#flow-post-xb5gbd4mggke2ets), as well as my own - this provides no benefit whatsoever and is probably a placebo.

[:material-page-first:Previous page <br>Optimization</br>](optimization.md){ .md-button } [Next page:material-page-last: <br>Downgrading</br>](downgrading.md){ .md-button .md-button--primary }