title: Additional Setup
description: Setting up launch options and optimal graphics settings

# Additional Setup

<div class="grid cards" markdown>

- If you're here after installing the archive or using the Setup Utility on Windows, **skip to optimal graphics settings**:

    [Optimal graphics settings:material-page-last:](#__tabbed_2_2){ .md-button }

</div>

If you're here after anything else (including installing the archive on Linux), start with the **launch options.**

---

## Launch options

!!! tip "Setup Utility (**Windows only**)"
    The [Setup Utility](../optimization.md/#setup-utility-automatic-installation) can set up the launch options automatically for you.

### Manual instructions

=== "1.2.0.59"
    1. Find the location for the game properties:
        - **:material-steam: Steam**: Right click the game in your library, press `Properties...` and locate the `Launch options` field.
        - **:simple-rockstargames: Rockstar Games Launcher**: Open the game page in your library, open settings and locate the `Launcher arguments` field.
        - **Shortcut**: Right click on the game shortcut, click `Properties` and locate the `Target` field.
    2. Paste the following:

        ```text
        -norestrictions -nomemrestrict -managed
        ```

    3. If using **FusionFix**, enable `Windowed` and `Borderless Windowed` in `Settings` - `Game` in-game.
=== "1.0.8.0"
    1. In the game folder, create a :material-file-cog:`commandline.txt` file.
    2. Open the file.
    3. Insert the following lines to it:

        ```text
        -norestrictions
        -nomemrestrict
        -windowed
        -managed
        ```

    4. If using **FusionFix**, `-windowed` can be removed in favor of the mod's in-game toggle.
    5. If using **FusionFix** and/or **ZolikaPatch**, enable `Borderless Windowed` in `Settings` - `Game` in-game or `BorderlessWindowed` in :material-file-cog:`ZolikaPatch.ini` depending on which of the two you install.
        - **If you don't plan to install either of the mods, remove `-windowed`.**
        - If using both, only enable the option in **FusionFix**.

???+ warning "If using DXVK..."
    - Remove `-managed`.
    - Add `-availablevidmem 3072.0` to the list of options.
        - Replace the value with your VRAM value in MBs if you have less than 3 GB of VRAM. Don't make it higher, though.
        - If using a version older than 1.0.8.0, this value is broken. Experiment manually to get as close to 3072 MB as possible (the value may looks something like 60.0, 80.0 etc).
    - If the game doesn't allow you to use the correct resolution/refresh rate in the graphics settings, add `-width`, `-height` and `-refreshrate` with your monitor's native values.
        - If that still doesn't help, add `d3d9.forceAspectRatio = 16:9` to :material-file-cog:`dxvk.conf`. Change `16:9` with your *[exact](https://stevewadsworth.github.io/calculateAspectRatio/)* aspect ratio if you don't use a 16:9 monitor.
    - If using Windows, make sure you disabled `Enable Shader Pre-caching` in `Settings` - `Downloads` on :material-steam: Steam.

??? abstract "Full list of available launch options"
    You can use these options for intensive tweaking or debugging.

    | Option | Description |
    | -----: | :---------- |
    | -help | Lists the available commands. |
    | -adapter | Uses the specified screen adapter. |
    | -autoconfig | Automatically adjusts the graphics settings depending on computer specifications. |
    | -availablevidmem | Sets the amount of available physical video memory. |
    | -benchmark | Launches the game in Benchmark mode and then quits it. |
    | -detailquality | Sets the game's detail distance (0-99). |
    | -disableimposters | Turns off imposter rendering for vehicles. |
    | -forcehighqualitymirrors | Unknown. |
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

---

## Optimal graphics settings

!!! note ""
    Following settings are targetted for the [recommended spec sheet hardware](index.md/#prerequisites).

    If you came here from the archive, use the FusionFix tab.

=== "Vanilla"
    | Setting | Optimal setting | Description |
    | :-----: | :-------------: | :---------: |
    | Video Mode | Your native resolution (max option, usually) | This setting controls your monitor resolution or, if the `-windowed` launch option is set, the size of the game window. |
    | Aspect Ratio | Auto | This setting controls the aspect ratio of the screen relative to the resolution of your monitor. |
    | Texture Quality | High | This setting controls the resolution of all textures. |
    | Reflection Resolution | Very High | This setting controls the resolution of reflections (excluding water reflections). |
    | Water Quality | Medium | This setting controls the density and intensity of waves in the water, aswell as the resolution of water reflections.<br>***Medium* is recommended as it is less extreme, more realistic and most similar to the intended look on the consoles.** |
    | Shadow Quality | High | This setting controls the resolution and render distance of shadows.<br>**Medium** and **Low** rely too much on static shadows, making them look ugly.<br>***Very High* consumes too much performance for little gain and may appear broken at times.** |
    | Night Shadows | Medium | This setting controls how many local lights (e.g. car headlights) can cast shadows. Each quality level adds 4 additional shadow maps. This setting does not affect the resolution of dynamic shadows.<br>**Setting it above *Medium* is known to create artifacts.** |
    | Texture Filter Quality | Anisotropic 16x | This setting controls texture filtering. |
    | View Distance | Between 21 and 70 | This setting controls the main LOD render distance for things like buildings and vehicles. Also affects the render distance for props.<br>**Setting it above *21* causes pop-in, and above *70* is known to cause instability and artifacts, as well as a negative impact on framerate.** |
    | Detail Distance | Between 10 and 70 | This setting controls the secondary LOD render distance for props detail.<br>**Setting it above *10* causes pop-in, and above *70* is known to cause instability and artifacts.** |
    | Vehicle Density | Below 70 | This setting controls the number of cars on the road.<br>**Setting it too high can make driving too much of a hassle, especially with the unstable traffic AI, which can occasionally create random blocks even on straight roads and bridges.** |
    | Definition | On<br>Off if playing at 1280x720 | This setting controls depth of field and motion blur (**Off** is enabled, **On** is disabled).<br>**If playing above 1280x720, *Off* ends up blurring the image on PC and effects simply do not scale up with resolution - due to that, keep it *On* unless you play at that resolution.**<br>Can be quickly toggled by pressing ++p++ button in-game.</br> |
    | VSync | Off if using DXVK<br>On | This setting controls vertical synchronization.<br>**If using [DXVK](optimization.md) with configuration applied, keep the game's implementation *Off* in favor of DXVK's implementation. ==Also add `d3d9.maxFrameRate = 60` to :material-file:`dxvk.conf` or limit framerate with other methods you know to 60 or 30 to avoid [timing-related issues](https://github.com/GTAmodding/GTAIV-Issues-List/issues/112).==** AMD Fluid Motion Frames (if DXVK is used) or [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) can be used to artificially increase the framerate. |
=== "FusionFix"
    !!! warning ""
        Following options require [FusionFix](../essential-modding/fusionfix.md).

    | Setting | Optimal setting | Description |
    | :-----: | :-------------: | :---------: |
    | Video Mode | Your native resolution (max option, usually) | This setting controls your monitor resolution or, if `Windowed` is enabled, the size of the game window. |
    | Aspect Ratio | Auto | This setting controls the aspect ratio of the screen relative to the resolution of your monitor. |
    | Texture Quality | High | This setting controls the resolution of all textures. |
    | Reflection Resolution | Very High | This setting controls the resolution of reflections (excluding water reflections). |
    | Water Quality | Very High | This setting *only* controls the resolution of the water reflections when using FusionFix. |
    | Shadow Quality | Very High | This setting controls the resolution and render distance of shadows.<br>**If the performance loss is too high, use *High* instead.**<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Night Shadows | Very High | This setting controls how many local lights (e.g. car headlights) can cast shadows. Each quality level adds 4 additional shadow maps. This setting does not affect the resolution of dynamic shadows.<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Texture Filter Quality | Anisotropic 16x | This setting controls texture filtering. |
    | View Distance | 25<br>Up to 70 | This setting controls the main LOD render distance for things like buildings and vehicles. Also affects the render distance for props.<br>**Setting it above *25* causes pop-in, and above *70* has diminishing results.** |
    | Detail Distance | 31<br>Up to 70 | This setting controls the secondary LOD render distance for props detail.<br>**Setting it above *31* causes pop-in, and above *70* has diminishing results.** |
    | Vehicle Density | Below 70<br>100 with a custom popcycle (archive) | This setting controls the number of cars on the road.<br>**Setting it too high can make driving too much of a hassle, especially with the unstable traffic AI, which can occasionally create random blocks even on straight roads and bridges.** |
    | VSync | Off if using DXVK<br>On | This setting controls vertical synchronization.<br>**If using [DXVK](optimization.md) with configuration applied, keep the game's implementation *Off* in favor of DXVK's implementation.** |
    | Shadow Filter | Preference | This setting controls how sharp the shadows look (as, in real life, shadows are pretty soft).<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Sun Shafts | Preference | This setting controls custom-implemented godrays.<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Anti-aliasing | SMAA | This setting controls the anti-aliasing method. |
    | FPS Limiter | 60<br>30 | This setting controls the FPS limit.<br>**Recommended to set to 60 or 30 to avoid [timing-related issues](https://github.com/GTAmodding/GTAIV-Issues-List/issues/112), although the story can be beaten above 60 if ignoring bugs. You may want to lower it to 30 for some minigames.**<br>AMD Fluid Motion Frames (if DXVK is used) or [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) can be used to artificially increase the framerate.<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | FOV | Preference | This setting controls the game FOV in increments from the game's default value. |
    | Lamppost Shadows | Preference | This setting enables lamppost shadows at the cost of potential pop-in and reduced performance. |

    !!! note ""
        Following options are located in the `Display` tab.

    | Setting | Optimal setting | Description |
    | :-----: | :-------------: | :---------: |
    | Motion Blur | Preference | This setting controls the motion blur effect. |
    | Bloom | On | This setting controls bloom. |
    | Console Gamma | Preference | This setting changes the gamma to match the console levels.<br>**The game was never supposed to be so whitewashed, so I recommend setting this to *On*.** |
    | Screen Filter | Default | This setting allows you to switch the timecyc file to match different screen filters (e.g. to have TBoGT filters in IV and vice versa). |
    | Depth of Field | Preference | This setting controls the intensity of the distant blur and allows you to lock Depth of Field only to cutscenes. |
    | Tree Lighting | Preference | This setting controls the vegetation's ambient occlusion.<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Tree Alpha | Preference | This setting controls the vegetation's "transparency".<br>Further tuning available in :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Definition | On | This setting smoothes out stippled and dithered objects to reduce shimmering and aliasing. |

    !!! note ""
        Following options are located in the `Game` tab.

    | Setting | Optimal setting | Description |
    | :-----: | :-------------: | :---------: |
    | Windowed | On | This setting controls whether game is in Exclusive Fullscreen mode or (Borderless) Windowed.<br>Borderless is generally more recommended than Exclusive Fullscreen for multitasking purposes. |
    | Windowed Borderless | On if using `Windowed`</br>Off | This setting controls if the game is a normal window or a Borderless Fullscreen window when the `Windowed` setting is **On**. |
    | Pause Game on Focus Loss | Off | This setting controls whether or not the game process will be locked when the window loses focus (alt-tabbing).<br>You should set this to **Off** to avoid potential crashes. |

=== "Console-identical"
    !!! info "What are these settings?"
        These settings are identical to the console versions of the game.

        I don't really recommend playing with these settings, so this list is more for referring to what settings are most authentic to the console version.

    !!! warning ""
        Following options require [FusionFix](../essential-modding/fusionfix.md).

    | Setting | Console-identical setting | Description |
    | :-----: | :-----------------------: | :---------: |
    | Video Mode | 1280x720 on X360<br>1152x640 on PS3 | This setting controls your monitor resolution or, if `Windowed` is enabled, the size of the game window. |
    | Texture Quality | Medium | This setting controls the resolution of all textures. |
    | Reflection Resolution | Medium | This setting controls the resolution of reflections (excluding water reflections). |
    | Water Quality | Medium | This setting *only* controls the resolution of the water reflections when using FusionFix. |
    | Shadow Quality | Medium (?) | This setting controls the resolution and render distance of shadows. |
    | Night Shadows | Off | This setting controls how many local lights (e.g. car headlights) can cast shadows. Each quality level adds 4 additional shadow maps. This setting does not affect the resolution of dynamic shadows. |
    | Texture Filter Quality | Tri-Linear | This setting controls texture filtering. |
    | View Distance | 21 | This setting controls the main LOD render distance for things like buildings and vehicles. Also affects the render distance for props. |
    | Detail Distance | 10 | This setting controls the secondary LOD render distance for props detail. |
    | Vehicle Density | 33 | This setting controls the number of cars on the road. |
    | Sun Shafts | Off | This setting controls custom-implemented godrays. |
    | Anti-aliasing | N/A | This setting controls the anti-aliasing method.<br>The game used SSAA 2x on the Xbox 360 and QAA on the PS3, neither of which are avaialable on PC. |
    | FPS Limiter | 30 | This setting controls the FPS limit. |
    | FOV | Default (lowest) | This setting controls the game FOV in increments from the game's default value. |
    | Lamppost Shadows | On | This setting enables lamppost shadows at the cost of potential pop-in and reduced performance. |

    !!! note ""
        Following options are located in the `Display` tab.

    | Setting | Console-identical setting | Description |
    | :-----: | :-----------------------: | :---------: |
    | Motion Blur | On | This setting controls the motion blur effect. |
    | Bloom | On | This setting controls bloom. |
    | Console Gamma | On | This setting changes the gamma to match the console levels. |
    | Screen Filter | Default | This setting allows you to switch the timecyc file to match different screen filters (e.g. to have TBoGT filters in IV and vice versa). |
    | Depth of Field | Very High (?) | This setting controls the intensity of the distant blur and allows you to lock Depth of Field only to cutscenes. |
    | Tree Lighting | Console | This setting controls the vegetation's ambient occlusion. |
    | Tree Alpha | Console | This setting controls the vegetation's "transparency" |
    | Definition | Off | This setting smoothes out stippled and dithered objects to reduce shimmering and aliasing. |

---

## Navigation

- If you came here after installing the archive, **congratulations - you are done here!**

- If you are going through the guide manually step-by-step, continue with **Essential Modding**.

[:material-page-first:Previous page <br>Optimization</br>](optimization.md){ .md-button } [Next page:material-page-last: <br>Essential Modding</br>](../essential-modding/index.md){ .md-button .md-button--primary }
