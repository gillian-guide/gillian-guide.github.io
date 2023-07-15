title: Зависимости для модов
description: Как установить зависимости для вашей установки GTA IV
hide: footer

# Зависимости для модов
==Если вы здесь в первый раз - устанавливайте только Ultimate ASI Loader.==

## Ultimate ASI Loader
Этот инструмент предназначен для загрузки модов `.asi` (один из наиболее распространенных типов модов для GTA IV) в игру. Он многоцелевой и может использоваться для многих других игр, но мы будем использовать его для GTA IV.

!!! warning ""
    Он уже включен в [FusionFix](essential-modding/fusionfix.md).

???+ note "Установка"
    * Перейдите к странице [релизов](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases).
    * Скачайте :material-zip-box:`Ultimate-ASI-Loader.zip`.
    ??? question "Почему не :material-zip-box:`Ultimate-ASI-Loader_x64.zip`? Моя система 64-битная"
        Ваша система в данном случае не имеет значения. Сама игра рассчитана на использование 32-битных библиотек, а не 64-битных.

        Проще говоря, игра не будет использовать файлы из :material-zip-box:`Ultimate-ASI-Loader_x64.zip`.
    * Распакуйте в папку с игрой.

??? tip "How to use .asi mods?"
    !!! warning ""
        Make sure your mod was built for Ultimate ASI Loader and not [ScriptHook](#scripthook) or [IV-SDK .NET](#iv-sdk-net).
    
    Extract the mod to either the game folder or :material-folder:==plugins== - either will do.

??? tip "Избавление от Games for Windows - LIVE (для старых патчей)"
    С помощью этого инструмента можно избавиться от [GFWL](../multiplayer/#games-for-windows-live), если вас не интересуют [мультиплеер](multiplayer.md) и достижения Xbox. Это уменьшит количество проблем с игрой.

    * Переименуйте :fontawesome-solid-gears:`dinput8.dll` в `xlive.dll`.

??? tip "Модлоадинг"
    Этот инструмент может быть использован для целей модлоадинга. См. раздел [модлоадинг](modloading.md).

## ScriptHook
!!! info ""
    Also known as ScriptHookDotNet and aru's ScriptHook.
!!! warning ""
    Compatible with all versions. See notes below.
This tool is used to run scripts written in any .NET language. Not to be confused with [IV-SDK .NET](#iv-sdk-net). See your mod's requirements to see whether it was built for ScriptHook or [IV-SDK .NET](#iv-sdk-net).

???+ note "Installation"
    * Go to [Releases](https://github.com/HazardX/gta4_scripthookdotnet/releases)
    * Download the version for the patch you want.
    * Extract :material-zip-box:`scripthookdotnet_vx_x_x_xb.zip` to your game folder.
    ??? note "Compatibility with 1.0.8.0"
        You may want to use [this version](https://gtaforums.com/topic/946154-release-gtaiv-net-scripthook-v1718-support-for-gta-iv-1080-and-eflc-1130-by-arinc9-zolika1351/) instead for 1.0.8.0 compatibility.
    ??? note "Compatibility with Complete Edition"
        Add this [patch](https://www.lcpdfr.com/downloads/gta4mods/g17media/26726-compatibility-patch-for-gta-iv-complete-edition/) for Complete Edition compatibility ontop. This is limited and you may experience problems.
??? tip "How to use .NET scripts?"
    !!! warning ""
        Make sure that your mod is built for ScriptHook and not for [IV-SDK .NET](#iv-sdk-.net).

    Extract the mod into :material-folder:==scripts==.

## IV-SDK .NET
!!! warning ""
    Only compatible with 1.0.8.0 and 1.0.7.0.
This tool is used to run scripts written in any .NET language. Not to be confused with [ScriptHook](#scripthook). See your mod's requirements to see whether it was built for IV-SDK .NET or for [ScriptHook](#scripthook).

???+ note "Installation"
    * Go to the [GTAForums page](https://gtaforums.com/topic/986510-iv-sdk-net/).
    * Download latest version.
    * Extract :material-zip-box:`IV-SDK.NET.vx_x_x.zip` to your game folder.
    ??? tip "Clonk's Coding Library"
        Some mods may require extensions from [Clonk's Coding Library](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/).
        
        - Installation:
            * Go to the [Releases](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/releases/tag/v1.3) page.
            * Download latest version.
            * Extract :material-zip-box:`ClonkCodingLib.GTAIV.vx_x.zip` into your game folder.
??? tip "How to use .NET scripts?"
    !!! warning ""
        Make sure your mod is built for IV-SDK .NET and not for [ScriptHook](#scripthook).

    Extract the mod to :material-folder:==IVSDKDotNot\scripts==.

[:material-page-first:Предыдущая страница <br>Давнгрейд</br>](downgrading.md){ .md-button } [Следующая страница:material-page-last: <br>Модлоадинг</br>](modloading.md){ .md-button .md-button--primary }