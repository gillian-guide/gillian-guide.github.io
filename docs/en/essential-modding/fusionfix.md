title: FusionFix
description: Graphics fixes, but even more than just that!

# [FusionFix](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix)

!!! warning "Compatibility"
    This mod is only officially supported on the Complete Edition, but with taking several things in account, you can also use it with 1.0.8.0.

    Support for non-CE versions may be axed at any time and the developers don't provide any support for them.
This project aims to fix or address most **graphical and gameplay issues** and introduces new graphics options. You can read the changelog on the [repository](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/tree/master#coregameplay-changelog).

---

<h2>Demo</h2> <a id="demo"></a>

<iframe width="560" height="315" src="https://www.youtube.com/embed/XTuOortPoY4?si=5HbNzCc6JboJjxUT" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<h2>Installation</h2> <a id="installation"></a>

=== "1.2.0.59"
    1. Go to the latest [release page](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest).
    2. Download the :material-zip-box:`GTAIV.EFLC.FusionFix.zip` archive.
    3. Extract the archive into the game folder.
        - Consider re-running the Setup Utility if you used it on the [Optimization](../../optimization.md) or [Additional Setup](../../additional-setup.md) pages.
        - See the [optimal graphics settings for FusionFix](../../additional-setup.md/#__tabbed_2_2).
=== "1.0.8.0"
    !!! info "Missing fixes"
        Installing FusionFix on 1.0.8.0 compromises on some fixes, and you won't receive any official support from Fusion Team shall any issues arise. Keep that in mind.
    1. Go to the latest [release page](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest).
    2. Download :material-zip-box:`GTAIV.EFLC.FusionFix.zip`.
    3. Extract the archive into the game folder.
    4. Move the files out of the :material-folder: ==plugins== folder into the game folder (don't ask me why, this tends to improve stability).
        - Rename :fontawesome-solid-gears:`dinput8.dll` to `xlive.dll` **if not using GFWL**. Replace if needed.
        - Consider re-running the Setup Utility if you used it on the [Optimization](../../optimization.md) or [Additional Setup](../../additional-setup.md) pages.
        - See the [optimal graphics settings for FusionFix](../../additional-setup.md/#__tabbed_2_2).
        - **Do not enable `Check For Fusion Fix Updates`.**

    !!! tip "If using GFWL for multiplayer..."
        Apply this [patch](https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL/releases/latest) on top.

        If **only playing multiplayer**, consider the multiplayer-only [patch](https://github.com/SandeMC/GTAIV.EFLC.FusionFix-GFWLMin/releases/latest) for increased stability instead.

<h3>Additional steps for Linux users</h3> <a id="ff-linux"></a>

1. Install [Protontricks](https://github.com/Matoking/protontricks)
2. Open a terminal and run the following command in the GTA IV prefix:

    ```bash
    protontricks 12210 -q d3dx9_43
    ```

    If you installed Protontricks through Flatpak, run this:

    ```bash
    flatpak run com.github.Matoking.protontricks 12210 -q d3dx9_43
    ```

3. Wait until DirectX installs (may take a few minutes).

!!! tip "Modloading"
    This mod can be used for modloading purposes. See [Fusion Overloader](../../extras/modloading.md/#fusion-overloader) for more details.

---

<h2>Configuration</h2> <a id="configuration"></a>

Most of options are available in the in-game settings.

You can edit :material-file-cog:`GTAIV.EFLC.FusionFix.ini` or :material-file-cog:`GTAIV.EFLC.FusionFix.cfg` if you need to edit the settings outside of the game for some reason. See [the list of non-ingame options](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix?tab=readme-ov-file#details) if you need to tweak them.

---

<h2>Navigation</h2> <a id="navigation"></a>

<div class="grid cards" markdown>

- If your **game is downgraded**, continue with ZolikaPatch:

    [Next page:material-page-last: <br>ZolikaPatch</br>](zolikapatch.md){ .md-button .md-button--primary }

- If it isn't, continue with Various Fixes instead:

    [Next page:material-page-last: <br>Various Fixes</br>](various-fixes.md){ .md-button .md-button--primary }

</div>

[:material-page-first:Previous page <br>Essential Modding</br>](index.md){ .md-button }
