---
title: Модлоадинг
description: Уф, все оригинальные файлы на месте!
---

# Модлоадинг

Многие моды требуют заменять файлы игры через [OpenIV](../resources/openiv.md). Этого можно избежать с помощью модлоадера.

---

## [Fusion Overloader](../essential-modding/fusionfix.md)

!!! warning "Совместимость"
    Поддерживает и Complete Edition, и 1.0.8.0/1.0.7.0, если установлена последняя версия [FusionFix](../essential-modding/fusionfix.md).

Этот модлоадер работает так: файлы загружаются из папки :material-folder: ==update== *вместо* основных файлов игры, поэтому оригинальные файлы не заменяются.

### Установка модов, упакованных под Fusion Overloader

Скорее всего, они уже упакованы в папку :material-folder: ==update==. Просто закиньте эту папку в корневую папку игры.

---

### Установка модов с файлами, которые идут в архивы `.img`

Пример: мод требует положить файл в :material-file:`vehicles.img`.

!!! info "Для модов, которые предоставляют целиком архив `.img`"
    Если, скажем, мод собирает весь `vehicles.img`, а заменяет только одну машину - упаковывать нужно только эту отдельную машину. Можно, конечно, *не* отделять измененные файлы, но так вы сломаете совместимость с другими модами. Так что, пожалуйста, не делайте так.

    Если вы всё-таки хотите отделить измененные файлы, распакуйте архивы мода и ванильный в разные папки и сравните их чем-нибудь вроде [WinMerge](https://winmerge.org/).

1. Соберите все файлы, которые должны попасть в `.img`, в один архив `.img` (или несколько, если архивы превышают `1.5GB` - во избежание проблем) с помощью [OpenIV](../resources/openiv.md).
2. Если у вас есть файлы, которые должны внедряться только в TLAD, TBoGT или IV, а не в остальные (т.е. мод дает отдельные файлы для базовой IV и EFLC), соберите отдельный `.img` для каждой части.
3. Создайте в папке :material-folder: ==update== папку с названием вашего мода (если ее нет в папке с игрой, создайте).
4. Положите туда собранные `.img` файлы.
5. Если вы выполняли шаг 2, создайте еще папки :material-folder: ==IV==, :material-folder: ==TLAD== и :material-folder: ==TBoGT== и положите отдельные `.img` файлы туда.

!!! tip "Приоритет"
    Если у вас несколько модов, заменяющих одни и те же файлы, и нужна система приоритетов, можно добавить перед названием число или символ (например, !).

    Что выше в папке при сортировке по **имени (по возрастанию)** - то и в приоритете.

    ??? info "Ожидаемая структура папок"
        В этом примере Mod 2 должен иметь более высокий приоритет, чем Mod 1.

        * :material-folder: ==GTAIV==\
            * :material-folder: ==update==\
                * :material-folder: ==1 Mod 2==\
                    *  :material-file:`Mod2.ForEveryGame.img`
                * :material-folder: ==2 Mod 1==\
                    *  :material-file:`Mod1.ForEveryGame.img`
                    * :material-folder: ==IV==\
                        * :material-file:`Mod 1.IVOnly.img`
                    * :material-folder: ==TLAD==\
                        * :material-file:`Mod 1.TLADOnly.img`
                    * :material-folder: ==TBoGT==\
                        * :material-file:`Mod 1.TBoGTOnly.img`

---

### Установка модов с другими типами файлов

Пример: мод требует изменить :material-file:`gta.dat`.

Пример 2: мод требует изменить :material-file:`playerped.rpf` (сначала скопируйте ванильный файл и меняйте уже его).

!!! note ""
    Под другими типами файлов я имею в виду буквально любые заменяемые файлы, которые идут в :material-folder: ==pc==, :material-folder: ==common==, :material-folder: ==TLAD== или :material-folder: ==TBoGT==. Главное, чтобы это были не файлы `.img`.

    Просто положить файлы в папки модов не сработает.

1. Воссоздайте структуру папок из ванильной в :material-folder: ==update==.
2. Положите заменяемые файлы точно так же, как в ванили, только в :material-folder: ==update==.
3. Если два мода заменяют одни и те же файлы, объедините их с помощью инструмента сравнения (мне нравится [WinMerge](https://winmerge.org/)).

??? info "Ожидаемая структура папок"

    * :material-folder: ==GTAIV==\
        * :material-folder: ==update==\
            * :material-folder: ==common==\
                * :material-folder: ==data==\
                    * :material-file:`WeaponInfo.xml`
            * :material-folder: ==TLAD==\
                * :material-folder: ==common==\
                    * :material-folder: ==data==\
                        * :material-file:`WeaponInfo.xml`

---

## [IV Tweaker](https://zolika1351.pages.dev/mods/ivtweaker)

!!! warning "Совместимость"
    Поддерживает только 1.0.8.0 и 1.0.7.0.

У этого модлоадера есть несколько преимуществ перед Fusion Overloader: например, он умеет внедрять не только `.img`, но и другие файлы, при этом оригиналы остаются целы. Он также позволяет увеличивать лимиты.

### Установка

1. Перейдите на [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivtweaker)
2. Прокрутите страницу вниз и скачайте архив.
3. Распакуйте архив :material-zip-box:`IVTweaker_vx.x.zip` в папку с игрой.

---

### Установка модов

!!! warning "Для модов, которые предоставляют целиком архив `.img`"
    Если, скажем, мод собирает весь `vehicles.img`, а заменяет только одну машину - упаковывать нужно только эту отдельную машину. Можно, конечно, *не* отделять измененные файлы, но так вы сломаете совместимость с другими модами. Так что, пожалуйста, не делайте так.

    Если вы всё-таки хотите отделить измененные файлы, распакуйте архивы мода и ванильный в разные папки и сравните их чем-нибудь вроде [WinMerge](https://winmerge.org/).

1. Соберите все файлы, которые должны попасть в `.img`, в один архив `.img` (или несколько, если архивы превышают `1.5GB` - во избежание проблем) с помощью [OpenIV](../resources/openiv.md).
2. Если у вас есть файлы, которые должны внедряться только в TLAD, TBoGT или IV, а не в остальные, соберите для них отдельный `.img`.
    - Можно также пропустить оба шага выше и использовать обычные файлы.
3. Создайте в :material-folder: ==modloader== папку с названием вашего мода.
4. Положите туда собранные `.img` или обычные файлы.
5. Если вам пришлось выполнять шаг 3, создайте также отдельные папки для IV, TLAD или TBoGT и положите конкретные файлы туда.
6. Если мод не должен загружаться в других частях, можете добавить :material-file:`GTAIVOnly`, :material-file:`TLADOnly` или :material-file:`TBoGTOnly`. Иначе отредактируйте :material-file-cog:`modloader.ini`, чтобы задать приоритет и условия загрузки модов.

??? warning "Ожидаемая структура папок"

    * :material-folder: ==GTAIV==\
        * :material-folder: ==modloader==\
            * :material-folder: ==Mod1==\
                * :material-file:`IVAnims.ForEveryGame.img`
                * :material-file:`WeaponInfo.xml`
            * :material-folder: ==Mod1.TLADOnly==\
                * :material-file:`TLADOnly`
                * :material-file:`TLADAnims.img`
                * :material-file:`WeaponInfo.xml`
            * :material-folder: ==Mod1.TBoGTOnly==\
                * :material-file:`TBoGTOnly`
                * :material-file:`TBoGTAnims.img`

---

### Настройка модлоадера

Чтобы настроить модлоадер, отредактируйте :material-file-cog:`modloader.ini` в :material-folder: ==modloader==.

- Убедитесь, что правильно выставлен приоритет, чтобы ненужные моды не перекрывали другие (больше число - выше приоритет).
- Убедитесь, что моды, которые должны внедряться *только* в TBoGT или TLAD, отключены для IV (Ep0), моды *только* для TBoGT отключены для TLAD (Ep1), а моды *только* для TLAD отключены для TBoGT (Ep2).
    - Это не нужно, если вы оставили в папках файлы :material-file:`GTAIVOnly`, :material-file:`TLADOnly` или :material-file:`TBoGTOnly`.

??? warning "Ожидаемая конфигурация"
    Для примера возьмем мод Improved Animations.

    ``` { .ini }
    [DisabledMods]
    IVImprovedAnimations=0
    TLADImprovedAnimations=0
    TBoGTImprovedAnimations=0

    [Priorities]
    IVImprovedAnimations=1
    TLADImprovedAnimations=2
    TBoGTImprovedAnimations=2

    [DisabledForEp0]
    TLADImprovedAnimations=1
    TBoGTImprovedAnimations=1

    [DisabledForEp1]
    TBoGTImprovedAnimations=1

    [DisabledForEp2]
    TLADImprovedAnimations=1
    ```

!!! info "Увеличение лимитов"
    Чтобы увеличить лимиты, отредактируйте :material-file-cog:`IVTweaker.ini`.

    Это может понадобиться, если вы ставите моды, которые, например, меняют текстуры машин - для них стоит поднять лимиты бюджета транспорта.

---

## Навигация

[:material-page-first:Предыдущая страница <br>Дополнения</br>](index.md){ .md-button }
