title: Optimization
description: Methods to optimize your GTA IV install.
---
hide:
  - footer
---

# Optimization
We all know how horrible the optimization of the game was at release. Unfortunately, we still don't have an ultimate solution - but we do have a pretty good one.

## DXVK
Currently the only good solution for improving game's performance. Although not officially supported for Windows, it works perfectly with GTA IV as of Version 2.2 of DXVK.

!!! warning ""
    Make sure your PC meets the [DXVK requirements](https://github.com/doitsujin/dxvk/wiki/Driver-support "DXVK's GitHub Wiki") or at least the [Legacy DXVK Requirements](https://github.com/doitsujin/dxvk/wiki/Driver-support#dxvk-1103 "DXVK's GitHub Wiki") - preferably the recommended versions. Most 2014 and newer GPUs should support the normal version, and 2012 and newer GPUs should support the legacy version, but you can use [GPU-Z](https://www.techpowerup.com/download/gpu-z/ "TechPowerUp GPU-Z)'s Advanced tab to check for yourself. The legacy version will have less performance and may have more bugs.

??? warning "ENB Support"
    DXVK doesn't officially support [ENB](Graphics-Enhancement\ENB) (and vice-versa) and is strongly discouraged by the ENB community. However, it will still work for more basic effects - but expect problems.

    Ignore this if you don't plan to use [ENB's](Graphics-Enhancement\ENB)

### What benefit can I expect?
It's hard to say, because DXVK's improvement can vary from device to device. But for a rough comparison, you can use my benchmark:
<iframe width="560" height="315" src="https://www.youtube.com/embed/mSSjw8uf5Rw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Installation
=== "Latest"
    !!! warning ""
        Use this version if your GPU supports the latest version. See the warning above to make sure.

    - Instructions:
        * Go to [DXVK Releases](https://github.com/doitsujin/dxvk/releases) and download the latest version - :material-zip-box:`dxvk-x.x.tar.gz`.
        * After downloading, open the archive and navigate to :material-zip-box:==dxvk-x.x.tar\\dxvk-x.x\\x32\\==
        * Extract :fontawesome-solid-gears:`d3d9.dll` to your game folder.
    
    ??? question "Why not :fontawesome-solid-gears:`dxgi.dll` or other files in the folder?"
        The game uses the Direct3D 9 graphics API. The other dll's are for Direct3D 10 and Direct3D 11. 
        
        In simpler words, the game will not use any other files.
    
    ??? question "Why :material-folder:==x32==? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-folder:==x64==.
    
    ??? warning "If you have problems..."
        Use version 2.2 or version 2.0, which are the latest versions confirmed to be safe to use. 
       
        If your game won't start at all, your GPU doesn't support the latest version. Use the Legacy version instead.
=== "Legacy"
    !!! warning ""
        Only use this version if your GPU only supports the Legacy version. See the warning above to make sure.

    - Instructions:
        * Go to the [1.10.3 release of DXVK](https://github.com/doitsujin/dxvk/releases/tag/v1.10.3) and download the :material-zip-box:`dxvk-1.10.3.tar.gz`.
        !!! note ""
            [DXVK-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3) can be used instead for smoother performance.
        * After downloading, open the archive and navigate to :material-zip-box:==dxvk-1.10.3.tar_3\\dxvk-1.10.3\\x32\\==<br>Or :material-zip-box:==dxvk-async-1.10.3.tar_2\\dxvk-async-1.10.3\\x32\\==</br>
        * Extract :fontawesome-solid-gears:`d3d9.dll` to your game folder.
    
    ??? question "Why not :fontawesome-solid-gears:`dxgi.dll` or other files in the folder?"
        The game uses the Direct3D 9 graphics API. The other dll's are for Direct3D 10 and Direct3D 11. 
        
        In simpler words, the game will not use any other files.
    
    ??? question "Why :material-folder:==x32==? My system is 64-bit"
        Your system is irrelevant in this case. The game itself is designed to use 32-bit libraries, not 64-bit ones.
        
        In simpler words, the game will not use the files from :material-folder:==x64==.
    
    ??? warning "If you have problems..."
        If your game won't start at all, your GPU doesn't support DXVK.
    
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
??? abstract "Full list of DXVK options"
    You can see the full list [here](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf).

## DxWrapper
??? note "What's DxWrapper and how to use it?"
    Some part of GTA IV community believes [DxWrapper](https://github.com/elishacloud/dxwrapper/releases/) can increase performance. From my experiments, using `v1.0.6387.21` only worsened my performance and did not provide any benefits whatsoever. 
    
    To use it, extract :material-file:`dxwrapper.asi`, :material-file-edit:`dxwrapper.ini` and :fontawesome-solid-gears:`dxwrapper.dll`, and in the :material-file-edit:`dxwrapper.ini` enable `DDrawCompat` and `DDrawCompatNoProcAffinity`.
    
    If you can prove to me with indefinite comparisons that it *can* improve performance, [contact me](contact-me.md).

[:material-page-first:Previous page <br>Introduction</br>](index.md){ .md-button } [Next page:material-page-last: <br>Additional Setup</br>](Additional-Setup.md){ .md-button .md-button--primary }