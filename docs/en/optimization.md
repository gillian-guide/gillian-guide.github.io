title: Optimization
description: Everything about DXVK for GTA IV

# Optimization

We all know how horrible the optimization of the game was at release. Unfortunately, we still don't have a one-for-all solution - but that doesn't mean we can't make things better.

---

## What is DXVK?

[DXVK](https://github.com/doitsujin/dxvk) is a translation layer that converts DirectX API calls to Vulkan.

While it isn't a magic tool to improve performance and is more of a compatibility tool for Linux, the condition of GTA IV on PC allows it to improve performance for most - but not everyone - mainly by improving CPU performance through better drawcall handling.

??? question "What benefit can I expect from DXVK?"
    It's hard to say, because DXVK's improvement can vary from device to device. **There is a chance that DXVK will not improve performance for you if you're GPU-bound.** So, the only answer is that you can expect *some* improvement if you are CPU-bound.

    Under right conditions, though, you can expect something comparable to this benchmark:
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mSSjw8uf5Rw;start=3" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; gyroscope; picture-in-picture; web-share;" allowfullscreen></iframe>

---

## Prerequisites

!!! warning ""
    - Make sure your [drivers](../preparation.md/#drivers) are up-to-date.
    - If using Windows, disable `Shader Pre-caching` in :material-steam: Steam, located in `Settings` - `Downloads`.
    - If using Linux, skip to [configuration](#configuration), since Proton already uses DXVK.

---

## [Setup Utility](https://github.com/gillian-guide/GTAIVSetupUtility) (Automatic installation)

Using this tool you can set up DXVK and [launch options](../additional-setup.md/#launch-options) easily and automatically. It also takes care of compatibility between FusionFix, ZolikaPatch and other specifics - you can read the feature list [here](https://github.com/gillian-guide/GTAIVSetupUtility?tab=readme-ov-file#features).

!!! info ""
    - You should re-run the tool **if you downgrade and/or install FusionFix and/or ZolikaPatch later.**
    - The tool is unnecessary on Linux, as DXVK is already used, but it can be used for other purposes if launched under Proton.

### Usage

!!! note "FusionFix"
    Note that FusionFix already includes DXVK by default and you can toggle it on in the Graphics tab. However, you can still update DXVK manually.

1. Go to the latest [release page](https://github.com/gillian-guide/GTAIVSetupUtility/releases/latest).
2. Download :material-file-download:`GTAIVSetupUtility.exe`.
3. Run the tool.
4. Press `Open` and select your game folder. Follow the in-app instructions if any pop-ups appear.
5. Press `Install DXVK` and `Setup launch options` in sequence.
    - If experienced, you can manually configure the options. There is usually no need to, though.
    - Updating DXVK can be done by pressing `Reinstall DXVK`.
    - If any issues occur, [report them on the Discord server](../index.md/#navigation).

???+ warning "For NVIDIA 50-series RTX GPU users"
    Make sure your drivers are up-to-date. For several months, the drivers used to insta-crash all 50-series users. Latest drivers don't have that problem.

After using the tool, you can freely skip to optimal graphics settings:

[Next page:material-page-last: <br>Additional Setup: Optimal graphics settings</br>](additional-setup.md/#optimal-graphics-settings){ .md-button .md-button--primary }

---

## Manual installation { data-search-exclude }

=== "Latest"
    ???+ warning "Requirements"
        - Use this version if your GPU is:
            - **NVIDIA**: A Maxwell (GeForce 800 series) GPU or newer, plus GTX 745, GTX 750 and GTX 750 Ti.
                - GeForce 810M, GeForce 820M, GeForce 825M, GTX 870M, GTX 880M, GeForce 910M and GeForce 920M are not supported.
            - **AMD**: A GCN4 (RX400 series and Vega series) (i)GPU or newer.
            - **Intel**: A Skylake (6th generation Intel Core CPUs) iGPU or newer. All Arc GPUs are supported. Select iGPUs may be limited to Legacy.
            - **Mac**: An Intel Mac with support for Vulkan 1.3 (check manually by opening the command prompt and typing `vulkaninfo`).

        If you're don't fall under the list, check the Legacy tab. **This list only applies to Windows.**

    ---

    <h3>Instructions</h3>

    1. Go to the latest [release page](https://github.com/doitsujin/dxvk/releases/latest).
    2. Download the :material-zip-box:`dxvk-x.x.tar.gz` archive.
    3. After downloading, open the archive and navigate to :material-folder: ==dxvk-x.x\x32\\==.
    4. Extract :fontawesome-solid-gears:`d3d9.dll` into the game folder. If you want to retain FusionFix's toggle functionality, rename the file to :fontawesome-solid-gears:`vulkan.dll` first.

    !!! question "About the `async` patch"
        DXVK, from version 2.0 onwards, implemented Graphics Pipeline Library support, which, in the context of GTA IV, completely eliminates shader building stutter given the GPL and Fast Linking support from the GPU.

        If using a modern GPU, those features should be there, and if you have no frequent stutter - it is there. **If you do, however, experience frequent stutter on this version, check if your drivers are up-to-date, and if they are, use the [dxvk-gplasync](https://gitlab.com/Ph42oN/dxvk-gplasync/-/releases) fork to reduce stutter.**

=== "Legacy"
    ???+ warning "Requirements"
        - You can use this version if your GPU is:
            - **NVIDIA**: A Kepler (GeForce 600 series) GPU or newer.
            - **AMD**: A GCN1 (Radeon HD 7700 series) (i)GPU or newer.
            - **Intel**: A Skylake (6th generation Intel Core CPUs) iGPU or newer. Select iGPUs may be limited to DXVK 1.10.1.
            - **Mac**: An Intel Mac with support for Vulkan 1.1 (check manually by opening the command prompt and typing `vulkaninfo`).

        If you're don't fall under the list, you can not use DXVK. **This list only applies to Windows.**

    ---

    <h3>Instructions</h3>

    1. Go to the latest [DXVK-Sarek release page](https://github.com/pythonlover02/dxvk-Sarek/releases/latest).
        - If experiencing issues with this fork, you can also use [dxvk-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3) or [official DXVK 1.10.3](https://github.com/doitsujin/dxvk/releases/tag/1.10.3) instead.
    2. Download the :material-zip-box:`dxvk-sarek-async-1.10.x.tar.gz` archive.
    3. After downloading, open the archive and navigate to :material-folder: ==dxvk-sarek-async-1.10.3\\x32\\==
    4. Extract :fontawesome-solid-gears:`d3d9.dll` into the game folder. If you want to retain FusionFix's toggle functionality, rename the file to :fontawesome-solid-gears:`vulkan.dll` first.

??? question "Why not :fontawesome-solid-gears:`dxgi.dll` or other files in the folder?"
    The game uses the Direct3D 9 graphics API. The other `dll`'s are for Direct3D 10 and Direct3D 11.

    In simpler words, the game will not use any other files.

??? question "Why :material-folder: ==x32==? My system is 64-bit"
    Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.

    In simpler words, the game will not use the files from the :material-folder: ==x64== folder.

??? warning "If you have problems..."
    Try going down a version or two.

    If your game won't start at all, your GPU doesn't support the latest version. Use the Legacy version instead.

    See [troubleshooting](../resources/troubleshooting.md).
???+ warning "For NVIDIA 50-series RTX GPU users"
    Make sure your drivers are up-to-date. For several months, the drivers used to insta-crash all 50-series users. Latest drivers don't have that problem.

---

### Configuration

Create a :material-file-cog:`dxvk.conf` file in the game folder and add following lines to the file with any text editor:

``` { .cpp }
# maxFrameLatency is used to avoid or reduce occasional frame skipping and stuttering. This option enforces a stricter maximum frame latency.
d3d9.maxFrameLatency = 1
# presentInterval is used to enable VSync. We're going to use it in favor of game's VSync implementation. This gives us better CPU overhead.
d3d9.presentInterval = 1
# numBackBuffers may further improve frametime stability while using Vsync. This option overrides back buffer count for the Vulkan swap chain.
d3d9.numBackBuffers = 3
```

If using `dxvk-async` or `dxvk-gplasync`, add the following lines to the same file:

``` { .cpp }
# Following options are used to enable async
dxvk.enableAsync = true
dxvk.gplAsyncCache = true
```

If you're unhappy with shader compilation speed, add the following and configure manually to adjust for your CPU thread amount:

``` { .cpp }
dxvk.numAsyncThreads = 4
dxvk.numCompilerThreads = 4
```

For more in-depth configuration, you can see the full list of available options [here](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf).

---

## Navigation

After performing optimization, you should continue off with additional setup to finish optimizing the game.

[:material-page-first:Previous page <br>Downgrading</br>](../downgrading/index.md){ .md-button } [Next page:material-page-last: <br>Additional Setup</br>](additional-setup.md){ .md-button .md-button--primary }
