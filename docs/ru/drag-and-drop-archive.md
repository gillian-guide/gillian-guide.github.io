title: Готовый архив
description: Полностью готовая к игре сборка для лучшего опыта сюжетки GTA IV

# Готовый архив { data-search-exclude }

Готовый архив - это полностью готовая к игре сборка для лучшего опыта сюжетки GTA IV. Все, что нужно для установки, это просто забросить файлы в папку с игрой и сделать несколько дополнительных действий - отсюда и название.

!!! warning ""
    Убедитесь, что все предварительные требования выполнены и была проведена подготовка. Если вы пропустили один из шагов, у вас могут возникнуть проблемы с использованием этой сборки, и вы не получите поддержку.

    [:material-page-first:Вступление: Предварительные требования</br>](index.md/#_3){ .md-button } [:material-page-first:Подготовка</br>](preparation.md){ .md-button }

---

## Демонстрация

TBA

---

## Установка { data-search-exclude }

!!! warning "Архивы устарели!"
    Архивы в текущий момент является сильно устаревшими.

    Ожидайте обновление через несколько дней/недель!

!!! question "Какую версию ставить?"
    Следующий переключитель относится к версии игры - базовые различия между ними смотрите [здесь](../downgrading/downgrading-the-game.md/#версии-игры). Моды в обоих архивах в основном идентичны, но **1.0.8.0 включает больше изменений в роде Quality of Life взамен на некоторые исправления в FusionFix и удаляет Rockstar Games Launcher, в то время как 1.2.0.59 считается более стабильным.**

=== "1.2.0.59"
    Последний раз обновлено: **[09.03.2024](#_9)**

    !!! warning ""
        - **Эта сборка НЕ обеспечивает наилучшую производительность - цель, в первую очередь, создать лучший ванильный-плюс опыт игры.** Если вы только хотите лучшую производительность - начинайте моддинг вручную.
        - **Не ожидайте поддержки если устанавливаете моды за пределами [дополнительных модов](#_8) - скорее всего, вы ее не получите.**
        - Не пытайтесь установить эту версию на уже-даунгрейднутую игру.
        - Если используете Linux, пропустите шаги 3-6 и [примените параметры запуска вручную](additional-setup.md/#_2).

    1. [Скачайте архив](https://drive.google.com/file/d/1tMwlvFiTE1tNuq8C4v2MNoDVXlCbLfoY/view?usp=sharing).
    2. Распакуйте :material-zip-box:`1.2 archive.7z` в папку с игрой (та, в которой :material-file:`GTAIV.exe`).
    3. Запустите :material-file-download:`GTAIVSetupUtilityWPF.exe`. Вам возможно потребуется установить [.NET 6 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-6.0.32-windows-x64-installer).
    4. Нажмите `Open`, выберите ту же папку с игрой.
    5. Нажмите `Install DXVK`, после чего `Setup launch options`. Не трогайте переключатели, если не знаете что делаете.
    6. После нажатия `Setup launch options` и `ОК` параметры запуска будут у вас в буфере обмена, поэтому сделайте одно из следующих действий:
        - **:material-steam: Steam**: Нажмите правой кнопкой мыши на игре в библиотеке, нажмите `Свойства...` и вставьте содержимое в поле `Параметры запуска`.
        - **:simple-rockstargames: Rockstar Games Launcher**: Откройте страницу с игрой в библиотеке, откройте настройки и вставьте содержимое в поле `Параметры запуска`.
        - **Что-то другое**: Нажмите правой кнопкой мыши по ярлыку, нажмите `Свойства` и вставьте содержимое в конец поля `Цель`.
    6. Вы готовы к игре!
        - Запускайте игру через :material-steam: Steam, :simple-rockstargames: Rockstar Games Launcher или `PlayGTAIV.exe`.
        - **Если используете Linux**, добавьте `WINEDLLOVERRIDES="dinput8=n,b" %command%` к параметрам запуска.
        - Предпочтительнее начинать **новую игру**. Существующие файлы сохранения могут работать, но могут возникнуть проблемы.
        - Если вы хотите **больше модов, просмотрите [дополнительные моды](#_8)**.

    !!! info "Обновление"
        Если вы обновляете сборку, сначала удалите папку :material-folder: ==update== и удалите все :material-file:`.asi` файлы (но не трогайте остальные) из папки :material-folder: ==plugins==.
=== "1.0.8.0"
    Последний раз обновлено: **[21.05.2024](#_9)**

    !!! warning ""
        - **Эта сборка НЕ обеспечивает наилучшую производительность - цель, в первую очередь, создать лучший ванильный-плюс опыт игры.** Если вы только хотите лучшую производительность - начинайте моддинг вручную.
        - **Не ожидайте поддержки если устанавливаете моды за пределами [дополнительных модов](#_8) - скорее всего, вы ее не получите.**
        - Не выполняйте даунгрейд самостоятельно. В архив уже входит даунгрейдер.
        - Если используете Linux, пропустите шаги 3-5 и [примените параметры запуска вручную](additional-setup.md/#_2).

    1. [Скачайте архив](https://www.mediafire.com/file/cx6dct4npfqtc5z/1.0_archive.7z/file).
    2. Распакуйте :material-zip-box:`1.0 archive.7z` в папку с игрой (та, в которой :material-file:`GTAIV.exe`).
    3. Запустите :material-file-download:`GTAIVSetupUtilityWPF.exe`. Вам возможно потребуется установить [.NET 6 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-6.0.32-windows-x64-installer).
    4. Нажмите `Open`, выберите ту же папку с игрой.
    5. Нажмите `Install DXVK`, после чего `Setup launch options`. Не трогайте переключатели, если не знаете что делаете.
    6. Вы готовы к игре!
        - Запускайте игру через :material-steam: Steam или `PlayGTAIV.exe`.
        - **Если используете :simple-rockstargames: Rockstar Games Launcher**, не запускайте игру через лаунчер и удалите :material-file:`SteamAchievements.asi`.
        - **Если используете Linux**, просмотрите [Заставляем ScriptHookDotNet и IV-SDK .NET работать на Linux](../resources/mod-dependencies.md/#_5) (или удалите файлы и папки начинающиеся на `IVSDKDotNet`).
        - Предпочтительнее начинать **новую игру**. Существующие файлы сохранения могут работать, но могут возникнуть проблемы. Также, если вы уже начали играть на 1.2.0.59, вам потребуется сделать [даунгрейд сохранения](../downgrading/downgrading-the-game.md/#_4)
        - Если вы хотите **больше модов, просмотрите [дополнительные моды](#_8)**.

    !!! info "Обновление"
        Если вы обновляете сборку, сначала удалите папки :material-folder: ==update== и :material-folder: ==modloader== (если есть) и удалите все :material-file:`.asi` файлы (но не трогайте остальные) из папки с игрой.

??? bug "Игра не запускается | Игра странно себя ведет | Игра случайно вылетает"
    Просмотрите [исправление проблем](../resources/troubleshooting.md).

    Отключайте моды по одному, чтобы найти виновника, удаляя папки/файлы :material-folder: ==update== или файлы :material-file:`.asi`.

    Сообщите о проблеме на [Discord сервере](../index.md/#_4).

---

## Навигация

<div class="grid cards" markdown>

- После установки архива, **примените оптимальные настройки графики**:

    [Следующая страница:material-page-last: <br>Второстепенная настройка: Оптимальные настройки графики</br>](additional-setup.md/#_4){ .md-button .md-button--primary }

- **Если используете Linux,** также примените параметры запуска вручную:

    [Следующая страница:material-page-last: <br>Второстепенная настройка: Параметры запуска</br>](additional-setup.md/#_3){ .md-button .md-button--primary }

</div>

---

## Список модов { data-search-exclude }

### Общие моды { data-search-exclude }

Все моды из следующего списка присутствуют в обоих архивах с идентичными версиями:

| Мод | Разработчик(и) | Детали |
| :-: | :------------: | :----: |
| [Radio Downgrader](http://downgraders.rockstarvision.com/) | Tomasak и другие | Простой даунгрейдер радио.<br>Использованный аддон: [Restored original TBoGT Menu Vocals](https://www.nexusmods.com/gta4/mods/234/?tab=files&category=archived).</br> |
| [FusionFix~2.5.6~](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/) | ThirteenAG, Fusion Team и другие | Самый главный мод: он включает в себя кучу исправлений, улучшений, новые настройки а также выступает в качестве модлоадера.<br>==Некоторые фиксы не присутствуют в версии для 1.0.8.0.==</br> |
| [Various Fixes~1.8.1~](https://gtaforums.com/topic/975211-various-fixes/) | Attramet и другие | Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
| [Trilogy Characters Fixes](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/) | TheYoshiPunch, (Japan) GTA Love и другие | Исправляет несоответствие персонажей в основной GTA IV и EFLC. |
| [Improved Animations Pack~1.3~](https://gtaforums.com/topic/958625-improved-animations-pack/) | B Dawg | Фиксы для некоторых проблем анимаций оружия, таких как задержка стрельбы. |
| [IV Fixes and Improvements](https://gtaforums.com/topic/909155-iv-fixes-improvements/) | Zolika1351 и другие | Сборник маленьких фиксов и улучшений - список на сайте.<br>Используются только старые улучшения из `.img` - и некоторые из них вырезаны из-за их существования в Various Fixes и других модах.</br> |
| [Фиксы для `carcols.dat` и `cargrp.dat`](https://drive.google.com/file/d/13OgDDm0xakbdRONPlrnN5zRfshdAgwhd/view?usp=sharing) | iiCriminnaaL | Несколько файлов из [Responsive Plus](https://gtaforums.com/topic/931069-iveflc-responsive-plus/) которые исправляют некоторые недочеты в оригинальных файлах, из-за которых некоторые автомобили не спавнятся так, как положено. |
| [Restored Pedestrians](https://gtaforums.com/topic/981864-restored-pedestrians/) | Attramet | Восстанавливает пешеходов, которые либо не использовались, либо присутствовали только в бетах. |
| [Various Pedestrians Actions](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Attramet | Добавляет, исправляет и завершает недоделанные действия для пешеходов. |
| [Restored Trees Position](https://gtaforums.com/topic/984591-restored-trees-position/) | Attramet | Восстанавливает деревья, которые присутствовали в бета-версиях, но были вырезаны в финальном релизе - либо случайно, либо из-за проблем с производительностью. |
| [More Visible Interiors](https://gtaforums.com/topic/974099-more-visible-interiors/) | Attramet | Делает интерьер более заметными снаружи, хотя имеет недостаток в виде появления интерьеров на глазах. |
| [Higher Resolution Miscellaneous Pack~1.1~](https://www.nexusmods.com/gta4/mods/357/) | Ash_735 | Улучшает качество текстур мелких объектов. |
| [Project Glass](https://discord.gg/gZvZmFt2p7) | DayL | Добавляет cubemap-отражения туда, где раньше было тупо прозрачное стекло. |
| [Vehicle Pack~2.0~](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736) | Ash_735 | Улучшает качество текстур всего транспорта в игре. Некоторые текстуры апскейлнуты, некоторые взяты из Max Payne 3 и GTA V. |
| [Dodgy Doc - Higher Quality](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Улучшает текстуры мутного доктора в миссии TBA. |
| [High Quality Pigeons](https://www.gtainside.com/gta4/mods/166924-high-quality-pigeons/) | Supreme Dear Leader | Улучшает качество модели и текстур для голубей. |
| [Resized Blista Compact](https://www.gtainside.com/en/gta4/cars/188730-resized-blista-compact/) | Thundersmacker | Уменьшение размера Blista Compact для соответствия реальному аналогу (Honda CR-X).  |
| [Fixed LCPD Buffalo](https://www.gtainside.com/en/gta4/cars/181342-fixed-lcpd-buffalo/) | Ooboy | Исправление модели и текстур полицейского Buffalo. |
| [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | B Dawg | Исправляет зеленоватые текстуры на некоторых моделях персонажей. |
| [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | _ys | Исправление некорректного костюма в Perseus, т.к. вы покупаете костюм, отличный от отображаемого. |
| [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | B Dawg | Исправление голосовых линий байкеров из IV в EFLC. |
| [Default Pistol Iron Sight Fix](https://www.nexusmods.com/gta4/mods/15) | grasscid | Исправляет ошибку в модели пистолета, где прицел не имеет смысла. |
| [Liberty Ferry Terminal - Waiting Room Sign Fix](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Исправление сломанной UV-карты на текстуре знака "Waiting Room". |
| [Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Редактирует UV-карту знака, чтобы включить в его неиспользуемую текстуру. |
| [Luis' Helmet Reflections Fix](https://www.gtainside.com/en/gta4/skins/125863-luis-s-helmet-reflections-fix/) | 6135 | Исправляет мрачное отражение на шлеме модели игрока в TBoGT. |
| [Luis' Bag Texture Fix](https://www.gtainside.com/en/gta4/skins/136118-luis-s-bag-texture-fix/) | 6135 | Добавляет недостающие карты нормалей и спекуляций и улучшает качество текстур на сумке модели игрока в TBoGT. |
| [Johnny's Shoe Texture Fix](https://www.gtainside.com/en/gta4/skins/125196-johnny-s-shoe-texture-fix/) | 6135 | Добавляет недостающие карты нормалей и спекуляций в обувь модели игрока в TLAD. |
| [Reduced Traffic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | GladiTek | Измените уровень шума транспорта в Algonquinе, чтобы он соответствовал реальному уровню, который можно обычно услышать на Times Square. |
| [Menu Art Fix](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072165611) | _ys | Исправляет фоны с низким разрешением в меню EFLC и удаляет текст Social Club. |
| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871) | Ash_735 | Повышает качество иконок радио на интерфейсе, так как они сильно не соответствуют другим частям интерфейса. |

### Раздельные моды { data-search-exclude }

Моды или их конкретные версии в следующем списке присутствуют только в одном из архивов из-за несовместимости с другой версией.

=== "1.2.0.59"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Console Visuals~1.6~](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | nastyyaboi и другие | Сборник портированных ассетов с консольной версии. <br>В архив включены только Fusion Console Vegetation, Console Peds и Console Select Menu. Просмотрите [дополнительные моды](#_8) для других аддонов.</br> |
    | [Project2DFX](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv) | ThirteenAG | Улучшает огни в далеке ночью. <br>==Можно отключить, удалив файлы `IVLodLights` из папки :material-folder: `plugins`==</br> |
    | [Xbox Rain Droplets](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Добавляет на экран красивые капельки воды. </br>==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets` из папки :material-folder: `plugins`.==</br> |
=== "1.0.8.0"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | Даунгрейд до 1.0.8.0 | Gillian (файлы пренадлежат Rockstar) |  A simple downgrade to 1.0.8.0 without replacing too many files. |
    | [ZolikaPatch IV~7.65~](https://zolika1351.pages.dev/mods/ivpatch) | Zolika1351 | Добавляет множество мелких исправлений исключительно для 1.0.8.0. |
    | [Console Visuals~1.6~](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | nastyyaboi и другие | Сборник портированных ассетов с консольной версии. <br>В архив включены только Fusion Console Vegetation и Console Peds. Просмотрите Просмотрите [дополнительные моды](#_8) для других аддонов.</br> |
    | [Liberty Tweaks~1.4.1~](https://gtaforums.com/topic/991160-liberty-tweaks/) | catsmackaroo, ItsClockAndre и другие | Мод, нацелений на улучшение различных аспектов игры и ее общий Quality of Life. Много настроек.<br>==Позволяет быстро сохраняться на ++f9++ и имеет множество геймплейных фич - если вам не нравятся настройки по умолчанию, вы можете изенить все на свой вкус в файле :material-file-cog:`LibertyTweaks.ini` который находится в :material-folder: `IVSDKDotNet\scripts\`==</br> |
    | [Project Thunder](https://gtaforums.com/topic/982902-project-thunder/) | ItsClockAndre | Улучшает грозу, с улучшениями к освещению и атмосфере. Много настроек. |
    | [VAmbience](https://gtaforums.com/topic/981402-vambience/) | ItsClockAndre | Добавляет в игру фоновый шум, например, езда автомобилей в дали или стрельба, как в GTA V. Много настроек. |
    | [Xbox Rain Droplets](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Добавляет на экран красивые капельки воды. </br>==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.==</br> |
    | [Steam Achievements~v2~](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/) | Zolika1351 | Позволяет получать достижения в :material-steam: Steam на старых патчах. |

---

## Дополнительные моды { data-search-exclude }

Эти моды не включены по умолчанию, но их легко установить поверх архива. Любые другие моды, не упомянутые в этом списке, не поддерживаются.

=== "1.2.0.59"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Аддоны Console Visuals](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo и другие | Сборник портированных ассетов с консольной версии. <br>Установка: Распакуйте желаемые части в папку с игрой.</br> |
    [Enhanced Snow Mod Repack](https://drive.google.com/file/d/11PFXrFnvB8JEKVajseL2GIWRd6MdLBBy/view?usp=drive_link) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_, Lover of Winter, Straysify, gdanbo, Attramet и Gillian | [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Realistic Winter Trees](https://www.gtainside.com/en/gta4/mods/177373-realistic-winter-trees/), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) и [Beta Winter Pedestrians](https://gtaforums.com/topic/987173-beta-winter-pedestrians/) собранные для Fusion Overloader с личными твиками. <br>Установка: Создайте бэкап папки :material-folder: ==update==. Распакуйте папку :material-folder: ==update== из архива в папку с игрой, заменяя файлы если нужен. Отключите/удалите `GTATrees.img` от FusionFix и `FusionConsolevegetation.img` от Console Visuals. Поставьте Screen Filter на `TBoGT`. Не играйте в DLC.</br> |
    | [UHD Vanilla Map and Radar](https://nexusmods.com/gta4/mods/456) | Valentyn_L | Карта высокого разрешения для мониторов с разрешением 1440p и 4K (на мониторах с разрешением 1080p и ниже карта может выглядеть хуже). <br>Установка: Распакуйте архив в папку с игрой.</br> |
    | [Aura](https://gtaforums.com/topic/989259-aura/) | catsmackaroo, nastyyaboi, ItsClockAndre и cubabori | Графический мод, построенный на ванильном визуале.<br>Installation: Установка: Распакуйте архив в папку :material-folder: ==update==.</br> |
    | [Improved Vanilla Timecyc](https://www.gtainside.com/gta4/mods/189357-improved-vanilla-timecyc-v1-1/) | pidarasnahui516 | Еще один timecyc мод, построенный на ванильном визуале. <br>Установка: Распакуйте папку :material-folder: ==Main Files\\pc\\== из архива в папку :material-folder: ==update==.</br> |
=== "1.0.8.0"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Официальный руссификатор (текст)](https://drive.google.com/file/d/1GbOA3CBAQGgXW6SjODzd8G8Cj-a8G6dt/view?usp=drive_link) | 1C SoftClub | Установка: Распакуйте папку :material-folder: ==update== в папку с игрой, в `Settings` - `Display` - `Language` смените язык на `Русский`. |
    | Настройки Liberty Tweaks | catsmackaroo, ItsClockAndre и другие | Features many options that severely change the gameplay - if you're not a fan of the defaults, you can modify things to your taste in :material-file-cog:`LibertyTweaks.ini` located in :material-folder: ==IVSDKDotNet\scripts\\==. |
    | [Аддоны Console Visuals](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo и другие | Сборник портированных ассетов с консольной версии. <br>Установка: Распакуйте желаемые части в папку с игрой.</br> |
    | [Snow Mod](https://github.com/akifle47/Snow/releases/latest) | AssaultKifle47 | Маленький мод на снег построенный на шейдерах, а не на текстурах. |
    | [Аддоны для Snow Mod](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_, Lover of Winter, Straysify, gdanbo, Attramet и Gillian | [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Realistic Winter Trees](https://www.gtainside.com/en/gta4/mods/177373-realistic-winter-trees/), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) and [Beta Winter Pedestrians](https://gtaforums.com/topic/987173-beta-winter-pedestrians/) собраны в ввиде аддонов для Snow Mod от AssaultKifle47.<br>Установка: Создайте бэкап папки :material-folder: ==update==. Распакуйте папку :material-folder: ==update== из архива в папку с игрой, заменяя файлы если нужен. Отключите/удалите `GTATrees.img` от FusionFix и `FusionConsolevegetation.img` от Console Visuals. Поставьте Screen Filter на `TBoGT`. Не играйте в DLC.</br> |
    | [UHD Vanilla Map and Radar](https://nexusmods.com/gta4/mods/456) | Valentyn_L | Карта высокого разрешения для мониторов с разрешением 1440p и 4K (на мониторах с разрешением 1080p и ниже карта может выглядеть хуже). <br>Установка: Распакуйте архив в папку с игрой.</br> |
    | [Aura](https://gtaforums.com/topic/989259-aura/) | catsmackaroo, nastyyaboi, ItsClockAndre и cubabori | Графический мод, построенный на ванильном визуале.<br>Installation: Установка: Распакуйте архив в папку :material-folder: ==update==.</br> |
    | [Improved Vanilla Timecyc](https://www.gtainside.com/gta4/mods/189357-improved-vanilla-timecyc-v1-1/) | pidarasnahui516 | Еще один timecyc мод, построенный на ванильном визуале. <br>Установка: Распакуйте папку :material-folder: ==Main Files\\pc\\== из архива в папку :material-folder: ==update==.</br> |
    | [IV-Presence](https://gtaforums.com/topic/975850-iv-presence/) | ItsClockAndre | Добавляет Discord Rich Presence (кастомный статус активности).<br>Installation: Откройте архив, в нем откройте папку material-folder: ==For GTA IV 1070 and 1080== и распакуйте файлы :fontawesome-solid-gears:`discord-rpc.dll` и :material-file:`IVPresence.asi` в папку с игрой. Если возникли проблемы, также распакуйте :material-file:`IVPresenceDependenciesChecker.exe` с его конфигом, запустите его и вы увидите, каких зависимостей вам не хватает.</br> |

---

## Список изменений { data-search-exclude }

=== "1.2.0.59"
    !!! info "Последняя версия"
        - 09.03.2024:
            - Обновлены More Visible Interiors, Xbox Rain Droplets.
            - *Наконец-то* исправлен Three Leaf Clover.
    ??? quote "Старые изменения"
        - 07.03.2024:
            - Обновлены FusionFix, Console Visuals, Higher Resolution Misc Pack.
        - 28.01.2024:
            - Обновлен FusionFix.
        - 14.01.2024:
            - Обновлен FusionFix.
        - 13.01.2024:
            - Обновлен FusionFix.
            - Исправлены проблемы с анимациями оружия.
            - Исправлены сломанные шляпы в IV.
            - Удалено больше дупликатов из Minor Mods.
        - 04.01.2024:
            - Обновлены Radio Downgrader, FusionFix, Project2DFX, Xbox Rain Droplets, Various Fixes, More Visible Interiors, Restored Trees Position.
            - Перепакованы большинство модов - должно исправить больше проблем и больше несотвествий.
            - Удален Improved Weapon Spec в пользу Higher Resolution Miscellaneous Pack.
            - Добавлен Restored Pedestrians, Various Pedestrians Actions.
        - 18.12.2023:
            - Обновлен FusionFix.
            - Удален Vanilla Road Texture Enhancement от DayL.
            - Удален Xbox One/Series S+X Buttons (в пользу FusionFix).
        - 12.12.2023 (хотфикс):
            - Исправлен краш в TBoGT при загрузке.
                - Ручной фикс: добавьте `DISABLE_FILE common:/data/newchar.ide` в :material-folder: ==/update/TBoGT/:material-file:`content.dat`==
        - 10.12.2023:
            - Обновлен FusionFix.
            - Исправлен пропавший NPC в миссии Three Leaf Clover.
        - 27.11.2023:
            - Обновлены FusionFix, Various Fixes и Console Visuals.
        - 01.11.2023:
            - Обновлен FusionFix.
            - Добавлен Higher Resolution Miscellaneous Pack.
            - Удалены несколько аддонов Console Visuals перемещены в дополнительные моды.
        - 21.09.2023:
            - Обновлен Various Fixes
            - Setup Utility заменен на переделанный.
        - 15.09.2023:
            - Обновлены FusionFix, Radio Downgrader (очень урезает размер архива), Setup Utility.
            - Добавлен IV Bikers in Episodes voice sets fix.
        - 08.09.2023:
            - Обновлен Various Fixes
            - Добавлены пропавшие файлы которые пропали из неизвестных причин.
        - 07.09.2023:
            - Обновлен FusionFix.
            - Добавлены Reduced Traffic Screech и High Quality Pigeons.
        - 06.09.2023:
            - Обновлены FusionFix - с ним, Shader Fixes.
            - Включен Setup Utility.
            - Удален Traffic Cops in the Toolbooths - FusionFix теперь включает его.
            - Удален DXVK, вы теперь можете автоматически установить его используя :material-file-download:`GTAIVSetupUtility.exe`.
        - 28.08.2023:
            - Исправлен Dodgy Doc HQ мод - теперь используется.
            - Добавлен `dxvk.gplAsyncCache = true` к :material-file-cog:`dxvk.conf`.
        - 26.08.2023:
            - Обновлен Project Glass.
            - Добавлены фиксы от коммьюнити к Various Fixes.
            - Возвращены более новые файлы от Shader Fixes files, так как я их случайно заменил в предудыщем обновлении.
        - 22.08.2023:
            - Обновлены FusionFix, Xbox One/Series S+X Buttons.
            - Добавлен Menu Art Fix.
        - 18.08.2023:
            - Обновлен Various Fixesfiles.
            - Исправлена проблема с моделью клабхауса Angels of Death в TLAD.
        - 17.08.2023:
            - Обновлен Project Glass.
            - Добавлен More Visible Interiors.
            - Слегка изменены конфиги.
        - 12.08.2023:
            - Исправлены известные краши и софтлоки в TLAD и TBoGT.
            - Ввостановлена фоновая музыка в меню TBoGT.
        - 11.08.2023:
            - Обновлен Shader Fixes (вручную собран).
            - Слегка изменен бюджет транспорта.
            - Изменен файл волос Нико дабы исправить визуальные проблемы.
        - 10.08.2023:
            - Обновлен Project Glass.
        - 07.08.2023:
            - Обновлен FusionFix.
        - 03.08.2023:
            - Добавлен Restored Trees Position.
        - 02.08.2023:
            - Обновлены FusionFix, Trilogy Characters Fixes, Console Visuals.
        - 25.07.2023:
            - Обновлен Fix Collection.
            - Маленькие изменения в .ini.
        - 23.07.2023:
            - Добавлены Road Texture Enhancement, Project Glass(+lighthing for bus stops), Dodgy Doc - Higher Quality, Rescaled Blista Compact, Player Outfit Texture Fixes, LCPD Buffalo Fix, Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Fixed Suit Display и взято паро фиксов из Responsive Plus.
            - Исправлен приоритет для модов.
            - Перепакованы моды чтобы уменьшить количество папок.
        - 20.07.2023:
            - Обновлен FusionFix.
            - Изменен dxvk на dxvk-gplasync.
        - 19.07.2023:
            - Обновлен FusionFix и Shader Fixes.
            - Добавлены Radio Downgrader, GTA Online QUB3D Background, Traffic Cops in the Toolbooths, Xbox Rain Droplets, Fixed Pistol Sights.
            - Добавлен Dualsense buttons to optionals.
            - Удалены Pedestrians with Unused Clothing Restored и Varied Alderney State Trooper Ped из-за возможных несовместимостей.
        - 13.07.2023:
            - Исправлены пропадающие ассеты в офисе Романа.
            - Изменен лимит FPS в катсценах на 32.
        - 12.07.2023:
            - Добавлены (новый) IV Fixes и Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec.
            - Удален TBoGT Texture Quality Fix т.к. Various Fixes уже содержит этот фикс.
        - 10.07.2023:
            - Изменен файл волос Нико, теперь нет визуальных проблем.
        - 09.07.2023:
            - Удален IV Fixes и Improvements.
            - Добавлен Various Fixes.
        - 08.07.2023:
            - Обновлены FusionFix, Shader Fixes.
            - Изменен конфиг DXVK.
            - Удален dxgi.dll.
            - Некоторые моды перепакованы.
        - 02.07.2023:
            - Перепакованы моды в более удобный формат.
        - 01.07.2023:
            - Обновлен Shader Fixes.
            - Перепакованые некоторые моды для Fusion Overloader.
        - 30.06.2023:
            - Обновлены моды.
        - 27.06.2023:
            - Обновлены моды.
        - 26.06.2023:
            - Архив создан.
=== "1.0.8.0"
    !!! info "Последняя версия"
        - 21.05.2024:
            - Перезалив архива на Mediafire ибо гугл заебет.
            - Обновлены IVSDKDotNet и Liberty Tweaks (также немного перенастроены).
    ??? quote "Старые изменения"
        - 09.03.2024:
            - Обновлены More Visible Interiors, Liberty Tweaks (исправлен краш при использовании транспорта).
            - Удален Project2DFX из-за поломки дальних огней на 1.0.8.0.
            - *Наконец-то* исправлен Three Leaf Clover.
            - Исправлена проблема невозможности запуска игры.
        - 07.03.2024:
            - Обновлены FusionFix, Liberty Tweaks, Console Visuals, Higher Resolution Misc Pack.
        - 28.01.2024:
            - Обновлен FusionFix.
        - 14.01.2024:
            - Обновлен FusionFix.
        - 13.01.2024:
            - Обновлен FusionFix.
            - Исправлены проблемы с анимациями оружия.
            - Исправлены сломанные шляпы в IV.
            - Удалено больше дупликатов из Minor Mods.
            - Отключены проблематичные настройки в ZolikaPatch.
        - 04.01.2024:
            - Обновлены Radio Downgrader, FusionFix, Various Fixes, More Visible Interiors, Restored Trees Position, Restored Pedestrians, Various Pedestrians Actions.
            - Перепакованы большинство модов - должно исправить больше проблем и больше несотвествий.
            - Убран IV Tweaker в пользу Fusion Overloader - одним меньше инжектором, лучше стабильность.
            - Удален Improved Weapon Spec в пользу Higher Resolution Miscellaneous Pack.
        - 22.12.2023:
            - Обновлены IVSDK .NET, Clonk's Coding Library и Liberty Tweaks. Должно улучшить стабильность и исправить некоторые проблемы с Liberty Tweaks.
        - 18.12.2023:
            - Обновлен FusionFix.
            - Отключен Vanilla Road Texture Enhancement от DayL.
            - Удалены Dualshock, Dualsense и Xbox One/Series S+X Buttons в пользу FusionFix.
        - 12.12.2023:
            - Повторная попытка исправить Three Leaf Clover issues. Не хотфикс, т.к. не хватало файлов.
        - 10.12.2023:
            - Обновлен FusionFix.
            - Исправлен пропавший NPC в миссии Three Leaf Clover.
        - 27.11.2023:
            - Обновлены FusionFix, Various Fixes и Console Visuals.
        - 03.11.2023:
            - Исправлена проблема с даунгрейдом.
            - Исправлена неправильное название папки.
            - Отключены несовместимые и ненужные настройки в :material-file-cog:`ZolikaPatch.ini`.
        - 01.11.2023:
            - Обновлен FusionFix.
            - Добавлен Higher Resolution Miscellaneous Pack.
            - Удалены некоторые аддоны Console Visuals, перемещены в дополнительные моды.
            - Удален Extra Options из-за несовместимостью с FusionFix 2.0.
        - 04.10.2023 (hotfix):
            - Исправлена проблема с даунгрейдингом которая ломала настройки.
        - 27.09.2023:
            - Обновлены Setup Utility, ZolikaPatch, IV Tweaker, Liberty Tweaks.
            - Добавлен Extra Options.
        - 21.09.2023:
            - Обновлен Various Fixes.
            - Заменен Setup Utility на новый.
        - 16.09.2023 (hotfix):
            - Удален :material-file:`IVMenuAPI.asi` который появился случайно.
        - 15.09.2023:
            - Обновлены FusionFix, ZolikaPatch, IV Tweaker, IV Fixes and Improvements, Liberty Tweaks, Radio Downgrader (очень уменьшает размер архива), Setup Utility.
            - Добавлен IV Bikers in Episodes voice sets fix.
        - 08.09.2023:
            - Обновлен Various Fixes (должно исправить поврежденные сохранения).
            - Добавлен VAmbience.
        - 07.09.2023:
            - Обновлен FusionFix.
            - Добавлены Reduced Traffic Screech и High Quality Pigeons.
        - 06.09.2023:
            - Обновлены ZolikaPatch, FusionFix.
            - Включен Setup Utility.
            - Удален Traffic Cops in the Toolbooths - FusionFix теперь включает его.
            - Удалены DXVK и commandline.txt, вы теперь можете установить их автоматически используя :material-file-download:`GTAIVSetupUtility.exe`.
        - 28.08.2023:
            - Исправлена бесконечная загрузка на миссии Three Leaf Clover (нужно решение получше - на данный момент, в катсцене отсутсвует одна модель NPC из-за этого).
            - Исправлен мод Dodgy Doc HQ что-бы он по настоящему использовался.
            - Добавлен `dxvk.gplAsyncCache = true` в :material-file-cog:`dxvk.conf`.
            - Удален Better Wardrobes.
        - 26.08.2023:
            - Обновлены FusionFix, Project Glass, Xbox One/Series S+X Buttons.
            - Добавлен Menu Art Fix.
            - Перепакован Various Fixes, а также добавлены фиксы от коммьюнити.
        - 18.08.2023:
            - Обновлен Various Fixes
            - Исправлена проблема с моделью клабхауса Angels of Death в TLAD.
        - 17.08.2023:
            - Обновлен Project Glass.
            - Добавлен More Visible Interiors.
            - Немного изменены конфиги.
        - 12.08.2023:
            - Исправлен известные краши и софтлоки в TLAD и TBoGT.
            - Ввостановлена фоновая музыка в меню TBoGT.
        - 11.08.2023:
            - Обновлены FusionFix, Shader Fixes (вручную собран).
            - Исправлены краши (IV Tweaker из обновленного даунгрейдера не был обновленным).
            - Слегка изменен бюджет транспорта.
            - Изменен файл волос Нико для исправления визуальных проблем.
        - 10.08.2023:
            - Обновлены даунгрейдер, ZolikaPatch и Project Glass.
        - 07.08.2023:
            - Обновлен FusionFix.
        - 03.08.2023:
            - Обновлен Console Visuals.
            - Добавлен Restored Trees Position.
            - Перемещены некоторые файлы во избежание несовместимостей.
        - 02.08.2023:
            - Обновлены FusionFix, Trilogy Characters Fixes - также слегка перепакованы.
        - 25.07.2023:
            - Обновлен Fix Collection.
            - Добавлен Project Thunder, Restored Pedestrians, Various Pedestrian Actions.
            - Мелкие изменения .ini.
        - 24.07.2023:
            - Перепакованы моды для уменьшения количества папок.
            - Добавлены Road Texture Enhancement, Project Glass(+lighthing for bus stops), Dodgy Doc - Higher Quality, Rescaled Blista Compact, Player Outfit Texture Fixes, LCPD Buffalo Fix, Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Fixed Suit Display и взято пару фиксов из Responsive Plus (далее: Fix Collection).
        - 20.07.2023:
            - Обновлен FusionFix.
            - Изменен dxvk на dxvk-gplasync.
        - 19.07.2023:
            - Обновлены даунгрейдер, ZolikaPatch, IV Tweaker, FusionFix, Shader Fixes.
            - Добавлен Radio Downgrader, GTA Online QUB3D Background, Better Wardrobes, Traffic Cops in the Toolbooths, Xbox Rain Droplets, Fixed Pistol Sights.
            - Добавлены кнопки для Dualsense в дополнительные моды.
            - Удалены Pedestrians with Unused Clothing Restored и Varied Alderney State Trooper Ped из-за возможный несовместимостей.
        - 15.07.2023:
            - Добавлен Liberty Tweaks.
        - 13.07.2023:
            - Исправлены пропадающие ассеты в офисе Романа.
            - Изменен лимит FPS в катсценах на 32.
        - 12.07.2023:
            - Обновлен ZolikaPatch.
            - Добавлены (новый) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos, Improved Weapon Spec.
            - Various Fixes перемещен в папку update из-за возможных несовместимостей.
            - Удален TBoGT Texture Quality Fix т.к. Various Fixes уже содержит этот фикс.
            - Удален TBoGT Vehicle Fix из modloader т.к. FusionFix уже содержит этот фикс.
            - Удален IVPresence.
        - 11.07.2023:
            - Исправлена проблема с крашем основной игры.
        - 10.07.2023:
            - Обновлен даунгрейдер.
            - Добавлен порт FusionFix 1.60 от Zolika.
            - Исправлен краш в TLAD, изменен файл волос Нико, теперь не имеет визуальных проблем.
        - 09.07.2023:
            - Изменен даунгрейдер - теперь входит в архив.
            - Удален IV Fixes and Improvements.
            - Добавлен Various Fixes.
            - Добавлены кнопки Dualshock в дополнительные моды.
        - 08.07.2023:
            - Обновлен Shader Fixes.
            - Удален Simple Traffic Loader.
            - Моды полностью перепакованы для использования модлоадера.
        - 01.07.2023:
            - Обновлен Shader Fixes.
            - Перепакованы некоторые моды.
        - 30.06.2023:
            - Обновлен Shader Fixes.
        - 26.06.2023:
            - Архив создан.