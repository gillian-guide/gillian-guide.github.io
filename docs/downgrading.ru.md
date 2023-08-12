title: Даунгрейд
description: Методы даунгрейдинга GTA IV с Complete Edition

# Даунгрейд
Вы можете совершить даунгрейд до 1.0.8.0 или более ранних патчей, в основном для совместимости с модами. Complete Edition поддерживает гораздо меньшее количество модов, и в основном не поддерживает [ZolikaPatch](essential-modding/zolikapatch.md), Liberty Tweaks и [IV Tweaker](../extras/modloading/#iv-tweaker). 

Однако у нас есть несколько даунгрейдеров на выбор.

### Примечания
!!! info ""
	1. 1.2.0.59 это Complete Edition, т.е. последняя версия в [:material-steam:Steam](https://store.steampowered.com/app/12210/) и [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv). В нем убрана поддержка мультиплеера и Games for Windows - LIVE, при этом добавлены Rockstar Games Launcher (с его DRM) и оверлей Social Club (с его достижениями). ==Количество поддерживаемых модов в этой версии также значительно ограничено - большинство модов создано для версий 1.0.8.0 и 1.0.7.0==.
	2. 1.0.8.0 является последним патчем для дисковой/старой версии, с поддержкой ZolikaPatch и мультиплеера. ==Эта версия лучше подходит для совместимости с модами.==
    3. 1.0.4.0 - это более старый патч с полной совместимостью с ENB, а также со старым алгоритмом теней, который, по мнению некоторых людей в коммьюнити, лучше.

## Какой даунгрейдер выбрать?
Это зависит от ваших целей. Если вам нужно что-то простое, как распаковка архива - выбирайте даунгрейдер от Zolika1351. Если нужно что-то с большим количеством опций - выбирайте даунгрейдер от ItsClockAndre.

???+ question "Сравнение"
    * :material-plus-minus: означает "Частично" или "Не так хорошо".

    | Преимущества | от Zolika1351 | от ItsClockAndre |
    | :----------: | :-----------: | :--------------: |
    | Даунгрейд до 1.0.8.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Даунгрейд до 1.0.7.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Даунгрейд до 1.0.4.0 | :material-cancel: | :material-checkbox-marked-circle: |
    | Простота | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Размер | :material-checkbox-marked-circle: | :material-plus-minus: |
    | Возможность выбора дополнительных модов | :material-plus-minus: | :material-checkbox-marked-circle: |
    | Дополнительная поддержка [GFWL](../multiplayer/#games-for-windows-live) | :material-cancel: | :material-checkbox-marked-circle: |
    | Включен даунгрейд радио | :material-cancel: | :material-checkbox-marked-circle: |
    | Включена конвертация сохранений | :material-cancel: | :material-checkbox-marked-circle: |

## Даунгрейдер от Zolika1351
Этот даунгрейдер очень маленький по размеру и заменяет минимальное количество файлов(что отдаляет этот даунгрейд от настоящей дисковой версии), но при этом не содержит ни даунгрейд радио, ни способа даунгрейда до версии 1.0.4.0.  Он включает в себя [ZolikaPatch](essential-modding/zolikapatch.md) и [IV Tweaker](../extras/modloading/#iv-tweaker), а также имеет дополнительную поддержку портированной версии [FusionFix](essential-modding/fusionfix.md). Однако он совершенно не совместим с [Games for Windows - LIVE](../multiplayer/#games-for-windows-live).

???+ note "Установка"
    * Создайте исключение в антивирусе для папки с игрой. (Необязательно, но настоятельно рекомендуется).
    * Зайдите на сайт [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch/downgrading).
    * Скачайте архив с даунгрейдом (версия для 1.0.7.0 ниже).
    * Распаковать содержимое :material-zip-box:`IV_Downgrade_10x0_vxx.zip` в папку с игрой, заменив все, если требуется.
    * Запустите :material-file-download:`vcredist_x86.exe` и дайте ему установиться.
    * Запустите игру.
    * Если все работает нормально, можно также установить один из дополнительных модов(Optional mods), перечисленных ниже (не рекомендуется устанавливать оба; предпочтительнее [FusionFix](essential-modding/fusionfix.md)).

## Даунгрейдер от ItsClockAndre
Этот даунгрейдер работает в онлайн-режиме и загружает только то, что вы выбрали для загрузки. Он заменяет больше файлов, чем даунгрейдер от Zolika1351, что усложняет восстановление установки, если вы не сделали резервную копию, но это также делает данный даунгрейдер более близким к настоящей дисковой версии. Этот даунгрейдер также может быть не таким актуальным, как от Zolika1351. В этом даунгрейдере также есть возможность понизить версию до 1.0.4.0.

???+ note "Установка"
    * Создайте исключение в антивирусе для папки с игрой. (Необязательно, но настоятельно рекомендуется).
    * Зайдите на [страницу на GTAForums](https://gtaforums.com/topic/976691-gta-iv-downgrader/) и скачайте последнюю версию.
    * Распаковать архив, запустить :material-file:`IVDowngrader.exe`. с :fontawesome-solid-shield-halved:==правами администратора==.
    ??? info "Автономный режим"
        Вы можете настроить даунгрейдер для работы в автономном режиме. Скачайте файлы [отсюда](https://mega.nz/folder/Fn0Q3LhY#_0t1VZQFuQX22lMxRZNB1A) и распакуйте их в :material-folder:==Downgrader\\Data\\Temp==. Запускайте :material-file:`LaunchInOfflineMode.exe`.
    * Следуйте инструкциям в приложении. Обязательно прочитайте предупреждения при выборе модов.
    * При настройке на поддержку GFWL обязательно проверьте [эту страницу](../multiplayer/#games-for-windows-live). Если нет, убедитесь, что мод `xliveless` включен.
    !!! info ""
        Если вы каким-то образом пропустили этот шаг, настройте [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) на избавление от GFWL.

## Даунгрейдер радио
!!! note ""
    Этот даунгрейдер может быть использован как для Complete Edition, так и для старых версий. Читайте примечания ниже.

    Этот даунгрейдер уже является частью [даунгрейдера от ItsClockAndre](#itsclockandre) если вы не пропустили этап даунгрейда радиостанций - в этом случае вы можете пропустить эту часть.
Более 50 треков радиостанций были удалены из игры в апреле 2018 года из-за просроченных лицензий. Однако мы можем их восстановить.
???+ note "Установка"
    * Установите последнюю версию [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) для его модлоадера (также [ZolikaPatch](essential-modding/zolikapatch.md) если вы используете старые версии; мы можем обойти это, читайте примечание позже)
    * Перейдите на сайт [Various GTA Downgraders](http://downgraders.rockstarvision.com/) и прокрутите страницу до конца.
    * Скачайте Radio downgrader для GTA IV.
    * Распакуйте :material-zip-box:`IVCE_RADIO_DOWNGRADER.rar` в папку с игрой (исключая папки :material-folder:`... new vladivostok`).
    * Запустите :material-file-download:`install.bat` и дождитесь, пока консоль сама закроется.
    * Теперь распакуйте либо :material-folder:`with new vladivostok`, либо :material-folder:`without new vladivostok` в папку с игрой.
    ???+ question "В чем разница?"
        Rockstar добавили на Владивосток новые треки взамен вырезанных. :material-folder:`with new vladivostok` сохраняет их вместе с восстановленными вырезанными, а :material-folder:`without new vladivostok` вырезает их, оставляя только восстановленные.
    ???+ tip "Аддоны"
        Существует множество аддонов - смотрите их [здесь](https://www.nexusmods.com/gta4/mods/234?tab=files)
    ??? question "Как обойтись без использования Ultimate ASI Loader?"
        Переместите содержимое папки :material-folder:`update` в папку с игрой, заменяя файлы при появлении запроса.

## Даунгрейд сохранения
Если вы уже начали играть на Complete Edition, то, возможно, вам захочется понизить свой файл сохранения до старых версий.

* Сначала найдите свои сохранения в :material-folder:==Documents\Rockstar Games\GTA IV\Profiles\(id)\\==. Они называются :material-file:`SGTAxxx`.
* Загрузите тот, который вы хотите конвертировать на [GTASnP](https://gtasnp.com/).
* Разверните вкладку `Modifications`.
* Выберите `1.0.8.0 IV / 1.1.3.0 EFLC and older` в `Downgrade Version`.
* Выберите слот, в который вы хотите сохранить свой файл сохранения. У вас должно загрузиться конвертированное сохранение.
* Расположите его в :material-folder:==C:\Users\(user)\AppData\Local\Rockstar Games\GTA IV\savegames\user_(id)\\==.

## Руссификатор
После даунгрейдинга, у вас не будет русского языка. Скачайте [оффициальный руссификатор](https://drive.google.com/file/d/1YCoM0BTfCiVYNPl2UxgOK6QiV4j1nAMG/view) и установите его как для EFLC в папку с игрой. 

???+ note "Альтернативная версия"
    Также есть версия для [UAL'овского модлоадера](../extras/modloading/#ultimate-asi-loader). Скачать можно [здесь](https://drive.google.com/file/d/1GbOA3CBAQGgXW6SjODzd8G8Cj-a8G6dt/view?usp=drive_link)

В Настройках - Дисплей измените язык на Русский.

[:material-page-first:Предыдущая страница <br>Второстепенная настройка</br>](additional-setup.md){ .md-button } [Следующая страница:material-page-last: <br>Зависимости для модов</br>](mod-dependencies.md){ .md-button .md-button--primary }