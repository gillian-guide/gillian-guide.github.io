title: Зависимости для модов
description: Как установить зависимости для вашей установки GTA IV

# Зависимости для модов
==Если вы здесь в первый раз - устанавливайте только Ultimate ASI Loader.==

## Ultimate ASI Loader
Этот инструмент предназначен для загрузки модов `.asi` (один из наиболее распространенных типов модов для GTA IV) в игру. Он многоцелевой и может использоваться для многих других игр, но мы будем использовать его для GTA IV.

!!! warning ""
    Этот инструмент совместим со всеми версиями.

    Он уже включен в [FusionFix](essential-modding/fusionfix.md).

???+ note "Установка"
    * Перейдите к странице [релизов](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases).
    * Скачайте :material-zip-box:`Ultimate-ASI-Loader.zip`.
    ??? question "Почему не :material-zip-box:`Ultimate-ASI-Loader_x64.zip`? Моя система 64-битная"
        Ваша система в данном случае не имеет значения. Сама игра рассчитана на использование 32-битных библиотек, а не 64-битных.

        Проще говоря, игра не будет использовать файлы из :material-zip-box:`Ultimate-ASI-Loader_x64.zip`.
    * Распакуйте в папку с игрой.

??? tip "Как использовать `.asi` моды?"
    !!! warning ""
        Убедитесь, что ваш мод был создан для Ultimate ASI Loader, а не для [ScriptHook](#scripthook) или [IV-SDK .NET](#iv-sdk-net).
    
    Распакуйте мод либо в папку с игрой, либо в :material-folder:==plugins== - подойдет любой из вариантов.

??? tip "Избавление от Games for Windows - LIVE (для старых патчей)"
    С помощью этого инструмента можно избавиться от [GFWL](../multiplayer/#games-for-windows-live), если вас не интересуют [мультиплеер](multiplayer.md) и достижения Xbox. Это уменьшит количество проблем с игрой.

    * Переименуйте :fontawesome-solid-gears:`dinput8.dll` в `xlive.dll`.

??? tip "Модлоадинг"
    Этот инструмент может быть использован для целей модлоадинга. См. раздел [модлоадинг](extras/modloading.md).

## ScriptHook
!!! info ""
    Также известен как ScriptHookDotNet и aru's ScriptHook.
!!! warning ""
    Совместим со всеми версиями. См. примечания ниже.
Этот инструмент используется для запуска скриптов, написанных на любом языке .NET. Не следует путать с [IV-SDK .NET](#iv-sdk-net). Посмотрите в требованиях к вашему моду, чтобы узнать, был ли он создан для ScriptHook или [IV-SDK .NET](#iv-sdk-net).

???+ note "Установка"
    * Перейдите на страницу [релизов](https://github.com/HazardX/gta4_scripthookdotnet/releases)
    * Скачайте версию для желаемого патча.
    * Распакуйте :material-zip-box:`scripthookdotnet_vx_x_x_xb.zip` в папку с игрой.
    ??? note "Совместимость с 1.0.8.0"
        Для совместимости с 1.0.8.0 лучше использовать [эту версию](https://gtaforums.com/topic/946154-release-gtaiv-net-scripthook-v1718-support-for-gta-iv-1080-and-eflc-1130-by-arinc9-zolika1351/).
    ??? note "Совместимость с Complete Edition"
        Добавьте этот [патч](https://www.lcpdfr.com/downloads/gta4mods/g17media/26726-compatibility-patch-for-gta-iv-complete-edition/) поверх для совместимости с Complete Edition. Патч не идеален и вы, возможно, встретите проблемы.
??? tip "Как использовать .NET скрипты?"
    !!! warning ""
        Убедитесь, что ваш мод создан для ScriptHook, а не для [IV-SDK .NET](#iv-sdk-net).

    Распакуйте мод в :material-folder:==scripts==.

## IV-SDK .NET
!!! warning ""
    Совместим только с 1.0.8.0 и 1.0.7.0. Совершите [даунгрейд](downgrading.md), если вы используете Complete Edition.
Этот инструмент используется для запуска скриптов, написанных на любом языке .NET. Не следует путать с [ScriptHook](#scripthook). Посмотрите в требованиях к вашему моду, чтобы узнать, был ли он создан для IV-SDK .NET или для [ScriptHook](#scripthook).

???+ note "Установка"
    * Перейдите на [страницу GTAForums](https://gtaforums.com/topic/986510-iv-sdk-net/).
    * Скачайте последнюю версию.
    * Распакуйте :material-zip-box:`IV-SDK.NET.vx_x_x.zip` в папку с игрой.
    ??? tip "Clonk's Coding Library"
        Для некоторых модов могут потребоваться расширения из [Clonk's Coding Library](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/).
        
        - Установка:
            * Перейдите на страницу [релизов](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/releases/tag/v1.3).
            * Скачайте последнюю версию.
            * Распакуйте :material-zip-box:`ClonkCodingLib.GTAIV.vx_x.zip` в папку с игрой.
??? tip "Как использовать .NET скрипты?"
    !!! warning ""
    Убедитесь, что ваш мод создан для IV-SDK .NET, а не для [ScriptHook](#scripthook).

    Распакуйте мод в :material-folder:==IVSDKDotNot\scripts==.

[:material-page-first:Предыдущая страница <br>Даунгрейд</br>](downgrading.md){ .md-button } [Следующая страница:material-page-last: <br>Важные моды</br>](essential-modding/index.md){ .md-button .md-button--primary }