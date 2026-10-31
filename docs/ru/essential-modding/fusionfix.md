---
title: FusionFix
description: Графические исправления - и даже больше!
---

# [FusionFix](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix)

!!! warning "Совместимость"
    Этот мод официально поддерживается только на Complete Edition, но с учетом некоторых моментов его можно использовать и на 1.0.8.0.

    Поддержку версий помимо Complete Edition могут в любой момент прекратить, и разработчики не оказывают им никакой поддержки.
Этот проект нацелен на исправление большинства **графических и геймплейных проблем** и добавляет новые настройки графики. Список изменений можно прочитать в [репозитории](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/tree/master#coregameplay-changelog).

---

<h2>Демо</h2> <a id="_2"></a>

<iframe width="560" height="315" src="https://www.youtube.com/embed/XTuOortPoY4?si=5HbNzCc6JboJjxUT" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<h2>Установка</h2> <a id="_3"></a>

=== "1.2.0.59"
    1. Перейдите на [страницу последнего релиза](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest).
    2. Скачайте архив :material-zip-box:`GTAIV.EFLC.FusionFix.zip`.
    3. Распакуйте архив в папку с игрой.
        - Если вы использовали Setup Utility на страницах [оптимизации](../optimization.md) или [второстепенной настройки](../additional-setup.md), лучше запустите его заново.
        - Посмотрите [оптимальные настройки графики для FusionFix](../additional-setup.md#__tabbed_2_2).
=== "1.0.8.0"
    !!! info "Недостающие исправления"
        Устанавливая FusionFix на 1.0.8.0, вы лишаетесь части исправлений, а официальной поддержки от Fusion Team при возникновении проблем не будет. Имейте это в виду.
    1. Перейдите на [страницу последнего релиза](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest).
    2. Скачайте :material-zip-box:`GTAIV.EFLC.FusionFix.zip`.
    3. Распакуйте архив в папку с игрой.
    4. Переместите файлы из папки :material-folder: ==plugins== в папку с игрой (не спрашивайте почему - так обычно повышается стабильность).
        - Переименуйте :fontawesome-solid-gears:`dinput8.dll` в `xlive.dll`, **если не используете GFWL**. Замените файл, если потребуется.
        - Если вы использовали Setup Utility на страницах [оптимизации](../optimization.md) или [второстепенной настройки](../additional-setup.md), лучше запустите его заново.
        - Посмотрите [оптимальные настройки графики для FusionFix](../additional-setup.md#__tabbed_2_2).
        - **Не включайте `Check For Fusion Fix Updates`.**

    !!! tip "Если для мультиплеера используется GFWL..."
        Сверху примените этот [патч](https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL/releases/latest).

        Если вы играете **только в мультиплеер**, вместо него рассмотрите [патч только для мультиплеера](https://github.com/SandeMC/GTAIV.EFLC.FusionFix-GFWLMin/releases/latest) - он стабильнее.

<h3>Дополнительные действия для пользователей Linux</h3> <a id="ff-linux"></a>

1. Установите [Protontricks](https://github.com/Matoking/protontricks)
2. Откройте терминал и выполните следующую команду в префиксе GTA IV:

    ```bash
    protontricks 12210 -q d3dx9_43
    ```

    Если Protontricks установлен через Flatpak (а он так установлен, если вы запускаете Steam через Flatpak), выполните вместо нее эту:

    ```bash
    flatpak run com.github.Matoking.protontricks 12210 -q d3dx9_43
    ```

3. Дождитесь установки DirectX (это может занять несколько минут).

!!! tip "Модлоадинг"
    Этот мод можно использовать для модлоадинга. Подробности смотрите в разделе [Fusion Overloader](../extras/modloading.md#fusion-overloader).

---

<h2>Настройка</h2> <a id="_4"></a>

Большая часть настроек доступна в настройках самой игры.

Если вам зачем-то нужно менять настройки вне игры, отредактируйте :material-file-cog:`GTAIV.EFLC.FusionFix.ini` или :material-file-cog:`GTAIV.EFLC.FusionFix.cfg`. Если нужно что-то подкрутить, смотрите [список настроек вне игры](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix?tab=readme-ov-file#details).

---

<h2>Навигация</h2> <a id="_5"></a>

<div class="grid cards" markdown>

- Если ваша **игра даунгрейднута**, продолжите с OpenPreCEPatch:

    [Следующая страница:material-page-last: <br>OpenPreCEPatch</br>](openprecepatch.md){ .md-button .md-button--primary }

- Если нет, вместо него продолжите с Various Fixes:

    [Следующая страница:material-page-last: <br>Various Fixes</br>](various-fixes.md){ .md-button .md-button--primary }

</div>

[:material-page-first:Предыдущая страница <br>Обязательные моды</br>](index.md){ .md-button }
