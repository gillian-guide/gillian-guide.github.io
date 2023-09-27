title: Готовый архив
description: Полноценный готовый архив для игры в желаемую версию GTA IV

# Готовый архив { data-search-exclude }
Вы можете выбрать архив в зависимости от желаемой версии - будь то 1.2.0.59 или 1.0.8.0(если вы используете версию [:material-steam:Steam](https://store.steampowered.com/app/12210/) или [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv), то в архив также входит даунгрейдер). Вы можете сравнить список модов [ниже](#_4) - 1.0.8.0 имеет больше значимых модов, имейте это ввиду.

### Примечания { data-search-exclude }
!!! info ""
	1. 1.2.0.59 это Complete Edition, т.е. последняя версия в [:material-steam:Steam](https://store.steampowered.com/app/12210/) или [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv). В нем убрана поддержка мультиплеера и Games for Windows - LIVE, при этом добавлены Rockstar Games Launcher (с его DRM) и оверлей Social Club (с его достижениями). ==Количество поддерживаемых модов в этой версии также значительно ограничено - большинство модов создано для версий 1.0.8.0 и 1.0.7.0==.
	2. 1.0.8.0 является последним патчем для дисковой/старой версии, с поддержкой ZolikaPatch и много других значимых модов. Но, этот архив НЕ поддерживает какую-либо поддержку для Games for Windows - LIVE. Если вы хотите мультиплеер, перейдите к пунктам [даунгрейд](downgrading.md) и [мультиплеер](multiplayer.md). ==Эта версия имеет намного лучше совместимость с модами==.

!!! warning ""
	* Я сам не могу слишком часто обновлять архив - загляните на страницы и посмотрите, не было ли обновлений у модов, особенно у тех, что наверху.
	* Убедитесь, что прошли через всю [подготовку](index.md) (кроме необходимого места на диске).
	* Убедитесь, что установлены последние [драйвера](../optimization/#_2).
	* Убедитесь, что папка с игрой чистая и без лишних модов (:material-steam:Steam не удаляет старые моды).
	* После установки архива рекомендуется начать игру с нового файла сохранения, но можно продолжать играть и с существующими файлами сохранения - просто возникнут небольшие проблемы (например, второстепенные объекты окажутся там, где их не должно быть).

!!! warning "Производительность"
	**Этот архив НЕ обеспечивает максимальную возможную производительность - цель состоит прежде всего в том, чтобы обеспечить наилучший ванильный опыт игры. Если вы хотите получить максимальную производительность - модифицируйте игру вручную. В большинстве случаев производительность остается вполне приемлемой, и большинство людей не должны замечать небольшого снижения производительности.**

!!! warning "Примечание"
    Данный раздел и архив не будут обновляться до дальнейшего примечания в связи с продолжающейся драмой между Fusion Team и Zolika, а также неизвестности будущей ситуации. Мое руководство стремится быть максимально объективным, стараясь предоставлять только актуальную информацию для модинга GTA IV.

## Установка { data-search-exclude }

=== "1.0.8.0"
	[:material-download-circle: Скачать](https://drive.google.com/file/d/1O1qD8ocbJ_fnERTvvVzyw6_bsw-k_evo/view){ .md-button .md-button--primary }  Последнее обновление: **[21.09.2023](#_6)**
	
	Скачайте архив и просто распакуйте его содержимое в папку с игрой (:material-folder:==GTAIV==, а не :material-folder:==Grand Theft Auto IV==). В архив уже включен даунгрейдер. ==После установки запустите :material-file-download:`GTAIVSetupUtilityWPF.exe` и пройдите через установку (если его нету, [скачайте здесь](../optimization/#setup_utility)) и просмотрите [дополнительные моды](#_5)==. Для оптимальных настроек графики, см. [эту страницу](https://gillian-guide.github.io/ru/additional-setup/#_3).
	!!! warning "Предупреждения"
		Архив должен быть установлен поверх чистой, без модов установке Complete Edition из [:material-steam:Steam](https://store.steampowered.com/app/12210/) или [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv). 
		
		Если вы используете версию [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv), не загружайте игру из самого лаунчера, а используйте :material-file:`PlayGTAIV.exe` - в противном случае файлы игры будут заменены.

		Если вы используете Linux, добавьте `WINEDLLOVERRIDES="xlive=n,b" %command%` в параметры запуска. Также удалите файлы, которые начинаются на :material-file:`IVSDKDotNet` - DotNet не работает на Proton должным образом на данный момент.
		
		Какой-либо другой способ установки не поддерживается.
		
		Кроме того, я не буду поддерживать никаких дополнительных модификаций файлов, кроме уже перечисленных инструкций.
	???+ info "Обновление"
		Если вы обновляете архив после его предварительной установки, сначала удалите :material-folder:==update== и :material-folder:==modloader== из папки с игрой.
	??? warning "Если игра не запускается"
		Попробуйте установить :material-file-download:`vcredist_x86.exe` из папки с игрой.

		Отключите антивирус или добавьте папку с GTA IV в исключения. Распакуйте :material-file:`ZolikaPatch.asi` заново.

		Просмотрите [исправление проблем](troubleshooting.md).
	??? warning "Моя игра нестабильна | Моя игра случайно вылетает"
		Просмотрите [исправление проблем](troubleshooting.md).

		Отключайте моды по одному, чтобы увидеть виновника, редактируя :material-file-edit:`modloader.ini` в :material-folder:==modloader== или удаляя моды в :material-folder:==update==.
		
=== "1.2.0.59"
	[:material-download-circle: Скачать](https://drive.google.com/file/d/1eJ4cbVhJ4tnTGJByh_Lf4eS5SS2ShmHO/view){ .md-button .md-button--primary }  Последнее обновление: **[21.09.2023](#_6)**

	Скачайте архив и просто распакуйте его содержимое в папку с игрой (:material-folder:==GTAIV==, а не :material-folder:==Grand Theft Auto IV==). ==После установки запустите :material-file-download:`GTAIVSetupUtilityWPF.exe` и пройдите через установку== (если его нету, [скачайте здесь](../optimization/#setup_utility)) и просмотрите [дополнительные моды](#_5). Для оптимальных настроек графики, см. [эту страницу](https://gillian-guide.github.io/ru/additional-setup/#_3).
	!!! warning "Предупреждения"
		Архив должен быть установлен поверх чистой, без модов установке Complete Edition из [:material-steam:Steam](https://store.steampowered.com/app/12210/) или [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv). 

		Если вы используете Linux, добавьте `WINEDLLOVERRIDES="xlive=n,b" %command%` в параметры запуска. Также удалите файлы, которые начинаются на :material-files:`IVSDKDotNet` - DotNet не работает на Proton должным образом на данный момент.
		
		Какой-либо другой способ установки не поддерживается.
		
		Кроме того, я не буду поддерживать никаких дополнительных модификаций файлов, кроме уже перечисленных инструкций.
	???+ info "Обновление"
		Если вы обновляете архив после его предварительной установки, сначала удалите :material-folder:==update== из папки с игрой.
	??? warning "Моя игра нестабильна | Моя игра случайно вылетает | Моя игра не запускается"
		Просмотрите [исправление проблем](troubleshooting.md).

		Отключайте моды по одному, чтобы увидеть виновника, удаляя моды в :material-folder:==update==.

## Список модов { data-search-exclude }
=== "1.0.8.0"
	| Мод | Описание |
	| :-: | :------: |
	| [Downgrader от Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| Простой и автоматический даунгрейд до 1.0.8.0. |
	| [Radio Downgrader от Tomasak и других](http://downgraders.rockstarvision.com/)| Простой даунгрейдер радио.<br>Использованный аддон: [Restored original TBoGT Menu Vocals](https://www.nexusmods.com/gta4/mods/234?tab=files)</br> |
	| [ZolikaPatch IV~7.65~ от Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| Первый основной мод в сборке: добавляет множество фиксов и исправлений - а также без него не запустится игра. |
	| [IV Tweaker~2.43~ от Zolika1351](https://zolika1351.pages.dev/mods/ivtweaker)| Выступает основным модлоадером в сборке, а также позволяет увеличить лимиты для других модов. |
	| [Steam Achievements~v2~ от Zolika1351](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/)| Позволяет получать достижения в :material-steam:Steam |
	| [FusionFix~1.96~ от ThirteenAG, Tomasak и других](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Второй основной мод сборки, в котором куча исправлений, а также выступает в качестве модлоадера вместе с [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader). Включает [Shader Fixes Collection by Parallellines0451 и других](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection) и [Traffic Cops: Back in the Toolbooths от Olanov](https://www.gtainside.com/en/gta4/mods/187365-traffic-cops-back-in-the-tollbooths/). <br>[Используется форк от Zolika1351](https://github.com/Zolika1351/GTAIV.EFLC.FusionFix/)</br>|
	| [Console Visuals~1.3~ от nastyyaboi и других](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Сборник портированного визуала с консольной версии - от timecyc, до анимаций.<br>Использованные аддоны: Console Clothing, Console Fences, Console Trees(Console Leaves)</br> |
	| [Various Fixes~1.60~ от Attramet и других](https://gtaforums.com/topic/975211-various-fixes/)| Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
	| [Trilogy Characters Fixes от TheYoshiPunch, (Japan) GTA Love, DizCo12, JohnnyK NeverDie и других](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/page/25/#comment-1072185890)| Крупный сборник фиксов для несостыковок между появлениями персонажей в IV и EFLC - плюс, несколько фиксов просто для моделек.<br>Использованный аддон: Niko's Original GTAIV Hair</br> |
	| [Extra Options~1.1~ от Zolika1351](https://zolika1351.pages.dev/mods/ivoptions) | Добавляет множество полезных переключателей в меню игры. |
	| [Liberty Tweaks~1.2.1~ от The Westside Minions & Коммьюнити моддинга GTA IV](https://gtaforums.com/topic/991160-liberty-tweaks/)| Мод с большим количеством quality-of-life изменений. ==Этот мод позволяет совершить быстрое сохранение с помощью клавиши ++f9++. Он также позволяет убирать оружие в кобуру с помощью клавиши ++h++.== |
	| [Improved Animations Pack~1.3~ от B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Фиксы для некоторых анимаций оружия, как задержка стрельбы. |
	| [IV Fixes and Improvements~3.41~ от Zolika1351 и других](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| Сборник фиксов и улучшений - список на сайте. |
	| [Fix Collection от iiCriminnaaL, nkjellman и меня](https://drive.google.com/file/d/13OgDDm0xakbdRONPlrnN5zRfshdAgwhd/view?usp=sharing) | Несколько исправлений из Responsive Plus и Graphics Fix, а именно - `carcols.dat` и `cargrp.dat` и файлы, связанные с эффектами брызг дождя. Моя работа здесь заключается только в том, что я их собрал отдельно. |
	| [Project2DFX~4.3~ от ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Добавляет приятные огни в далеке ночью. ==Можно отключить, удалив файлы `IVLodLights`.== |
	| [Xbox Rain Droplets от ThirteenAG](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv)| Добавляет на экран красивые капельки воды. ==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.== |
	| [Restored Pedestrians от Attramet](https://gtaforums.com/topic/981864-restored-pedestrians/) | Восстанавливает различных вырезанных/не включенных педов. |
	| [Various Pedestrians Actions от Attramet](https://gtaforums.com/topic/976318-various-pedestrian-actions/) | Восстанавливает различные вырезанные/не включенные действия педов. |
	| [Restored Trees Position от Attramet](https://gtaforums.com/topic/984591-restored-trees-position/) | Восстановлено несколько деревьев, которые присутствовали только в бета-версии. |
	| [More Visible Interiors от Attramet](https://gtaforums.com/topic/974099-more-visible-interiors/) | Делает интерьеры более видимыми снаружи. |
	| [Vanilla Road Texture Enhancement by DayL](https://discord.gg/gZvZmFt2p7) | 2x AI апскейлинг для текстур дорог и растительности, а также сгенерированные карты нормалей и спекуляров. ==WIP==. |
	| [Project Glass by DayL](https://discord.gg/gZvZmFt2p7) | Добавляет кубические отражения в большинство стекол в мире, чтобы они больше не выглядели как прозрачный пластик. ==WIP==. |
	| [Project Thunder от ItsClockAndre](https://gtaforums.com/topic/982902-project-thunder/) | Добавляет настраиваемый эффект грозы в погоду Lighting. |
	| [VAmbience от ItsClockAndre](https://gtaforums.com/topic/981402-vambience/) | Добавляет настраиваемые звуки отдаленных машин и стрельбы, аналогичные GTA V. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Улучшенные и портированные текстуры транспорта из GTA V и Max Payne 3. |
	| [Improved Weapon Spec от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=107165200)| Текстуры спекулярных мапок для оружий в более высоком разрешении. |
	| [Dodgy Doc - Higher Quality от donnits](https://gtaforums.com/topic/974798-donnits-bakery/) | Текстуры более высокого разрешения для Dodgy Doc. |
	| [High Quality Pigeons от Supreme Dear Leader](https://www.gtainside.com/gta4/mods/166924-high-quality-pigeons/) | Текстуры и модель более высокого качества для голубей. |
	| [Resized Blista Compact от Thundersmacker](https://www.gtainside.com/en/gta4/cars/188730-resized-blista-compact/) | Исправление модели для Blista Compact, придание ей правильных размеров и исправление ошибок моделирования. |
	| [Fixed LCPD Buffalo от Ooboy](https://www.gtainside.com/en/gta4/cars/181342-fixed-lcpd-buffalo/) | Исправлены ошибки в модели и текстуре полицейского Buffalo. |
	| [Player Outfit Texture Fixes от B Dawg](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | Исправлены зеленоватые текстуры одежды. |
	| [Fixed Suit Display in Perseus от _ys](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | Исправлено некорректное отображение костюмов в Perseus. |
	| [IV Bikers in Episodes voice sets fix от B Dawg](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | Исправляет набор голосов байкеров из IV. |
	| [Default Pistol Iron Sight Fix от grasscid](https://www.nexusmods.com/gta4/mods/15)| Исправляет неправильный прицел на пистолетах. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Исправляет сломанную текстуру на табличке "Waiting Room". |
	| [Sugar Chomps - Separate Signs от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Редактирует UV-мапку на вывеске Sugar Chomps для использования неиспользованной текстуры. |
	| [Luis' Helmet Reflections Fix от 6135](https://www.gtainside.com/en/gta4/skins/125863-luis-s-helmet-reflections-fix/) | Исправлено отражение на шлеме Луиса. |
	| [Luis' Bag Texture Fix от 6135](https://www.gtainside.com/en/gta4/skins/136118-luis-s-bag-texture-fix/) | Исправлены недостающие карты нормалей и спекуляров текстуры на сумке Луиса, улучшено качество текстур. |
	| [Johnny's Shoe Texture Fix от 6135](https://www.gtainside.com/en/gta4/skins/125196-johnny-s-shoe-texture-fix/) | Исправлены недостающие карты нормалей и спекуляров текстуры на обуви Джонни. |
	| [GTA Online QUB3D Background от Zolika1351](https://zolika1351.pages.dev/mods/ivqub3d)| Портированный фон QUB3D (без сетки) из GTA Online. |
	| [Xbox One/Series S+X Buttons от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| Более современные текстуры для кнопок контроллера. |
	| [Reduced Traffic Screech (Audio Tweak) от GladiTek](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | Уменьшает шум от визга транспорта до приятного, более естественного уровня. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)| Текстуры радиостанций в более высоком разрешении. |
=== "1.2.0.59"
	| Мод | Описание |
	| :-: | :------: |
	| [Radio Downgrader от Tomasak и других](http://downgraders.rockstarvision.com/)| Простой даунгрейдер радио. |
	| [FusionFix~1.96~ от ThirteenAG, Tomasak и других](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Главный мод сборки, в котором куча исправлений, а также выступает в качестве модлоадера вместе с [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader)<br>Включает [Shader Fixes Collection by Parallellines0451 и других](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection) и [Traffic Cops: Back in the Toolbooths от Olanov](https://www.gtainside.com/en/gta4/mods/187365-traffic-cops-back-in-the-tollbooths/).</br> |
	| [Console Visuals~1.3~ от nastyyaboi и других](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Сборник портированного визуала с консольной версии - от timecyc, до анимаций.<br>Использованные аддоны: Console Clothing, Console Fences, Console Trees(Console Leaves)</br> |
	| [Various Fixes~1.60~ от Attramet и других](https://gtaforums.com/topic/975211-various-fixes/)| Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
	| [Trilogy Characters Fixes~2023-07-28~ от TheYoshiPunch, (Japan) GTA Love, DizCo12, JohnnyK NeverDie и других](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/page/25/#comment-1072185890)| Крупный сборник фиксов для несостыковок между появлениями персонажей в IV и EFLC - плюс, несколько фиксов просто для моделек.<br>Использованный аддон: Niko's Original GTAIV Hair</br> |
	| [Improved Animations Pack~1.3~ от B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Фиксы для некоторых анимаций оружия, как задержка стрельбы. |
	| [IV Fixes and Improvements от Zolika1351 и других](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| Сборник фиксов и улучшений - список на сайте. Включены только старые `.img` исправления. |
	| [Fix Collection от iiCriminnaaL, nkjellman и меня](https://drive.google.com/file/d/13OgDDm0xakbdRONPlrnN5zRfshdAgwhd/view?usp=sharing) | Несколько исправлений из Responsivle Plus и Graphics Fix, а именно - `stipple.wtd`, `coronas.wtd`, `carcols.dat` и `cargrp.dat` и файлы, связанные с эффектами брызг дождя. Моя работа здесь заключается только в том, что я их собрал отдельно. |
	| [Project2DFX~4.5~ от ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Добавляет приятные огни в далеке ночью. ==Можно отключить, удалив файлы `IVLodLights`.== |
	| [Xbox Rain Droplets от ThirteenAG](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv)| Добавляет на экран красивые капельки воды. ==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.== |
	| [Restored Trees Position от Attramet](https://gtaforums.com/topic/984591-restored-trees-position/) | Восстановлено несколько деревьев, которые присутствовали только в бета-версии. |
	| [More Visible Interiors от Attramet](https://gtaforums.com/topic/974099-more-visible-interiors/) | Делает интерьеры более видимыми снаружи. |
	| [Vanilla Road Texture Enhancement by DayL](https://discord.gg/gZvZmFt2p7) | 2x AI апскейлинг для текстур дорог и растительности, а также сгенерированные карты нормалей и спекуляров. ==WIP==. |
	| [Project Glass by DayL](https://discord.gg/gZvZmFt2p7) | Добавляет кубические отражения в большинство стекол в мире, чтобы они больше не выглядели как прозрачный пластик. ==WIP==. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Улучшенные и портированные текстуры транспорта из GTA V и Max Payne 3. |
	| [Dodgy Doc - Higher Quality от donnits](https://gtaforums.com/topic/974798-donnits-bakery/) | Текстуры более высокого разрешения для Dodgy Doc. |
	| [High Quality Pigeons от Supreme Dear Leader](https://www.gtainside.com/gta4/mods/166924-high-quality-pigeons/) | Текстуры и модель более высокого качества для голубей. |
	| [Resized Blista Compact от Thundersmacker](https://www.gtainside.com/en/gta4/cars/188730-resized-blista-compact/) | Исправление модели для Blista Compact, придание ей правильных размеров и исправление ошибок моделирования. |
	| [Fixed LCPD Buffalo от Ooboy](https://www.gtainside.com/en/gta4/cars/181342-fixed-lcpd-buffalo/) | Исправлены ошибки в модели и текстуре полицейского Buffalo. |
	| [Player Outfit Texture Fixes от B Dawg](https://gtaforums.com/topic/925011-player-outfit-texture-fixes) | Исправлены зеленоватые текстуры одежды. |
	| [Fixed Suit Display in Perseus от _ys](https://gtaforums.com/topic/984565-iv-fixed-suit-display-in-perseus/) | Исправлено некорректное отображение костюмов в Perseus. |
	| [IV Bikers in Episodes voice sets fix от B Dawg](https://gtaforums.com/topic/992050-iv-bikers-in-episodes-voice-sets-fix/) | Исправляет набор голосов байкеров из IV. |
	| [Default Pistol Iron Sight Fix от grasscid](https://www.nexusmods.com/gta4/mods/15)| Исправляет неправильный прицел на пистолетах. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Исправляет сломанную текстуру на табличке "Waiting Room". |
	| [Sugar Chomps - Separate Signs от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Редактирует UV-мапку на вывеске Sugar Chomps для использования неиспользованной текстуры. |
	| [Luis' Helmet Reflections Fix от 6135](https://www.gtainside.com/en/gta4/skins/125863-luis-s-helmet-reflections-fix/) | Исправлено отражение на шлеме Луиса. |
	| [Luis' Bag Texture Fix от 6135](https://www.gtainside.com/en/gta4/skins/136118-luis-s-bag-texture-fix/) | Исправлены недостающие карты нормалей и спекуляров текстуры на сумке Луиса, улучшено качество текстур. |
	| [Johnny's Shoe Texture Fix от 6135](https://www.gtainside.com/en/gta4/skins/125196-johnny-s-shoe-texture-fix/) | Исправлены недостающие карты нормалей и спекуляров текстуры на обуви Джонни. |
	| [GTA Online QUB3D Background от Zolika1351](https://zolika1351.pages.dev/mods/ivqub3d)| Портированный фон QUB3D (без сетки) из GTA Online. |
	| [Menu Art Fix](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072165611) | Исправляет низкокачественные фоны главных меню в EFLC. |
	| [Xbox One/Series S+X Buttons от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| Более современные текстуры для кнопок контроллера. |
	| [Reduced Traffic Screech (Audio Tweak) от GladiTek](https://gtaforums.com/topic/990400-reduced-traffic-screech-audio-tweak/) | Уменьшает шум от визга транспорта до приятного, более естественного уровня. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)| Текстуры радиостанций в более высоком разрешении. |
	| [Improved Weapon Spec от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=107165200)| Текстуры спекулярных мапок для оружий в более высоком разрешении. |

## Дополнительные моды { data-search-exclude }
Эти моды не включены по умолчанию, но не требуют дополнительных действий для установки поверх архива.
=== "1.0.8.0"
	| Мод | Описание |
	| :-: | :------: |
	| [Оффициальный руссификатор (текст) от 1C SoftClub](https://drive.google.com/file/d/1GbOA3CBAQGgXW6SjODzd8G8Cj-a8G6dt/view?usp=drive_link)| Установка: распаковываем в папку с игрой, в Settings - Display - Language смените язык на Русский. |
	| [Radio Downgrader Addons](https://www.nexusmods.com/gta4/mods/234?tab=files) | Вы можете установить следующие аддоны: `Combine Old and New Songs on Vladivostok FM` и `No EFLC Music in GTA IV Radio`. <br>Установка: распакуйте скачанный аддон в папку с игрой.</br> | 
	| Настройки Liberty Tweaks | `Improved AI`(Улучшенный ИИ) и `Remove Weapons on Death`(Удаление оружий при смерти) были отключены - их можно вернуть в :material-file-cog:`LibertyTweaks.ini`, расположенном в :material-folder:==IVSDKDotNet\scripts==. Там же можно настроить FOV, а также изменить привязки клавиш для быстрого сохранения и убирания оружия в кобуру (по умолчанию ++f9++ и ++h++). |
	| [ColAccel от ThirteenAG](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Ускоряет загрузки в несколько раз, ==но может вызвать проблемы с памятью а также не кэширует моменты из сюжета(таких как сгоревший гараж)==.<br>Установка: скачиваем версию ==1.4==, распакуйте :material-file:`IV.EFLC.ColAccel.asi` в :material-folder:==plugins== или в папку с игрой</br> |
	| [Vanilla PC TLAD Noise от меня](https://drive.google.com/file/d/1zxCWhWQ4qP4rJvUablTGjfqpFUp3UOS3/view?usp=sharing) | Удаляет исправленный шум в TLAD из Shader Fixes, делая его идентичным ванильному шуму на ПК<br>Установка: Распаковать в папку с игрой.</br> |
	| [Aura от catsmackaroo, Nastyyaboi, ItsClockAndre и cubabori](https://gtaforums.com/topic/989259-aura/) | Графический мод, построенный на ванильном визуале.<br>Установка: Извлеките установленные файлы в :material-folder:==update==. ==Рекомендуется использовать с Vanilla PC TLAD Noise.==</br> | 
	| [Improved Vanilla Timecyc от pidarasnahui516](https://www.gtainside.com/gta4/mods/189357-improved-vanilla-timecyc-v1-1/) | Еще один Timecyc мод, построенный на ванильном визуале. <br>Установка: Извлеките :material-folder:==Main Files\\pc\\== в :material-folder:==update==. ==Рекомендуется использовать с Vanilla PC TLAD Noise.==</br> |
	| [Enhanced Minor Characters от Datalvarezguy](https://drive.google.com/file/d/19VffQ6h_6NKR1k6CLDV610DDei7RwK_5/view?usp=sharing) | [Страница мода](https://gtaforums.com/topic/978737-grand-theft-auto-iv-enhanced-minor-characters/). Заменяет ванильных педов в некоторых миссиях на авторское видение персонажей. <br>Установка: Распакуйте в папку с игрой.</br> |
	| [Console Visuals Addons](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | Вы можете добавить несколько аддонов, таких как консольные загрузочные экраны и прочее. Однако сначала проверьте, не установлен ли уже нужный вам аддон.<br>Установка: Скачайте версию Complete Edition и распакуйте желаемые папки ==update==.</br> |
	| [Better Wardrobes от Zolika1351](https://zolika1351.pages.dev/mods/ivwardrobe)| Заменяет неудобный шкаф на более приятный, однако некоторым он может оказаться неудобным а также ==мод разблокирует всю одежду с самого старта.==<br>Установка: Распакуйте :material-file:`WardrobeMod.asi` в папку с игрой.</br> |
	| [IV-Presence от ItsClockAndre](https://gtaforums.com/topic/975850-iv-presence/) | Добавляет Discord Rich Presence.<br>Установка: Из архива, переносим :fontawesome-solid-gears:`discord-rpc.dll` и :material-file:`IVPresence.asi` из :material-folder:==For GTA IV 1070 and 1080== в папку с игрой. Если возникают проблемы, также распакуйте :material-file:`IVPresenceDependenciesChecker.exe` с его конфигом, запустите и посмотрите, каких зависимостей вам не хватает.</br>|
	| [Текстуры кнопок Dualshock 4 от tehherb](https://www.gtagaming.com/360-to-ps4-controller-icons-f30380.html)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualshock 4.<br>Установка: В :material-folder:==modloader== измените в :material-file-edit:`modloader.ini` `DualshockButtons=1` на `0` в начале файла, а `XboxButtons=0` на `1`</br> |
	| [Текстуры кнопок Dualsense от COZlerCae](https://www.nexusmods.com/gta4/mods/286)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualsense.<br>Установка: В :material-folder:==modloader== измените в :material-file-edit:`modloader.ini` `DualsenseButtons=1` на `0` в начале файла, а `XboxButtons=0` на `1`</br> |

=== "1.2.0.59"
	| Название мода | Детали |
	| :-----------: | :----: |
	| [Radio Downgrader Addons](https://www.nexusmods.com/gta4/mods/234?tab=files) | Вы можете установить следующие аддоны: `Combine Old and New Songs on Vladivostok FM` и `No EFLC Music in GTA IV Radio`. <br>Установка: распакуйте скачанный аддон в папку с игрой.</br> | 
	| [ColAccel от ThirteenAG](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Ускоряет загрузки в несколько раз, ==но может вызвать проблемы с памятью а также не кэширует моменты из сюжета(таких как сгоревший гараж)==.<br>Установка: скачиваем версию ==1.5==, распакуйте :material-file:`IV.EFLC.ColAccel.asi` в :material-folder:==plugins== или в папку с игрой</br> |
	| [Vanilla PC TLAD Noise от меня](https://drive.google.com/file/d/1zxCWhWQ4qP4rJvUablTGjfqpFUp3UOS3/view?usp=sharing) | Удаляет исправленный шум в TLAD из Shader Fixes, делая его идентичным ванильному шуму на ПК<br>Установка: Распаковать в папку с игрой.</br> |
	| [Aura от catsmackaroo, Nastyyaboi, ItsClockAndre и cubabori](https://gtaforums.com/topic/989259-aura/) | Графический мод, построенный на ванильном визуале.<br>Установка: Извлеките установленные файлы в :material-folder:==update==. ==Рекомендуется использовать с Vanilla PC TLAD Noise.==</br> | 
	| [Improved Vanilla Timecyc от pidarasnahui516](https://www.gtainside.com/gta4/mods/189357-improved-vanilla-timecyc-v1-1/) | Еще один Timecyc мод, построенный на ванильном визуале.<br>Установка: Извлеките :material-folder:==Main Files\\pc\\== в :material-folder:==update==. ==Рекомендуется использовать с Vanilla PC TLAD Noise.==</br> |
	| [Enhanced Minor Characters от Datalvarezguy](https://drive.google.com/file/d/1gYIa6nVtoMj1ijksjagONA1KS5X2MpSj/view?usp=sharing) | [Страница мода](https://gtaforums.com/topic/978737-grand-theft-auto-iv-enhanced-minor-characters/). Заменяет ванильных педов в некоторых миссиях на авторское видение персонажей. <br>Установка: Распакуйте в папку с игрой.</br> |
	| [Console Visuals Addons](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition) | Вы можете добавить несколько аддонов, таких как консольные загрузочные экраны и прочее. Однако сначала проверьте, не установлен ли уже нужный вам аддон.<br>Установка: Скачайте версию Complete Edition и распакуйте желаемые папки ==update==.</br> |
	| [Текстуры кнопок Dualshock 4 от tehherb](https://www.gtagaming.com/360-to-ps4-controller-icons-f30380.html)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualshock 4.<br>Установка: в :material-folder:==update/pc/textures==, замените :material-file:`360_buttons.wtd`</br> |
	| [Текстуры кнопок Dualsense от COZlerCae](https://www.nexusmods.com/gta4/mods/286)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualsense<br>Установка: в :material-folder:==update/pc/textures==, замените :material-file:`360_buttons.wtd`</br>.

## Список изменений { data-search-exclude }
=== "1.0.8.0"
	Архив часто обновляется, ниже приведен список его изменений:

	* 27.09.2023 - Обновлены Setup Utility, ZolikaPatch, IV Tweaker, Liberty Tweaks. Добавлен Extra Options.
	* 21.09.2023 - Обновлен Various Fixes. Заменен Setup Utility на переписанную версию.
	* 16.09.2023 - Хотфикс: Удален :material-file:`IVMenuAPI.asi` который был включен по случайности.
	* 15.09.2023 - Обновлены FusionFix, ZolikaPatch, IV Tweaker, IV Fixes and Improvements, Liberty Tweaks, Radio Downgrader (что прилично уменьшило размер архива), Setup Utility. Добавлен IV Bikers in Episodes voice sets fix.
	* 08.09.2023 - Обновлен Various Fixes (должно исправить повреждение сохранений). Добавлен VAmbience.
	* 07.09.2023 - Обновлен FusionFix. Добавлены Reduced Traffic Screech и High Quality Pigeons.
	* 06.09.2023 - Обновлены ZolikaPatch, FusionFix - вместе с ним и Shader Fixes. Включен Setup Utility. Удален Traffic Cops in the Toolbooths - FusionFix теперь включает его. Удалены DXVK и commandline.txt, теперь их можно установить автоматически через :material-file-download:`GTAIVSetupUtility.exe`.
	* 28.08.2023 - Исправлена бесконечная загрузка на миссии Three Leaf Clover (нужно другое решение - на данный момент из-за этого в катсцене нету одного NPC). Исправлен мод Dodgy Doc HQ - теперь должен быть использован. Добавлено `dxvk.gplAsyncCache = true` в :material-file-cog:`dxvk.conf`. Удалено Better Wardrobes.
	* 26.08.2023 - Обновлены FusionFix, Project Glass, Xbox One/Series S+X Buttons. Добавлен Menu Art Fix. Перепакован Various Fixes, а также добавлены исправления от сообщества.
	* 18.08.2023 - Обновлены файлы Various Fixes. Исправлена модель клабхауса Angels of Death в TLAD. 
	* 17.08.2023 - Обновлен Project Glass. Добавлен More Visible Interiors. Немного изменены конфиги.
	* 12.08.2023 - Исправлены известные вылеты и софтлоки в TLAD и TBoGT. Ввостановлен трек из меню TBoGT.
	* 11.08.2023 - Исправлены вылеты (IV Tweaker из давнгрейдера являлся устаревшим). Обновлён FusionFix, Shader Fixes (вручную собрано). Немного изменён VehicleBudget. Изменен файл волос Нико для исправления визуальных проблем.
	* 10.08.2023 - Обновлены Downgrader, ZolikaPatch и Project Glass. 
	* 07.08.2023 - Обновлен FusionFix. 
	* 03.08.2023 - Добавлен Restored Trees Position. Перепакованы несколько файлов дабы избежать несовместимостей. Обновлён Console Visuals.
	* 02.08.2023 - Обновлены FusionFix, Trilogy Characters Fixes - также слегка перепакован.
	* 25.07.2023 - Обновлён Fix Collection. Небольшие изменения в .ini файлах. Добавлены Project Thunder, Restored Pedestrians, Various Pedestrian Actions.
	* 24.07.2023 - Перепакованы моды дабы использовать меньше папок. Добавлены улучшения текстур дорог, Project Glass (+освещение для автобусных остановок), Dodgy Doc - Higher Quality, Rescaled Blista Compact, Player Outfit Texture Fixes, LCPD Buffalo Fix, Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Fixed Suit Display и несколько исправлений позаимствованы из Responsive Plus.
	* 20.07.2023 - Изменен dxvk на dxvk-gplasync. Обновлён FusionFix.
	* 19.07.2023 - Обновлены Downgrader, ZolikaPatch, IV Tweaker, FusionFix, Shader Fixes. Добавлены Radio Downgrader, GTA Online QUB3D Background, Better Wardrobes, Traffic Cops in the Toolbooths, Xbox Rain Droplets, Fixed Pistol Sights. Добавлен Dualsense buttons в дополнительные моды. Удалены Pedestrians with Unused Clothing Restored и Varied Alderney State Trooper Ped из-за несовместимостей.
	* 15.07.2023 - Добавлен Liberty Tweaks.
	* 13.07.2023 - Исправлено исчезновение обьектов в кабинете Романа. Ограничение FPS в катсценах изменено на 32.
	* 12.07.2023 - Добавлены следующие моды: (обновлённый) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos In-Game, Higher Res Radio Logos Menu, Improved Weapon Spec. Various Fixes перемещён в папку update ради совместимости. Удалён TBoGT Vehicle Fixes из папки modloader - он уже включён в FusionFix. Удалён TBoGT Texture Quality Fix т.к. Various Fixes уже добавляет этот фикс. Удалён IV Presence. Обновлён ZolikaPatch.
	* 11.07.2023 - Исправил проблему с крашем в основной игре.
	* 10.07.2023 - Обновлён давнгрейдер. Добавлен порт FusionFix 1.60 от Zolika. Чуть позже: Исправил проблему с крашами в TLAD. Изменил файл волос Нико, теперь без визуальных проблем должны быть.
	* 09.07.2023 - Изменен давнгрейдер - теперь включен в архив. Убран IV Fixes and Improvements. Добавлен Various Fixes. Добавлены кнопки для Dualshock(опционально)
	* 08.07.2023 - Обновлён Shader Fixes. Убран Simple Traffic Loader. Полностью перепакованы моды для использования модлоадера.
	* 01.07.2023 - Обновлён Shader Fixes, некоторые моды перепакованы.
	* 30.06.2023 - Обновлён Shader Fixes.
	* 26.06.2023 - Создание архива.
=== "1.2.0.59"
  	Архив часто обновляется, ниже приведен список его изменений:

	* 21.09.2023 - Обновлен Various Fixes. Заменен Setup Utility на переписанную версию.
	* 15.09.2023 - Обновлены FusionFix, Radio Downgrader (что прилично уменьшило размер архива), Setup Utility. Добавлен IV Bikers in Episodes voice sets fix.
	* 08.09.2023 - Обновлен Various Fixes (должно исправить повреждение сохранений). Добавлены файлы которые отсутсвовали по таинственным причинам.
	* 07.09.2023 - Обновлен FusionFix. Добавлены Reduced Traffic Screech и High Quality Pigeons.
	* 06.09.2023 - Обновлен FusionFix - вместе с ним и Shader Fixes. Включен Setup Utility. Удален Traffic Cops in the Toolbooths - FusionFix теперь включает его. Удален DXVK, теперь его можно установить автоматически через :material-file-download:`GTAIVSetupUtility.exe`.
	* 28.08.2023 - Исправлен мод Dodgy Doc HQ - теперь должен быть использован. Добавлено `dxvk.gplAsyncCache = true` в :material-file-cog:`dxvk.conf`.
	* 26.08.2023 - Обновлен Project Glass. Добавлены исправления от сообщества в Various Fixes. Возвращена более новая версия Shader Fixes, т.к. я случайно её перезаписал в прошлом обновлении.
	* 22.08.2023 - Обновлены FusionFix, Xbox One/Series S+X Buttons. Добавлен Menu Art Fix.
	* 18.08.2023 - Обновлены файлы Various Fixes. Исправлена модель клабхауса Angels of Death в TLAD. 
	* 17.08.2023 - Обновлен Project Glass. Добавлен More Visible Interiors. Немного изменены конфиги.
	* 12.08.2023 - Исправлены известные вылеты и софтлоки в TLAD и TBoGT. Ввостановлен трек из меню TBoGT. 
	* 11.08.2023 - Обновлен Shader Fixes (вручную собрано). Немного изменен VehicleBudget. Изменен файл волос Нико для исправления визуальных проблем.
	* 10.08.2023 - Обновлен Project Glass.  
	* 07.08.2023 - Обновлен FusionFix. 
	* 03.08.2023 - Добавлен Restored Trees Position.
	* 02.08.2023 - Обновлены FusionFix, Trilogy Characters Fixes, Console Visuals.
	* 25.07.2023 - Обновлён Fix Collection. Небольшие изменения в .ini файлах.
	* 23.07.2023 - Исправлен приоритет для модов. Перепакованы моды дабы использовать меньше папок. Добавлены улучшения текстур дорог, Project Glass (+освещение для автобусных остановок), Dodgy Doc - Higher Quality, Rescaled Blista Compact, Player Outfit Texture Fixes, LCPD Buffalo Fix, Luis' Helmet Reflections Fix, Luis' Bag Texture Fix, Johnny's Shoe Texture Fix, Fixed Suit Display и несколько исправлений позаимствованы из Responsive Plus.
	* 20.07.2023 - Изменен dxvk на dxvk-gplasync. Обновлён FusionFix.
	* 19.07.2023 - Обновлены FusionFix и Shader Fixes. Добавлены Radio Downgrader, GTA Online QUB3D Background, Traffic Cops in the Toolbooths, Xbox Rain Droplets, Fixed Pistol Sights. Добавлен Dualsense buttons в дополнительные моды. Удалены Pedestrians with Unused Clothing Restored и Varied Alderney State Trooper Ped из-за несовместимостей.
	* 13.07.2023 - Исправлено исчезновение обьектов в кабинете Романа. Ограничение FPS в катсценах изменено на 32.
	* 12.07.2023 - Добавлены следующие моды: (обновлённый) IV Fixes and Improvements, Liberty Ferry Terminal - Waiting Room Sign Fix, Sugar Chomps - Separate Signs, Pedestrians with Unused Clothes Restored, Varied Alderney State Trooper Ped, Higher Res Radio Logos In-Game, Higher Res Radio Logos Menu, Improved Weapon Spec. Удалён TBoGT Texture Quality Fix т.к. Various Fixes уже добавляет этот фикс.
	* 10.07.2023 - Изменил файл волос Нико, теперь без проблем должны быть.
	* 09.07.2023 - Удалён IV Fixes and Improvements. Добавлен Various Fixes.
	* 08.07.2023 - Обновлён FusionFix, Shader Fixes, изменён конфиг DXVK, удалён dxgi.dll а также перепакованы некоторые моды.
	* 02.07.2023 - Перепакованы моды в более удобном формате.
	* 01.07.2023 - Обновлён Shader Fixes. Портированы моды с старых версий.
	* 30.06.2023 - Обновлены моды.
	* 27.06.2023 - Обновлены моды.
	* 26.06.2023 - Создание архива.

[:material-page-first:Предыдущая страница <br>Введение</br>](index.md){ .md-button } [Следующая страница:material-page-last: <br>Второстепенная настройка</br>](additional-setup.md){ .md-button .md-button--primary }