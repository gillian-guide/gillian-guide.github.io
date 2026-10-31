---
title: Зависимости модов
description: Почему все моды не используют UAL - всем было бы проще жить
---

# Зависимости модов

---

## [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader)

 UAL используется для загрузки `.asi` модов (одного из самых распространенных типов модов GTA IV) в игру. Он универсален и подходит для многих других игр, но мы будем использовать его для GTA IV.

!!! info "Совместимость"
    Ultimate ASI Loader совместим со всеми версиями игры.

<h3>Установка</h3>

1. Перейдите на страницу последнего [релиза](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases/latest).
2. Скачайте :material-zip-box: `Ultimate-ASI-Loader.zip` (**не :material-zip-box:`Ultimate-ASI-Loader_x64.zip`**).
3. Распакуйте архив в папку с игрой.

!!! warning "Если используется Linux..."
    Добавьте `WINEDLLOVERRIDES="dinput8=n,b" %command%` в параметры запуска:

    - **:material-steam: Steam**: Нажмите правой кнопкой на игру в библиотеке, откройте `Свойства...` и вставьте строку в поле `Параметры запуска`.
    - **:simple-rockstargames: Rockstar Games Launcher**: Откройте страницу игры в библиотеке, откройте настройки и вставьте строку в поле `Параметры запуска`.
    - **Ярлык Windows**: Нажмите правой кнопкой на ярлык игры, выберите `Свойства` и вставьте строку в поле `Цель`.

!!! tip "Избавляемся от Games for Windows - LIVE (для розничных патчей)"
    Этот инструмент поможет избавиться от GFWL, если вам не нужны официальный [мультиплеер GFWL](../extras/multiplayer.md#games-for-windows-live) и достижения Xbox Live. Так вы избавите себя от кучи возни с настройкой.

    - Переименуйте :fontawesome-solid-gears:`dinput8.dll` в `xlive.dll`

!!! tip "Модлоадинг"
    Ultimate ASI Loader можно использовать для модлоадинга. Подробности смотрите в разделе [модлоадинг](../extras/modloading.md).

---

## [ScriptHookDotNet](https://github.com/HazardX/gta4_scripthookdotnet/)

!!! warning "Совместимость"
    - Совместим со всеми версиями игры.
    - Если вы на Linux, смотрите раздел [Заставляем ScriptHookDotNet и IV-SDK .NET работать на Linux](#scripthookdotnet-iv-sdk-net-linux).

ScriptHookDotNet используется для запуска скриптов, написанных на любом языке .NET. Не путайте с [IV-SDK .NET](#iv-sdk-net).

<h3>Установка</h3>

=== "1.2.0.59"
    1. Перейдите на страницу последнего [релиза](https://github.com/Tomasak/gta4_scripthookdotnet/releases).
    2. Скачайте :material-zip-box:`scripthookdotnet_vx_x_x_x.zip`.
    3. Распакуйте архив в папку с игрой.
=== "1.0.8.0 и более старые"
    1. Перейдите на страницу последнего [релиза ScriptHook](https://github.com/themonthofjune/IV.1080.ScriptHook/releases).
    2. Скачайте :material-zip-box:`ScriptHook.zip`.
    3. Распакуйте архив :material-zip-box:`ScriptHook.zip` в папку с игрой.
    4. Перейдите на страницу последнего [релиза ScriptHookDotNet](https://github.com/ClonkAndre/gta4_scripthookdotnet/releases/tag/v1.7.2.0).
    5. Скачайте :material-file:`ScriptHookDotNet.asi`.
    6. Переместите файл в папку с игрой.

---

## [IV-SDK .NET](https://gtaforums.com/topic/986510-iv-sdk-net/)

!!! warning "Совместимость"
    - Совместим только с 1.0.8.0 и 1.0.7.0. Если у вас Complete Edition, сделайте [даунгрейд](../downgrading/downgrading-the-game.md).
    - Если вы на Linux, смотрите раздел [Заставляем ScriptHookDotNet и IV-SDK .NET работать на Linux](#scripthookdotnet-iv-sdk-net-linux).

IV-SDK .NET используется для запуска скриптов, написанных на любом языке .NET. Не путайте с [ScriptHookDotNet](#scripthookdotnet).

<h3>Установка</h3>

1. Перейдите на страницу последнего [релиза](https://github.com/ClonkAndre/IV-SDK-DotNet/releases/latest).
2. Скачайте :material-zip-box:`IV-SDK.NET.vx_x_x.zip`.
3. Распакуйте архив в папку с игрой.

???+ tip "Clonk's Coding Library"
    Некоторым модам могут понадобиться расширения из [Clonk's Coding Library](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/).

    <h4>Установка</h4>

    * Перейдите на страницу последнего [релиза](https://github.com/ClonkAndre/ClonksCodingLib.GTAIV/releases/latest).
    * Скачайте :material-zip-box:`ClonkCodingLib.GTAIV.vx_x.zip`.
    * Распакуйте архив в папку с игрой.

---

## Заставляем ScriptHookDotNet и IV-SDK .NET работать на Linux

По умолчанию ни один из них не работает на Linux. Но это можно исправить. Инструкции рассчитаны на опытного пользователя Linux, так что если что-то непонятно - ищите в интернете.

<h3>Инструкции</h3>

1. Во вкладке `Compatibility` игры в :material-steam:Steam временно смените версию Proton на одну из версий Proton 4.11-4.13
2. Найдите папку префикса вашей GTA IV, обычно она находится по пути :material-folder: ==~/.steam/Steam/steamapps/compatdata/12210/pfx==, и удалите ее
3. Запустите игру один раз - вы получите ошибку Rockstar Games Launcher, просто закройте ее, нам нужно только, чтобы папка префикса создалась заново
4. Установите [Protontricks](https://github.com/Matoking/protontricks) (если используете Lutris (или любой другой способ управления GTA IV вне Steam), используйте вместо него Winetricks)
5. Откройте терминал и выполните следующую команду, чтобы установить .NET в префикс GTA IV:

    ```bash
    protontricks 12210 -q dotnet472
    ```

    Если вы устанавливали Protontricks через Flatpak (а это так, если Steam у вас тоже через Flatpak), выполните вместо нее эту:

    ```bash
    flatpak run com.github.Matoking.protontricks 12210 -q dotnet472
    ```

6. Дождитесь окончания установки .NET (может занять от 5 до 30 минут)
7. Верните игре обычную версию Proton (настоятельно рекомендую использовать [Proton-GE](https://github.com/GloriousEggroll/proton-ge-custom/releases) (можно установить через [ProtonUp-Qt](https://davidotek.github.io/protonup-qt/)), которая улучшает стабильность и позволяет слушать Independence FM)
8. При запуске игры вы можете получить несколько ошибок .NET, но моды должны работать нормально.

За то, что нашли рабочее решение, спасибо Roigo и minidrwho.
