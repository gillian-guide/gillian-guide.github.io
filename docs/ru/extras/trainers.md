---
title: Тренеры
description: Пап, смотри, я умею баннихопить в GTA IV!
---

# Тренеры

Тренеры - это по сути модменю, которые добавляют кучу веселых и полезных возможностей. Еще это хорошая альтернатива очень ограниченному набору [читов](https://gta.fandom.com/wiki/Cheats_in_GTA_IV), которые предлагает игра. Тренер может пригодиться в [мультиплеере](multiplayer.md), но сначала убедитесь, что ваш клиент/сервер их разрешает.

!!! warning ""
    Оба тренера требуют [Ultimate ASI Loader](../resources/mod-dependencies.md#ultimate-asi-loader).

    И, пожалуйста, выберите один - не ставьте оба сразу.

---

## [ZMenuIV](https://zolika1351.pages.dev/mods/ivmenu)

!!! warning "Совместимость"
    Этот тренер несовместим с Complete Edition.
Самый мощный и полнофункциональный тренер для GTA IV. Включает и Chaos-мод с поддержкой стримеров, и такие абсурдные вещи, как физика GoldSrc.

<h3>Установка</h3>

1. Перейдите на [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivmenu).
2. Прокрутите страницу вниз и скачайте последнюю версию.
3. Распакуйте :material-zip-box:`ZMenuIV_vx.zip` в папку с игрой
    - Не распаковывайте :material-folder: `asi loader if not using xliveless`, :material-folder: `for developers`, :material-folder: `old version (has VR support)`, :material-folder: `parachute support(all into game folder)`. Подробности об этих папках читайте в :material-file:`readme.txt`.

<h3>Использование</h3>

Клавиши по умолчанию:

- ++f7++ - открыть/закрыть меню.
- ++num8++, ++num2++, ++num4++, ++num6++ - навигация, ++num5++ - подтвердить, ++num0++ - вернуться назад.
- ++right-control+num1++ - починить машину.
- ++right-control+num2++ - перевернуть машину.
- ++bracket-right++ (удерживать) - ускорить машину.
- ++f6++ - Airbreak (noclip).
- ++0++ - Always God Mode.
- ++bracket-left++ - Never Wanted.
- ++semicolon++ - Unlimited Ammo.
- ++equal++ - Collision.
- ++minus++ - Resurrect.
- ++m++ - Ragdoll.

Вы можете добавить свои горячие клавиши, которые объединяют несколько опций. Для этого включите `Custom Keybind Creator` в `Trainer Settings`, выделите нужную опцию и нажмите ++left-control+enter++, чтобы задать клавишу.

Чтобы изменить существующие привязки, отредактируйте раздел `[Keybinds]` в :material-file-cog:`ZMenuIV.ini`.

??? tip "Настройка клавиш без нумпада"
    Нумпад есть не у всех, я понимаю: 80-процентные (и меньше) клавиатуры - это удобно и практично. Откройте :material-file-cog:`ZMenuIV.ini` и найдите эти строки:

    ```{ .ini }
    [Keybinds]
    AirbreakUp=87
    AirbreakDn=83
    AirbreakForward=104
    AirbreakBack=98
    AirbreakLeft=100
    AirbreakRight=102
    MenuUp=104
    MenuDn=98
    MenuLeft=100
    MenuRight=102
    MenuEnter=101
    MenuBack=96
    ```

    и замените их на:

    ```{ .ini }
    [Keybinds]
    AirbreakUp=32
    AirbreakDn=160
    AirbreakForward=87
    AirbreakBack=83
    AirbreakLeft=65
    AirbreakRight=68
    MenuUp=73
    MenuDn=75
    MenuLeft=74
    MenuRight=76
    MenuEnter=13
    MenuBack=220
    ```

    Что будет означать:

    - ++i++++j++++k++++l++ - навигация. ++enter++ - подтвердить, ++backslash++ - вернуться назад.
    - ++w++++a++++s++++d++ - горизонтальное управление airbreak, ++space++ - вверх, ++lshift++ - вниз.

---

## [Liberty's Legacy](https://gtaforums.com/topic/973091-gta-iv-12043-libertys-legacy-trainer/)

!!! warning "Совместимость"
    Этот тренер совместим с Complete Edition, а также с патчами 1.0.8.0 и 1.0.7.0.
Этот тренер не такой мощный, как ZMenuIV, но тоже предлагает много полезных функций. Впрочем, это единственный тренер, который можно использовать с Complete Edition. Еще он поддерживает геймпады.

<h3>Установка</h3>

1. Установите [ScriptHookDotNet](../resources/mod-dependencies.md#scripthookdotnet), если вы не сделали этого сами вне руководства.
2. Перейдите на [страницу на GTAForums](https://gtaforums.com/topic/973091-gta-iv-12043-libertys-legacy-trainer/).
3. Скачайте последнюю версию.
4. Распакуйте архив :material-zip-box:`Liberty's Legacy Trainer xxx.zip` в папку с игрой.

<h3>Использование</h3>

Клавиши по умолчанию на клавиатуре и мыши:

- ++f11++ - открыть/закрыть меню.
- Стрелки - навигация, ++enter++ - подтвердить, ++backspace++ - вернуться назад.

Привязки на геймпаде:

- RB+X или R1+Square на геймпадах.
- D-Pad - навигация, A или Cross - подтвердить, B или Circle - вернуться назад.

Дополнительные привязки можно задать так: выделите нужную опцию, нажмите ++left-control+enter++ и нажмите клавишу, которую хотите привязать.

---

## Навигация

[:material-page-first:Предыдущая страница <br>Дополнения</br>](index.md){ .md-button }
