title: Liberty Tweaks
description: One of the nice mods to have for your GTA IV install that improves various aspects of the game

# Liberty Tweaks
!!! warning "Compatibility"
    This mod only supports 1.0.7.0/1.0.8.0 at the moment, but Complete Edition support is considered.
This project aims to improve various aspects of the game and it's general quality of life. You can see the features on the [GTAForums thread](https://gtaforums.com/topic/991160-liberty-tweaks/).

## Showcase { data-search-exclude }
![Liberty Tweaks - Overtaking fix](https://media.giphy.com/media/612lWEiuUnPgn6KD98/giphy.gif){: style="height:50%;width:50%";} ![Liberty Tweaks - Brake Lights Fix](https://media.giphy.com/media/3IOojdksuttI94tytB/giphy.gif){: style="height:50%;width:50%";}

![Liberty Tweaks - Weapon Magazines](https://media.giphy.com/media/9WkHpgdodMMkVwSxQK/giphy.gif){: style="height:50%;width:50%";} ![Liberty Tweaks - Quicksaves](https://media.giphy.com/media/gJsHuySiJtuM4odkNF/giphy.gif){: style="height:50%;width:50%";}

## Installation { data-search-exclude }
* Install [IV-SDK .NET and Clonk's Coding Library](../../mod-dependencies/#iv-sdk-net).
* In :material-file-cog:`IVSDKDotNet/config.ini` disable `PauseExecutionWhenNotInFocus` to prevent some issues.
* Go to the latest [Release](https://github.com/catsmackaroo/LibertyTweaks/releases/latest).
* Download the :material-zip-box:`LibertyTweaksx.x.zip`.
* Extract the contents of :material-folder:==1. Install== into the game folder. Replace files if prompted.
* Configure :material-file-cog:`IVSDKDotNet/scripts/LibertyTweaks.ini` as you wish.

???+ question "Why does this mod use IV-SDK .NET and not ScriptHookDotNet?"
    ScriptHookDotNet is an outdated and unmaintained API with a lot of issues (performance impact, rain issues) that are not going to be fixed. IV-SDK .NET is a new API built on Zolika1351's IV-SDK that is meant to supersede ScriptHookDotNet without it's issues.

[:material-page-first:Previous page <br>Various Fixes</br>](variousfixes.md){ .md-button } [Next page:material-page-last: <br>Characters Fixes</br>](charactersfixes.md){ .md-button .md-button--primary }