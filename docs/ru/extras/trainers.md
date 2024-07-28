title: Трейнеры
description: Добавьте в GTA IV дополнительные функции - неважно для чего!

# Трейнеры
Трейнеры - это, по сути, менюшки добавляющие множество интересных и полезных опций. Они также являются лучшей альтернативой очень ограниченному количеству [читкодов](https://gta.fandom.com/wiki/Cheats_in_GTA_IV), предлагаемых игрой. Вам может понадобиться один из них для [мультиплеера](../multiplayer.md), но убедитесь, что ваш сервер разрешает их использование.

## [ZMenuIV](https://zolika1351.pages.dev/mods/ivmenu)
!!! warning "Совместимость"
    Этот трейнер не совместим с Complete Edition. Совершите [даунгрейд](../downgrading.md), если вы используете Complete Edition.
Самый мощный и полноценный трейнер для GTA IV. Также в комплект входит Chaos-мод для стримеров и веселья. И... физика из Goldsrc...? Бхоппинг по фану, ig.
???+ info "Установка"
    * Установите последний [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader).
    * Перейдите на сайт [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivmenu).
    * Прокрутите страницу до конца и скачайте последнюю версию.
    * Распакуйте :material-zip-box:`ZMenuIV_vx.zip` в папку с игрой (исключая папки :material-folder: `asi loader if not using xliveless`, :material-folder: `for developers`, :material-folder: `old version (has VR support)`, :material-folder: `parachute support(all into game folder)`. Прочтите :material-file:`readme.txt` для деталей на эти папки).
    ??? question "Аддоны"
        Прочтите :material-file:`readme.txt` для деталей на аддоны.
???+ tip "Использование"
    - Управление по умолчанию:
        * ++f7++ для переключения меню.
        * ++num8++, ++num2++, ++num4++, ++num6++ для навигации. ++num5++ - принять, ++num0++ - назад.
        * ++right-control+num1++ для ремонта транспорта.
        * ++right-control+num2++ для переворота транспорта.
        * ++bracket-right++ (удерживать) для ускорения транспорта.
        * ++f6++ для Airbreak(noclip)
        * ++right-control++ для Special God 1.
        * ++f1++ для Special God 2.
        * ++0++ для Always God Mode(бессмертие).
        * ++bracket-left++ для Never Wanted(откл. розыск).
        * ++semicolon++ для Unlimited Ammo(бесконечные патроны).
        * ++equal++ для Collision.
        * ++minus++ для Resurrect(возрождения).
        * ++single-quote++ для Forward Through Door.
        * ++m++ для Ragdoll.
    
    Вы можете добавлять свои собственные привязки клавиш, которые могут сочетать в себе несколько опций. Для этого включите функцию `Custom Keybind Creator` в разделе `Trainer Settings`, выделите нужную опцию и нажмите ++left-control+enter++ для установки привязки.

    Отредактируйте категорию `[Keybinds]` в :material-file-cog:`ZMenuIV.ini` для изменения существующих привязок.
    ??? tip "Привязки клавиш без Numpad"
        Не у всех есть Numpad, я понимаю, 80% (и меньше) клавиатуры - это круто и удобно. Откройте :material-file-cog:`ZMenuIV.ini` и найдите эти строки:

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

        и измените их на:

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

        - Что будет:
            * ++i++++j++++k++++l++ для навигации. ++enter++ - принять, ++backslash++ - назад.
            * ++w++++a++++s++++d++ для горизонтального управления Airbreak, ++space++ для поднятия высоты, и ++lshift++ для спуска.

## [Liberty's Legacy](https://gtaforums.com/topic/973091-gta-iv-12043-libertys-legacy-trainer/)
!!! warning "Совместимость"
    Данный тренер совместим с Complete Edition, а также с патчами 1.0.8.0 и 1.0.7.0.
Этот трейнер не такой мощный, как ZMenuIV, но все же предлагает много полезных функций, особенно если вы играете с Complete Edition.
???+ info "Установка"
    * Установить последние [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader) и [ScriptHook](../../mod-dependencies/#scripthook).
    * Перейдите на [страницу GTAForums](https://gtaforums.com/topic/973091-gta-iv-12043-libertys-legacy-trainer/).
    * Скачайте последнюю версию.
    * Распакуйте :material-zip-box:`Liberty's Legacy Trainer xxx.zip` в папку с игрой.
???+ tip "Использование"
    - Управление по умолчанию:
        * ++f11++ или RB+X/R1+Квадрат для переключения меню.
        * Стрелки или крестовина для навигации. ++enter++ или A/X - принять, ++backspace++ или B/Кружок - назад.
    
    Дополнительные привязки клавиш можно установить, выделив нужную опцию, нажав ++left-control+enter++ и нажав клавишу, которую вы хотите привязать.

## [Simple Native Trainer](https://gtaforums.com/topic/392973-ivrel-simple-trainer-for-gtaiv/)
!!! warning "Совместимость"
    Данный трейнер совместим со всеми патчами.
Этот трейнер менее полный, чем два других, но... некоторым людям он будет полезен, я думаю.
???+ info "Установите"
    * Установить последние [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader) и [ScriptHook](../../mod-dependencies/#scripthook).
    * Перейдите на [страницу GTAForums](https://gtaforums.com/topic/392973-ivrel-simple-trainer-for-gtaiv/).
    * Скачайте последнюю версию (где-то в посте:material-trademark:).
    * Распакуйте :material-file:`trainer.asi`, :material-file-cog:`trainer.ini`, :material-file:`trainertbogt.asi`, :material-file-cog:`trainertbogt.ini`, :material-file:`trainertlad.asi`, :material-file-cog:`trainertlad.ini` из :material-zip-box:`trainervxx.rar` в папку с игрой.
???+ tip "Использование"
    ++f3++ для открытия меню,  ++num8++, ++num2++, ++num4++, ++num6++ для навигации. Читайте :material-file:`readme.doc` или страницу GTAForums для инструкций для изменения клавиш.

[:material-page-first:Предыдущая страница <br>Мультиплеер</br>](../multiplayer.md){ .md-button } [Следующая страница:material-page-last: <br>Лаунчер</br>](launcher.md){ .md-button .md-button--primary }