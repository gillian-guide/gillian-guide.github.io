title: Даунгрейд
description: Методы даунгрейдинга GTA IV с Complete Edition.
hide: footer

# Даунгрейд
Вы можете совершить даунгрейд до 1.0.8.0 или более ранних патчей, в основном для совместимости с модами. Complete Edition поддерживает гораздо меньшее количество модов, и в основном не поддерживает [ZolikaPatch](essential-modding/zolikapatch.md), Liberty Tweaks и [IV Tweaker](../modloading/#iv-tweaker). 

Однако у нас есть несколько даунгрейдеров на выбор.

### Примечания
!!! info ""
	1. 1.2.0.59 это Complete Edition, т.е. последняя версия в [:material-steam:Steam](https://store.steampowered.com/app/12210/) и [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv). В нем убрана поддержка мультиплеера и Games for Windows - LIVE, при этом добавлены Rockstar Games Launcher (с его DRM) и оверлей Social Club (с его достижениями). Количество поддерживаемых модов в этой версии также значительно ограничено - большинство модов создано для версий 1.0.8.0 и 1.0.7.0.
	2. 1.0.8.0 является последним патчем для дисковой/старой версии, с поддержкой ZolikaPatch и мультиплеера. Эта версия лучше подходит для совместимости с модами.
    3. 1.0.4.0 - это более старый патч с полной совместимостью с ENB, а также со старым алгоритмом теней, который, по мнению некоторых людей в коммьюнити, лучше.

## Какой даунгрейдер выбрать?
Это зависит от ваших целей. Если вам нужно что-то простое, как распаковка архива - выбирайте даунгрейдер от Zolika1351. Если нужно что-то с большим количеством опций - выбирайте даунгрейдер от ItsClockAndre.

???+ question "Сравнение"
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
Этот даунгрейдер очень маленький по размеру и заменяет минимальное количество файлов(что отдаляет этот даунгрейд от настоящей дисковой версии), но при этом не содержит ни даунгрейд радио, ни способа даунгрейда до версии 1.0.4.0.  Он включает в себя [ZolikaPatch](essential-modding/zolikapatch.md) и [IV Tweaker](../modloading/#iv-tweaker), а также имеет дополнительную поддержку портированной версии [FusionFix](essential-modding/fusionfix.md). Однако он совершенно не совместим с [Games for Windows - LIVE](../multiplayer/#games-for-windows-live), however.

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

[:material-page-first:Предыдущая страница <br>Второстепенная настройка</br>](additional-setup.md){ .md-button } [Следующая страница:material-page-last: <br>Зависимости для модов</br>](mod-dependencies.md){ .md-button .md-button--primary }