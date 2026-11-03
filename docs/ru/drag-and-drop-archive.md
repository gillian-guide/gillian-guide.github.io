---
title: Liberty Drag-and-Drop
description: Полностью готовая к игре сборка для лучшего опыта сюжетки GTA IV
---

# Liberty Drag-and-Drop { data-search-exclude }

Liberty Drag-and-Drop (ранее - Готовый архив, также известная как сборка Gillian, но теперь над ней работает больше людей) - это полностью готовая к игре сборка для лучшего опыта сюжетки GTA IV. Все, что нужно для установки, это просто забросить файлы в папку с игрой и сделать несколько дополнительных действий - отсюда и название.

!!! warning ""
    Убедитесь, что все предварительные требования выполнены и была проведена подготовка. Если вы пропустили один из шагов, у вас могут возникнуть проблемы с использованием этой сборки, и вы не получите поддержку.

    [:material-page-first:Вступление: Предварительные требования</br>](index.md#_3){ .md-button } [:material-page-first:Подготовка</br>](preparation.md){ .md-button }

---

## Обзоры

Если вы перед установкой хотите ознакомиться со сборкой, я рекомендую эти видео:

<div class="video-row">
<lite-youtube videoid="lzEbEIGlIRs" title="The definitive way to play GTA IV" playlabel="Воспроизвести: The definitive way to play GTA IV"><span class="lyt-author">catsmackaroo</span></lite-youtube>
<lite-youtube class="video-featured" videoid="ed3mmDQISik" title="Fixing and Improving GTA IV on PC (With Mods)" playlabel="Воспроизвести: Fixing and Improving GTA IV on PC (With Mods)"><span class="lyt-badges"><span class="lyt-star" role="img" aria-label="Favourite"></span><span class="lyt-author">Not AJ</span></span></lite-youtube>
<lite-youtube videoid="fvCPz3Fxj0w" title="BEST Way to Play Grand Theft Auto IV" playlabel="Воспроизвести: BEST Way to Play Grand Theft Auto IV"><span class="lyt-author">Retro Renew</span></lite-youtube>
</div>

---

## Установка { data-search-exclude }

!!! question "Есть ли что-нибудь попроще?"
    Да, на самом деле вы можете просто установить [FusionFix](essential-modding/fusionfix.md) и [Various Fixes](essential-modding/various-fixes.md) - и это исправит 90% проблем в игре, при этом имея значительно большую производительность и стабильность. Также можете использовать [Drag 'n Drop Archive от TJGM](https://tjgm.dev/resources/gtaiv/TJGM%27s-Drag-n%27-Drop-Archive/) - там чуть больше модов, и это по сути сборка только из самого необходимого, или, если хотите, лайт-версия моего модпака.

    Вы можете спросить: "Тогда в чём смысл этой сборки?" — и мой ответ будет, по сути, личным. Этот модпак создан с целью включить в себя все исправления от сообщества и базовые улучшения, которые я счёл достойными того, чтобы скомпилировать личную, "идеальную" и "definitive" версию игры, в которой исправлены все мельчайшие недочёты, но он не обязательно будет лучшим вариантом для вас, если вы не страдаете ОКР по поводу мелких проблем, несоответствий и неиспользуемого контента, которые вы могли бы использовать. Если вам нужны дополнительные аргументы в пользу модпака, посмотрите видео Not AJ выше, в котором подробно рассказывается, чем этот модпак отличается от простого использования двух вышеупомянутых модов, но я не могу заставить вас использовать его или считать его лучшим вариантом. Как говорится, выбирайте сами.

!!! question "Какую версию ставить?"
    Следующий переключитель относится к версии игры - базовые различия между ними смотрите [здесь](downgrading/downgrading-the-game.md#_2). Моды в обоих архивах в основном идентичны, но **1.0.8.0 включает больше изменений в роде Quality of Life и удаляет Rockstar Games Launcher, в то время как 1.2.0.59 считается более стабильным, доработанным и в общем ближе к оригиналу.**

    Лично я предпочитаю для первого, ванильного прохождения архив для Complete Edition, а архив Vanilla+ - для перепрохождения, т.к. он значительно меняет баланс и геймплей. Учтите, что Vanilla+ немного требовательнее по железу.

=== "Faithful Complete Edition (1.2.0.59)"
    Последний раз обновлено: **[02.11.2026 (хотфикс)](#_8)**

    !!! warning ""
        - **Эта сборка НЕ обеспечивает наилучшую производительность - и скорее всего значительно ухудшит ее - цель, в первую очередь, создать лучший ванильный-плюс опыт игры.** Если вы только хотите лучшую производительность - начинайте моддинг вручную.
        - **Не ожидайте поддержки если устанавливаете моды за пределами [дополнительных модов](#_7) - скорее всего, вы ее не получите.**
        - Не пытайтесь установить эту версию на уже-даунгрейднутую игру. **Архив должен ставиться исключительно на чистую копию игры.**
        - Если используете Linux, пропустите шаги 3-6, [примените параметры запуска вручную](additional-setup.md#_2) и [установите `d3dx9_43` в Wineprefix GTA IV](essential-modding/fusionfix.md#ff-linux). Я бы также порекомендовал использовать [Proton-GE](https://github.com/GloriousEggroll/proton-ge-custom/releases) (можно установить с помощью [ProtonUp-Qt](https://davidotek.github.io/protonup-qt/)) для улучшения стабильности и получения возможности слушать Independence FM.

    1. [Скачайте архив](https://www.mediafire.com/file/jqgop5ul1kha6kq/1.2_archive.7z/file) ([зеркало](https://buzzheavier.com/zsp81cr90e0g)) (5.2GB, SHA512: ~`63109f0e65c9fb011ac856bbcd321dc97117fcf1deb6f77779ccec198418792a9628e8bf02c752ef36c380bc76ed30274fcd3be8852bcc3bde8c661465eb430c`~).
    1. Распакуйте :material-zip-box:`1.2 archive.7z` в папку с игрой (та, в которой :material-file:`GTAIV.exe`).
    2. Запустите :material-file-download:`GTAIVSetupUtility.exe`. В связи с распространенной путаницей, я должен уточнить, что это просто надежный метод установки DXVK и настройка параметров запуска - утилита **не** обязателеньна для функциональности сборки.
    3. Нажмите `Открыть...` (`Open...`), выберите ту же папку с игрой.
    4. Нажмите `Переустановить DXVK` (`Reinstall DXVK`), после чего `Настроить параметры запуска` (`Setup launch options`). Настройте DLSS-IV по своему вкусу. Не трогайте переключатели, если не знаете что делаете.
    5. После нажатия `Настроить параметры запуска` (`Setup launch options`) и `ОК`, параметры запуска будут у вас в буфере обмена, поэтому сделайте одно из следующих действий:
        - **:material-steam: Steam**: Нажмите правой кнопкой мыши на игре в библиотеке, нажмите `Свойства...` и вставьте содержимое в поле `Параметры запуска`.
        - **:simple-rockstargames: Rockstar Games Launcher**: Откройте страницу с игрой в библиотеке, откройте настройки и вставьте содержимое в поле `Параметры запуска`.
        - **Ярлык**: Нажмите правой кнопкой мыши по ярлыку, нажмите `Свойства` и вставьте содержимое в конец поля `Цель`.
    6. Вы готовы к игре!
        - Запускайте игру через :material-steam: Steam, :simple-rockstargames: Rockstar Games Launcher или `PlayGTAIV.exe`.
        - В настройках, измените  `Графический API` на Vulkan. Если игра вылетает, удалите :material-file:`d3d9.cfg` и не трогайте эту настройку.
        - Предпочтительнее начинать **новую игру**. Существующие файлы сохранения могут работать, но могут возникнуть проблемы. Также следует отметить, что файлы сохранений (и папка для своих треков на радио) теперь находятся в папке :material-folder: ==Savefiles== внутри папки игры.
        - Выставьте настройку `Транспортный поток` на `100` для полноценной утилизации кастомного popcycle.
        - Potential Grim, по умолчанию, отключен в EFLC. Найдите :material-file:`RenameToEnable.img_` в :material-folder: ==update\1 Potential Grim\TBoGT== (или TLAD) и уберите _ для включения.
        - **Не включайте настройку `Fusion Fix: Проверять Обновления`.**
        - Если вы хотите **больше модов, просмотрите [дополнительные моды](#_7)**.

    !!! info "Обновление"
        Если вы обновляете сборку, сначала удалите папку :material-folder: ==update== и удалите все :material-file:`.asi` файлы (но не трогайте остальные) из папки :material-folder: ==plugins==.
=== "Vanilla+ (1.0.8.0)"
    Последний раз обновлено: **[02.11.2026 (хотфикс)](#_8)**

    !!! warning ""
        - **Эта сборка НЕ обеспечивает наилучшую производительность - и скорее всего значительно ухудшит ее - цель, в первую очередь, создать лучший ванильный-плюс опыт игры.** Если вы только хотите лучшую производительность - начинайте моддинг вручную.
        - **Не ожидайте поддержки если устанавливаете моды за пределами [дополнительных модов](#_7) - скорее всего, вы ее не получите.**
        - Не выполняйте даунгрейд самостоятельно. В архив уже входит даунгрейдер. **Архив должен ставиться исключительно на чистую копию игры.**
        - Если используете Linux, пропустите шаги 3-5, [примените параметры запуска вручную](additional-setup.md#_2) и [установите `d3dx9_43` в Wineprefix GTA IV](essential-modding/fusionfix.md#ff-linux). Дополнительно, просмотрите [Заставляем ScriptHookDotNet и IV-SDK .NET работать на Linux](resources/mod-dependencies.md#scripthookdotnet-iv-sdk-net-linux) (или удалите файлы и папки начинающиеся на `IVSDKDotNet`, что отключит Project Thunder и Liberty Tweaks). Я бы также порекомендовал использовать [Proton-GE](https://github.com/GloriousEggroll/proton-ge-custom/releases) (можно установить с помощью [ProtonUp-Qt](https://davidotek.github.io/protonup-qt/)) для улучшения стабильности и получения возможности слушать Independence FM.

    1. [Скачайте архив](https://buzzheavier.com/29vu95rn0qr7) (зеркало временно недоступно) (5.3GB, SHA512: ~`973635d7b947d611df0fa2d6e762be3ccfeacc6e142efb24e2422aaa4d9abc4c068e8b89ba23c829d0514cdaf4c74460cdae9c6a503345c63a9dfabc8e0f1794`~).
    2. Распакуйте :material-zip-box:`1.0 archive.7z` в папку с игрой (та, в которой :material-file:`GTAIV.exe`).
    3. Запустите :material-file-download:`GTAIVSetupUtilityWPF.exe`. Вам возможно потребуется установить [.NET 6 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-6.0.32-windows-x64-installer). В связи с распространенной путаницей, я должен уточнить, что это просто надежный метод установки DXVK и настройка параметров запуска - утилита **не** обязателеньна для функциональности сборки.
    3. Нажмите `Открыть...` (`Open...`), выберите ту же папку с игрой.
    4. Нажмите `Переустановить DXVK` (`Reinstall DXVK`), после чего `Настроить параметры запуска` (`Setup launch options`). Настройте DLSS-IV по своему вкусу.
    6. Вы готовы к игре!
        - Запускайте игру через :material-steam: Steam или `PlayGTAIV.exe`.
        - **Если используете :simple-rockstargames: Rockstar Games Launcher**, не запускайте игру через лаунчер и удалите :material-file:`SteamAchievements.asi`, оставшийся от старых архивов - теперь за достижения отвечает [OpenPreCEPatch](../essential-modding/openprecepatch.md).
        - Руссификатор доступен [ниже](#_7).
        - В настройках, измените  `Графический API` на Vulkan. Если игра вылетает, удалите :material-file:`d3d9.cfg` и не трогайте эту настройку.
        - Предпочтительнее начинать **новую игру**. Существующие файлы сохранения могут работать, но могут возникнуть проблемы. Также следует отметить, что файлы сохранений (и папка для своих треков на радио) теперь находятся в папке :material-folder: ==Savefiles== внутри папки игры. Также, если вы уже начали играть на 1.2.0.59 и хотите продолжить игру на том же сохранении, вам потребуется сделать [даунгрейд сохранения](downgrading/downgrading-the-game.md#_4).
        - Выставьте настройку `Транспортный поток` на `100` для полноценной утилизации кастомного popcycle.
        - Potential Grim, по умолчанию, отключен в EFLC. Найдите :material-file:`RenameToEnable.img_` в :material-folder: ==update\1 Potential Grim\TBoGT== (или TLAD) и уберите _ для включения.
        - **Не включайте настройку `Fusion Fix: Проверять Обновления`.**
        - Если вы хотите **больше модов, просмотрите [дополнительные моды](#_7)**.

    !!! info "Обновление"
        Если вы обновляете сборку, сначала удалите папки :material-folder: ==update== и :material-folder: ==modloader== (если есть) и удалите все :material-file:`.asi` файлы (но не трогайте остальные) из папки с игрой.

??? bug "Игра не запускается | Игра странно себя ведет | Игра случайно вылетает"
    Просмотрите [исправление проблем](resources/troubleshooting.md).

    Отключайте моды по одному, чтобы найти виновника, удаляя папки или файлы в :material-folder: ==update==, :material-folder: ==IVSDKDotNet\scripts== или файлы :material-file:`.asi` (вероятнее всего - Liberty Tweaks, SISCO, Potential Grim или любые дополнительные моды, которые вы поставили).

    Сообщите о проблеме на [Discord сервере](index.md#_4).

---

## Навигация

<div class="grid cards" markdown>

- После установки архива, **примените оптимальные настройки графики**:

    [Следующая страница:material-page-last: <br>Второстепенная настройка: Оптимальные настройки графики</br>](additional-setup.md#__tabbed_2_2){ .md-button .md-button--primary }

- **Если используете Linux,** также примените параметры запуска вручную:

    [Следующая страница:material-page-last: <br>Второстепенная настройка: Параметры запуска</br>](additional-setup.md#_3){ .md-button .md-button--primary }

</div>

---

## Список модов { data-search-exclude }

### Общие моды { data-search-exclude }

Все моды из следующего списка присутствуют в обоих архивах с идентичными версиями:

| Мод | Разработчик(и) | Детали |
| :-: | :------------: | :----: |
| [Radio Downgrader~23.05.2025~](https://github.com/Tomasak/GTA-Downgraders/releases/iv-latest) | Tomasak и другие | Простой даунгрейдер радио.<br>Использованный аддон: [Restored original TBoGT Menu Vocals](https://www.nexusmods.com/gta4/mods/234/?tab=files&category=archived).</br> |
| [FusionFix~5.1.2~](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/) | ThirteenAG, Fusion Team и другие | Самый главный мод: он включает в себя кучу исправлений, улучшений, новые настройки а также выступает в качестве модлоадера. |
| [Various Fixes~2.4~](https://gtaforums.com/topic/975211-various-fixes/) | Attramet и другие | Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
| [Trilogy Characters Fixes~custom~](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/) | TheYoshiPunch, (Japan) GTA Love и другие | Исправляет несоответствие персонажей между основной GTA IV и EFLC. Использованные фанатские аддоны: модели из Various Fixes, [Mitch The Cop TLAD Model от Pingwinek1234](https://www.nexusmods.com/gta4/mods/963), [Johnny K Eye Color V~1.2~ от nipahtard](https://www.nexusmods.com/gta4/mods/1110), [Brucie Kibbutz TBoGT Model for IV от nipahtard](https://www.nexusmods.com/gta4/mods/988), [Eugene Reaper and Triad 1 Fix от Pingwinek1234](https://www.nexusmods.com/gta4/mods/1469) и множество других отдельных исправлений и оптимизаций от Pingwinek1234 |
| [EFLC Vehicle Addon Pack For GTA IV~1.2~](https://gtaforums.com/topic/972433-eflc-vehicle-addon-pack-for-gta-iv-with-proper-audio-and-naming/) | 7urbo1ag | **ВКЛЮЧЕНЫ ТОЛЬКО АДДОНЫ, МАШИНЫ НЕ ДОБАВЛЯЮТСЯ**: Направлено на дополнительное исправление несоответствия между основной GTA IV и EFLC. Использованы: Fixed Infernus Exit Animations, Correct Extras on Gracie's Fetzler in 'Blog This...', Fixed ZombieB Colors in 'Was it Worth It' |
| [DLSS-IV~1.1.1~](https://www.nexusmods.com/gta4/mods/1430) | Chunk | Добавляет в GTA IV DLSS, FSR и HDR, которые на голову выше встроенных в игру решений сглаживания. Использован аддон Better Cables. |
| [SISCO~1.0.8~](https://www.nexusmods.com/gta4/mods/1453) | Chunk | Снижает количество проблем со стримингом, если не убирает их вовсе, а также повышает общие лимиты игры. |
| [Console Visuals~2.1~](https://github.com/Tomasak/Console-Visuals/) | Tomasak, nastyyaboi, Ash_735, Attramet, brokensymmetry и Parallellines | Сборник портированных ассетов с консольной версии. <br>Включенные аддоны: Console Fences, Console Animations, Console Peds, Console Vegetation. Просмотрите [дополнительные моды](#_7) для других аддонов.</br> |
| [Improved Animations Pack~28.06.2024~](https://gtaforums.com/topic/958625-improved-animations-pack/#comments) | B Dawg и C1aude_III | Исправляет разные проблемы с анимациями оружий. |
| [Restored Pedestrians~2.0~](https://gtaforums.com/topic/981864-restored-pedestrians/) | Attramet | Восстанавливает пешеходов, которые либо не использовались, либо присутствовали только в бетах. <br>Включенные аддоны: Scenario Pedestrians (только на CE), Restored Taxi Drivers, M_Y_Garbage, M_Y_Amirguard_01</br> |
| [Various Pedestrians Actions~1.7~](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Attramet | Добавляет, исправляет и завершает недоделанные действия для пешеходов. |
| [Restored Vegetation~26.09.2026~](https://gtaforums.com/topic/984591-restored-trees-position/) | Attramet | Восстанавливает растительность, которая присутствовали в бета-версиях, но была вырезана в финальном релизе - либо случайно, либо из-за проблем с производительностью.<br>Включенный аддон: Beta Tree Positions</br> |
| [Restored Graffiti](https://gtaforums.com/topic/1005785-restored-graffiti/) | Attramet | Восстанавливает граффити, которые были полностью вырезаны из фильного состояния игры. |
| [More Visible Interiors~2.0~](https://gtaforums.com/topic/974099-more-visible-interiors/) | Attramet | Делает интерьер более заметными снаружи, хотя имеет недостаток в виде появления интерьеров на глазах. |
| [Miscellaneous LOD Fixes~1.3.1~](https://www.nexusmods.com/gta4/mods/1580?tab=description) | quarterstogo2 | Исправляет некоторые LODы, которые не совпадают между IV и EFLC или в целом имеют проблемы. |
| [Niko's Appearance Overhaul~2.0b~](https://www.nexusmods.com/gta4/mods/961?tab=posts) | ColbyDash | Исправления и улучшения текстур Нико без каких-либо изменений не в духе оригинала. |
| [Redone Fingerless Gloves](https://www.gtainside.com/gta4/skins/new-look-model/192441-redone-fingerless-gloves-for-niko) | BrynnaDaRosa | Исправленная модель и меш перчаток без пальцев. |
| [Higher Resolution Miscellaneous Pack~3.1~](https://www.nexusmods.com/gta4/mods/357/) | Ash_735 | Улучшает качество текстур мелких объектов. |
| [Project Glass~10.06.2026~](https://discord.gg/gZvZmFt2p7) | DayL | Добавляет cubemap-отражения туда, где раньше было тупо прозрачное стекло. |
| [Vehicle Pack~2.4~](https://www.nexusmods.com/gta4/mods/282?tab=files) | Ash_735 | Улучшает качество текстур всего транспорта в игре. Некоторые текстуры апскейлнуты, некоторые взяты из Max Payne 3 и GTA V. |
| [LibertyCityPlates~1.2.6.4b~](https://www.nexusmods.com/gta4/mods/875?tab=description) | Ash_735 | Делает номерной знак уникальным для каждой машины. |
| [Potential Grim~15.01.2024~](https://gtaforums.com/topic/945227-iveflc-potential-grim/) | Lord Criminal | Добавляет больше разнообразия педов, исправляет некоторые особенности поведения педов и добавляет прогрессивные отношения между бандами. Использованный фанатский аддон: [Optimized biker textures from Hardcore Lost MC от B Dawg](https://gtaforums.com/topic/945227-iveflc-potential-grim/?do=findComment&comment=1072426693). |
| [Drive-By Pre-Aim~1.2~](https://www.nexusmods.com/gta4/mods/1362) | Xatriya | Позволяет прицеливаться *до* выстрела при стрельбе из машины. [Версия для 1.0.8.0](https://www.nexusmods.com/gta4/mods/1564) |
| [Broker Bridge and Electric Wires Appearance Fix](https://www.gtainside.com/en/gta4/mods/214695-broker-bridge-and-electric-wires-appearance-fix/) | yarrabandi | Улучшенные шейдеры для моста Брокер. |
| [New game parameters for transport and traffic~2.3.5~](https://www.nexusmods.com/gta4/mods/616?tab=description) | Ushan27 | Увеличивает и улучшает разнообразие транспорта и педов в разных регионах. |
| [Fidelity Popcycle~1.0~](https://www.nexusmods.com/gta4/mods/405?tab=description) | Chunk | Замена popcycle в духе оригинала который делает жизнь в городе более разнообразной и реалистичной. |
| [Bullet Penetration - Minimal Edition](https://gtaforums.com/topic/989496-bullet-penetration/) | Internet Rob | Позволяет пулям пробивать стекла так, как с лобовыми стеклами. |
| [No Way on the Subway Continuity Fix](https://www.nexusmods.com/gta4/mods/1502) | nipahtard | Исправляет нестыковку с TLAD |
| [Escuela of the Sleep](https://www.nexusmods.com/gta4/mods/507?tab=description) | ServalEd | Делает миссию 'Эскуэла улиц' быстрее, выкинув ПДД из головы водителя. |
| [Clean Getaway - Destination Fix](https://gtaforums.com/topic/989680-attramets-workshop/page/3/#comment-1072596471) | Attramet | Изменяет назначение в миссии 'Чистое бегство' на то, что указано в диалоге. |
| [Xbox Rain Droplets~01.11.2026~](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Добавляет на экран красивые капельки воды. </br>==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.==</br> |
| [Props Restoration~16.05.2026~](https://gtaforums.com/topic/1004764-props-restoration/) | Attramet | Ввостанавливает пре-релизные, бета и неиспользованые пропы на карту. |
| [Beta-Inspired Bank of Liberty](https://gtaforums.com/topic/1002675-interior-mod-beta-inspired-bank-of-liberty/) | Scott1 | Ввостанавливает интерьер Банка Либерти до состояния, которое можно было увидеть в Трейлере 1 (главная деталь - у здания теперь есть купол на потолке). |
| [Artwork Joni](https://www.nexusmods.com/gta4/mods/975) | BrynnaDaRosa | Модель Джони (не путать с Джонни) переделанная для сходства с ее 2д артом, т.к. игровая модель ужасная. [Текстуры из Characters Fixes добавлены Pingwinek1234'ом](https://discord.com/channels/1129805289307242577/1494424154097586206/1541387694398246992). |
| [Dodgy Doc - Higher Quality](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Улучшает текстуры мутного доктора в миссии "Имейте сердце". [Текстуры из Characters Fixes добавлены Pingwinek1234'ом](https://discord.com/channels/1129805289307242577/1494424154097586206/1541456029353508904). |
| [High Quality Pigeons](https://www.gtainside.de/gta4/mods/166924-high-quality-pigeons/) | Supreme Dear Leader | Улучшает модель и качество текстуры голубей. [Оптимизированные текстуры от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1538872350928408737). |
| [Resized Blista Compact~1.2~](https://www.gtainside.de/en/gta4/cars/188730-resized-blista-compact/) | Thundersmacker | Уменьшение размера Blista Compact для соответствия реальному аналогу (Honda CR-X). |
| [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | B Dawg | Исправляет зеленоватые текстуры на некоторых моделях персонажей. Включен [патч от Pingwinek1234](https://discord.com/channels/1129805289307242577/1548364567199875174) который заменяет текстуры Black Modo Jacket Map Prop и одной рубашки, и [доп. патч от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1548369285519507586) который применяет эти улучшения к Characters Fixes |
| [Remove Luis Texture Compression (Greening)~1.5~](https://www.nexusmods.com/gta4/mods/1401?tab=description) | lettersandnumb192, B Dawg | Исправляет зеленоватые текстуры Луиса. |
| [Story Characters Variety Animations~21.10.2026~](https://www.gtainside.com/gta4/skins/new-look-model/221653-story-characters-variety-animations) | f_y_street_02 | Добавляет уникальные анимации к сюжетным персонажам для избавления от монотонности. Оба доп. патча применены. |
| [Restored Motorcycle Helmets](https://www.nexusmods.com/gta4/mods/1006?file_id=2604) | Attramet | Ввостанавливает вырезанные мотошлема. [Соедененные файлы с Project Glass и Characters Fixes от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1539243333136683099). |
| [Track Jackets Fix](https://www.nexusmods.com/gta4/mods/773) | Niikowo | Исправляет тени на спортивной курте для соответсвия зеленой куртке. |
| [Improved Spyde Jacket](https://www.gtainside.com/en/gta4/skins/213587-improved-spyde-jacket/) | Lukakion | Улучшает модель спортивной куртки для большей полигональности и исправляет карту нормалей. |
| [Puffer Jacket Logo](https://www.nexusmods.com/gta4/mods/542) | erwasabo | Добавляет недостающего логотипа Puffer на одну из желеток. |
| [No More Hand Seams for Niko](https://www.gtainside.com/en/gta4/skins/192418-no-more-hand-seams-for-niko/) | BrynnaDaRosa | Исправляет проблемы с текстурой руки Нико. Использованные аддоны: [TBoGT Niko In-Game Hands Fix](https://discord.com/channels/452421215076876288/461150059552178176/1535212054997241896), [TLAD Niko In-Game Hands Fix](https://discord.com/channels/1129805289307242577/1494424154097586206/1538900507618451587); оба от Pingwinek1234 |
| [Johnny's Hand Seams Fix](https://www.nexusmods.com/gta4/mods/1315) | nipahtard | Исправляет швы на текстуре рук модели Джонни. Применено к модели для катсцен Pingwinek1234. |
| [Johnny K pants fix~1.1~](https://www.nexusmods.com/gta4/mods/1464) | nipahtard | Исправляет небольшое пересечение полигонов при анимации прыжка в TLAD. |
| [Ray Boccino Shirt Fix](https://www.nexusmods.com/gta4/mods/959) | DeathWrench | Исправляет плохие текстуры Рэй Боччино. |
| [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | _ys | Исправление некорректного костюма в Perseus, т.к. вы покупаете костюм, отличный от отображаемого. |
| [Clothing Props Fix Overhaul](https://www.nexusmods.com/gta4/mods/1354) | Pingwinek1234 | Исправляет и убирает большинство бета-остатков, спрятанных в пропах, и заменяет их финальными моделями. |
| [Schottler Parked Vehicles Fix](https://www.moddb.com/mods/schottler-parked-vehicles-fix) | Callistonian | Исправляет неправильно припаркованные автомоболи в районе Шоттлер. |
| [Plane Flight Path Improvements](https://www.gtagaming.com/plane-flight-path-improvements-f33591.html) | C4PT41N BOMB4RD | Делает пути полёта самолетов более реалистичными. |
| [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | B Dawg | Исправление голосовых линий байкеров из IV в EFLC. |
| [Pistol UV map fix](https://discord.com/channels/452421215076876288/461150059552178176/1561930593766215770) | gooberboiuwu | Исправляет UV-развертку и прицел (iron sight) модели пистолета. |
| [Liberty Ferry Terminal - Waiting Room Sign Fix](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Исправление сломанной UV-карты на текстуре знака "Waiting Room". |
| [Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Редактирует UV-карту знака, чтобы включить в его неиспользуемую текстуру. |
| [Replaced Esperanto by Roman's Taxi in Cab Depot](https://gtaforums.com/topic/989680-attramets-workshop/) | Attramet | Заменяет Esperanto возле оффиса Романа на его же такси. |
| [Reduced Traffic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | GladiTek | Изменяет уровень шума транспорта в Algonquinе, чтобы он соответствовал реальному уровню, который можно обычно услышать на Times Square. |
| [Stevie Car Theft Photo-Fixes](https://www.gtainside.com/en/gta4/mods/212547-stevie-car-theft-photo-fixes/) | AXL163 | Переделывает некоторые фото угона автомобилей для Стиви для соответствия релизному/модифицированному виду игры и транспорта. |
| [Sensible Rival Cars and No Rubber banding](https://www.nexusmods.com/gta4/mods/1516) | Musclewannabe | Меняет машины соперников в гонках на соответствующие вашей, а также убирает rubberbanding для честности |
| [Better Tree LODs](https://discord.com/channels/693286101686812722/1551212072711225345/1551212560999522326) | nidzo | Улучшенные LOD-биллборды деревьев - переходы между ними стали менее заметными. |
| [Menu Art Fix](https://drive.google.com/file/d/1g1AtEBNV2ElitGECGBD14Y0EsDN6XXR_/view?usp=drive_link) | _ys | Исправляет фоны с низким разрешением в меню EFLC. |
| [GTA V's fxdecals](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Изменяет некоторые декали на точно такие же, но в высшем разрешении, из GTA V. |
| [TBoGT timecyc with DoF and Bloom](https://gtaforums.com/topic/934545-fusion-fix/page/149/#comment-1072589037) | Magic_Al | Включает Глубину резкости и Свечение в TBoGT (которые отключены по дизайну Rockstar). |
| [Consistent Pump Shotgun](https://drive.google.com/file/d/1AaYVYhaRVW9pA5dzTcsAEj_EgjeV2ST5/view?usp=sharing) | Haxogone, я, Ash_735 | Небольшое смещение файлов, чтобы использовать геймплейную и проп-модель помпового дробовика из TLAD в IV и TBoGT. |
| Увеличенные LODы в `visualSettings.dat` | Gillian | Изменяет некоторые значения файла `visualSettings.dat`, чтобы сделать LODы идентичными до GTA V. |
| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871) | Ash_735 | Повышает качество иконок радио на интерфейсе, так как они сильно не соответствуют другим частям интерфейса. |

### Раздельные моды { data-search-exclude }

Моды или их конкретные версии в следующем списке присутствуют только в одном из архивов из-за несовместимости с другой версией.

=== "Faithful Complete Edition (1.2.0.59)"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | [Console Select Menu](https://github.com/gennariarmando/iv-console-select-menu/) | _AG | Заменяет селектор эпизода на более похожий к консольному, который, по моему мнению, выглядит лучше. <br>==Можно отключить, удалив файлы `ConsoleSelectMenuIV` из папки :material-folder: `plugins`.==</br> |
=== "Vanilla+ (1.0.8.0)"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | Даунгрейд до 1.0.8.0 | Gillian (файлы пренадлежат Rockstar) |  A simple downgrade to 1.0.8.0 without replacing too many files. |
    | [OpenPreCEPatch~1.1.1~](https://github.com/gillian-guide/IV.EFLC.OpenPreCEPatch) | Gillian, Zolika1351 | Продолжение ZolikaPatch - добавляет несколько мелких исправлений, эксклюзивных для PreCE-версий, позволяет сохранить сохранения и файлы из CE, а также поддержку достижений Steam. |
    | [Liberty Tweaks~1.8beta~](https://gtaforums.com/topic/991160-liberty-tweaks/) | catsmackaroo, ItsClonkAndre и другие | Мод, нацелений на улучшение различных аспектов игры и ее общий Quality of Life. Много настроек. Использованный аддон: [Armored Cops with EFLC heads from Characters Fixes от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1540680532780916757). <br>==Позволяет быстро сохраняться на ++f9++ и имеет множество геймплейных фич - если вам не нравятся настройки по умолчанию, вы можете изенить все на свой вкус в файле :material-file-cog:`LibertyTweaks.ini` который находится в :material-folder: `IVSDKDotNet\scripts\`==</br> |
    | [BetterRaceIV~1.0~](https://github.com/LotsofEds/BetterRaceIV) | ServalEd | Делает соперников в гонках менее тупыми. |
    | [Project Thunder~2.2.1~](https://gtaforums.com/topic/982902-project-thunder/) | ItsClonkAndre | Улучшает грозу, с улучшениями к освещению и атмосфере. Много настроек. |
    | [VAmbience~1.0~](https://gtaforums.com/topic/981402-vambience/) | ItsClonkAndre | Добавляет в игру фоновый шум, например, езда автомобилей в дали или стрельба, как в GTA V. Много настроек. |
    | [CloudFixIV](https://www.mediafire.com/file/3ywonu77m57wv3z/CloudFixIV+1.1.rar/file) | Chunk | Исправляет некоторые проблемы связанные с ImGui и рендерингом облаков. |

---

## Дополнительные моды { data-search-exclude }

Эти моды не включены по умолчанию, но их легко установить поверх архива. Любые другие моды, не упомянутые в этом списке, не поддерживаются.

=== "Faithful Complete Edition (1.2.0.59)"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | Альтернативный/ванильный popcycle | Ushan27 | Если вам не нравится popcycle в архиве (плотность транспортных средств, которая зависит от местности, погоды и времени суток), вы можете попробовать альтернативный popcycle из мода New game parameters for transport and traffic или вовсе удалить модифицированный popcycle. <br>Установка: переименуйте файл :material-file:`popcycle.dat_alt` в :material-file:`popcycle.dat` в папке :material-folder: ==update/common/data==, заменив существующий файл, или удалите файл :material-file:`popcycle.dat`, чтобы вернуться к ванильному состоянию.</br> |
    | [Proper Grass](https://www.nexusmods.com/gta4/mods/1660) | paulopatine | Исправляет проблему, из-за которой пропадает процедуральная трава и пропы. Возможно, позже войдет в сам архив.<br>Установка: поместите файлы в папку :material-folder: ==plugins==; настройте по необходимости. |
    | [Liberty Loadout](https://www.nexusmods.com/gta4/mods/1226) | Delusional94 | Колесо выбора оружия и радио как в GTA V.<br>Установка: поместите файлы в папку :material-folder: ==plugins==; настройте по необходимости. |
    | [Liberty Shoulder](https://www.nexusmods.com/gta4/mods/1229) | Delusional94 | Shoulder swapping without any extras.<br>Установка: поместите файлы в папку :material-folder: ==plugins==; настройте по необходимости. |
    | [Toggleable Gloves](https://www.nexusmods.com/gta4/mods/1576) | StrangeLifeOG | Позволяет включать и выключать перчатки кнопкой. Не включен, т.к. требует [ScriptHookDotNet](resources/mod-dependencies.md#scripthookdotnet), которого нет в сборке. |
    | [Animated Weapons](https://www.nexusmods.com/gta4/mods/641?tab=description) | ImpossibleEchoes, Spartan112 | Добавляет детализированные анимации к пушкам. Не включен в архив из-за агрессивных изменений, которые не идеально работают с другими модами, но вы можете его использовать по желанию. <br>Установка: скачайте :material-file:`WeaponAnimations.asi` с [последнего релиза](https://github.com/ImpossibleEchoes/WeaponAnimations/releases), поместите его в папку :material-folder: ==plugins==, после скачайте версию `Animated Weapons 3.0 (Fusion Overloader)` с [NexusMods](https://www.nexusmods.com/gta4/mods/641?tab=files) и распакуйте папку :material-folder: ==AW3_Fusion_Overload\Weapon Animations 3.0\update== в папку с игрой. Переименуйте :material-folder: ==1Weapon Animations== на ==0 Weapon Animations==.</br> |
    | [Аддоны Console Visuals](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo и другие | Сборник портированных ассетов с консольной версии. <br>Установка: Распакуйте желаемые части в папку с игрой.</br> |
    | Сезонные читы (снег и хэллоуин) | ThirteenAG & Fusion Team | Для включения или выключения снега, введите `7665550100` на телефоне. Для хэллоуина, введите `2665550100`. |
    | [Longer Loading Screen](https://www.nexusmods.com/gta4/mods/1394?tab=description) | excinus | Позволяет задержаться на экране загрузки подольше - ради атмосферы или просто так. |
    | [Аддоны для "снежного режима"](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_,  Straysify, gdanbo, ThirteenAG и Gillian | Часть [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) и [Project2DFX](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest) собраны в ввиде аддонов для "снежного режима" выше.<br>Инструкции по установке находятся в :material-file:`Readme.txt` внутри архива.</br> |
    | [Файлы Potential Grim после начала игры](https://gtaforums.com/topic/945227-iveflc-potential-grim/) | Lord Criminal | Если вы уже начали игру и достаточно продвинулись, проверьте `Additional options`>`Gang acquaintances` на наличие нужных вам файлов. Вы должны вручную добавить их с помощью [OpenIV](resources/openiv.md).
    | [HQ Map](https://www.nexusmods.com/gta4/mods/356?tab=description) | Alkimical | Карта высокого разрешения для меню паузы. Рекомендуется только к разрешениям 1440р и выше - на низких разрешениях выглядит грубо. |
    | [Correction of physical parameters of transport](https://www.nexusmods.com/gta4/mods/714) | Ushan27 | Измененные параметры вождения, чтобы управление автомобилем стало более предсказуемым, не внося при этом радикальных изменений в систему. Подробности можно прочитать на странице. <br>Установка: Скачайте основной архив, распакуйте содержимое в :material-folder: ==update==. Также установите :material-folder: ==Compatibility with LibertyCityPlates== из Optional content.
    | [Solitude](https://www.nexusmods.com/gta4/mods/417) | Chunk | Мод timecyc, построенный на ванильном визуале.<br>Установка: Найдите папку :material-folder: ==Fusion overloader install== в архиве и распакуйте папку :material-folder: ==update== из-под нее в папку с игрой. Примените рекомендуемые настройки.</br> |
=== "Vanilla+ (1.0.8.0)"
    | Мод | Разработчик(и) | Детали |
    | :-: | :------------: | :----: |
    | Альтернативный/ванильный popcycle | Ushan27 | Если вам не нравится popcycle в архиве (плотность транспортных средств, которая зависит от местности, погоды и времени суток), вы можете попробовать альтернативный popcycle из мода New game parameters for transport and traffic или вовсе удалить модифицированный popcycle. <br>Установка: переименуйте файл :material-file:`popcycle.dat_alt` в :material-file:`popcycle.dat` в папке :material-folder: ==update/common/data==, заменив существующий файл, или удалите файл :material-file:`popcycle.dat`, чтобы вернуться к ванильному состоянию.</br> |
    | [Proper Grass](https://www.nexusmods.com/gta4/mods/1660) | paulopatine | Исправляет проблему, из-за которой пропадает процедуральная трава и пропы. Возможно, позже войдет в сам архив.<br>Установка: поместите файлы в папку :material-folder: ==plugins==; настройте по необходимости. |
    | [Toggleable Gloves](https://www.nexusmods.com/gta4/mods/1576) | StrangeLifeOG | Позволяет включать и выключать перчатки кнопкой. Не включен, т.к. требует [ScriptHookDotNet](resources/mod-dependencies.md#scripthookdotnet), которого нет в сборке. |
    | [Animated Weapons](https://www.nexusmods.com/gta4/mods/641?tab=description) | ImpossibleEchoes, Spartan112 | Добавляет детализированные анимации к пушкам. Не включен в архив из-за агрессивных изменений, которые не идеально работают с другими модами, но вы можете его использовать по желанию. <br>Установка: скачайте :material-file:`WeaponAnimations_preCE.asi` с [последнего релиза](https://github.com/ImpossibleEchoes/WeaponAnimations/releases), поместите его в папку :material-folder: ==plugins==, после скачайте версию `Animated Weapons 3.0 (Fusion Overloader)` с [NexusMods](https://www.nexusmods.com/gta4/mods/641?tab=files) и распакуйте папку :material-folder: ==AW3_Fusion_Overload\Weapon Animations 3.0\update== в папку с игрой. Переименуйте :material-folder: ==1Weapon Animations== на ==0 Weapon Animations==.</br> |
    | [Официальный руссификатор (текст)](https://drive.google.com/file/d/1GbOA3CBAQGgXW6SjODzd8G8Cj-a8G6dt/view?usp=drive_link) | 1C SoftClub | Установка: Распакуйте папку :material-folder: ==update== в папку с игрой, в `Settings` - `Display` - `Language` смените язык на `Русский`. |
    | Настройки Liberty Tweaks | catsmackaroo, ItsClonkAndre и другие | В этом моде множество настроек, которые сильно изменяют геймплей - если вам такое не нравится, вы можете изменить настройки под свой вкус в :material-file-cog:`LibertyTweaks.ini` который находится в папке :material-folder: ==IVSDKDotNet\scripts\\==. |
    | [Аддоны Console Visuals](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | catsmackaroo и другие | Сборник портированных ассетов с консольной версии. <br>Установка: Распакуйте желаемые части в папку с игрой.</br> |
    | Сезонные читы (снег и хэллоуин) | ThirteenAG & Fusion Team | Для включения или выключения снега, введите `7665550100` на телефоне. Для хэллоуина, введите `2665550100`. |
    | [Longer Loading Screen](https://www.nexusmods.com/gta4/mods/1394?tab=description) | excinus | Позволяет задержаться на экране загрузки подольше - ради атмосферы или просто так. |
    | [Аддоны для "снежного режима"](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_,  Straysify, gdanbo, ThirteenAG и Gillian | Часть [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) и [Project2DFX](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest) собраны в ввиде аддонов для "снежного режима" выше.<br>Инструкции по установке находятся в :material-file:`Readme.txt` внутри архива.</br> |
    | [Файлы Potential Grim после начала игры](https://gtaforums.com/topic/945227-iveflc-potential-grim/) | Lord Criminal | Если вы уже начали игру и достаточно продвинулись, проверьте `Additional options`>`Gang acquaintances` на наличие нужных вам файлов. Вы должны вручную добавить их с помощью [OpenIV](resources/openiv.md).
    | [HQ Map](https://www.nexusmods.com/gta4/mods/356?tab=description) | Alkimical | Карта высокого разрешения для меню паузы. Рекомендуется только к разрешениям 1440р и выше - на низких разрешениях выглядит грубо. |
    | [Correction of physical parameters of transport](https://www.nexusmods.com/gta4/mods/714) | Ushan27 | Измененные параметры вождения, чтобы управление автомобилем стало более предсказуемым, не внося при этом радикальных изменений в систему. Подробности можно прочитать на странице. <br>Установка: Скачайте основной архив, распакуйте содержимое в :material-folder: ==update==. Также установите :material-folder: ==Compatibility with LibertyCityPlates== из Optional content.
    | [Solitude](https://www.nexusmods.com/gta4/mods/417) | Chunk | Мод timecyc, построенный на ванильном визуале.<br>Установка: Найдите папку :material-folder: ==Fusion overloader install== в архиве и распакуйте папку :material-folder: ==update== из-под нее в папку с игрой. Примените рекомендуемые настройки.</br> |
    | [IV-Presence](https://gtaforums.com/topic/975850-iv-presence/) | ItsClonkAndre | Добавляет Discord Rich Presence (кастомный статус активности).<br>Installation: Откройте архив, в нем откройте папку :material-folder: ==For GTA IV 1070 and 1080== и распакуйте файлы :fontawesome-solid-gears:`discord-rpc.dll` и :material-file:`IVPresence.asi` в папку с игрой. Если возникли проблемы, также распакуйте :material-file:`IVPresenceDependenciesChecker.exe` с его конфигом, запустите его и вы увидите, каких зависимостей вам не хватает.</br> |

---

## Список изменений { data-search-exclude }

=== "Faithful Complete Edition (1.2.0.59)"
    !!! info "Последняя версия"
        - 02.11.2026 (хотфикс)
            - [Хотфикс](https://discord.com/channels/1129805289307242577/1131636134376644759/1566949078200352888) включает:
                - Обновлены Xbox Rain Droplets, DLSS-IV, Console Select Menu (кастомная сборка для исправления вылетов), New game parameters for transport and traffic, Resized Blista Compact, Setup Utility.
                - Добавлен SISCO.
                - Исправлен вылет, связанный с :material-file:`waveslots.xml`
                - Некоторые моды объединены в Minor Mods
                - Исправлен конфиг Xbox Rain Droplets
        - 30.10.2026
            - Обновления от Dashii:
                - Добавлены Johnny's Hand Seams Fix, Clothing Props Fix Overhaul, Drive-By Pre-Aim, Niko's Appearance Overhaul, Redone Fingerless Gloves, Better Tree LODs, DLSS-IV + Better Cables Addon, Eugene Reaper and Triad 1 Fix, Johnny K pants fix, No Way on The Subway Continuity Fix, Miscellaneous LOD Fixes, Pistol UV map fix, Sensible Rival Cars и No Rubber banding.
                - Обновлены FusionFix, Various Fixes, Xbox Rain Droplets, Johnny K Eye Color V, Remove Luis Texture Compression (Greening) и Restored Vegetation, Setup Utility.
                - Исправлены мипмапы для текстур рук в катсценах и волос в игре у Нико из Characters Fixes для EFLC.
                - Восстановлены альфа-карты для диффузных текстур головы Нико в основной игре и эпизодах.
                - Исправлен баг Project Thunder с отсутствием молний и звуков грома.
            - Обновления от Pingwinek1234:
                - 'Restored Hove Beach Telegraph Pole and Trees' от Entitled Little Prick перемещен в MinorMods.img, а brook_s.img удален (чтобы не конфликтовало с Various Fixes)
                - Удален мод 'Yes Way on The Subway' от ServalEd, чтобы он не конфликтовал с 'No Way on The Subway Continuity Fix' от nipahtard
                - Добавлен патч совместимости Beta Bank of Liberty для мода Eugene Reaper and Triad 1 Fix
                - Оптимизированы текстуры Джима Фицджеральда в CharacterFixes.IV.img
                - В gta.dat добавлен 'DELAYED_IDE', чтобы не ломать сохранения и прочее
                - В newchar.ide добавлен walkstyle Джима Фицджеральда из мода 'Story Characters Variety Animations' от f_y_street_02
    ??? quote "Старые изменения"
        - 15.09.2026
            - Обновлены Various Fixes, Xbox Rain Droplets, Higher Resolution Miscellaneous Pack
            - Обновления от Pingwinek1234:
                - Обновленный Player Outfit Texture Fixes с доп. фиксами и применением к Characters Fixes
                - Добавлены Remove Luis Texture Compression, Story Characters Variety Animations
        - 24.08.2026 (хотфикс)
            - Удален Grass and Procedural Props Fix из-за повышенной нестабильности; перемещен в Дополнительные моды
            - Хотфикс от Pingwinek1234:
                - Исправлен `player_p`, больше не включает лишние файлы
                - Изменения Джонни и Бруси перемещены в Characters Fixes
                - Добавлены текстуры из Characters Fixes к Artwork Joni и Dodgy Doc Higher Quality
                - Небольшие исправления
        - 23.08.2026
            - Обновлены More Visible Interiors, Higher Resolution Miscellaneous Pack, LibertyCityPlates, New game parameters for transport and traffic, Johnny K Eye Color V, Brucie Kibbutz TBoGT Model for IV
            - Добавлены Grass and Procedural Props Fix, Restored Motorcycle Helmets, Artwork Joni, TBoGT and TLAD Niko In-Game Hands Fix
            - Добавлены обновления от Pingwinek1234:
                - Соедененный файл `player_p` файлами из Project Glass, Restored Motorcycle Helmets, Character Fixes и Customizable Niko
                - Соедененный файл `peds.ide` и ему относящиеся которых не хватало в моей версии
                - Оптимизированные текстуры High Quality Pigeons
                - Исправлен `public_2.ide`
            - (спасибо Dashii за сборку некоторых обновлений что-бы мне было проще)
        - 18.07.2026
            - Обновлены Liberty City Plates, Restored Graffiti
            - Добавлен хотфикс от Pingwinek1234:
                - Исправлен баг, из-за которого у Рэя Боччино отсутствовал торс (эхххх)
                - Исправлена модель Бруси из TBoGT в IV, теперь она используется
                - Удалена модель Билли (тюремная) из Potential Grim, т.к. в Characters Fixes есть текстура получше
                - Дефрагментация файлов из Project Glass и Potential Grim
                - Другие исправления, о которых мне неизвестно
        - 27.06.2026
            - Обновлены Console Visuals, More Visible Interiors, Project Glass, New game parameters for transport and traffic, Rescaled Blista Compact, Ultimate ASI Loader, Xbox Rain Droplets.
            - Добавлены Ray Boccino Shirt Fix, Johnny K Eye Color V, Mitch The Cop TLAD Model (фанатский аддон), Puffer Jacket Logo, Broker Bridge and Electric Wires Appearance Fix, Optimized biker textures for Potential Grim (фанатский аддон).
            - Обновлен Characters Fixes с репаком от Pingwinek1234.
            - Слегка изменены некоторые .ide и .dat для включения большего количества модов.
            - Исправлен Clean Getaway - Destination Fix, теперь работает.
            - Исправлен Fidelity Popcycle, теперь работает.
            - Исправлены некоторые несостыковки файлов.
        - 27.05.2026
            - Обновлены FusionFix, Restored Pedestrians, Vehicle Pack, LibertyCityPlates, New game parameters for transport and traffic, Xbox Rain Droplets, Props Restoration.
            - Restored Trees Position заменен на Restored Vegetation.
            - Добавлен Restored Graffiti.
            - Новый билд Console Select Menu с новыми либами, надеюсь исправит рандомные краши.
            - Удалены Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix из-за похожего фикса в FusionFix.
        - 13.01.2026
            - Обновлены Xbox Rain Droplets, Project Glass, Setup Utility.
            - Добавлены New game parameters for transport and traffic, Track Jackets Fix, No More Hand Seams for Niko, Clean Getaway - Destination Fix, Stevie Car Theft Photo-Fixes, Props Restoration, Improved Spyde Jacket, LibertyCityPlates, Escuela of the Sleep.
            - Potential Grim отключен в EFLC по умолчанию (файлы все еще на месте если вы хотите включить его обратно, они всего-лишь отключены).
            - Удалены все изменения GTA V-like `visualSettings.dat` кроме LODов. Яркий свет лишь мешает тонмаппингу FusionFix.
        - 27.10.2025
            - Обновлены FusionFix, Various Fixes, Restored Trees Position, Xbox Rain Droplets.
            - Переустановлен More Visible Interiors для исправления совместимости.
            - Заново применены GTA V-like `visualSettings.dat` и TBoGT timecyc with DoF and Bloom ибо в прошлой версии они были забыты.
            - Удален Panoramic Towers LOD Fix из-за его включения в Various Fixes.
        - 05.10.2025
            - Обновлены FusionFix, Xbox Rain Droplets.
            - Исправлен приоритет подгрузки между FusionFix и Various Fixes.
        - 20.09.2025
            - **Установка игры теперь портативна — файлы сохранений и настройки находятся в папке игры.**
            - Обновлены FusionFix, Various Fixes, Console Visuals.
            - Добавлен TBoGT timecyc c Глубиной резкости и Свечением.
            - Вернул Console Vegetation, так как я передумал — консольная растительность выглядит лучше.
            - Отключены поворотники по умолчанию, ибо лично я считаю, что они не совсем вписываются в игру.
        - 13.09.2025
            - Обновлены FusionFix, Xbox Rain Droplets.
            - Добавлены Beta-Inspired Bank of Liberty, Schottler Parked Vehicles Fix, TBoGT Blade Fix, Plane Flight Path Improvements.
            - Удален индивидуальный Project2DFX из-за его интеграции в FusionFix.
            - Удален Console Vegetation (я все-равно использую ПКшное освещение).
            - Исправлен вылет в миссии "Торт на миллион".
        - 09.07.2025
            - Обновлены Restored Pedestrians, Project2DFX, Setup Utility.
            - Добавлены EFLC Vehicle Addon Pack For GTA IV (только аддоны), Yes Way On The Subway.
            - Убраны кастомные изменения в Vehicle Pack изменен бюджет транспорта.
            - Исправлены сломанные занавески.
            - Исправлены неправильные текстуры на аксесуарах Луиса.
        - Хотфикс 1:
            - Исправлен вылет при запуске (возвращен ванильный vehicles.ide и изменена только строчка с Infernus).
            - Убрано изменение из GTA V-like visualSettings.dat, которое убирало освещение от светофоров.
        - Хотфикс 2:
            - Исправлена невозможность ударить педов (удалите `pedpersonality.ide` из `update/common/data` и `update/TLAD/common/data`).
            - Удален `move_rifle.wad` из `TBoGT.FusionFix.img` для исправления пропавшего звука ходьбы Луиса при беге с ружьем (спасибо Haxogone за нахождение исправления).
        - Хотфикс 3:
            - Исправлены некоторые случаи испорченных сохранений и вылетов в рандомных миссиях (уберите `IG_Eugene` и `IG_Triad2` из `update/common/data/peds.ide`).
        - 26.05.2025
            - Обновлены Radio Restoration, Project Glass, Xbox Rain Droplets, Ultimate ASI Loader, Setup Utility.
            - Добавлен Console Vegetation.
            - Попытка исправить проблемы с памятью (уменьшено разрешение текстур в Vehicle Pack, изменен бюджет транспорта, убран увеличенный бюджет педов)
        - 26.01.2025
            - Обновлены Restored Pedestrians, Ultimate ASI Loader, Setup Utility.
            - Добавлен Potential Grim (возможно нестабилен хз).
            - Ввостановлена обновленная модель Луиса в IV.
        - 13.01.2025 (хотфикс)
            - Обновлен Setup Utility.
            - Исправлена Мэллори.
        - 30.12.2024
            - Обновлены FusionFix, Trilogy Characters Fixes, Console Visuals, Higher Resolution Misc Pack, Project Glass, Project2DFX, Xbox Rain Droplets.
            - По-нормальному соеденен `peds.ide` из файлов Various Fixes, Trilogy Characters Fixes и Player Outfit Texture Fixes.
            - Удалены некоторые пофикшенные модели для катсцен из Trilogy Characters Fixes из-за сломанных волос.
        - 13.11.2024:
            - Обновлены FusionFix, Various Fixes, Restored Pedestrians, Project Glass, Xbox Rain Droplets.
            - Добавлен GTA V-like `visualSettings.dat`.
            - Удален HD HUD из-за создания крашей.
            - Удален Console Clothing ибо я не могу разобраться с приоритетом.
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
=== "Vanilla+ (1.0.8.0)"
    !!! info "Последняя версия"
        - 02.11.2026 (хотфикс)
            - [Хотфикс](https://discord.com/channels/1129805289307242577/1131636134376644759/1566949078200352888) включает:
                - Обновлены Xbox Rain Droplets, DLSS-IV, New game parameters for transport and traffic, Resized Blista Compact, Setup Utility.
                - Добавлен SISCO.
                - Исправлен вылет, связанный с :material-file:`waveslots.xml`.
                - Некоторые моды объединены в Minor Mods.
                - Исправлен конфиг Xbox Rain Droplets.
        - 30.10.2026
            - Обновления от Dashii:
                - Добавлены Johnny's Hand Seams Fix, Clothing Props Fix Overhaul, Drive-By Pre-Aim, Niko's Appearance Overhaul, Redone Fingerless Gloves, Better Tree LODs, DLSS-IV + Better Cables Addon, Eugene Reaper and Triad 1 Fix, Johnny K pants fix, No Way on The Subway Continuity Fix, Miscellaneous LOD Fixes, Pistol UV map fix, Sensible Rival Cars и No Rubber banding.
                - Обновлены FusionFix, Various Fixes, Liberty Tweaks, Xbox Rain Droplets, OpenPreCEPatch, Johnny K Eye Color V, Remove Luis Texture Compression (Greening), Restored Vegetation, Setup Utility.
                - Исправлены мипмапы для текстур рук в катсценах и волос в игре у Нико из Characters Fixes для EFLC.
                - Восстановлены альфа-карты для диффузных текстур головы Нико в основной игре и эпизодах.
            - Обновления от Pingwinek1234:
                - 'Restored Hove Beach Telegraph Pole and Trees' от Entitled Little Prick перемещен в MinorMods.img, а brook_s.img удален (чтобы не конфликтовало с Various Fixes)
                - Удален мод 'Yes Way on The Subway' от ServalEd, чтобы он не конфликтовал с 'No Way on The Subway Continuity Fix' от nipahtard
                - Добавлен патч совместимости Beta Bank of Liberty для мода Eugene Reaper and Triad 1 Fix
                - Оптимизированы текстуры Джима Фицджеральда в CharacterFixes.IV.img
                - В gta.dat добавлен 'DELAYED_IDE', чтобы не ломать сохранения и прочее
                - В newchar.ide добавлен walkstyle Джима Фицджеральда из мода 'Story Characters Variety Animations' от f_y_street_02
    ??? quote "Старые изменения"
        - 15.09.2026
            - Обновлены Various Fixes, Xbox Rain Droplets, Higher Resolution Miscellaneous Pack, Liberty Tweaks
            - Отключен стрит-рейсинг в Liberty Tweaks ибо функция чисто спавнила пустые машины посреди дороги
            - Обновления от Pingwinek1234:
                - Обновленный Player Outfit Texture Fixes с доп. фиксами и применением к Characters Fixes
                - Добавлены Remove Luis Texture Compression, Story Characters Variety Animations
        - 24.08.2026 (хотфикс)
            - Удален Grass and Procedural Props Fix из-за повышенной нестабильности; перемещен в Дополнительные моды
            - Хотфикс от Pingwinek1234:
                - Исправлен `player_p`, больше не включает лишние файлы
                - Изменения Джонни и Бруси перемещены в Characters Fixes
                - Добавлены текстуры из Characters Fixes к Artwork Joni и Dodgy Doc Higher Quality
                - Небольшие исправления
        - 23.08.2026
            - Обновлены Liberty Tweaks, More Visible Interiors, Higher Resolution Miscellaneous Pack, LibertyCityPlates, New game parameters for transport and traffic, Johnny K Eye Color V, Brucie Kibbutz TBoGT Model for IV
            - Добавлены Grass and Procedural Props Fix, Restored Motorcycle Helmets, Artwork Joni, TBoGT and TLAD Niko In-Game Hands Fix, CloudFixIV
            - Добавлены обновления от Pingwinek1234:
                - Соедененный файл `player_p` файлами из Project Glass, Restored Motorcycle Helmets, Character Fixes и Customizable Niko
                - Соедененный файл `peds.ide` и ему относящиеся которых не хватало в моей версии
                - Оптимизированные текстуры High Quality Pigeons
                - Исправлен `public_2.ide`
            - Заново включены некоторые настройки Liberty Tweaks которые, вроде как, больше не должны вызывать проблем.
            - (спасибо Dashii за сборку некоторых обновлений что-бы мне было проще)
        - 18.07.2026
            - Обновлены Liberty City Plates, Restored Graffiti
            - Добавлен хотфикс от Pingwinek1234:
                - Исправлен баг, из-за которого у Рэя Боччино отсутствовал торс (эхххх)
                - Исправлена модель Бруси из TBoGT в IV, теперь она используется
                - Удалена модель Билли (тюремная) из Potential Grim, т.к. в Characters Fixes есть текстура получше
                - Дефрагментация файлов из Project Glass и Potential Grim
                - Другие исправления, о которых мне неизвестно
        - 27.06.2026
            - Обновлены Console Visuals, More Visible Interiors, Project Glass, New game parameters for transport and traffic, Rescaled Blista Compact, Ultimate ASI Loader, Xbox Rain Droplets, Liberty Tweaks.
            - Добавлены Ray Boccino Shirt Fix, Johnny K Eye Color V, Mitch The Cop TLAD Model (фанатский аддон), Puffer Jacket Logo, Broker Bridge and Electric Wires Appearance Fix, Optimized biker textures for Potential Grim (фанатский аддон).
            - Обновлен Characters Fixes с репаком от Pingwinek1234.
            - Слегка изменены некоторые .ide и .dat для включения большего количества модов.
            - Исправлен Clean Getaway - Destination Fix, теперь работает.
            - Исправлен Fidelity Popcycle, теперь работает.
            - Отключены конфликтные настройки в Liberty Tweaks по умолчанию(Vehicle Tilt & Rotation, Personal Vehicles - Basic Vehicles, Reckless Drivers, Extended Weapon Pool).
            - Исправлены некоторые несостыковки файлов.
            - Изменены настройки FusionFix по умолчанию для исправления бега и отражений.
        - 27.05.2026
            - Обновлены FusionFix, Restored Pedestrians, Vehicle Pack, LibertyCityPlates, New game parameters for transport and traffic, Xbox Rain Droplets, Props Restoration, руссификатор.
            - Restored Trees Position заменен на Restored Vegetation.
            - Добавлен Restored Graffiti.
            - Удалены Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Ultimate Train Swerving Fix из-за похожих фиксов в FusionFix.
        - 13.01.2026
            - Обновлены Xbox Rain Droplets, Project Glass, Liberty Tweaks, Setup Utility.
            - Добавлены New game parameters for transport and traffic, Track Jackets Fix, No More Hand Seams for Niko, Clean Getaway - Destination Fix, Stevie Car Theft Photo-Fixes, Props Restoration, Improved Spyde Jacket, LibertyCityPlates, Escuela of the Sleep.
            - Potential Grim отключен в EFLC по умолчанию (файлы все еще на месте если вы хотите включить его обратно, они всего-лишь отключены).
            - Удалены все изменения GTA V-like `visualSettings.dat` кроме LODов. Яркий свет лишь мешает тонмаппингу FusionFix.
        - 27.10.2025
            - Обновлены FusionFix, Various Fixes, Restored Trees Position, Xbox Rain Droplets, Liberty Tweaks.
            - Переустановлен More Visible Interiors для исправления совместимости.
            - Заново применены GTA V-like `visualSettings.dat` и TBoGT timecyc with DoF and Bloom ибо в прошлой версии они были забыты.
            - Удален Panoramic Towers LOD Fix из-за его включения в Various Fixes.
            - Добавлены файлы локализации из 1.0.8.0 для удаления текста, относящегося к Social Club.
            - Руссификатор обновлен для исправления проблем, которые появились с версии 4.0 FusionFix.
        - 05.10.2025
            - Обновлены FusionFix, Xbox Rain Droplets, Liberty Tweaks (beta, however, so expect issues), Project Thunder.
            - Вернут Ultimate Train Swerving Fix из-за обновления IVSDKDotNet.
            - Добавлен BetterRaceIV.
            - Исправлен приоритет подгрузки между FusionFix и Various Fixes.
            - Personal Vehicles заново включены т.к. новая версия Liberty Tweaks должна исправить проблемы с этой фичей - но сильно не надейтесь.
        - 20.09.2025
            - **Установка игры теперь портативна — файлы сохранений и настройки находятся в папке игры.**
            - Обновлены FusionFix, Various Fixes, Console Visuals.
            - Добавлен TBoGT timecyc c Глубиной резкости и Свечением.
            - Вернул Console Vegetation, так как я передумал — консольная растительность выглядит лучше.
            - Отключены поворотники по умолчанию, ибо лично я считаю, что они не совсем вписываются в игру.
            - Перенастроил ZolikaPatch и Liberty Tweaks для устранения некоторых проблем.
            - Отключены Personal Vehicles из-за проблем, вызываемых текущей версией этой функции. Возможно, позже будет включена снова.
            - Удален Ultimate Train Swerving Fix, так как в текущей конфигурации сборки мод работает очень нестабильно.
        - 13.09.2025
            - Обновлены FusionFix, Xbox Rain Droplets.
            - Добавлены Beta-Inspired Bank of Liberty, Schottler Parked Vehicles Fix, TBoGT Blade Fix, Plane Flight Path Improvements, Ultimate Train Swerving Fix.
            - Удален индивидуальный Project2DFX из-за его интеграции в FusionFix.
            - Удален Console Vegetation (я все-равно использую ПКшное освещение).
            - Исправлен вылет в миссии "Торт на миллион".
        - 09.07.2025
            - Обновлены Restored Pedestrians, Setup Utility.
            - Добавлены EFLC Vehicle Addon Pack For GTA IV (только аддоны), Yes Way On The Subway.
            - Откат Liberty Tweaks до 1.6 из-за стабильности.
            - Удален TimeLoopFix из-за присутствия такого-же исправления в Liberty Tweaks.
            - Убраны кастомные изменения в Vehicle Pack изменен бюджет транспорта.
            - Исправлены сломанные занавески.
            - Исправлены неправильные текстуры на аксесуарах Луиса.
        - Хотфикс 1:
            - Исправлен вылет при запуске (возвращен ванильный vehicles.ide и изменена только строчка с Infernus).
            - Убрано изменение из GTA V-like visualSettings.dat, которое убирало освещение от светофоров.
        - Хотфикс 2:
            - Исправлена невозможность ударить педов (удалите `pedpersonality.ide` из `update/common/data` и `update/TLAD/common/data`).
            - Удален `move_rifle.wad` из `TBoGT.FusionFix.img` для исправления пропавшего звука ходьбы Луиса при беге с ружьем (спасибо Haxogone за нахождение исправления).
        - Хотфикс 3:
            - Исправлены сломанные мотоциклы при доставке их в TLAD (мотоциклы добавлены в исключения Improved Crashes в Liberty Tweaks).
        - Хотфикс 4:
            - Исправлены некоторые случаи испорченных сохранений и вылетов в рандомных миссиях (уберите `IG_Eugene` и `IG_Triad2` из `update/common/data/peds.ide`).
        - 26.05.2025
            - Обновлены Radio Restoration, Project Glass, Xbox Rain Droplets, Liberty Tweaks, Ultimate ASI Loader, Setup Utility.
            - Добавлены TimeLoopFixIV, Console Vegetation.
            - Попытка исправить проблемы с памятью (уменьшено разрешение текстур в Vehicle Pack, изменен бюджет транспорта, убран увеличенный бюджет педов)
        - 26.01.2025
            - Обновлены Restored Pedestrians, Liberty Tweaks, Ultimate ASI Loader, Setup Utility.
            - Добавлен Potential Grim (возможно нестабилен хз).
            - Ввостановлена обновленная модель Луиса в IV.
        - 13.01.2025 (хотфикс)
            - Обновлены Liberty Tweaks, Setup Utility.
        - 31.12.2024 (хотфикс)
            - Обновлены IV-SDK .NET и Liberty Tweaks.
            - Удалены лишние файлы от Console Visuals.
        - 30.12.2024
            - Обновлены FusionFix, Trilogy Characters Fixes, Console Visuals, Higher Resolution Misc Pack, Project Glass, Project2DFX, Xbox Rain Droplets, Liberty Tweaks.
            - По-нормальному соеденен `peds.ide` из файлов Various Fixes, Trilogy Characters Fixes и Player Outfit Texture Fixes.
            - Удалены некоторые пофикшенные модели для катсцен из Trilogy Characters Fixes из-за сломанных волос.
            - Исправлена Мэллори.
        - 13.11.2024:
            - Обновлены FusionFix, Various Fixes, Restored Pedestrians, Project Glass, Xbox Rain Droplets.
            - Добавлен GTA V-like `visualSettings.dat`.
            - Удален HD HUD из-за создания крашей.
            - Удален Console Clothing ибо я не могу разобраться с приоритетом.
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
