title: Optimization
description: Methods to optimize your GTA IV install

# Optimization
We all know how horrible the optimization of the game was at release. Unfortunately, we still don't have an ultimate solution - but we do have a pretty good one.

## Drivers
This may sound obvious, but a lot of people don't install drivers, so I feel the need to mention it. Select your GPU vendor (for the dedicated GPU, not integrated one) and follow the instructions for that vendor only.

=== "NVIDIA"
    === "NVCleanstall"
        !!! warning ""
            This installation method is recommended because it allows you to install only what you need, for example, if you do not want GeForce Experience or Telemetry.
        * Go to the [official website](https://www.techpowerup.com/nvcleanstall/).
        * Download the latest version.
        * Run the :material-file-download:`NVCleanstall_x.x.x.exe`.
        * Select `Install best driver for my hardware`.
        * Check `Periodically check for driver updates in background` to always have the latest drivers.
        * Select the components you want/need (if unsure - click `Recommended` and read the module descriptions and toggle them as needed).
        * After the download, select tweaks as needed (if unsure - leave them as they are).
        * Install the driver.
    === "Official"
        !!! warning ""
            This method installs things you may not want, such as Telemetry or GeForce Experience. See NVCleanstall to avoid this.
        * Go to the [official website](https://www.nvidia.com/en-us/geforce/drivers/).
        * Install GeForce Experience. If you want the driver separately, select it from the [manual driver search](https://www.nvidia.com/Download/index.aspx?lang=en-us).
        * Follow the in-app instructions to install the driver.
=== "AMD"
    * Go to the [official website](https://www.amd.com/en/support).
    * Press `Download Windows Drivers`. If you want to manually select your driver instead, use the manual search below.
    * Follow the in-app instructions to install the driver.
    * Select `Optional` drivers over `Recommended` to get the latest drivers.
    * Select `Minimal Install` over `Full Install` if you don't need the extra features of the Adrenaline app.
=== "Intel"
    * Go to the [official website](https://www.intel.com/content/www/us/en/download-center/home.html).
    * Either use the automatic tool to detect and install drivers automatically, or browse through the list of video drivers and install the driver you want.
    * Follow the in-app instructions to install the driver.

## Setup Utility
Using this tool you can set up DXVK and [Launch Options](../additional-setup/#launch-options) semi-automatically. It automatically checks your hardware and what options should be available (aswell as setting defaults).
!!! info "Usage"
    - [Download the tool](https://github.com/SandeMC/GTAIVSetupUtilityWPF/releases).
    - Launch it and follow the in-app instructions (or just press `Install DXVK` and `Setup launch options` buttons and don't touch anything else).
    - If any issues occur, [report it on the discord server](contact-me.md). You can also try using the deprecated [Python version](https://github.com/SandeMC/GTAIVSetupUtility/releases).

## DXVK
Currently the only good solution for improving game's performance. 

!!! warning "Information"
    * DXVK mainly improves CPU performance through better drawcall handling - the ones the game abuses so much. There is a chance that DXVK will not improve performance for you if you're GPU-bound instead.
    * DXVK does not officially support Windows, but it works perfectly for GTA IV.
    * For Linux users using Proton, only apply [configuration](#configuration), since Proton already uses DXVK.
!!! warning "Prerequisites"
    * Make sure your [drivers](#drivers) are up-to-date.
    * Make sure your PC meets the [DXVK requirements](https://github.com/doitsujin/dxvk/wiki/Driver-support "DXVK's GitHub Wiki") or at least the [Legacy DXVK Requirements](https://github.com/doitsujin/dxvk/wiki/Driver-support#dxvk-1103 "DXVK's GitHub Wiki") - preferably the recommended versions. Most 2015 and newer GPUs should support the normal version, and 2012-2014 GPUs should support the legacy version, but you can use [GPU-Z](https://www.techpowerup.com/download/gpu-z/ "TechPowerUp GPU-Z")'s Advanced - Vulkan tab to check for yourself. The Legacy version will have less performance and may have more bugs. 
    * Intel iGPU's only support the Legacy version `1.10.1`.
    * Disable `Shader Pre-caching` in :material-steam:Steam `Settings` - `Downloads` tab.

??? warning "ENB Support"
    DXVK doesn't officially support ENB (and vice-versa) and is strongly discouraged by the ENB community. However, it will still work for more basic effects - but expect problems.

    Ignore this if you don't plan to use ENB's.

### What benefit can I expect?
It's hard to say, because DXVK's improvement can vary from device to device. But for a rough comparison, you can use my benchmark:
<iframe width="560" height="315" src="https://www.youtube.com/embed/mSSjw8uf5Rw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Installation { data-search-exclude }
=== "Latest"
    !!! warning ""
        * Use this version if your GPU supports the latest version. See the warning above to make sure.

    - Instructions:
        * Go to [DXVK Releases](https://github.com/doitsujin/dxvk/releases) and download the latest version - :material-zip-box:`dxvk-x.x.tar.gz`.
        !!! note ""
            [DXVK-gplasync patch](https://gitlab.com/Ph42oN/dxvk-gplasync/-/releases) can be used instead for smoother performance on AMD and Intel Arc GPU's, as only Nvidia gets shader pre-compilation at the moment.
        * After downloading, open the archive and navigate to :material-zip-box:==dxvk-x.x.tar\\dxvk-x.x\\x32\\==
        * Extract :fontawesome-solid-gears:`d3d9.dll` into the game folder.
    
    ??? question "Why not :fontawesome-solid-gears:`dxgi.dll` or other files in the folder?"
        The game uses the Direct3D 9 graphics API. The other dll's are for Direct3D 10 and Direct3D 11. 
        
        In simpler words, the game will not use any other files.
    
    ??? question "Why :material-folder:==x32==? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-folder:==x64==.
    
    ??? warning "If you have problems..."
        Use version 2.2 or version 2.0, which are the latest versions confirmed to be safe to use. 
       
        If your game won't start at all, your GPU doesn't support the latest version. Use the Legacy version instead.

        See [troubleshooting](troubleshooting.md).
=== "Legacy"
    !!! warning ""
        * Only use this version if your GPU only supports the Legacy version. See the warning above to make sure.
        * If using an Intel iGPU, stick to [1.10.1](https://github.com/doitsujin/dxvk/releases/tag/v1.10.1)([async](https://github.com/Sporif/dxvk-async/releases/tag/1.10.1)) instead.

    - Instructions:
        * Go to the [1.10.3 release of DXVK](https://github.com/doitsujin/dxvk/releases/tag/v1.10.3) and download the :material-zip-box:`dxvk-1.10.3.tar.gz`.
        !!! note ""
            [DXVK-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3) can be used instead for smoother performance.
        * After downloading, open the archive and navigate to :material-zip-box:==dxvk-1.10.3.tar_3\\dxvk-1.10.3\\x32\\==<br>Or :material-zip-box:==dxvk-async-1.10.3.tar_2\\dxvk-async-1.10.3\\x32\\==</br>
        * Extract :fontawesome-solid-gears:`d3d9.dll` into the game folder.
    
    ??? question "Why not :fontawesome-solid-gears:`dxgi.dll` or other files in the folder?"
        The game uses the Direct3D 9 graphics API. The other dll's are for Direct3D 10 and Direct3D 11. 
        
        In simpler words, the game will not use any other files.
    
    ??? question "Why :material-folder:==x32==? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-folder:==x64==.
    
    ??? warning "If you have problems..."
        If your game won't start at all, your GPU doesn't support DXVK.

        See [troubleshooting](troubleshooting.md).
### Configuration
Create a :material-file-cog:`dxvk.conf` in the game folder and add following lines to the file with any text editor(sourced from [PCGW](https://www.pcgamingwiki.com/wiki/Grand_Theft_Auto_IV#DXVK)):
``` { .py }
# maxFrameLatency is used to avoid or reduce occasional frame skipping and stuttering. This option enforces a stricter maximum frame latency.
d3d9.maxFrameLatency = 1
# presentInterval is used to enable VSync. We're going to use it in favor of game's VSync implementation. This gives us better CPU overhead. 
d3d9.presentInterval = 1
# numBackBuffers may further improve frametime stability while using Vsync. This option overrides back buffer count for the Vulkan swap chain.
d3d9.numBackBuffers = 3
```
Also add `dxvk.enableAsync = true` if using an async patch and `dxvk.gplAsyncCache = true` additionally if using a gplasync patch.
??? abstract "Full list of DXVK options"
    You can see the full list [here](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf).
Also go through [additional setup](additional-setup.md).

## DxWrapper
??? note "What's DxWrapper and how to use it?"
    Some part of GTA IV community believes [DxWrapper](https://github.com/elishacloud/dxwrapper/releases/) can increase performance. From my experiments, using `v1.0.6387.21` only worsened my performance and did not provide any benefits whatsoever. 
    
    To use it, extract :material-file:`dxwrapper.asi`, :material-file-edit:`dxwrapper.ini` and :fontawesome-solid-gears:`dxwrapper.dll` into the game folder, and in the :material-file-edit:`dxwrapper.ini` enable `DDrawCompat` and `DDrawCompatNoProcAffinity`.
    
    If you can prove to me with indefinite comparisons that it *can* improve performance, [contact me](contact-me.md).

[:material-page-first:Previous page <br>Introduction</br>](index.md){ .md-button } [Next page:material-page-last: <br>Additional Setup</br>](additional-setup.md){ .md-button .md-button--primary }