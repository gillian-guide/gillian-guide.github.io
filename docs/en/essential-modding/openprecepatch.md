---
title: OpenPreCEPatch
description: Some fixes for your downgraded copy, mainly for enjoying multiplayer.
---

# [OpenPreCEPatch](https://github.com/gillian-guide/IV.EFLC.OpenPreCEPatch)

!!! warning "Compatibility"
    This mod is compatible with all downgraded versions, but not Complete Edition. Skip this mod if you do not intend to downgrade - the improvements are negligible if you do not play the [multiplayer](../extras/multiplayer.md).

This project **improves core multiplayer experience, adds DLC support to PreCE patches and is considered essential for downgraded versions**. You can read the changelog [here](https://zolika1351.pages.dev/mods/ivpatch).

---

<h2>Installation</h2> <a id="installation"></a>

1. Go to the [Releases](https://github.com/gillian-guide/IV.EFLC.OpenPreCEPatch/releases/latest) page.
2. Download the latest release.
3. Extract :material-zip-box:`OpenPreCEPatch.zip` into the game folder.

??? tip "ZolikaPatch"
    OpenPreCEPatch is an experimental open source successor to ZolikaPatch that already includes all of its' meaningful features. It already includes FusionFix compatibility and patches to existing issues of ZolikaPatch.

    If you desire to install specifically ZolikaPatch for whatever purposes, however, instructions are available below:

    1. Go to [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch).
    2. Scroll to the bottom of the page and download the latest version.
    3. Extract :material-zip-box:`ZolikaPatch_vx_x.zip` into the game folder.
        - An open-source compilation of the mod is available [here](https://github.com/gillian-guide/ZolikaPatch/releases/latest) - it's behaviorally the same.
        - Consider re-running the Setup Utility if you used it on the [Optimization](../optimization.md) or [Additional Setup](../additional-setup.md) pages.
        - Do **NOT** extract :material-file:`PlayGTAIV.exe` or :material-file:`IVMenuAPI.asi`. Remove the latter if you already did.

    <a id="incompatible-options"></a>

    !!! warning "If using FusionFix..."
        !!! tip "Setup Utility (**Windows only**)"
            The [Setup Utility](../optimization.md#setup-utility-automatic-installation) can take care of this automatically for you.

        Open :material-file-cog:`ZolikaPatch.ini` and disable the following options:

        - BenchmarkFix
        - BikePhoneAnimsFix
        - BorderlessWindowed
        - BuildingAlphaFix
        - BuildingDynamicShadows
        - CarDynamicShadowFix
        - CarPartsShadowFix
        - CutsceneFixes
        - DoNotPauseOnMinimize
        - DualVehicleHeadlights
        - EmissiveLerpFix
        - EpisodicVehicleSupport
        - EpisodicWeaponSupport
        - ForceCarHeadlightShadows
        - ForceDynamicShadowsEverywhere
        - ForceShadowsOnObjects
        - HighFPSBikePhysicsFix
        - HighFPSSpeedupFix
        - HighQualityReflections
        - ImprovedShaderStreaming
        - MouseFix
        - NewMemorySystem
        - NoLiveryLimit
        - NoLODLightHeightCutoff
        - OutOfCommissionFix
        - PoliceEpisodicWeaponSupport
        - RemoveBoundingBoxCulling
        - RemoveUselessChecks
        - ReversingLightFix
        - SkipIntro
        - SkipMenu
        - SCOSignatureFix

        Note that this doesn't break or actually disable anything, as these features are reimplemented by FusionFix.

    !!! question "What's :material-file:`GFWLProtectionDisabler2019.asi`?"
        This file is required to prevent GFWL from blocking :material-file:`.asi` mods.

---

<h2>Configuration</h2> <a id="configuration"></a>

Open :material-file-cog:`IV.EFLC.OpenPreCEPatch.ini` or :material-file-cog:`XLivelessAddon.ini` and configure the file as needed. All the options have explanations next to them.

---

<h2>Navigation</h2> <a id="navigation"></a>

[:material-page-first:Previous page <br>FusionFix</br>](fusionfix.md){ .md-button } [Next page:material-page-last: <br>Various Fixes</br>](various-fixes.md){ .md-button .md-button--primary }
