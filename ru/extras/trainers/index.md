# Тренеры

Тренеры - это по сути модменю, которые добавляют кучу веселых и полезных возможностей. Еще это хорошая альтернатива очень ограниченному набору [читов](<https://gta.fandom.com/wiki/Cheats_in_GTA_IV>), которые предлагает игра. Тренер может пригодиться в [мультиплеере](<https://gillian-guide.github.io/ru/extras/multiplayer/index.md>), но сначала убедитесь, что ваш клиент/сервер их разрешает.

> [!WARNING]
>
> Оба тренера требуют [Ultimate ASI Loader](<https://gillian-guide.github.io/ru/resources/mod-dependencies/#ultimate-asi-loader>).
>
> И, пожалуйста, выберите один - не ставьте оба сразу.

---

## [ZMenuIV](<https://zolika1351.pages.dev/mods/ivmenu>)

> [!WARNING]
>
> **Совместимость**
>
> Этот тренер несовместим с Complete Edition.

Самый мощный и полнофункциональный тренер для GTA IV. Включает и Chaos-мод с поддержкой стримеров, и такие абсурдные вещи, как физика GoldSrc.

### Установка

1. Перейдите на [Zolika1351's Zone](<https://zolika1351.pages.dev/mods/ivmenu>).
2. Прокрутите страницу вниз и скачайте последнюю версию.
3. Распакуйте `ZMenuIV_vx.zip` в папку с игрой

   - Не распаковывайте `asi loader if not using xliveless`, `for developers`, `old version (has VR support)`, `parachute support(all into game folder)`. Подробности об этих папках читайте в `readme.txt`.

### Использование

Клавиши по умолчанию:

- <kbd class="key-f7">F7</kbd> - открыть/закрыть меню.
- <kbd class="key-num8">Num 8</kbd>, <kbd class="key-num2">Num 2</kbd>, <kbd class="key-num4">Num 4</kbd>, <kbd class="key-num6">Num 6</kbd> - навигация, <kbd class="key-num5">Num 5</kbd> - подтвердить, <kbd class="key-num0">Num 0</kbd> - вернуться назад.
- <kbd class="key-right-control">Right Ctrl</kbd>\+<kbd class="key-num1">Num 1</kbd> - починить машину.
- <kbd class="key-right-control">Right Ctrl</kbd>\+<kbd class="key-num2">Num 2</kbd> - перевернуть машину.
- <kbd class="key-bracket-right">]</kbd> (удерживать) - ускорить машину.
- <kbd class="key-f6">F6</kbd> - Airbreak (noclip).
- <kbd class="key-0">0</kbd> - Always God Mode.
- <kbd class="key-bracket-left">[</kbd> - Never Wanted.
- <kbd class="key-semicolon">;</kbd> - Unlimited Ammo.
- <kbd class="key-equal">=</kbd> - Collision.
- <kbd class="key-minus">-</kbd> - Resurrect.
- <kbd class="key-m">M</kbd> - Ragdoll.

Вы можете добавить свои горячие клавиши, которые объединяют несколько опций. Для этого включите `Custom Keybind Creator` в `Trainer Settings`, выделите нужную опцию и нажмите <kbd class="key-left-control">Left Ctrl</kbd>\+<kbd class="key-enter">Enter</kbd>, чтобы задать клавишу.

Чтобы изменить существующие привязки, отредактируйте раздел `[Keybinds]` в `ZMenuIV.ini`.

> [!TIP]
>
> **Настройка клавиш без нумпада**
>
> Нумпад есть не у всех, я понимаю: 80-процентные (и меньше) клавиатуры - это удобно и практично. Откройте `ZMenuIV.ini` и найдите эти строки:
>
> ```ini
> [Keybinds]
> AirbreakUp=87
> AirbreakDn=83
> AirbreakForward=104
> AirbreakBack=98
> AirbreakLeft=100
> AirbreakRight=102
> MenuUp=104
> MenuDn=98
> MenuLeft=100
> MenuRight=102
> MenuEnter=101
> MenuBack=96
> ```
>
> и замените их на:
>
> ```ini
> [Keybinds]
> AirbreakUp=32
> AirbreakDn=160
> AirbreakForward=87
> AirbreakBack=83
> AirbreakLeft=65
> AirbreakRight=68
> MenuUp=73
> MenuDn=75
> MenuLeft=74
> MenuRight=76
> MenuEnter=13
> MenuBack=220
> ```
>
> Что будет означать:
>
> - <kbd class="key-i">I</kbd><kbd class="key-j">J</kbd><kbd class="key-k">K</kbd><kbd class="key-l">L</kbd> - навигация. <kbd class="key-enter">Enter</kbd> - подтвердить, <kbd class="key-backslash">\</kbd> - вернуться назад.
> - <kbd class="key-w">W</kbd><kbd class="key-a">A</kbd><kbd class="key-s">S</kbd><kbd class="key-d">D</kbd> - горизонтальное управление airbreak, <kbd class="key-space">Space</kbd> - вверх, <kbd class="key-left-shift">Left Shift</kbd> - вниз.

---

## [Liberty's Legacy](<https://gtaforums.com/topic/973091-gta-iv-12043-libertys-legacy-trainer/>)

> [!WARNING]
>
> **Совместимость**
>
> Этот тренер совместим с Complete Edition, а также с патчами 1.0.8.0 и 1.0.7.0.

Этот тренер не такой мощный, как ZMenuIV, но тоже предлагает много полезных функций. Впрочем, это единственный тренер, который можно использовать с Complete Edition. Еще он поддерживает геймпады.

### Установка

1. Установите [ScriptHookDotNet](<https://gillian-guide.github.io/ru/resources/mod-dependencies/#scripthookdotnet>), если вы не сделали этого сами вне руководства.
2. Перейдите на [страницу на GTAForums](<https://gtaforums.com/topic/973091-gta-iv-12043-libertys-legacy-trainer/>).
3. Скачайте последнюю версию.
4. Распакуйте архив `Liberty's Legacy Trainer xxx.zip` в папку с игрой.

### Использование

Клавиши по умолчанию на клавиатуре и мыши:

- <kbd class="key-f11">F11</kbd> - открыть/закрыть меню.
- Стрелки - навигация, <kbd class="key-enter">Enter</kbd> - подтвердить, <kbd class="key-backspace">Backspace</kbd> - вернуться назад.

Привязки на геймпаде:

- RB+X или R1+Square на геймпадах.
- D-Pad - навигация, A или Cross - подтвердить, B или Circle - вернуться назад.

Дополнительные привязки можно задать так: выделите нужную опцию, нажмите <kbd class="key-left-control">Left Ctrl</kbd>\+<kbd class="key-enter">Enter</kbd> и нажмите клавишу, которую хотите привязать.

---

## Навигация
