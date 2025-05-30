title: Второстепенная настройка
description: Настройка параметров запуска и оптимальных настроек графики

# Второстепенная настройка

<div class="grid cards" markdown>

- Если вы попали сюда после установки готового архива или использования Setup Utility на Windows, **перейдите к оптимальным настройкам графики**:

    [Оптимальные настройки графики:material-page-last:](#__tabbed_2_2){ .md-button }

</div>

Если же вы попали сюда после чего-либо другого (включая установку архива на Linux), начните с **параметров запуска.**

---

## Параметры запуска

!!! tip "Setup Utility (**Только для Windows**)"
    [Setup Utility](../optimization.md/#setup-utility-automatic-installation) может автоматически настроить параметры запуска за вас.

### Ручная настройка

=== "1.2.0.59"
    1. Откройте свойства игры:
        - **:material-steam: Steam**: Нажмите правой кнопкой мыши на игре в библиотеке, нажмите `Свойства...` и найдите поле `Параметры запуска`.
        - **:simple-rockstargames: Rockstar Games Launcher**: Откройте страницу с игрой в библиотеке, откройте настройки и найдите поле `Параметры запуска`.
        - **Ярлык**: Нажмите правой кнопкой мыши по ярлыку, нажмите `Свойства` и найдите поле `Цель`.
    2. Вставьте туда следующее:

        ```text
        -norestrictions -nomemrestrict -managed
        ```

    3. Если установлен **FusionFix**, включите `Оконный режим` и `Оконный режим без рамки` в `Настройки` - `Игра` в игре.
=== "1.0.8.0"
    1. Создайте файл :material-file-cog:`commandline.txt` в папке с игрой.
    2. Откройте файл.
    3. Вставьте в него следующее:

        ```text
        -norestrictions
        -nomemrestrict
        -windowed
        -managed
        ```

    4. Если установлен **FusionFix**, `-windowed` может быть убран в пользу переключателей в самой игре.
    5. Если установлен **FusionFix** и/или **ZolikaPatch**, включите `Borderless Windowed` в `Настройки` - `Игра` в игре или `BorderlessWindowed` в :material-file-cog:`ZolikaPatch.ini` в зависимости от того, что из двух вы установите.
        - **Если не планируете ставить ни то, ни другое, уберите `-windowed`.**
        - Если установлены оба, включите только настройку от **FusionFix**.

???+ warning "Если используется DXVK..."
    - Уберите `-managed`.
    - Добавьте `-availablevidmem 3072.0` к списку настроек.
        - Замените значение на ваше значение видеопамяти в МБ если у вас меньше 3 ГБ видеопамяти. Но не делайте его выше.
        - Если используете версию старше 1.0.8.0, это значение некорректно работает. Поэкспериментируйте вручную и доберитесь как можно ближе к 3072 МБ (значение может выглядеть как 60.0, 80.0 и т.п.).
    - Если игра не дает использовать ваше разрешение или герцовку монитора в настройках, добавьте `-width`, `-height` и `-refreshrate` с вашими нативными значениями монитора.
        - Если это все еще не помогло, добавьте `d3d9.forceAspectRatio = 16:9` к :material-file-cog:`dxvk.conf`. Измените `16:9` на ваше *[точное](https://stevewadsworth.github.io/calculateAspectRatio/)* соотношение сторон если у вас не 16:9 монитор.
    - Если используете Windows, убедитесь, что отключили `кэш шейдеров`, который находится в `Настройки` - `Загрузки` в :material-steam: Steam.

??? abstract "Полный список доступных параметров запуска"
    Вы можете использваоть эти настройки для более детальной настройки или дебага.

    | Настройка | Описание |
    | --------: | :------- |
    | -help | Список доступных команд. |
    | -adapter | Используется указанный адаптер экрана. |
    | -autoconfig | Автоматически настраивает графические параметры в зависимости от характеристик компьютера. |
    | -availablevidmem | Устанавливает объем доступной физической видеопамяти. |
    | -benchmark | Запускает игру в режиме Benchmark и затем завершает ее. |
    | -detailquality | Устанавливает глубину детализации игры (0-99). |
    | -disableimposters | Отключает рендеринг ненастоящего траффика в далеке. |
    | -forcehighqualitymirrors | ? |
    | -forcer2vb | Принудительный рендеринг в Vertex Buffer. |
    | -frameLimit | Устанавливает настройку для V-Sync. |
    | -framelockinwindow | Заставляет framelock работать даже в окне. |
    | -fullscreen | Заставляет полноэкранный режим. |
    | -fullspecaudio | Принудительное использование высоко-качественного звука. |
    | -gpucount | Позволяет вручную установить количество GPU, если запрос не выполняется. |
    | -height | Устанавливает вертикальное разрешение. |
    | -managed | Использует управляемые ресурсы времени выполнения D3D. |
    | -memrestrict | Ограничивает объем доступной памяти, которую может использовать игра. |
    | -minspecaudio | Принудительное использование низко-качественного звука. |
    | -no_3GB | Отключает поддержку памяти 3 ГБ в 32-разрядных ОС, в которых установлено, что игры и приложения могут использовать такой объем памяти. |
    | -noBlockOnLostFocus | Запрещает игре блокировать обновление окна при потере фокуса.  |
    | -noprecache | Отключает предварительное кэширование ресурсов. |
    | -nomemrestrict | Отключает ограничение памяти. |
    | -nominimize | Отключает возможность восстановления игры из режима минимизации и изменения разрешения (уменьшает занимаемую системную память). |
    | -norestrictions | Отключает ограничения на настройки графики. |
    | -noswapdelay | Отключает задержку перед Present (отключает исправление hard present stalls). |
    | -notimefix | Отключает Time Fix. |
    | -novblank | Отключение вертикального бланкирования для V-Sync. |
    | -percentvidmem | Процент видеопамяти, который должен быть доступен для игры. |
    | -refreshrate | Устанавливает частоту обновления (установленные значения должны поддерживаться используемым монитором). |
    | -reserve | Устанавливает объем памяти, который будет использоваться другими программами. |
    | -reservedApp | Устанавливает объем памяти, который должен оставаться доступным в пространстве приложения. |
    | -renderquality | Настраивает анизотропную фильтрацию (0-4). |
    | -safemode | Устанавливает минимально возможные настройки графики игры. |
    | -shadowdensity | Настраивает ночные тени (0-16). |
    | -shadowquality | Устанавливает качество теней (0-4). |
    | -stereo | Устанавливает режим стерео рендеринга. Что опция делает - неизвестно; возможно, фича вообще не реализована. |
    | -texturequality | Устанавливает качество текстур игры (0-2). |
    | -unmanaged | Использует ресурсы, управляемые приложением. |
    | -usedirectinput | Позволяет использовать поддержку DirectInput наряду с поддержкой XInput. |
    | -viewdistance | Устанавливает расстояние обзора игры (0-99). |
    | -windowed | Устанавливает оконный режим. |
    | -width | Устанавливает разрешение по горизонтали. |

---

## Оптимальные настройки графики

!!! note ""
    Следующие настройки рассчитаны на [рекомендуемые требования по железу](index.md/#_3).

    Если вы попали сюда после установки архива, используйте вкладку FusionFix.

=== "Ванилла"
    | Настройка | Оптимальное значение | Описание |
    | :-------: | :------------------: | :------: |
    | Видеорежим | Ваше нативное разрешение (максимальное значение, обычно) | Эта настройка регулирует разрешение вашего монитора или, если стоит параметр запуска `-windowed`, размер игрового окна. |
    | Соотношение сторон | Авто | Эта настройка регулирет соотношение сторон экрана относительно разрешения вашего монитора. |
    | Качество текстур | Высокое | Эта настройка регулирует разрешение всех текстур. |
    | Разрешение отражений | Очень высокое | Эта настройка регулирует разрешение отражений (кроме отражений в воде). |
    | Качество воды | Среднее | Эта настройка регулирует плотность и интенсивность волн в воде и качество отражений в воде. <br>**Рекомендуется использовать *Среднее*, так как вода с этой настройкой менее 'раздутая' и более реалистичнее, а также ближе всего к нужному виду на консолях.** |
    | Качество теней | Высокое | Эта настройка регулирует разрешение и расстояние рендеринга теней.<br>**Среднее** и **низкое** очень сильно используют статические тени, что выглядит довольно убого. <br>***Очень высокое* слишком сильно сказывается производительности ради мелких улучшений и иногда тени выглядят сломанными.** |
    | Улучшенные ночные тени | Среднее | Эта настройка регулирует сколько элементов локального света (например, фар автомобиля) могут отбрасывать тени. Каждый уровень качества добавляет 4 дополнительные карты теней. Эта настройка не влияет на разрешение динамических теней. <br>**Настройки выше *Среднее* вызывают артефакты.** |
    | Качество фильтрации текстур | Анизотропная 16x | Эта настройка регулирует фильтрацией текстур. |
    | Дистанция обзора | Между 21 и 70 | Эта настройка регулирует основное расстояние рендеринга LOD для таких объектов, как здания и транспорт. Также влияет на расстояние рендеринга пропов.<br>**Установка значения выше *21* создаст резкие проявления объектов, а выше *70* нестабильность и артефакты, и негативное влияение на производительность.** |
    | Глубина детализации | Между 10 и 70 | Эта настройка регулирует расстояние вторичного рендеринга LOD для деталей в пропах.<br>**Установка значения выше *10* создаст резкие проявления объектов, а выше *70* нестабильность и артефакты.** |
    | Транспортный поток | До 70<br>100, если есть кастомный popcycle (архив) | Эта настройка регулирует количество транспорта по дорогах. <br>**Установка слишком высокого значения делает езду по дороге очень неприятной, особенно с нестабильным ИИ траффика, который иногда застревает даже на прямых дорогах и мостах.** |
    | Глубина поля наблюдения | Вкл<br>Откл если играете в 1280x720 | Эта настройка регулирует глубину резкости и размытие в движении (**Откл** - включено, **Вкл** - отключение).<br>**Если играете на разрешении выше 1280x720, *Откл* только блюрит изображение на ПК, а эффекты попросту не масштабируются по разрешению - из-за этого, оставьте настройку на *Вкл* если не играете в этом разрешении.**<br>Можно быстро переключать кнопкой ++p++ в игре.</br> |
    | Вертикальная синхронизация | Откл если используется DXVK<br>Вкл | Эта настройка регулирует вертикальную синхронизацию.<br>**Если используется [DXVK](optimization.md) с конфигурацией, поставьте настройку в игре на *Откл* в пользу DXVK. ==Также добавьте `d3d9.maxFrameRate = 60` к :material-file:`dxvk.conf` или ограничьте кадры другими способами до 60 или 30 во избежание [проблем с таймингом](https://github.com/GTAmodding/GTAIV-Issues-List/issues/112).==** AMD Fluid Motion Frames (если используется DXVK) или [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) может использоваться для искусственного увеличения частоты кадров. |
=== "FusionFix"
    !!! warning ""
        Следующие настройки требуют [FusionFix](../essential-modding/fusionfix.md).

    | Настройка | Оптимальное значение | Описание |
    | :-------: | :------------------: | :------: |
    | Видеорежим | Ваше нативное разрешение (максимальное значение, обычно) | Эта настройка регулирует разрешение вашего монитора или, если включена настройка `Оконный режим`, размер игрового окна. |
    | Соотношение сторон | Авто | Эта настройка регулирет соотношение сторон экрана относительно разрешения вашего монитора. |
    | Качество текстур | Высокое | Эта настройка регулирует разрешение всех текстур. |
    | Разрешение отражений | Очень высокое | Эта настройка регулирует разрешение отражений (кроме отражений в воде). |
    | Качество воды | Очень высокое | Эта настройка регулирует *только* разрешение отражений воды когда используется FusionFix. |
    | Качество теней | Очень высокое | Эта настройка регулирует разрешение и расстояние рендеринга теней.<br>**Если слишком сильно падает фпс, понизьте до *Высокое*.**<br>Настройка поглубже доступна в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Улучшенные ночные тени | Очень высокое | Эта настройка регулирует сколько элементов локального света (например, фар автомобиля) могут отбрасывать тени, а также само разрешение этих теней.<br>Настройка поглубже доступна в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Качество фильтрации текстур | Анизотропная 16x | Эта настройка регулирует фильтрацией текстур. |
    | Дистанция обзора | 25<br>До 70 | Эта настройка регулирует основное расстояние рендеринга LOD для таких объектов, как здания и транспорт. Также влияет на расстояние рендеринга пропов. <br>**Установка значения выше *25* создаст резкие проявления объектов, а выше *70* не имеет сущных улучшений.** |
    | Глубина детализации | 31<br>До 70 | Эта настройка регулирует расстояние вторичного рендеринга LOD для деталей в пропах.<br>**Установка значения выше *31* создаст резкие проявления объектов, а выше *70* не имеет сущных улучшений.** |
    | Транспортный поток | До 70<br>100, если есть кастомный popcycle (архив) | Эта настройка регулирует количество транспорта по дорогах. <br>**Установка слишком высокого значения делает езду по дороге очень неприятной, особенно с нестабильным ИИ траффика, который иногда застревает даже на прямых дорогах и мостах.** |
    | Вертикальная синхронизация | Откл если используется DXVK<br>Вкл | Эта настройка регулирует вертикальную синхронизацию.<br>**Если используется [DXVK](optimization.md) с конфигурацией, поставьте настройку в игре на *Откл* в пользу DXVK.** |
    | Солнечные лучи | По предпочтению | Эта настройка регулирует кастомные лучи солнца.<br>Настройка поглубже доступна в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Сглаживание | SMAA | Эта настройка регулирует сглаживание. |
    | Ограничитель кадров | 60<br>30 | Эта настройка регулирует ограничением кадров.<br>**Рекомдентуеся установить значение на 60 или 30 во избежание [проблем с таймингом](https://github.com/GTAmodding/GTAIV-Issues-List/issues/112), хотя сюжет может быть пройден и выше 60, если игнорировать баги. Вы, возможно, захотите понизить ограничение от 30 для миниигр.**<br>AMD Fluid Motion Frames (если используется DXVK) или [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) могут быть использованы для искусственного увеличения частоты кадров.<br>Настройка поглубже доступна в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | FOV | По предпочтению | Эта настройка регулирует игровым FOV с увеличением от значения по умолчанию в игре. |
    | Тени от фонарей | По предпочтению | Эта настройка регулирует тени от фонарей ценой возможного резкого проявления теней и ухудшенной производительности. |

    !!! note ""
        Следующие настройки находятся на вкладке `Экран`.

    | Настройка | Оптимальное значение | Описание |
    | :-------: | :------------------: | :------: |
    | Размытие при движении | По предпочтению | Эта настройка регулирует эффектом размытия при движении. |
    | Свечение | Вкл | Эта настройка регулирует свечение. |
    | Консольная гамма | По предпочтению | Эта настройка изменяет гамму для придания игре консольного вида.<br>**Игра никогда не должна была быть такой "белой", поэтому я рекомендую установить значение на *Вкл*.** |
    | Фильтр экрана | По умолчанию | Эта настройка позволяет переключать файл timecyc длч соотвествия другим фильтрам экрана (к примеру, фильтры TBoGT в IV или наоборот). |
    | Глубина резкости | По предпочтению | Эта настройка регулирует глубину резкости и позволяет использовать эффект только в катсценах. |
    | Освещение деревьев | По предпочтению | Эта настройка регулирует окружающую окклюзию растительности.<br>Настройка поглубже доступна в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Прозрачность деревьев | По предпочтению | Эта настройка регулирует прозрачность деревьев.<br>Настройка поглубже доступна в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. |
    | Глубина поля наблюдения | Вкл | Эта настройка регулирует сглаживание "сетчатых" и "точечных" объектов, чтобы уменьшить мерцание и ступенчатость. |

    !!! note ""
        Следующие настройки находятся на вкладке `Игра`.

    | Настройка | Оптимальное значение | Описание |
    | :-------: | :------------------: | :------: |
    | Оконный режим | Вкл | Эта настройка регулирует, находится ли игра в экслюзивном полноэкранном режиме или (безрамночном) оконном.<br>Безрамочный режим в основном более рекомендован, чем экслюзивный полноэкранный в пользу мультизадачности.  |
    | Оконный режим без рамки | Вкл если включен `Оконный режим`</br>Откл | Эта настройка регулирует, находится ли игра в обычном окне или безрамочном когда **включена** настройка `Оконный`. |
    | Автоматически ставить игру на паузу в фоне | Откл | Эта настройка регулирует, будет ли процесс игры "останавливаться" когда окно игры теряет фокусировку (альт-таббинг).<br>Рекомендуется ставить на **Выкл** во избежание потенциальных вылетов. |

=== "Идентичные к консоли"
    !!! info "Что это за настройки?"
        Эти настройки идентичны к консольной версии игры.

        Я не рекомендую играть с этими настройками, по этому этот список более к сведенью какие настройки наиболее аутентичны консольной версии.

    !!! warning ""
        Следующие настройки требуют [FusionFix](../essential-modding/fusionfix.md).

    | Настройка | Значение, идентичное к консоли | Описание |
    | :-------: | :----------------------------: | :------: |
    | Видеорежим | 1280x720 на X360<br>1152x640 на PS3 | Эта настройка регулирует разрешение вашего монитора или, если включена настройка `Оконный режим`, размер игрового окна. |
    | Качество текстур | Среднее | Эта настройка регулирует разрешение всех текстур. |
    | Разрешение отражений | Среднее | Эта настройка регулирует разрешение отражений (кроме отражений в воде). |
    | Качество воды | Среднее | Эта настройка регулирует *только* разрешение отражений воды когда используется FusionFix. |
    | Качество теней | Среднее (?) | Эта настройка регулирует разрешение и расстояние рендеринга теней. |
    | Улучшенные ночные тени | Откл | Эта настройка регулирует сколько элементов локального света (например, фар автомобиля) могут отбрасывать тени, а также само разрешение этих теней. |
    | Качество фильтрации текстур | Трилинейная | Эта настройка регулирует фильтрацией текстур. |
    | Дистанция обзора | 21 | Эта настройка регулирует основное расстояние рендеринга LOD для таких объектов, как здания и транспорт. Также влияет на расстояние рендеринга пропов. |
    | Глубина детализации | 10 | Эта настройка регулирует расстояние вторичного рендеринга LOD для деталей в пропах. |
    | Транспортный поток | 33 | Эта настройка регулирует количество транспорта по дорогах. |
    | Солнечные лучи | Откл | Эта настройка регулирует кастомные лучи солнца. |
    | Сглаживание | Н/П | Эта настройка регулирует сглаживание.<br>Игра использовала SSAA 2x на Xbox 360 и QAA на PS3, и ни одно из двух не доступно на ПК. |
    | Ограничитель кадров | 30 | Эта настройка регулирует ограничением кадров. |
    | FOV | По умолчанию (самое низкое значение) | Эта настройка регулирует игровым FOV с увеличением от значения по умолчанию в игре. |
    | Тени от фонарей | Вкл | Эта настройка регулирует тени от фонарей ценой возможного резкого проявления теней и ухудшенной производительности. |

    !!! note ""
        Следующие настройки находятся на вкладке `Экран`.

    | Настройка | Значение, идентичное к консоли | Описание |
    | :-------: | :----------------------------: | :------: |
    | Размытие при движении | Вкл | Эта настройка регулирует эффектом размытия при движении. |
    | Свечение | Вкл | Эта настройка регулирует свечение. |
    | Консольная гамма | Вкл | Эта настройка изменяет гамму для придания игре консольного вида. |
    | Фильтр экрана | По умолчанию | Эта настройка позволяет переключать файл timecyc длч соотвествия другим фильтрам экрана (к примеру, фильтры TBoGT в IV или наоборот). |
    | Глубина резкости | Очень высокое (?) | Эта настройка регулирует глубину резкости и позволяет использовать эффект только в катсценах. |
    | Освещение деревьев | Console | Эта настройка регулирует окружающую окклюзию растительности. |
    | Прозрачность деревьев | Console | Эта настройка регулирует прозрачность деревьев.|
    | Глубина поля наблюдения | Откл | Эта настройка регулирует сглаживание "сетчатых" и "точечных" объектов, чтобы уменьшить мерцание и ступенчатость. |

---

## Навигация

- Если вы попали сюда после установки архива, **поздравляю, вы заканчиваете здесь!**

- Если вы проходите через руководство вручную, продолжайте к **обязательным модам**.

[:material-page-first:Предыдущая страница <br>Оптимизация</br>](optimization.md){ .md-button } [Следующая страница:material-page-last: <br>Обязательные моды</br>](../essential-modding/index.md){ .md-button .md-button--primary }
