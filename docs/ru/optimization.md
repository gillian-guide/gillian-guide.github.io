title: Оптимизация
description: Все про DXVK для GTA IV

# Оптимизация

Мы все знаем, насколько ужасной была оптимизация игры на момент релиза. К сожалению, у нас до сих пор нет универсального решения - но это не значит, что мы не можем улучшить ситуацию.

---

## Что такое DXVK?

[DXVK](https://github.com/doitsujin/dxvk) это слой совместимости, который преобразует вызовы DirectX API в Vulkan.

Конечно, это не магия для улучшения производительности, а скорее слой совместимости для Linux, но состояние GTA IV на ПК настолько ужасное, что поможет что-угодно - хотя и не всем - за счет улучшения повышение производительности на стороне ЦП за счет лучшей обработки вызовов drawcall.

??? question "Каких улучшений можно ждать от DXVK?"
    Сказать напрямую сложно, т.к. улучшения от DXVK полностью разные от одного ПК к другому. **Есть вероятность, что DXVK вам вообще не поможет, если у вас ГП и так на сотню загружен.** Так что единственный ответ - вы можете ожидать *какого-то* улучшения, если у вас нагрузка забита на ЦП.

    Однако при определенных условиях можно ожидать чего-то сопоставимого с этим тестом:
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mSSjw8uf5Rw;start=3" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; gyroscope; picture-in-picture; web-share;" allowfullscreen></iframe>

---

## Предварительные требования

!!! warning ""
    - Убедитесь, что у вас последние [драйвера](../preparation.md/#_4).
    - Если используете Windows, отключите `кэш шейдеров` в :material-steam: Steam, который находится в `Настройки` - `Загрузки`.
    - Если используете Linux, пропустите страницу до [настройки](#_7), т.к. Proton уже использьует DXVK.

---

## [Setup Utility](https://github.com/gillian-guide/GTAIVSetupUtilityWPF) (Автоматическая установка)

С помощью этого софта вы можете установить DXVK и [параметры запуска](../additional-setup.md/#_2) автоматически и без особых усилий. Она также позаботится о совместимости между FusionFix, ZolikaPatch и другими особенностями - вы можете прочитать список фич [здесь](https://github.com/gillian-guide/GTAIVSetupUtilityWPF?tab=readme-ov-file#features).

!!! info ""
    - Вы должны использовать тулзу заново **если вы позже совершите даунгрейд или установите FusionFix и/или ZolikaPatch.**
    - Вы не можете, да и не должны, использовать эту тулзу на Linux.

### Использование

1. Перейдите на [страницу последнего релиза](https://github.com/gillian-guide/GTAIVSetupUtilityWPF/releases/latest).
2. Скачайте :material-file-download:`GTAIVSetupUtilityWPF.exe`.
3. Запустите программу.
4. Нажмите `Open` и выберите вашу папку с игрой. Следуйте инструкциям в приложении, если появятся всплывающие окна.
5. Нажмите `Install DXVK` и `Setup launch options` в этой же последовательности.
    - Если вы знаете что делаете, можете вручную поменять какие-либо переключатели. Обычно, в этом нет нужды.
    - Если появятся какие-либо проблемы, [сообщите о них на Discord сервере](../../index.md/#navigation).

??? warning "Для пользователей 50-серии NVIDIA RTX"
    В настоящее время игра не запускается при установленном DXVK с последними драйверами. Обход следующий:

    1. Установите DXVK.
    2. Временно удалите/переименуйте :fontawesome-solid-gears:'dinput8.dll' из папки с игрой.
    3. Откройте командную строку от имени администратора и выполните следующую команду:

        ```bash
        reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v DevOverrideEnable /t REG_DWORD /d 1.
        ```

    4. Перезагрузите компьютер.
    5. Перейдите на последнюю [страницу релиза](https://github.com/marekzajac97/nvgpucomp32_patch) нужного патча.
    6. Скачайте файл :fontawesome-solid-gears:`nvgpucomp32.dll`. Убедитесь, что версия вашего драйвера совпадает с названием релиза.
    7. В папке с игрой создайте папки с названиями :material-folder: ==PlayGTAIV.exe.local== и :material-folder: ==GTAIV.exe.local== и поместите скачанный файл в обе папки.
    8. Запустите игру один раз.
    9. Убедившись, что игра загрузилась, восстановите :fontawesome-solid-gears:`dinput8.dll` в папку с игрой.
    10. Откройте командную строку от имени администратора и выполните следующую команду:

        ```bash
        reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v DevOverrideEnable /t REG_DWORD /d 0.
        ```
    11. Перезагрузите компьютер еще раз.

    При обновлении драйверов процедуру необходимо повторить (шаги 5-7 можно пропустить), пока NVIDIA не решит проблему.

После использования тулзы, вы можете спокойно приступить к оптимальным настройкам графики:

[Следующая страница:material-page-last: <br>Второстепенная настройка: Оптимальные настройки графики</br>](additional-setup.md/#_4){ .md-button .md-button--primary }

---

## Ручная установка { data-search-exclude }

=== "Последняя версия"
    ???+ warning "Требования"
        - Используйте эту версию если ваш ГП:
            - **NVIDIA**: ГП серии Maxwell (серия GeForce 800) или новее, плюс GTX 745, GTX 750 и GTX 750 Ti.
                - GeForce 810M, GeForce 820M, GeForce 825M, GTX 870M, GTX 880M, GeForce 910M и GeForce 920M не поддерживаются.
            - **AMD**: ГП или встройка серии GCN4 (серии RX400 и Vega) или новее.
            - **Intel**: Встройка серии Skylake (6-е поколение ЦП Intel Core) или новее. Все ГП Arc поддерживаются. Выборочные встройки могут быть ограничены до Legacy.
            - **Mac**: Mac на Intel с поддержкой Vulkan 1.3 (проверьте вручную, открыв командную строку и ввев `vulkaninfo`).

        Если вы не входите в этот список, проверьте версию Legacy. **Этот список применим только к Windows.**

    ---

    <h3>Инструкции</h3>

    1. Перейдите на [страницу последнего релиза](https://github.com/doitsujin/dxvk/releases).
    2. Скачайте архив :material-zip-box:`dxvk-x.x.tar.gz`.
    3. После скачивания, откройте архив и перейдите в папку ==dxvk-x.x\x32\\==.
    4. Распакуйте :fontawesome-solid-gears:`d3d9.dll` в папку с игрой.

    !!! question "Про патч `async`"
        DXVK, начиная от версии 2.0, добавили поддержку Graphics Pipeline Library, который, в контексте GTA IV, полностью удаляет фризы при создании шейдеров если ваш ГП поддерживает GPL и Fast Linking.

        Если у вас относительно современный ГП, эти фичи уже у вас должны быть, и если у вас нет частых микрофризов - они есть. **Если же у вас *есть* очень частые микрофризы на этой версии, проверьте, обновлены ли у вас драйвера, и если они обновлены, то используйте форк [dxvk-gplasync](https://gitlab.com/Ph42oN/dxvk-gplasync/-/releases) для уменьшения количества микрофризов.**
=== "Legacy"
    ???+ warning "Требования"
        - Вы можете использовать эту версию если ваш ГП:
            - **NVIDIA**: ГП серии Kepler (серия GeForce 600) или новее.
            - **AMD**: ГП или встройка серии GCN1 (серия Radeon HD 7700) или новее.
            - **Intel**: Встройка серии Skylake (6-е поколение ЦП Intel Core) или новее. Все ГП Arc поддерживаются. Выборочные встройки могут быть ограничены до DXVK 1.10.1.
            - **Mac**: Mac на Intel с поддержкой Vulkan 1.1 (проверьте вручную, открыв командную строку и ввев `vulkaninfo`).

        Если вы не входите в этот список, вы не можете использовать DXVK. **Этот список применим только к Windows.**

    ---

    <h3>Инструкции</h3>

    1. Перейдите на [страницу последнего релиза DXVK-Sarek](https://github.com/pythonlover02/dxvk-Sarek/releases/latest).
    2. Скачайте архив :material-zip-box:`dxvk-sarek-async-1.10.3.tar.gz`.
        - Если вы испытываете проблемы с этим форком, можете использовать [dxvk-async 1.10.3](https://github.com/Sporif/dxvk-async/releases/tag/1.10.3) или [официальный DXVK 1.10.3](https://github.com/doitsujin/dxvk/releases/tag/1.10.3).
    3. После скачивания, откройте архив и перейдите в папку :material-folder: ==dxvk-async-1.10.3\\x32\\==
    4. Распакуйте :fontawesome-solid-gears:`d3d9.dll` в папку с игрой.

??? question "Почему не :fontawesome-solid-gears:`dxgi.dll` или другие файлы из папки?"
    Игра использует графический API Direct3D 9. Другие `dll` для Direct3D 10 и Direct3D 11.

    В простых словах, игра не будет использовать любые другие файлы.

??? question "Почему :material-folder: ==x32==? Моя система 64-х битная"
    В этом случае, ваша система не имеет значения. Сама игра рассчитана на использование 32-х битных библиотек, а не 64-х битных.

    В простых словах, игра не будет использовать файлы из папки :material-folder: ==x64==

??? warning "Если возникли проблемы..."
    Попробуйте понизить версию на один или два релиза.

    Если игра вообще не запускайте, ваш ГП не поддерживает последнюю версию. Используйте замисть этой версии версию Legacy.

    Просмотрите [исправление проблем](../resources/troubleshooting.md).
??? warning "Для пользователей 50-серии NVIDIA RTX"
    В настоящее время игра не запускается при установленном DXVK с последними драйверами. Обход следующий:

    1. Установите DXVK.
    2. Временно удалите/переименуйте :fontawesome-solid-gears:'dinput8.dll' из папки с игрой.
    3. Откройте командную строку от имени администратора и выполните следующую команду:

        ```bash
        reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v DevOverrideEnable /t REG_DWORD /d 1
        ```

    4. Перезагрузите компьютер.
    5. Перейдите на последнюю [страницу релиза](https://github.com/marekzajac97/nvgpucomp32_patch) нужного патча.
    6. Скачайте файл :fontawesome-solid-gears:`nvgpucomp32.dll`. Убедитесь, что версия вашего драйвера совпадает с названием релиза.
    7. В папке с игрой создайте папки с названиями :material-folder: ==PlayGTAIV.exe.local== и :material-folder: ==GTAIV.exe.local== и поместите скачанный файл в обе папки.
    8. Запустите игру один раз.
    9. Убедившись, что игра загрузилась, восстановите :fontawesome-solid-gears:`dinput8.dll` в папку с игрой.
    10. Откройте командную строку от имени администратора и выполните следующую команду:

        ```bash
        reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v DevOverrideEnable /t REG_DWORD /d 0
        ```
    11. Перезагрузите компьютер еще раз.

---

### Настройка

Создайте файл :material-file-cog:`dxvk.conf` в папке с игрой и добавьте следующие строки с помощью любого текстового редактора:

``` { .cpp }
# maxFrameLatency используется для предотвращения или уменьшения случайных пропусков кадров и фризов. Эта опция устанавливает более строгую максимальную задержку кадров.
d3d9.maxFrameLatency = 1
# presentInterval используется для включения VSync. Мы будем использовать его в пользу игрового VSync. Так мы получим лучшую нагрузку на процессор.
d3d9.presentInterval = 1
# numBackBuffers может дополнительно улучшить стабильность FPS при использовании Vsync. Эта опция переопределяет количество обратных буферов для цепочки подкачки Vulkan.
d3d9.numBackBuffers = 3
```

Если используется `dxvk-async` или `dxvk-gplasync`, также добавьте следующие строки в тот же файл:

``` { .cpp }
# Следующие опции используются для включения async
dxvk.enableAsync = true
dxvk.gplAsyncCache = true
```

Если вас не устраивает скорость компиляции шейдеров, добавьте следующие строки и измените значения под ваше значение потоков на ЦП:

``` { .cpp }
dxvk.numAsyncThreads = 4
dxvk.numCompilerThreads = 4
```

Для более детальной настройки вы можете посмотреть полный список доступных опций [здесь](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf).

---

## Навигация

После выполнения оптимизации следует продолжить c второстепенной настройкой, чтобы завершить оптимизацию игры.

[:material-page-first:Предыдущая страница <br>Даунгрейдинг</br>](../downgrading/index.md){ .md-button } [Следующая страница:material-page-last: <br>Второстепенная настройка</br>](additional-setup.md){ .md-button .md-button--primary }
