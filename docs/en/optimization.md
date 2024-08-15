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

## [Setup Utility](https://github.com/gillian-guide/GTAIVSetupUtilityWPF) (Automatic installation)

Using this tool you can set up DXVK and [launch options](../additional-setup.md/#launch-options) easily and automatically. It also takes care of compatibility between FusionFix, ZolikaPatch and other specifics - you can read the feature list [here](https://github.com/gillian-guide/GTAIVSetupUtilityWPF?tab=readme-ov-file#features).

!!! info ""
    - You should re-run the tool **if you downgrade or install FusionFix and/or ZolikaPatch later.**
    - You cannot, nor should you, use the tool on Linux.

### Usage

1. Go to the latest [release page](https://github.com/gillian-guide/GTAIVSetupUtilityWPF/releases/latest).
2. Download :material-file-download:`GTAIVSetupUtilityWPF.exe`.
3. Run the tool.
4. Press `Open` and select your game folder. Follow the in-app instructions if any pop-ups appear.
5. Press `Install DXVK` and `Setup launch options` in sequence.
    - If experienced, you can manually configure the options. There is usually no need to, though.
    - If any issues occur, [report them on the Discord server](../index.md/#navigation).

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
        - On non-NVIDIA GPUs, [dxvk-gplasync](https://gitlab.com/Ph42oN/dxvk-gplasync/-/releases) can instead be used to replace stutter with graphical issues - **both issues are temporary.** NVIDIA GPUs are unaffected.
    3. After downloading, open the archive and navigate to :material-folder: ==dxvk-x.x\x32\\==.
    4. Extract :fontawesome-solid-gears:`d3d9.dll` into the game folder.
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

    1. Go to the [1.10.3 release of DXVK-async](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3).
    2. Download the :material-zip-box:`dxvk-async-1.10.3.tar.gz` archive.
        - If you would prefer stutter instead of graphical issues when building shaders, use [official DXVK 1.10.3](https://github.com/doitsujin/dxvk/releases/tag/1.10.3) instead. **Both issues are temporary.**
    3. After downloading, open the archive and navigate to :material-folder: ==dxvk-async-1.10.3\\x32\\==
    4. Extract :fontawesome-solid-gears:`d3d9.dll` into the game folder.

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

For more in-depth configuration, you can see the full list of available options [here](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf).

---

## Navigation

After performing optimization, you should continue off with additional setup to finish optimizing the game.

[:material-page-first:Previous page <br>Downgrading</br>](../downgrading/index.md){ .md-button } [Next page:material-page-last: <br>Additional Setup</br>](additional-setup.md){ .md-button .md-button--primary }
