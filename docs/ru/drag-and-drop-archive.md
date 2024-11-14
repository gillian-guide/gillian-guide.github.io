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

!!! question "Какую версию ставить?"
    Следующий переключитель относится к версии игры - базовые различия между ними смотрите [здесь](../downgrading/downgrading-the-game.md/#версии-игры). Моды в обоих архивах в основном идентичны, но **1.0.8.0 включает больше изменений в роде Quality of Life взамен на некоторые исправления в FusionFix и удаляет Rockstar Games Launcher, в то время как 1.2.0.59 считается более стабильным.**

    Лично я предпочитаю для ванильного прохождения архив для 1.2.0.59, а для ванильного+ прохождения (может заново захотелось поиграть) - архив для 1.0.8.0.


=== "1.2.0.59"
    Последний раз обновлено: **[13.11.2024](#_9)**

    !!! warning ""
        - **Эта сборка НЕ обеспечивает наилучшую производительность - цель, в первую очередь, создать лучший ванильный-плюс опыт игры.** Если вы только хотите лучшую производительность - начинайте моддинг вручную.
        - **Не ожидайте поддержки если устанавливаете моды за пределами [дополнительных модов](#_8) - скорее всего, вы ее не получите.**
        - Не пытайтесь установить эту версию на уже-даунгрейднутую игру.
        - Если используете Linux, пропустите шаги 3-6 и [примените параметры запуска вручную](additional-setup.md/#_2).

    1. [Скачайте архив](https://www.mediafire.com/file/iqc4ynuegyxry9d/1.2_archive.7z/file) (3.73ГБ, SHA512: `1793ddf78569828124ba8f63a035997cd0b8079b57912fbb6def62c32322a67fb7af19faa7b8e4f86d342366c8176f0061c2427382714df5af4206be114d453a`).
    2. Распакуйте :material-zip-box:`1.2 archive.7z` в папку с игрой (та, в которой :material-file:`GTAIV.exe`).
    3. Запустите :material-file-download:`GTAIVSetupUtilityWPF.exe`. Вам возможно потребуется установить [.NET 6 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-6.0.32-windows-x64-installer).
    4. Нажмите `Open`, выберите ту же папку с игрой.
    5. Нажмите `Install DXVK`, после чего `Setup launch options`. Не трогайте переключатели, если не знаете что делаете.
    6. После нажатия `Setup launch options` и `ОК` параметры запуска будут у вас в буфере обмена, поэтому сделайте одно из следующих действий:
        - **:material-steam: Steam**: Нажмите правой кнопкой мыши на игре в библиотеке, нажмите `Свойства...` и вставьте содержимое в поле `Параметры запуска`.
        - **:simple-rockstargames: Rockstar Games Launcher**: Откройте страницу с игрой в библиотеке, откройте настройки и вставьте содержимое в поле `Параметры запуска`.
        - **Ярлык**: Нажмите правой кнопкой мыши по ярлыку, нажмите `Свойства` и вставьте содержимое в конец поля `Цель`.
    7. Вы готовы к игре!
        - Запускайте игру через :material-steam: Steam, :simple-rockstargames: Rockstar Games Launcher или `PlayGTAIV.exe`.
        - **Если используете Linux**, добавьте `WINEDLLOVERRIDES="dinput8=n,b" %command%` к параметрам запуска.
        - Предпочтительнее начинать **новую игру**. Существующие файлы сохранения могут работать, но могут возникнуть проблемы.
        - Выставьте настройку `Транспортный поток` на `100` для полноценного использования кастомного popcycle.
        - Если вы хотите **больше модов, просмотрите [дополнительные моды](#_8)**.

    !!! info "Обновление"
        Если вы обновляете сборку, сначала удалите папку :material-folder: ==update== и удалите все :material-file:`.asi` файлы (но не трогайте остальные) из папки :material-folder: ==plugins==.
=== "1.0.8.0"
    Последний раз обновлено: **[13.11.2024](#_9)**

    !!! warning ""
        - **Эта сборка НЕ обеспечивает наилучшую производительность - цель, в первую очередь, создать лучший ванильный-плюс опыт игры.** Если вы только хотите лучшую производительность - начинайте моддинг вручную.
        - **Не ожидайте поддержки если устанавливаете моды за пределами [дополнительных модов](#_8) - скорее всего, вы ее не получите.**
        - Не выполняйте даунгрейд самостоятельно. В архив уже входит даунгрейдер.
        - Если используете Linux, пропустите шаги 3-5 и [примените параметры запуска вручную](additional-setup.md/#_2).

    1. [Скачайте архив](https://www.mediafire.com/file/cx6dct4npfqtc5z/1.0_archive.7z/file) (3.81ГБ, SHA512: `2faa59e19881e504f4a96ba0d241fcd8fb229fff68a23fdb3ab4bff4f4364bc89d66a1eb5b7e0cfb130a46237f56cacadf890aa34275b710e502a6262188344d`).
    2. Распакуйте :material-zip-box:`1.0 archive.7z` в папку с игрой (та, в которой :material-file:`GTAIV.exe`).
    3. Запустите :material-file-download:`GTAIVSetupUtilityWPF.exe`. Вам возможно потребуется установить [.NET 6 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-6.0.32-windows-x64-installer).
    4. Нажмите `Open`, выберите ту же папку с игрой.
    5. Нажмите `Install DXVK`, после чего `Setup launch options`. Не трогайте переключатели, если не знаете что делаете.
    6. Вы готовы к игре!
        - Запускайте игру через :material-steam: Steam или `PlayGTAIV.exe`.
        - **Если используете :simple-rockstargames: Rockstar Games Launcher**, не запускайте игру через лаунчер и удалите :material-file:`SteamAchievements.asi`.
        - **Если используете Linux**, просмотрите [Заставляем ScriptHookDotNet и IV-SDK .NET работать на Linux](../resources/mod-dependencies.md/#_5) (или удалите файлы и папки начинающиеся на `IVSDKDotNet`).
        - Предпочтительнее начинать **новую игру**. Существующие файлы сохранения могут работать, но могут возникнуть проблемы. Также, если вы уже начали играть на 1.2.0.59, вам потребуется сделать [даунгрейд сохранения](../downgrading/downgrading-the-game.md/#_4).
        -  Выставьте настройку `Транспортный поток` на `100` для полноценного использования кастомного popcycle.
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

    [Следующая страница:material-page-last: <br>Второстепенная настройка: Оптимальные настройки графики</br>](additional-setup.md/#__tabbed_2_2){ .md-button .md-button--primary }

- **Если используете Linux,** также примените параметры запуска вручную:

    [Следующая страница:material-page-last: <br>Второстепенная настройка: Параметры запуска</br>](additional-setup.md/#_3){ .md-button .md-button--primary }

</div>

---

## Список модов { data-search-exclude }

### Общие моды { data-search-exclude }

Все моды из следующего списка присутствуют в обоих архивах с идентичными версиями:

| Мод | Разработчик(и) | Детали |
| :-: | :------------: | :----: |
| [Radio Downgrader~31.08.2024~](https://github.com/Tomasak/GTA-Downgraders/releases/iv-latest) | Tomasak и другие | Простой даунгрейдер радио.<br>Использованный аддон: [Restored original TBoGT Menu Vocals](https://www.nexusmods.com/gta4/mods/234/?tab=files&category=archived).</br> |
| [FusionFix~3.4.0~](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/) | ThirteenAG, Fusion Team и другие | Самый главный мод: он включает в себя кучу исправлений, улучшений, новые настройки а также выступает в качестве модлоадера.<br>==Некоторые фиксы не присутствуют в версии для 1.0.8.0.==</br> |
| [Various Fixes~2.0.2~](https://gtaforums.com/topic/975211-various-fixes/) | Attramet и другие | Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
| [Trilogy Characters Fixes~05.07.2024-custom~](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/) | TheYoshiPunch, (Japan) GTA Love и другие | Исправляет несоответствие персонажей в основной GTA IV и EFLC. |
| [Console Visuals~1.7~](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | nastyyaboi и другие | Сборник портированных ассетов с консольной версии. <br>Включенные аддоны: Console Fences, Console Animations, Console Peds. Просмотрите [дополнительные моды](#_8) для других аддонов.</br> |
| [Improved Animations Pack~28.06.2024~](https://gtaforums.com/topic/958625-improved-animations-pack/#comments) | B Dawg и C1aude_III | Исправляет разные проблемы с анимациями оружий. |
| [Restored Pedestrians~05.10.2024~](https://gtaforums.com/topic/981864-restored-pedestrians/) | Attramet | Восстанавливает пешеходов, которые либо не использовались, либо присутствовали только в бетах. |
| [Various Pedestrians Actions~04.11.2023~](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Attramet | Добавляет, исправляет и завершает недоделанные действия для пешеходов. |
| [Restored Trees Position~31.10.2023~](https://gtaforums.com/topic/984591-restored-trees-position/) | Attramet | Восстанавливает деревья, которые присутствовали в бета-версиях, но были вырезаны в финальном релизе - либо случайно, либо из-за проблем с производительностью. |
| [More Visible Interiors~29.02.2024~](https://gtaforums.com/topic/974099-more-visible-interiors/) | Attramet | Делает интерьер более заметными снаружи, хотя имеет недостаток в виде появления интерьеров на глазах. |
| [Higher Resolution Miscellaneous Pack~1.1~](https://www.nexusmods.com/gta4/mods/357/) | Ash_735 | Улучшает качество текстур мелких объектов. |
| [Project Glass~18.10.2024~](https://discord.gg/gZvZmFt2p7) | DayL | Добавляет cubemap-отражения туда, где раньше было тупо прозрачное стекло. |
| [Vehicle Pack~2.1~](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736) | Ash_735 | Улучшает качество текстур всего транспорта в игре. Некоторые текстуры апскейлнуты, некоторые взяты из Max Payne 3 и GTA V. |
| [Fidelity Popcycle~14.02.2024~](https://www.nexusmods.com/gta4/mods/405?tab=description) | Chunk | Замена popcycle в духе оригинала который делает жизнь в городе более разнообразным и реалистичным. |
| [Bullet Penetration - Minimal Edition](https://gtaforums.com/topic/989496-bullet-penetration/) | Internet Rob | Позволяет пулям пробивать стекла так, как с лобовыми стеклами. |
| [Project2DFX~28.06.2024~](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv) ([1.0.8.0](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest)) | ThirteenAG | Улучшает огни в далеке ночью. <br>==Можно отключить, удалив файлы `IVLodLights`.==</br> |
| [Xbox Rain Droplets~10.10.2024~](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Добавляет на экран красивые капельки воды. </br>==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.==</br> |
| [Dodgy Doc - Higher Quality](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Улучшает текстуры мутного доктора в миссии "Имейте сердце". |
| [High Quality Pigeons](https://www.gtainside.com/gta4/mods/166924-high-quality-pigeons/) | Supreme Dear Leader | Улучшает модель и качество текстуры голубей. |
| [Resized Blista Compact](https://www.gtainside.com/en/gta4/cars/188730-resized-blista-compact/) | Thundersmacker | Уменьшение размера Blista Compact для соответствия реальному аналогу (Honda CR-X).  |
| [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | B Dawg | Исправляет зеленоватые текстуры на некоторых моделях персонажей. |
| [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | _ys | Исправление некорректного костюма в Perseus, т.к. вы покупаете костюм, отличный от отображаемого. |
| [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | B Dawg | Исправление голосовых линий байкеров из IV в EFLC. |
| [Pistol Iron Sight Fix](https://drive.google.com/file/d/1YJLc7dsrDiEQEgzfv4Mn6UmMjQcVBcmg/view?usp=sharing) | Gillian (я) | Исправляет недочет в моделе пистолета где прицел не имеет вообще никакого смысла. |
| [Liberty Ferry Terminal - Waiting Room Sign Fix](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Исправление сломанной UV-карты на текстуре знака "Waiting Room". |
| [Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Редактирует UV-карту знака, чтобы включить в его неиспользуемую текстуру. |
| [Luis' Helmet Reflections Fix](https://www.gtainside.com/en/gta4/skins/125863-luis-s-helmet-reflections-fix/) | 6135 | Исправляет поблекшие отражения на шлеме модели игрока в TBoGT. |
| [Luis' Bag Texture Fix](https://www.gtainside.com/en/gta4/skins/136118-luis-s-bag-texture-fix/) | 6135 | Добавляет недостающие карты нормалей и спекуляций и улучшает качество текстур на сумке модели игрока в TBoGT. |
| [Johnny's Shoe Texture Fix](https://www.gtainside.com/en/gta4/skins/125196-johnny-s-shoe-texture-fix/) | 6135 | Добавляет недостающие карты нормалей и спекуляций в обувь модели игрока в TLAD. |
| [Replaced Esperanto by Roman's Taxi in Cab Depot](https://gtaforums.com/topic/989680-attramets-workshop/) | Attramet | Заменяет Esperanto возле оффиса Романа на его же такси. |
| [Fixed Pedestrian Reactions](https://gtaforums.com/topic/989680-attramets-workshop/) | Attramet | Отключает странные реакции пешеходов которые не имеют смысла. |
| [Reduced Traffic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | GladiTek | Изменяет уровень шума транспорта в Algonquinе, чтобы он соответствовал реальному уровню, который можно обычно услышать на Times Square. ||
| [Menu Art Fix](https://drive.google.com/file/d/1g1AtEBNV2ElitGECGBD14Y0EsDN6XXR_/view?usp=drive_link) | _ys | Исправляет фоны с низким разрешением в меню EFLC. |
| [GTA V's fxdecals](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Изменяет некоторые декали на точно такие же, но в высшем разрешении, из GTA V. |
| [GTA V-like `visualSettings.dat`](https://drive.google.com/drive/folders/1n6dMxi5CdK6-4KV06ki_zbEi81NDDqrj) | MagicAl6244225 |  Изменяет некоторые значения файла `visualSettings.dat`, чтобы сделать его более похожим на GTA V. Увеличение спекулярности дождя было исключено. |
| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871) | Ash_735 | Повышает качество иконок радио на интерфейсе, так как они сильно не соответствуют другим частям интерфейса. |

### Раздельные моды { data-search-exclude }

Моды или их конкретные версии в следующем списке присутствуют только в одном из архивов из-за несовместимости с другой версией.

=== "1.2.0.59"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Console Select Menu](https://github.com/gennariarmando/iv-console-select-menu/) | _AG | Заменяет селектор эпизода на более похожий к консольному, который, по моему мнению, выглядит лучше. <br>==Можно отключить, удалив файлы `ConsoleSelectMenuIV` из папки :material-folder: `plugins`.==</br> |
=== "1.0.8.0"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | Даунгрейд до 1.0.8.0 | Gillian (файлы пренадлежат Rockstar) |  A simple downgrade to 1.0.8.0 without replacing too many files. |
    | [ZolikaPatch IV~7.65~](https://zolika1351.pages.dev/mods/ivpatch) | Zolika1351 | Добавляет мелкие исправления исключительно для 1.0.8.0. |
    | [Liberty Tweaks~1.5~](https://gtaforums.com/topic/991160-liberty-tweaks/) | catsmackaroo, ItsClockAndre и другие | Мод, нацелений на улучшение различных аспектов игры и ее общий Quality of Life. Много настроек.<br>==Позволяет быстро сохраняться на ++f9++ и имеет множество геймплейных фич - если вам не нравятся настройки по умолчанию, вы можете изенить все на свой вкус в файле :material-file-cog:`LibertyTweaks.ini` который находится в :material-folder: `IVSDKDotNet\scripts\`==</br> |
    | [Project Thunder~2.2~](https://gtaforums.com/topic/982902-project-thunder/) | ItsClockAndre | Улучшает грозу, с улучшениями к освещению и атмосфере. Много настроек. |
    | [VAmbience~1.0~](https://gtaforums.com/topic/981402-vambience/) | ItsClockAndre | Добавляет в игру фоновый шум, например, езда автомобилей в дали или стрельба, как в GTA V. Много настроек. |
    | [Steam Achievements](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/) | Zolika1351 | Позволяет получать достижения в :material-steam: Steam на старых патчах. |

---

## Дополнительные моды { data-search-exclude }

Эти моды не включены по умолчанию, но их легко установить поверх архива. Любые другие моды, не упомянутые в этом списке, не поддерживаются.

=== "1.2.0.59"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Аддоны Console Visuals](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo и другие | Сборник портированных ассетов с консольной версии. <br>Установка: Распакуйте желаемые части в папку с игрой.</br> |
    | Чит на снег | ThirteenAG & Fusion Team | Для включения снега, введите `7665550100` на телефоне. Для отключения, введите `2665550100`. |
    | [Аддоны для "снежного режима"](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_,  Straysify, gdanbo, ThirteenAG и Gillian | Часть [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) и [Project2DFX](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest) собраны в ввиде аддонов для "снежного режима" выше.<br>Инструкции по установке находятся в :material-file:`Readme.txt` внутри архива.</br> |
    | [Solitude](https://www.nexusmods.com/gta4/mods/417) | Chunk | Мод timecyc, построенный на ванильном визуале.<br>Установка: Найдите папку :material-folder: ==Fusion overloader install== в архиве и распакуйте папку :material-folder: ==update== из-под нее в папку с игрой. Примените рекомендуемые настройки.</br> |
=== "1.0.8.0"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Официальный руссификатор (текст)](https://drive.google.com/file/d/1GbOA3CBAQGgXW6SjODzd8G8Cj-a8G6dt/view?usp=drive_link) | 1C SoftClub | Установка: Распакуйте папку :material-folder: ==update== в папку с игрой, в `Settings` - `Display` - `Language` смените язык на `Русский`. |
    | Настройки Liberty Tweaks | catsmackaroo, ItsClockAndre и другие | В этом моде множество настроек, которые сильно изменяют геймплей - если вам такое не нравится, вы можете изменить настройки под свой вкус в :material-file-cog:`LibertyTweaks.ini` который находится в папке :material-folder: ==IVSDKDotNet\scripts\\==. |
    | [Аддоны Console Visuals](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo и другие | Сборник портированных ассетов с консольной версии. <br>Установка: Распакуйте желаемые части в папку с игрой.</br> |
    | [Пресеты от коммьюнити](https://drive.google.com/drive/folders/1H0yRkfND1Cte30zUT_yUFcdZASJMEWjb?usp=sharing) | Люди с моего Discord сервера | Пресеты от коммьюнит для Liberty Tweaks и Project Thunder, основанные на популярном голосе людей из Discord сервера. |
    | Чит на снег | ThirteenAG & Fusion Team | Для включения снега, введите `7665550100` на телефоне. Для отключения, введите `2665550100`. |
    | [Аддоны для "снежного режима"](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_,  Straysify, gdanbo, ThirteenAG и Gillian | Часть [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) и [Project2DFX](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest) собраны в ввиде аддонов для "снежного режима" выше.<br>Инструкции по установке находятся в :material-file:`Readme.txt` внутри архива.</br> |
    | [Solitude](https://www.nexusmods.com/gta4/mods/417) | Chunk | Мод timecyc, построенный на ванильном визуале.<br>Установка: Найдите папку :material-folder: ==Fusion overloader install== в архиве и распакуйте папку :material-folder: ==update== из-под нее в папку с игрой. Примените рекомендуемые настройки.</br> |
    | [IV-Presence](https://gtaforums.com/topic/975850-iv-presence/) | ItsClockAndre | Добавляет Discord Rich Presence (кастомный статус активности).<br>Installation: Откройте архив, в нем откройте папку :material-folder: ==For GTA IV 1070 and 1080== и распакуйте файлы :fontawesome-solid-gears:`discord-rpc.dll` и :material-file:`IVPresence.asi` в папку с игрой. Если возникли проблемы, также распакуйте :material-file:`IVPresenceDependenciesChecker.exe` с его конфигом, запустите его и вы увидите, каких зависимостей вам не хватает.</br> |

---

## Список изменений { data-search-exclude }

=== "1.2.0.59"
    !!! info "Последняя версия"
        - 13.11.2024:
            - Обновлены FusionFix, Various Fixes, Restored Pedestrians, Project Glass, Xbox Rain Droplets.
            - Добавлен GTA V-like `visualSettings.dat`.
            - Удален HD HUD из-за создания крашей.
            - Удален Console Clothing ибо я не могу разобраться с приоритетом.
    ??? quote "Старые изменения"
        - 25.09.2024:
            - Обновлены FusionFix, Various Fixes.
            - Исправлены сломанные елементы HUDа.
            - Исправлены волосы Нико.
            - Вручную переделан прицел пистолета.
        - 17.09.2024:
            - Обновлены FusionFix, Radio Downgrader, Restored Pedestrians.
            - Теперь реально добавил Various Pedestrian Actions, лол.
            - Вернул Improved Animations Pack.
            - Удален Console Weapon Animations.
            - Временно удален UHD Vanilla Map and Radar пока не будут исправлены краши.
            - Исправлен краш в миссии Марта, благодати полная (Marta Full of Grace) (TLAD).
            - Исправлены сломанные модели копов в EFLC.
        - 07.09.2024:
            - Обновлен FusionFix.
            - Добавлен Bullet Penetration - Minimal Edition.
            - Исправлен вылет в TLAD, который случался когда проезжаешь мимо таксопарка Романа.
            -  Исправлена консольная одежда.
        - 01.09.2024:
            - Обновлены FusionFix, Various Fixes (должно исправить некоторые баги).
            - Временно удален :material-file:`hud.txd` из-за крашей. Странно.
        - 24.08.2024:
            - Обновлен FusionFix.
            - Исправлено пропавшее тело Мэллори в миссии "Ирландское счастье".
            - Добавлена геймплейная и проповая модель помпового дробовика из TLAD в IV и TBoGT.
        - 23.08.2024:
            - Обновлен FusionFix.
            - Добавлены HD HUD and Reticle, фиксы для `cargrp` от RecklessGlue540.
            - Удалены новые треки на радио, Fixed Carwash Price Text (создавал краши).
        - 15.08.2024:
            - Обновлены Radio Downgrader, FusionFix, Various Fixes (вручную собран из файлов репозитория), Console Visuals, Characters Fixes, Project Glass, Vehicle Pack, Xbox Rain Droplets, Project2DFX и Setup Utility.
            - Добавлены Fidelity Popcycle, UHD Vanilla Map and Radar, Replaced Esperanto by Roman's Taxi in Cab Depot, Fixed Pedestrian Reactions, Fixed Carwash Price Text, donnits' GTA V fxdecals.
            - Удалены Improved Animations Pack, IV Fixes and Improvements, GTA Online QUB3D Background и Fixed LCPD Buffalo.
            - Папка :material-folder: ==update== полностью перепакована во избежание лишних файлов.
        - 09.03.2024:
            - Обновлены More Visible Interiors, Xbox Rain Droplets.
            - *Наконец-то* исправлен Three Leaf Clover.
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
        - 13.11.2024:
            - Обновлены FusionFix, Various Fixes, Restored Pedestrians, Project Glass, Xbox Rain Droplets.
            - Добавлен GTA V-like `visualSettings.dat`.
            - Удален HD HUD из-за создания крашей.
            - Удален Console Clothing ибо я не могу разобраться с приоритетом.
    ??? quote "Старые изменения"
        - 25.09.2024:
            - Обновлены FusionFix, Various Fixes, Liberty Tweaks.
            - Исправлены сломанные елементы HUDа.
            - Исправлены волосы Нико.
            - Вручную переделан прицел пистолета.
        - 17.09.2024:
            - Обновлены FusionFix, Radio Downgrader, Restored Pedestrians, Liberty Tweaks.
            - Теперь реально добавил Various Pedestrian Actions, лол.
            - Вернул Improved Animations Pack.
            - Удален Console Weapon Animations.
            - Временно удален UHD Vanilla Map and Radar пока не будут исправлены краши.
            - Исправлен краш в миссии Марта, благодати полная (Marta Full of Grace) (TLAD).
            - Исправлены сломанные модели копов в EFLC.
        - 07.09.2024:
            - Обновлены FusionFix, Liberty Tweaks.
            - Добавлен Bullet Penetration - Minimal Edition.
            - Исправлен вылет в TLAD, который случался когда проезжаешь мимо таксопарка Романа.
            - Исправлена консольная одежда.
        - 01.09.2024:
            - Обновлены FusionFix, Various Fixes (должно исправить некоторые баги).
            - Временно удален :material-file:`hud.txd` из-за крашей. Странно.
        - 24.08.2024:
            - Обновлен FusionFix.
            - Исправлено пропавшее тело Мэллори в миссии "Ирландское счастье".
            - Добавлена геймплейная и проповая модель помпового дробовика из TLAD в IV и TBoGT.
        - 23.08.2024:
            - Обновлены FusionFix, Liberty Tweaks.
            - Добавлены HD HUD and Reticle, фиксы для `cargrp` от RecklessGlue540.
            - Удалены новые треки на радио, Fixed Carwash Price Text (создавал краши).
        - 15.08.2024:
            - Обновлены Radio Downgrader, FusionFix, Various Fixes (вручную собран из файлов репозитория), Console Visuals, Characters Fixes, Project Glass, Vehicle Pack, Liberty Tweaks, Project Thunder и Setup Utility.
            - Добавлены Fidelity Popcycle, UHD Vanilla Map and Radar, Replaced Esperanto by Roman's Taxi in Cab Depot, Fixed Pedestrian Reactions, Fixed Carwash Price Text, donnits' GTA V fxdecals.
            - Удалены Improved Animations Pack, IV Fixes and Improvements, GTA Online QUB3D Background и Fixed LCPD Buffalo.
            - Папка :material-folder: ==update== полностью перепакована во избежание лишних файлов.
        - 21.05.2024:
            - Перезалив архива на Mediafire ибо гугл заебет.
            - Обновлены IVSDKDotNet и Liberty Tweaks (также немного перенастроены).
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