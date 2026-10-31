---
title: Companion Mods
description: Сколько же модов в этой игре
---

# Companion Mods

На этой странице собраны моды, которые что-то исправляют, улучшают или делают еще что-нибудь - в общем, все то, что само по себе не тянет на обязательный мод, но так или иначе может улучшить впечатление от игры. Они разделены на 3 группы - [исправления](#_2), [улучшения](#_3) и [разное](#_4). Не ищите здесь моды для готового архива - архив уже включает все моды, которые я считаю нужными, а дополнительные моды для него можно найти [здесь](drag-and-drop-archive.md#_8).

!!! warning ""
    Для большинства модов требуется [FusionFix](essential-modding/fusionfix.md). **Эта страница исходит из того, что он у вас установлен, и больше напоминать об этом не будет.**

!!! warning "Для пользователей Linux"
    При установке модов обращайте внимание на регистр в названиях файлов (например, `weaponinfo.xml` и `weaponInfo.xml`). Обязательно объединяйте их как положено.

???+ tip "Как устанавливать моды?"
    Зависит от мода! Обычно бывает 6 типов:

    - Тип 1: обычные моды `.asi`, которым не нужен отдельный модлоадер: их кладут в папку :material-folder: ==plugins== или просто в корневую папку;
    - Тип 2: моды, упакованные под Fusion Overloader. Они идут с папкой :material-folder: ==update== - ее достаточно распаковать в папку с игрой. Но если есть конфликты, эти файлы придется объединять вручную чем-нибудь вроде [WinMerge](https://winmerge.org/downloads/?lang=en);
    - Тип 3: моды для :material-file:`playerped.rpf`. Инструкции по установке таких модов можно прочитать [на этой странице](extras/modloading.md#_2);
    - Тип 4: моды с отдельными файлами, которые должны попасть в :material-file:`.img`. Инструкции по установке можно прочитать [на этой странице](extras/modloading.md#img);
    - Тип 5: моды с отдельными файлами, которые должны попасть в папки вроде :material-folder: ==common/data/==. Инструкции по установке можно прочитать [на этой странице](extras/modloading.md#_2);
    - Тип 6: скриптовые моды, которым нужен отдельный модлоадер (ScriptHookDotNet или IVSDKDotNet): установите [нужный модлоадер](resources/mod-dependencies.md#scripthookdotnet), а затем сам мод по инструкции

    Тип обычно видно сразу, и как только вы начнете устанавливать моды, разобраться будет несложно. Если вам все-таки тяжело (или мод вообще какой-то другой), можете попросить помощи на моем [Discord-сервере](https://discord.gg/zwmsQqExbQ) в специальном канале #community-modding.

    Однако имейте в виду, что не все моды из списка на 100% совместимы друг с другом. Подразумевается, что *вы* сами решите, что оставить из двух конфликтующих модов, если их нельзя объединить (например, два разных мода на popcycle).

---

## Исправления

Эти моды исправляют какую-то часть игры, ничего не добавляя и не меняя радикально.

| Мод | Разработчик(и) | Детали |
| :-: | :----------: | :-----: |
| [Grass and Procedural Props Fix](https://www.nexusmods.com/gta4/mods/1230) | iammrmikeman | Поправляет лимит процедурной травы и пропов, из-за которого они попросту пропадают через некоторое время игры. |
| [Improved Animations Pack](https://gtaforums.com/topic/958625-improved-animations-pack/#comments) | B Dawg and C1aude_III | Исправляет разные проблемы с анимациями оружия. |
| [Broker Bridge and Electric Wires Appearance Fix](https://www.gtainside.com/en/gta4/mods/214695-broker-bridge-and-electric-wires-appearance-fix/) | yarrabandi | Улучшенные шейдеры для моста Брокер. |
| [Clean Getaway - Destination Fix](https://gtaforums.com/topic/989680-attramets-workshop/page/3/#comment-1072596471) | Attramet | Меняет пункт назначения в миссии 'Clean Getaway' так, чтобы он точнее соответствовал диалогу. |
| [Player Outfit Texture Fixes](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | B Dawg | Исправляет зеленоватые текстуры на некоторых моделях персонажей. Есть [патч от Pingwinek1234](https://discord.com/channels/1129805289307242577/1548364567199875174), который меняет текстуры Black Modo Jacket Map Prop и рубашки с тремя пуговицами в цвете ebony, и [еще один патч от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1548369285519507586), который переносит эти улучшения на Characters Fixes |
| [Remove Luis Texture Compression](https://www.nexusmods.com/gta4/mods/1401?tab=description) | lettersandnumb192, B Dawg | Убирает зеленоватый оттенок у текстур Луиса. |
| [Track Jackets Fix](https://www.nexusmods.com/gta4/mods/773) | Niikowo | Исправляет затенение на текстурах спортивных курток, чтобы они совпадали с зеленой курткой. |
| [Puffer Jacket Logo](https://www.nexusmods.com/gta4/mods/542) | erwasabo | Добавляет недостающий логотип на одну из курток Puffer. |
| [Miscellaneous LOD Fixes](https://www.nexusmods.com/gta4/mods/1580?tab=description) | quarterstogo2 | Исправляет некоторые LODы, которые не совпадают между IV и EFLC или в целом сделаны криво. |
| [No More Hand Seams for Niko](https://www.gtainside.com/en/gta4/skins/192418-no-more-hand-seams-for-niko/) | BrynnaDaRosa | Исправляет швы на текстуре рук в модели Нико. Использованные аддоны: [TBoGT Niko In-Game Hands Fix](https://discord.com/channels/452421215076876288/461150059552178176/1535212054997241896), [TLAD Niko In-Game Hands Fix](https://discord.com/channels/1129805289307242577/1494424154097586206/1538900507618451587); оба от Pingwinek1234 |
| [Ray Boccino Shirt Fix](https://www.nexusmods.com/gta4/mods/959) | DeathWrench | Исправляет убогие текстуры Рэя Боччино. |
| [Fixed Suit Display in Perseus](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | _ys | Исправляет неправильный костюм в Perseus: в итоге вы покупаете не тот, который отображается. |
| [Schottler Parked Vehicles Fix](https://www.moddb.com/mods/schottler-parked-vehicles-fix) | Callistonian | Исправляет неправильно припаркованные машины в районе Шоттлер. |
| [IV Bikers in Episodes voice sets fix](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | B Dawg | Исправляет реплики байкеров из IV в EFLC. |
| [Pistol Iron Sight Fix](https://drive.google.com/file/d/1YJLc7dsrDiEQEgzfv4Mn6UmMjQcVBcmg/view?usp=sharing) | Gillian (я) | Исправляет недочет в модели пистолета, из-за которого прицельное приспособление не имеет никакого смысла. |
| [Liberty Ferry Terminal - Waiting Room Sign Fix](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Исправляет сломанную UV-карту на текстуре таблички "Waiting Room". |
| [Sugar Chomps - Separate Signs](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Редактирует UV-карту вывески, чтобы задействовать неиспользуемую текстуру. |
| [EFLC Vehicle Addon Pack For GTA IV](https://gtaforums.com/topic/972433-eflc-vehicle-addon-pack-for-gta-iv-with-proper-audio-and-naming/) | 7urbo1ag | **ТОЛЬКО АДДОНЫ**: цель - дополнительно исправить несоответствия между основной GTA IV и EFLC. Использованы: Fixed Infernus Exit Animations, Correct Extras on Gracie's Fetzler in 'Blog This...', Fixed ZombieB Colors in 'Was it Worth It' |
| [OpenPreCEPatch](https://github.com/gillian-guide/IV.EFLC.OpenPreCEPatch) | Gillian, Zolika1351 | Позволяет получать достижения :material-steam: Steam на **старых патчах**, а также добавляет поддержку DLC для версий PreCE. |
| [CloudFixIV](https://discord.com/channels/452421215076876288/461150059552178176/1541206795769356488) | Chunk | Исправляет некоторые проблемы, связанные с ImGui и рендерингом облаков. **Актуально только для пользователей IVSDKDotNet.** |

---

## Улучшения

Эти моды улучшают то, что в игре уже есть, или то, что в ней явно напрашивается.

| Мод | Разработчик(и) | Детали |
| :-: | :----------: | :-----: |
| [Liberty Tweaks](https://gtaforums.com/topic/991160-liberty-tweaks/) | catsmackaroo, ItsClonkAndre и другие | Нацелен на улучшение разных аспектов игры и общего качества жизни. Много настроек. **Только 1.0.8.0.** Есть аддон: [Armored Cops with EFLC heads from Characters Fixes от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1540680532780916757)<br>==Позволяет быстро сохраняться по клавише ++f9++ и содержит кучу разных геймплейных фич - если вам не по вкусу значения по умолчанию, все можно подогнать под себя в :material-file-cog:`LibertyTweaks.ini` в папке :material-folder: `IVSDKDotNet\scripts\`==</br> |
| [Trilogy Characters Fixes](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/) | TheYoshiPunch, (Japan) GTA Love и другие | Нацелен на исправление несоответствий персонажей между основной GTA IV и EFLC. Сверху можно поставить [фанатские фиксы и аддоны](https://www.mediafire.com/file/njs6nre57kcpxfd/Characters_Fixes.7z/file), в том числе: [Mitch The Cop TLAD Model от Pingwinek123](https://www.nexusmods.com/gta4/mods/963), [Johnny K Eye Color V~1.2~ от nipahtard](https://www.nexusmods.com/gta4/mods/1110), [Brucie Kibbutz TBoGT Model for IV от nipahtard](https://www.nexusmods.com/gta4/mods/988) |
| [Story Characters Variety Animations](https://www.gtainside.com/gta4/skins/new-look-model/221653-story-characters-variety-animations) | f_y_street_02 | Добавляет сюжетным персонажам уникальные анимации, чтобы они не выглядели такими однообразными. Оба необязательных патча применены. |
| [Animated Weapons](https://www.nexusmods.com/gta4/mods/641?tab=description) | ImpossibleEchoes, Spartan112 | Добавляет детализированные анимации оружия к каждой анимации. **Может конфликтовать с другими модами**. |
| [More Visible Interiors](https://gtaforums.com/topic/974099-more-visible-interiors/) | Attramet | Делает интерьеры более заметными снаружи, хотя есть минус: они могут появляться на глазах. |
| [Higher Resolution Miscellaneous Pack](https://www.nexusmods.com/gta4/mods/357/) | Ash_735 | Улучшает качество текстур мелких объектов. |
| [HQ Map](https://www.nexusmods.com/gta4/mods/356?tab=description) | Alkimical | Карта в меню паузы в высоком разрешении. **Стоит использовать только на 1440p и выше - на низких разрешениях выглядит грубо.** |
| [UHD Vanilla Map and Radar](https://www.nexusmods.com/gta4/mods/456) | ValentynL | Альтернативная версия карты в меню паузы в высоком разрешении. **Стоит использовать только на 1440p и выше - на низких разрешениях выглядит грубо. К тому же может снизить стабильность.** |
| [HD HUD and Reticle](https://www.nexusmods.com/gta4/mods/455) | ValentynL | Интерфейс и прицел в высоком разрешении. **Стоит использовать только на 1440p и выше - на низких разрешениях выглядит грубо. К тому же может снизить стабильность.** |
| [Project Glass](https://discord.gg/gZvZmFt2p7) | DayL | Добавляет cubemap-отражения туда, где раньше было просто прозрачное стекло. |
| [Vehicle Pack](https://www.nexusmods.com/gta4/mods/282?tab=files) | Ash_735 | Улучшает качество текстур всего транспорта в игре. Некоторые текстуры апскейлнуты, некоторые взяты из Max Payne 3 и GTA V. |
| [LibertyCityPlates](https://www.nexusmods.com/gta4/mods/875?tab=description) | Ash_735 | Делает номерные знаки уникальными для каждой машины. |
| [Potential Grim](https://gtaforums.com/topic/945227-iveflc-potential-grim/) | Lord Criminal | Добавляет больше разнообразия педов, исправляет некоторые особенности их поведения и добавляет прогрессивные отношения между бандами. Фанатский аддон: [Optimized biker textures from Hardcore Lost MC от B Dawg](https://gtaforums.com/topic/945227-iveflc-potential-grim/?do=findComment&comment=1072426693). **Этот мод может быть сложным в установке - даже в готовом архиве он сильно урезан, так что имейте в виду.** |
| [BetterRaceIV](https://github.com/LotsofEds/BetterRaceIV) | ServalEd | Делает ИИ соперников в гонках более умелым. **Только 1.0.8.0.** |
| [New game parameters for transport and traffic](https://www.nexusmods.com/gta4/mods/616?tab=description) | Ushan27 | Увеличивает и улучшает разнообразие транспорта и педов в разных районах. |
| [Fidelity Popcycle](https://www.nexusmods.com/gta4/mods/405?tab=description) | Chunk | Popcycle в духе оригинала, который делает городскую жизнь более разнообразной и реалистичной. |
| [Bullet Penetration - Minimal Edition](https://gtaforums.com/topic/989496-bullet-penetration/) | Internet Rob | Позволяет пулям пробивать стекло так же, как они пробивают лобовые стекла машин. |
| [DLSS-IV](https://www.nexusmods.com/gta4/mods/1430) | Chunk | Добавляет в GTA IV DLSS, FSR и HDR, которые на голову выше встроенных в игру способов сглаживания. Использован аддон Better Cables. |
| [Niko's Appearance Overhaul](https://www.nexusmods.com/gta4/mods/961?tab=posts) | ColbyDash | Исправления и улучшения текстур Нико без каких-либо отступлений от оригинала. |
| [Redone Fingerless Gloves](https://www.gtainside.com/gta4/skins/new-look-model/192441-redone-fingerless-gloves-for-niko) | BrynnaDaRosa | Исправленные сетка и модель перчаток без пальцев. |
| [Yes Way On The Subway](https://www.gtainside.de/en/gta4/mods/200052-yes-way-on-the-subway-kill-jim-early/) | ServalEd | Снимает неуязвимость с цели в миссии 'No Way On The Subway'. |
| [Escuela of the Sleep](https://www.nexusmods.com/gta4/mods/507?tab=description) | ServalEd | Делает миссию 'Escuela of the Street' быстрее: водитель теперь плевать хотел на ПДД. |
| [Artwork Joni](https://www.nexusmods.com/gta4/mods/975) | BrynnaDaRosa | Модель Джони переделана под ее арт, потому что игровая модель просто уродлива. |
| [Dodgy Doc - Higher Quality](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Улучшает качество Dodgy Doc в миссии 'Have a Heart'. |
| [High Quality Pigeons](https://www.gtainside.de/gta4/mods/166924-high-quality-pigeons/) | Supreme Dear Leader | Улучшает модель и качество текстур голубей. [Текстуры уменьшены Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1538872350928408737). |
| [Improved Spyde Jacket](https://www.gtainside.com/en/gta4/skins/213587-improved-spyde-jacket/) | Lukakion | Повышает полигональность модели спортивной куртки и исправляет карты нормалей. |
| [Plane Flight Path Improvements](https://www.gtagaming.com/plane-flight-path-improvements-f33591.html) | C4PT41N BOMB4RD | Делает траектории полета самолетов более реалистичными. |
| [Replaced Esperanto by Roman's Taxi in Cab Depot](https://gtaforums.com/topic/989680-attramets-workshop/) | Attramet | Заменяет Esperanto в таксопарке Романа на его же такси. |
| [Reduced Traffic Screech (Audio Tweak)](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | GladiTek | Меняет высоту визга шин в Алгонквине до уровня, который обычно слышно на Таймс-сквер. |
| [Stevie Car Theft Photo-Fixes](https://www.gtainside.com/en/gta4/mods/212547-stevie-car-theft-photo-fixes/) | AXL163 | Переделывает некоторые фотографии из угонов Стиви под финальный (в том числе модифицированный) вид игры и машин. |
| [Menu Art Fix](https://drive.google.com/file/d/1g1AtEBNV2ElitGECGBD14Y0EsDN6XXR_/view?usp=drive_link) | _ys | Исправляет фоны низкого разрешения в меню EFLC. |
| [GTA V's fxdecals](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Заменяет некоторые декали на их версии в высоком разрешении из GTA V. |
| [TBoGT timecyc with DoF and Bloom](https://gtaforums.com/topic/934545-fusion-fix/page/149/#comment-1072589037) | Magic_Al | Включает глубину резкости и свечение в TBoGT (Rockstar отключили их по своему дизайну). |
| Increased LODs in `visualSettings.dat` | Gillian | Меняет некоторые значения в `visualSettings.dat`, чтобы использовались значения LOD из GTA V. |
| [Consistent Pump Shotgun](https://drive.google.com/file/d/1AaYVYhaRVW9pA5dzTcsAEj_EgjeV2ST5/view?usp=sharing) | Haxogone, я, Ash_735 | Небольшой сдвиг файлов, чтобы в IV и TBoGT использовались геймплейная модель и проп-модель помпового дробовика из TLAD. |
| [Fixed Combat Shotgun Icon](https://www.gtainside.com/gta4/mods/116711-fixed-combat-shotgun-icon) | DavSte | Иконка боевого дробовика изменена под игровую модель. Мне она не нравится: по сравнению с другими иконками выглядит слишком перегруженной. |
| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871) | Ash_735 | Повышает качество иконок радио в интерфейсе, так как они сильно выбиваются из остальных элементов интерфейса игры. |

---

## Разное

Эти моды не исправляют и не улучшают что-то обязательно - они так или иначе *изменят* впечатление от игры или что-то к нему добавят. Некоторые из них очень даже приятны, но просто не вписались в две предыдущие группы - вот так вот.

| Мод | Разработчик(и) | Детали |
| :-: | :----------: | :-----: |
| [Console Visuals](https://github.com/Tomasak/Console-Visuals/) | Tomasak, nastyyaboi, Ash_735, Attramet, brokensymmetry и Parallellines | Переносит отдельные консольные визуальные элементы на ПК-версию. |
| [Console Select Menu](https://github.com/gennariarmando/iv-console-select-menu/) | _AG | Заменяет выбор эпизода на меню в духе консольного, которое, по-моему, выглядит лучше. **Только 1.2.0.59**. [Ручная сборка более свежей версии](https://www.mediafire.com/file/1aiyfmcy74otkbj/ConsoleSelectMenuIV.asi/file). |
| [Customizable Protagonists](https://gtaforums.com/topic/974798-donnits-bakery/) | donnits | Куча новых вещей для гардероба протагонистов, взятых у NPC, из мультиплеера, консольной версии и невыпущенного контента. Применить можно только через тренер или сторонние реализации гардероба. |
| [Liberty Loadout](https://www.nexusmods.com/gta4/mods/1226) | Delusional94 | Колесо оружия и радио в духе GTA V. **Только 1.2.0.59**. |
| [Liberty Shoulder](https://www.nexusmods.com/gta4/mods/1229) | Delusional94 | Смена плеча без каких-либо дополнений. **Только 1.2.0.59**. |
| [Correction of physical parameters of transport](https://www.nexusmods.com/gta4/mods/714) | Ushan27 | Измененные параметры вождения: машина слушается более предсказуемо, при этом система не меняется радикально. Подробности можно прочитать на странице. |
| [Restored Pedestrians](https://gtaforums.com/topic/981864-restored-pedestrians/) | Attramet | Восстанавливает пешеходов, которые либо не использовались, либо были только в бетах. |
| [Various Pedestrians Actions](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Attramet | Добавляет, исправляет и доделывает незаконченные действия пешеходов. |
| [Restored Vegetation](https://gtaforums.com/topic/984591-restored-trees-position/) | Attramet | Восстанавливает растительность, которая была в бетах, но пропала в финальном релизе - то ли из-за недосмотра, то ли из-за производительности. |
| [Restored Graffiti](https://gtaforums.com/topic/1005785-restored-graffiti/) | Attramet | Восстанавливает граффити, которые полностью вырезали из финальной сборки игры. |
| [Xbox Rain Droplets](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv) | ThirteenAG | Добавляет на экран приятные капли воды. |
| [Project Thunder](https://gtaforums.com/topic/982902-project-thunder/) | ItsClonkAndre | Делает грозу в игре более настоящей: с реальным освещением и улучшенной атмосферой. Много настроек. **Только 1.0.8.0**. |
| [VAmbience](https://gtaforums.com/topic/981402-vambience/) | ItsClonkAndre | Добавляет в игру фоновые шумы - например, езду и стрельбу - как в GTA V. Много настроек. **Только 1.0.8.0**. |
| [Props Restoration](https://gtaforums.com/topic/1004764-props-restoration/) | Attramet | Возвращает на карту пре-релизные, бета- и неиспользуемые пропы. |
| [Beta-Inspired Bank of Liberty](https://gtaforums.com/topic/1002675-interior-mod-beta-inspired-bank-of-liberty/) | Scott1 | Возвращает интерьер Bank of Liberty к виду, похожему на тот, что был в Трейлере 1 (главное - теперь у потолка есть купол). |
| [Resized Blista Compact](https://www.gtainside.de/en/gta4/cars/188730-resized-blista-compact/) | Thundersmacker | Меняет размер Blista Compact под реальный прототип (Honda CR-X). |
| [Restored Motorcycle Helmets](https://www.nexusmods.com/gta4/mods/1006?file_id=2604) | Attramet | Возвращает вырезанные мотоциклетные шлемы. [Объединено с Project Glass и Characters Fixes от Pingwinek1234](https://discord.com/channels/1129805289307242577/1494424154097586206/1539243333136683099). |
| [TV Restoration](https://gtaforums.com/topic/977025-tv-restoration/) | Attramet | Телевизионные ролики в наивысшем качестве. |
| [Beta Radio](https://gtaforums.com/topic/1007007-iv-beta-radio/) | MrFinger | Возвращает 136 песен, вырезанных из GTA IV и EFLC. |
| [Addons for the Snow Mod](https://drive.google.com/file/d/1xlFkZUTVMfmqO538J4S1EEGQ4tzOrfOC/view?usp=sharing) | Jumbo0, gr8man, Jantsu92, Alisa Bellucci, Flash, Alexkander_, Straysify, gdanbo и ThirteenAG | Части [Enhanced Snow Mod](https://www.moddb.com/mods/gta-iv-snow-mod-enhanced), [Snow Mod Reaction Fix](https://www.lcpdfr.com/downloads/gta4mods/scripts/6919-snow-mod-reaction-fix/), [Realistic Snow Sounds](https://www.moddb.com/mods/realistic-snow-sounds/addons/realistic-snow-sounds) и [Project2DFX](https://github.com/gillian-guide/IV.Project2DFX-PreCE/releases/latest), собранные в виде аддонов для снежного режима FusionFix. |
| [IV-Presence](https://gtaforums.com/topic/975850-iv-presence/) | ItsClonkAndre | Добавляет Discord Rich Presence (кастомный статус активности). **Только 1.0.8.0** |

---

Следующие моды рекомендуются меньше - из-за разной степени нестабильности, сложностей с установкой или личной неприязни к ним (то есть они не совсем вписываются в мое видение ванильно-верной сборки GTA IV). Впрочем, если вам что-то понравилось, можете попробовать их поставить.

| Мод | Разработчик(и) | Детали |
| :-: | :----------: | :-----: |
| [Solitude](https://www.nexusmods.com/gta4/mods/417) | Chunk | Мод timecyc в духе Vanilla+. |
| [DayL's Natural Timecycle](https://www.nexusmods.com/gta4/mods/396) | DayL | Мод timecyc, приближенный к естественному виду. |
| [Revamped Visuals](https://libertycity.net/files/gta-4/217259-revamped-visuals-3-0.html) | Lukakion | Еще один мод timecyc в духе Vanilla+. |
| [Project Birds](https://gtaforums.com/topic/980018-project-birds) | Internet Rob | Добавляет в небо птиц. |
| [Liberty Rush](https://gtaforums.com/topic/979688-liberty-rush/) | Internet Rob, ItsClonkAndre, donnits, Datalvarezguy | Добавляет десятки улучшений, восстановленный контент, новые сценарии трафика и т.д. |
| [The Actual Complete Edition](https://gtaforums.com/topic/967792-grand-theft-auto-iv-the-actual-complete-edition/) | C1aude_III | Этот проект всерьез старается объединить IV и EFLC - от оружия, транспорта и ассетов до всей карты. **Сложен в установке и сильно конфликтует с другими модами**. |
| [TACE.lite](https://www.nexusmods.com/gta4/mods/774) | Snake Swagger | Облегченная версия предыдущего мода, которая объединяет только оружие и транспорт. |
| [Liberty Alive](https://gtaforums.com/topic/992467-liberty-alive/#comments) | nabo45 | Добавляет в мир кучу интерьеров. |
| [Enhanced Minor Characters](https://gtaforums.com/topic/978737-grand-theft-auto-iv-enhanced-minor-characters/) | Datalvarezguy | Заменяет ванильных педов в некоторых миссиях на авторское видение персонажей. |
| [Hi-Res Characters](https://www.gtainside.de/en/gta4/mods/176255-hi-res-characters-update-v1-1-upscaled-mod/) | Primusideus | Апскейлнутые текстуры персонажей в высоком разрешении. |
| [The Hardcore Lost MC](https://gtaforums.com/topic/908470-iveflc-the-hardcore-lost-mc/) | iiCriminnaaL | Улучшает игру за TLAD, меняет внешность и ИИ байкеров. |
| [Outfit Enhancements](https://gtaforums.com/topic/908611-outfit-enhancements/) | iiCriminnaaL | Несколько простых улучшений для некоторой одежды. |

---

## Рекомендуемый порядок загрузки и лимиты `.img`

После установки модов выше используйте следующий порядок загрузки (ставьте номер перед названием папки):

1. Мелкие моды (любой другой мод, которого нет ниже, считается мелким - их порядок не так важен, но грузиться они должны сверху)
2. Potential Grim
3. Восстановленные моды (Restored Pedestrians, Restored Vegetation и т.п.)
4. Higher Resolution Miscellaneous Pack
5. Моды транспорта (Vehicle Pack, Resized Blista и т.д.)
6. Characters Fixes
7. Console Visuals
8. Project Glass
9. More Visible Interiors
10. FusionFix (оставьте название папки по умолчанию, чтобы проще было обновлять)
11. Various Fixes (оставьте название папки по умолчанию, чтобы проще было обновлять)

Возможно, вам захочется вручную объединить некоторые `.img`-моды через [OpenIV](resources/openiv.md#_3), чтобы не выйти за лимит.

Насколько вы близки к лимитам, можно увидеть, если поставить `ExtraInfo` в `1` в :material-file-cog:`GTAIV.EFLC.FusionFix.ini` - в настройках внизу экрана появится число - **но только на 1.2.0.58**. Если у вас версия постарше, понять, что вы вышли за лимит, можно только зайдя в TBoGT и посмотрев, спавнится ли транспорт (если нет - вы за лимитом, и это знак объединить некоторые моды).

---

<h3>Мастерские</h3>

В этих мастерских может найтись еще несколько модов или инструментов, которые вам интересны:

[Мастерская Attramet](https://gtaforums.com/topic/989680-attramets-workshop/){ .md-button}  [Мастерская ItsClonkAndre](https://gtaforums.com/topic/988909-itsclonkandres-workshop/){ .md-button}

[Zolika1351's Zone](https://zolika1351.pages.dev/){ .md-button} [Donnit's Bakery](https://gtaforums.com/topic/974798-donnits-bakery/){ .md-button}

[:simple-discord: Моддинг-сообщество DayL](https://discord.gg/gZvZmFt2p7){ .md-button} [Мастерская Internet Rob](https://gtaforums.com/topic/984476-internet-robs-workshop){ .md-button}

---

<h3>Создание модов</h3>

Если вам интересно делать моды самому, заходите на этот Discord-сервер:

[:simple-discord: GTA IV Modding](https://discord.gg/p6RU4xJ){ .md-button .md-button--primary }

---

<h3>Хотите, чтобы ваш мод попал в список?</h3>

Напишите об этом в теме Mod Suggestions на моем Discord-сервере:

[:simple-discord: Мой сервер в Discord](https://discord.gg/zwmsQqExbQ){ .md-button .md-button--primary }

---

## Послесловие

Спасибо, что пользуетесь **моим** руководством по моддингу GTA IV!

Я искренне надеюсь, что помог вам привести игру в идеальное состояние. На поддержку руководства уходит время, и без всех этих замечательных модов ничего бы не вышло, так что подумайте о том, чтобы поддержать авторов: [Благодарности](resources/credits.md).

Если вам нужны еще такие руководства или модпаки, посмотрите [Похожие руководства и ресурсы](resources/similar-guides-modpacks.md).

Дополнительные ресурсы и инструменты можно найти на странице [Extras](extras/index.md) и в разделах Resources слева.

---

<h3>Навигация</h3>

[:material-page-first:Предыдущая страница <br>Обязательные моды</br>](essential-modding/index.md){ .md-button }
