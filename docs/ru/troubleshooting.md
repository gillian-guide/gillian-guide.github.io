title: Исправление проблем
description: Исправление проблем с вашей установкой GTA IV.

# Исправление проблем
У любого человека могут возникнуть проблемы с моддингом любимых игр, и GTA IV очень подвержена этому.

???+ info "Известные проблемы без решения"
    Я знаю про эти проблемы, не нужно про их мне сообщать - только если у вас есть решение.

    - После того, как вы напиваетесь, освещение в течение некоторого времени мерцает.
    - Если во время катсцены игра в свёрнутом режиме находится слишком долго, игра намертво зависает.
    - Звуки двигателя автомобиля периодически появляются и исчезают (решение проблемы - вернуть баг с такси - уменьшите TrafficBudget в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`).
    - Поездки на такси иногда приводят к вылету игры на 1.0.8.0.
    - Зависимости .NET не работают в Linux.

??? info "Я использую Rockstar Games Launcher и мои файлы постоянно пропадают"
    После даунгрейда или использования готового архива для 1.0.8.0 избегайте использования лаунчера и запускайте игру только с помощью :material-file:`PlayGTAIV.exe`.

    Если же вы хотите использовать CE, избегайте замены файлов.

??? info "Игра не запускается в нужном разрешении и нет возможности увеличить его в настройках"
    После установки [DXVK](optimization.md), установите эти [параметры запуска](../additional-setup/#_2):

    * `-width (горизонтальное разрешение)`
    * `-height (вертикальное разрешение)`
    * `-refreshrate (частота обновления)`

    К примеру:

    * `-width 1920`
    * `-height 1080`
    * `-refreshrate 60`

    Если проблема все ещё присутствует, добавьте `d3d9.forceAspectRatio = 16:9` (или ваше соотношение сторон) в :material-file-cog:`dxvk.conf`.

    Также проверьте наличие [обновлений драйверов видеокарты](../optimization/#_2).

??? info "Производительность никак не улучшилась"
    Убедитесь, что [DXVK](optimization.md) установлен правильно, и что используются [оптимальные настройки графики](../additional-setup/#_3). Не забудьте отключить кэш шейдеров в :material-steam:Steam в `Настройки` - `Загрузки` при использовании DXVK.

    Убедитесь, что не используются никакие оверлеи по типу Rainmeter в полноэкранном режиме, они могут очень плохо повлиять на производительность.

    Попробуйте понизить настройки графики, а именно:

    - SSAA 2x
    - Shadow Filter (PCSS)
    - Качество теней
    - Улучшенные ночные тени
    - Depth of Field
    - Distant Blur
    - Motion Blur
    - Дистанция обзора/глубина детализации
    - Разрешение отражений
    - Console Shadows

??? info "На последней миссии не получается попасть в вертолёт | Другие проблемы с таймингом при высоком FPS, например аркады"
    Установите [FusionFix](essential-modding/fusionfix.md). Некоторые проблемы решаются только ограничением FPS до 60 в `Настройки` - `Графика`.

??? info "Невозможно пройти TLAD - Женское влияние (Shifting Weight)"
    Откройте :material-file-cog:`ZolikaPatch.ini` и измените `HighFPSSpeedupFix` на `0`. После миссии можете изменить обратно на `1`.

??? info "Игра сразу загружается в сохранение при запуске, нету меню"
    Для вызова меню можно удерживать ++lshift++ при загрузке.

    Если вы хотите полностью отключить функцию, откройте :material-file-cog:`GTAIV.EFLC.FusionFix.ini` и измените `SkipMenu` на `0` (или перейдите в Настройки - Игра и переключите `Skip Menu` на Откл). Если проблема осталась, откройте :material-file-cog:`ZolikaPatch.ini` и измените эту же настройку там.

??? info "Не могу использовать компьютеры в интернет-кафе или взаимодействовать с развлекательными заведениями (бильярд, боулинг)"
    Вы можете сделать одно из следующих действий:

    * Начать новую игру и забыть про существующее сохранение.
    * Удалить файлы `LibertyTweaks` из :material-folder:==IVSDKDotNet\scripts== (если вы не используете `IVSDKDotNet` для других модов, вы также можете удалить все файлы относящееся к ему из папки с игрой).

??? info "Загрузки слишком долгие"
    - Удалите ColAccel.
    - Уберите `-managed` из [параметров запуска](../additional-setup/#_2).

??? info "Игра бесконечно загружается при загрузке сохранений | Постоянно пропадают текстуры | Игра показывает неправильное значение VRAM в настройках"
    Установите [параметр запуска](../additional-setup/#_2) `-availablevidmem` (со значением не выше 3072.0).

??? info "Случайные, но постоянные проблемы с фреймтаймингом (например, микрофриз каждые 0,5 секунды)"
    Попробуйте отключить геймпад. Если проблема исчезнет, попробуйте включить оверлей в стиме. Если проблема по прежнему не исчезает, попробуйте включить Steam Input.

??? info "Asi Loader Error | Другие проблемы с Visual C++"
    Установите [библиотеки](index.md).

??? info "Пропали достижения в :material-steam:Steam после даунгрейдинга"
    Установите [SteamAchievements](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/).

??? info "Достижения в GFWL не работают"
    Удалите :material-file:`SteamAchivements.asi` - либо одно, либо другое.

    Также отключите `TryToSkipAllErrors` и `VSyncFix` в :material-file-cog:`ZolikaPatch.ini`

??? info "Ошибка RMN60 на запуске"
    Случается после даунгрейда. Установите [ZolikaPatch](essential-modding/zolikapatch.md).

??? info "Сломанные LOD'ы во время долгих игровых сессий"
    Уменьшите количество модов на текстур - особенно текстуры дорог и подобные текстуры, которые всегда подгружены.

??? info "Игра вылетает прямо при запуске | Даже не запускается"
    * Убедитесь, что у вас нету дублей модов - вы могли, например, оставить [FusionFix](essential-modding/fusionfix.md) и в :material-folder:==plugins==, и в папке с игрой. Игра в таком случае не запустится.
    * Запускайте игру только через :material-steam:Steam или :material-file:`PlayGTAIV.exe`.
    * Если вы используете ZolikaPatch и FusionFix вместе, смотрите несовместимые опции [здесь](essential-modding/fusionfix.md).
    * Перезагрузите ПК.
    * Если вы даунгрейдились до 1.0.4.0, удалите :material-file-cog:`settings.cfg` в :material-folder:==C:/Users/(Название ПК)/AppData/Local/Rockstar Games/GTA IV/Settings==.
    * Убедитесь, что у вас не запущен MSI Afterburner и/или RivaTuner Statistics и другой подобный софт - оверлеи мешают запуску игры.
    * Установите [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) (и настройте его на избавление от GFWL) и [ZolikaPatch](essential-modding/zolikapatch.md).
    * Если всё еще не получается - пробуйте по одному удалять/отключать моды и смотреть какой не работает.

??? info "Игра вылетает во время или после загрузки"
    * Убедитесь, что вы начали с чистой установки (после удаления в Steam, вручную удалите остатки в папке).
    * Поврежденный файл сохранения может быть проблемой, если перед даунгрейдом вы играли на более новой версии. Исправить можно, [сделав даунгрейд сохранения](../downgrading/#_5).
    * Если вы устанавливали моды, которые добавляют в список машин новые и сохранили их возле вашего дома, то ваше сохранение скорее всего повреждено. Сменить машину в сохранении можно, используя эту [программу](https://x3t-infinity.com/GTAIV_SE).
    * Если всё еще не получается - пробуйте по одному удалять/отключать моды и смотреть какой не работает.

??? info "Игра случайно вылетает во время игры"
    * Если вы используете ZolikaPatch и FusionFix вместе, смотрите несовместимые опции [здесь](essential-modding/fusionfix.md).
    * Один из ваших модов нестабилен. Не устанавливайте слишком много модов.

??? info "Игра использует неправильную видеокарту (ноутбук на NVIDIA)"
    Откройте NVIDIA Control Panel, Управление параметрами 3D, добавьте :material-file:`gtaiv.exe` и в `Режиме управления электропитанием` выберите `Предпочитетелен режим максимальной производительности`.

Если вы знаете проблему и решение, которые я упустил, [свяжитесь со мной!](contact-me.md)

[:material-page-first:Предыдущая страница <br>Пожертвования</br>](support.md){ .md-button } [Следующая страница:material-page-last: <br>Сервер в Discord</br>](contact-me.md){ .md-button .md-button--primary }