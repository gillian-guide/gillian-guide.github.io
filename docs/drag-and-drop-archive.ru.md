title: Готовый архив
description: Полноценный готовый архив для игры в желаемую версию GTA IV

# Готовый архив { data-search-exclude }
Вы можете выбрать архив в зависимости от желаемой версии - будь то 1.2.0.59 или 1.0.8.0(если вы используете версию [:material-steam:Steam](https://store.steampowered.com/app/12210/) или [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv), то в архив также входит даунгрейдер). Вы можете сравнить список модов [ниже](#_4) - 1.0.8.0 имеет больше модов, имейте это ввиду. В основном у вас не будет [ZolikaPatch](essential-modding/zolikapatch.md) и Liberty Tweaks.

### Примечания { data-search-exclude }
!!! info ""
	1. 1.2.0.59 это Complete Edition, т.е. последняя версия в [:material-steam:Steam](https://store.steampowered.com/app/12210/) или [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv). В нем убрана поддержка мультиплеера и Games for Windows - LIVE, при этом добавлены Rockstar Games Launcher (с его DRM) и оверлей Social Club (с его достижениями). ==Количество поддерживаемых модов в этой версии также значительно ограничено - большинство модов создано для версий 1.0.8.0 и 1.0.7.0==.
	2. 1.0.8.0 является последним патчем для дисковой/старой версии, с поддержкой ZolikaPatch и мультиплеера. Но, этот архив НЕ поддерживает какую-либо поддержку для Games for Windows - LIVE. Если вы хотите мультиплеер, перейдите к пунктам [даунгрейд](downgrading.md) и [мультиплеер](multiplayer.md). ==Эта версия лучше подходит для совместимости с модами==.
!!! warning ""
	Я сам не могу слишком часто обновлять архив - загляните на страницы и посмотрите, не было ли обновлений у модов, особенно у тех, что наверху.

	Убедитесь, что установлены последние [драйвера](../optimization/#_2).


## Установка { data-search-exclude }

=== "1.0.8.0"
	[:material-download-circle: Скачать](https://drive.google.com/file/d/1O1qD8ocbJ_fnERTvvVzyw6_bsw-k_evo/view){ .md-button .md-button--primary }
	
	Скачайте архив и просто распакуйте его содержимое в папку с игрой. После установки пройдите через [второстепенную настройку](additional-setup.md).
	!!! warning "Предупреждение"
		Архив дожлжен быть установлен поверх чистой, без модов установке Complete Edition из [:material-steam:Steam](https://store.steampowered.com/app/12210/). 
		
		Если вы используете версию [Rockstar Games Launcher](https://store.rockstargames.com/game/buy-grand-theft-auto-iv), не загружайте игру из самого лаунчера, а используйте :material-file:`PlayGTAIV.exe` - в противном случае файлы игры будут заменены.
		
		Какой-либо другой способ установки не поддерживается.
		
		Кроме того, я не буду поддерживать никаких дополнительных модификаций файлов, кроме уже перечисленных инструкций.
	??? info "Обновление"
		Если вы обновляете архив после его предварительной установки, сначала удалите :material-folder:==update== и :material-folder:==modloader==.
	??? warning "Если игра не запускается"
		Попробуйте установить :material-file-download:`vcredist_x86.exe` из папки с игрой.

		Ваш ПК, возможно, не поддерживает DXVK - удалите :fontawesome-solid-gears:`d3d9.dll` из папки с игрой или попробуйте async 1.10.3 из [дополнительных модов](#_5).
	??? warning "Моя игра нестабильна/случайно вылетает"
		Отключайте моды по одному, чтобы увидеть виновника, редактируя :material-file-edit:`modloader.ini` в :material-folder:==modloader== или удаляя моды в :material-folder:==update==. [Сообщите мне о проблеме, если вы ее обнаружите.](contact-me.md)
=== "1.2.0.59"
	[:material-download-circle: Скачать](https://drive.google.com/file/d/1eJ4cbVhJ4tnTGJByh_Lf4eS5SS2ShmHO/view){ .md-button .md-button--primary }

	Скачайте архив и просто распакуйте его содержимое в папку с игрой. После установки пройдите через [второстепенную настройку](additional-setup.md).
	!!! warning "Предупреждение"
		Архив дожлжен быть установлен поверх чистой, без модов установке Complete Edition из [:material-steam:Steam](https://store.steampowered.com/app/12210/). 
		
		Какой-либо другой способ установки не поддерживается.
		
		Кроме того, я не буду поддерживать никаких дополнительных модификаций файлов, кроме уже перечисленных инструкций.
	??? info "Обновление"
		Если вы обновляете архив после его предварительной установки, сначала удалите :material-folder:==update==.
	??? warning "Если игра не запускается"
		Ваш ПК, возможно, не поддерживает DXVK - удалите :fontawesome-solid-gears:`d3d9.dll` из папки с игрой или попробуйте async 1.10.3 из [дополнительных модов](#_5).
	??? warning "Моя игра нестабильна/случайно вылетает"
		Отключайте моды по одному, чтобы увидеть виновника, удаляя моды в :material-folder:==update==. [Сообщите мне о проблеме, если вы ее обнаружите.](contact-me.md)

## Список модов { data-search-exclude }
=== "1.0.8.0"
	| Название мода | Детали |
	| :-----------: | :----: |
	| [Radio Downgrader от Tomasak и других](http://downgraders.rockstarvision.com/)| Простой даунгрейдер радио. |
	| [Downgrader~v20~ от Zolika1351](https://zolika1351.pages.dev/mods/ivpatch/downgrading)| Простой даунгрейд до 1.0.8.0 с Ultimate ASI Loader, ZolikaPatch, SteamAchievements и IV Tweaker. |
	| [ZolikaPatch IV~7.61~ от Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| Первый основной мод в сборке: добавляет множество фиксов и исправлений - а также без него не запустится игра. |
	| [IV Tweaker~2.35~ от Zolika1351](https://zolika1351.pages.dev/mods/ivpatch)| Выступает основным модлоадером в сборке, а также позволяет увеличить лимиты для других модов. |
	| [Steam Achievements~v2~ от Zolika1351](https://gtaforums.com/topic/957432-steam-achievements-for-1070-1080/)| Позволяет получать достижения в :material-steam:Steam |
	| [FusionFix~1.63~ от ThirteenAG и других](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Главный мод сборки, в котором куча исправлений, а также выступает в качестве модлоадера вместе с [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader).<br>[Портировано Zolika1351'ом](https://zolika1351.pages.dev/mods/ivpatch/downgrading)</br>|
	| [Shader Fixes Collection~V109~ от Parallellines0451 и других](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection)| Сборник многочисленных фиксов шейдеров, от простого скейлинга до ввостановления их консольных версий. |
	| [DXVK~2.2~](https://github.com/doitsujin/dxvk)| Переводит DirectX 9 в Vulkan - метод оптимизации. ==Удалите :fontawesome-solid-gears:`d3d9.dll` и измените параметры в :material-file-cog:`dxvk.conf` на параметры запуска Proton, если вы используете Linux (или просто удалите файл)== |
	| [Liberty Tweaks~1.1~ от The Westside Minions & Коммьюнити моддинга GTA IV](https://gtaforums.com/topic/991160-liberty-tweaks/)| Мод с большим количеством quality-of-life изменений. |
	| [Various Fixes~1.5~ от Attramet и других](https://gtaforums.com/topic/975211-various-fixes/)| Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
	| [IV Fixes and Improvements~3.3~ от Zolika1351 и других](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| Сборник фиксов и улучшений - список на сайте. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Исправляет сломанную текстуру на табличке "Waiting Room". |
	| [Sugar Chomps - Separate Signs от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Редактирует UV-мапку на вывеске Sugar Chomps для использования неиспользованной текстуры. |
	| [Traffic Cops: Back in the Toolbooths от Olanov](https://www.gtainside.com/en/gta4/mods/187365-traffic-cops-back-in-the-tollbooths/)| Простой скрипт, который заменяет педов из платных кабинок на дорожных полицейских. |
	| [Better Wardrobes от Zolika1351](https://zolika1351.pages.dev/mods/ivwardrobe)| Заменяет неудобный шкаф на более приятный. |
	| [Characters Fixes~2023-06-09~ от TheYoshiPunch, (Japan) GTA Love и других](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/)| Крупный сборник фиксов для несостыковок между появлениями персонажей в IV и EFLC - плюс, несколько фиксов просто для моделек.<br>Использованный аддон: Niko's Original GTAIV Hair</br> |
	| [Project2DFX~4.3~ от ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Добавляет приятные огни в далеке ночью. ==Можно отключить, удалив файлы `IVLodLights`.== |
	| [Xbox Rain Droplets от ThirteenAG](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv)| Добавляет на экран красивые капельки воды. ==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.== |
	| [Console Visuals~1.2~ от nastyyaboi и других](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Сборник портированного визуала с консольной версии - от timecyc, до анимаций.<br>Использованные аддоны: Console Clothing, Console Fences, Console Trees(PC Leaves)</br> |
	| [Improved Animations Pack~1.3~ от B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Фиксы для некоторых анимаций оружия, как задержка стрельбы. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Улучшенные и портированные текстуры транспорта из GTA V и Max Payne 3. |
	| [GTA Online QUBE3D Background от Zolika1351](https://zolika1351.pages.dev/mods/ivqub3d)| Портированный фон QUB3D (без сетки) из GTA Online. |
	| [Default Pistol Iron Sight Fix от grasscid](https://www.nexusmods.com/gta4/mods/15)| Исправляет неправильный прицел на пистолетах. |
	| [Xbox One/Series S+X Buttons от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| Более современные текстуры для кнопок контроллера. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)| Текстуры радиостанций в более высоком разрешении. |
	| [Improved Weapon Spec от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=107165200)| Текстуры спекулярных мапок для оружий в более высоком разрешении. |
=== "1.2.0.59"
	| Название мода | Детали |
	| :-----------: | :----: |
	| [FusionFix~1.64~ от ThirteenAG и других](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Главный мод сборки, в котором куча исправлений, а также выступает в качестве модлоадера вместе с [Ultimate ASI Loader](../mod-dependencies/#ultimate-asi-loader) |
	| [Shader Fixes Collection~V109~ от Parallellines0451 и других](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection)| Сборник многочисленных фиксов шейдеров, от простого скейлинга до ввостановления их консольных версий. |
	| [DXVK~2.2~](https://github.com/doitsujin/dxvk)| Переводит DirectX 9 в Vulkan - метод оптимизации. ==Удалите :fontawesome-solid-gears:`d3d9.dll` и измените параметры в :material-file-cog:`dxvk.conf` на параметры запуска Proton, если вы используете Linux (или просто удалите файл)== |
	| [Various Fixes~1.5~ от Attramet и других](https://gtaforums.com/topic/975211-various-fixes/)| Крупный сборник фиксов разного характера - в основном, кривые текстуры карты. |
	| [IV Fixes and Improvements~3.3~ от Zolika1351 и других](https://gtaforums.com/topic/909155-iv-fixes-improvements/)| Сборник фиксов и улучшений - список на сайте. |
	| [Liberty Ferry Terminal - Waiting Room Sign Fix от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Исправляет сломанную текстуру на табличке "Waiting Room". |
	| [Sugar Chomps - Separate Signs от donnits](https://gtaforums.com/topic/974798-donnits-bakery/)| Редактирует UV-мапку на вывеске Sugar Chomps для использования неиспользованной текстуры. |
	| [Traffic Cops: Back in the Toolbooths от Olanov](https://www.gtainside.com/en/gta4/mods/187365-traffic-cops-back-in-the-tollbooths/)| Простой скрипт, который заменяет педов из платных кабинок на дорожных полицейских. |
	| [Characters Fixes~2023-06-09~ от TheYoshiPunch, (Japan) GTA Love и других](https://gtaforums.com/topic/927583-grand-theft-auto-iv-and-episodes-from-liberty-city-characters-fixes/)| Крупный сборник фиксов для несостыковок между появлениями персонажей в IV и EFLC - плюс, несколько фиксов просто для моделек.<br>Использованный аддон: Niko's Original GTAIV Hair<br>[Вручную портировано.](https://drive.google.com/file/d/19LA4e31Ibux3QpXo2PxHsjGu1xROtTG9/view?usp=drive_link)</br></br> |
	| [Xbox Rain Droplets от ThirteenAG](https://github.com/ThirteenAG/XboxRainDroplets/releases/tag/gtaiv)| Добавляет на экран красивые капельки воды. ==Можно отключить, удалив файлы `GTAIV.XboxRainDroplets`.== |
	| [Project2DFX~4.5~ от ThirteenAG](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtaiv)| Добавляет приятные огни в далеке ночью. ==Можно отключить, удалив файлы `IVLodLights`.== |
	| [Console Visuals~1.2~ от nastyyaboi и других](https://gtaforums.com/topic/989098-console-visuals-the-complete-edition)| Сборник портированного визуала с консольной версии - от timecyc, до анимаций.<br>Использованные аддоны: Console Clothing, Console Fences, Console Trees(PC Leaves)</br> |
	| [Improved Animations Pack~1.3~ от B Dawg](https://gtaforums.com/topic/958625-improved-animations-pack/)| Фиксы для некоторых анимаций оружия, как задержка стрельбы. |
	| [GTA Online QUBE3D Background от Zolika1351](https://zolika1351.pages.dev/mods/ivqub3d)| Портированный фон QUB3D (без сетки) из GTA Online. |
	| [Vehicle Pack~2.0~ - 15th Anniversary Edition от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/5/#comment-1072121736)| Улучшенные и портированные текстуры транспорта из GTA V и Max Payne 3. <br>[Вручную портировано.](https://drive.google.com/file/d/1rMgtpkMBoyoaaFwYTl1bPV5eWEJwXQ4q/view?usp=drive_link)</br> |
	| [Xbox One/Series S+X Buttons от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/page/4/#comment-1071669058)| Более современные текстуры для кнопок контроллера. |
	| [Higher Res Radio Logos In-Game](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071559765) и [Higher Res Radio Logos Menu от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=1071512871)| Текстуры радиостанций в более высоком разрешении. |
	| [Improved Weapon Spec от Ash_735](https://gtaforums.com/topic/887527-ash_735s-workshop/?do=findComment&comment=107165200)| Текстуры спекулярных мапок для оружий в более высоком разрешении. |

## Дополнительные моды { data-search-exclude }
Эти моды не включены по умолчанию, но не требуют дополнительных действий для установки поверх архива.
=== "1.0.8.0"
	| Название мода | Детали |
	| :-----------: | :----: |
	| [Оффициальный руссификатор (текст) от 1C SoftClub](https://drive.google.com/file/d/1GbOA3CBAQGgXW6SjODzd8G8Cj-a8G6dt/view?usp=drive_link)| Установка: распаковываем в папку с игрой, в Settings - Display - Language смените язык на Русский. |
	| Настройки Liberty Tweaks | `Improved AI`(Улучшенный ИИ) и `Remove Weapons on Death`(Удаление оружий при смерти) были отключены - их можно вернуть в :material-file-cog:`LibertyTweaks.ini`, расположенном в :material-folder:==IVSDKDotNet\scripts==. Там же можно настроить FOV, а также изменить привязки клавиш для быстрого сохранения и убирания оружия в кобуру (по умолчанию ++f9++ и ++h++). |
	| [ColAccel от ThirteenAG](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Ускоряет загрузки в несколько раз, ==но может вызвать проблемы с памятью а также не кэширует моменты из сюжета(таких как сгоревший гараж)==.<br>Установка: скачиваем версию ==1.4==, распакуйте :material-file:`IV.EFLC.ColAccel.asi` в :material-folder:==plugins== или в папку с игрой</br> |
	| [DXVK-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3)| Если у вас древняя видеокарта(как GTX 600 серии) и у вас не работает DXVK из основного архива, используйте на замену эту версию.<br>Установка: Из архива, переносим :fontawesome-solid-gears:`d3d9.dll` из :material-folder:==x32== в папку с игрой</br> |
	| [DXVK-async 1.10.1](https://github.com/Sporif/dxvk-async/releases/tag/1.10.1)| Если вы используете интегрированную графику от Intel, вы можете использовать эту версию DXVK.<br>Установка: Из архива, переносим :fontawesome-solid-gears:`d3d9.dll` из :material-folder:==x32== в папку с игрой</br> |
	| [Radio Downgrader](http://downgraders.rockstarvision.com/)| Возвращает удалённые треки - которые удалили в 2018 из-за лицензий - обратно в игру.<br>Установка: распакуйте архив в папку с игрой, откройте :fontawesome-solid-gears:`install.bat`, после того как консоль закроется - переносим :material-folder:==update== из желаемого варианта владивостока (:material-folder:==with new vladivostok== и :material-folder:==without new vladivostok== - в without не будет новых треков, появившихся после выреза)</br> |
	| [Текстуры кнопок Dualshock 4 от tehherb](https://www.gtagaming.com/360-to-ps4-controller-icons-f30380.html)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualshock 4.<br>Установка: В :material-folder:==modloader== измените в :material-file-edit:`modloader.ini` `DualshockButtons=1` на `0` в начале файла, а `XboxButtons=0` на `1`</br> |
	| [Текстуры кнопок Dualsense от COZlerCae](https://www.nexusmods.com/gta4/mods/286)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualsense.<br>Установка: В :material-folder:==modloader== измените в :material-file-edit:`modloader.ini` `DualsenseButtons=1` на `0` в начале файла, а `XboxButtons=0` на `1`</br> |

=== "1.2.0.59"
	| Название мода | Детали |
	| :-----------: | :----: |
	| [ColAccel от ThirteenAG](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/)| Ускоряет загрузки в несколько раз, ==но может вызвать проблемы с памятью а также не кэширует моменты из сюжета(таких как сгоревший гараж)==.<br>Установка: скачиваем версию ==1.5==, распакуйте :material-file:`IV.EFLC.ColAccel.asi` в :material-folder:==plugins== или в папку с игрой</br> |
	| [DXVK-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3)| Если у вас древняя видеокарта(как GTX 600 серии) и у вас не работает DXVK из основного архива, используйте на замену эту версию.<br>Установка: Из архива, переносим :fontawesome-solid-gears:`d3d9.dll` из :material-folder:==x32== в папку с игрой</br> |
	| [DXVK-async 1.10.1](https://github.com/Sporif/dxvk-async/releases/tag/1.10.1)| Если вы используете интегрированную графику от Intel, вы можете использовать эту версию DXVK.<br>Установка: Из архива, переносим :fontawesome-solid-gears:`d3d9.dll` из :material-folder:==x32== в папку с игрой</br> |
	| [Radio Downgrader](http://downgraders.rockstarvision.com/)| Возвращает удалённые треки - которые удалили в 2018 из-за лицензий - обратно в игру.<br>Установка: распакуйте архив в папку с игрой, откройте :fontawesome-solid-gears:`install.bat`, после того как консоль закроется - переносим :material-folder:==update== из желаемого варианта владивостока (:material-folder:==with new vladivostok== и :material-folder:==without new vladivostok== - в without не будет новых треков, появившихся после выреза)</br> |
	| [Текстуры кнопок Dualshock 4 от tehherb](https://www.gtagaming.com/360-to-ps4-controller-icons-f30380.html)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualshock 4.<br>Установка: в :material-folder:==update/pc/textures==, замените :material-file:`360_buttons.wtd`</br> |
	| [Текстуры кнопок Dualsense от COZlerCae](https://www.nexusmods.com/gta4/mods/286)| Заменяет текстуры кнопок Xbox 360 на кнопки Dualsense<br>Установка: в :material-folder:==update/pc/textures==, замените :material-file:`360_buttons.wtd`</br>.

## Список изменений { data-search-exclude }
=== "1.0.8.0"
	- Архив часто обновляется, ниже приведен список его изменений:
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
	- Архив часто обновляется, ниже приведен список его изменений:
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