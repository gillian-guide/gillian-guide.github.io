title: Модлоадинг
description: Методы установки модов в GTA IV, позволяющие избежать замены внутренних файлов

# Модлоадинг
Большинство модов требуют замены внутренних файлов с помощью [OpenIV](openiv.md). Мы можем обойти это, используя модлоадер - или два!

## В чем разница между Fusion Overloader и IV Tweaker?
Хотя они и отличаются в некоторых отношениях, вы можете использовать оба, если вы используете 1.0.8.0 или 1.0.7.0. Например, Fusion Overloader может покрыть то, что не поддерживает IV Tweaker. Лично мне нравится загружать моды `.img` через IV Tweaker для удобства настройки, а любые другие файлы - через Fusion Overloader.

## [Fusion Overloader](../essential-modding/fusionfix.md)
!!! warning "Совместимость"
    Поддерживает Complete Edition и 1.0.8.0/1.0.7.0 при условии, что установлена последняя версия [FusionFix](../essential-modding/fusionfix.md).

    Хотя можно установить только [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader) (и последний [ZolikaPatch](../essential-modding/zolikapatch.md) для старых патчей) и опустить FusionFix, вы можете лишиться некоторых дополнительных функций, которые FusionFix реализует для него.
Этот модлоадер не такой продвинутый, как IV Tweaker, но может заменять большее количество файлов. Он работает, загружая файлы из :material-folder: ==update== вместо основных файлов игры, избегая удаления оригинальных файлов.

???+ info "Использование"

    !!! note "Установка модов, упакованных для Fusion Overloader"
        Скорее всего, они уже упакованы в папку :material-folder: ==update==. Просто забросьте эту папку в корневую папку игры.

    ??? "Установка модов с файлами, которые находятся в архивах `.img`"
        !!! warning "Примечание"
            Хотя вы *можете* обойтись без компиляции отдельных файлов (если, скажем, мод компилирует весь `vehicles.img`, а изменяет только одну машину), вы испортите любую совместимость с другими модами. Поэтому, пожалуйста, не делайте этого.

        1. Скомпилируйте все файлы, входящие в `.img`, в один архив `.img` (или несколько, если ваши архивы превышают `1.5GB`, чтобы избежать проблем), используя [OpenIV](openiv.md).
        2. Если мод объединяет эти файлы с файлами ванильной игры и нет возможности получить их отдельно, извлеките оба `.img` мода и ванильный `.img` и используйте любую тулзу для сравнения (лично я пользуюсь [WinMerge](https://winmerge.org/)), чтобы найти отличающиеся файлы. После этого вернитесь к пункту 1.
        3. Если у вас есть файлы, которые должны быть только в TLAD, TBoGT или IV, но не в другие длс, скомпилируйте для них отдельный файл `.img`.
        4. Создайте папку с названием вашего мода в :material-folder: ==update== (создайте папку, если она не существует).
        5. Закиньте скомпилированные файлы `.img` в эту папку.
        6. Если вам пришлось пройти через пункт 3, также создайте папки с названиями :material-folder: ==IV==, :material-folder: ==TLAD== или :material-folder: ==TBoGT== и бросьте туда соответствующие файлы `.img`.
        7. Если у вас есть несколько модов, которые заменяют похожие файлы, вы можете установить приоритет, сделав так, чтобы при сортировке по именам они отображались выше по возрастанию. Это можно сделать, добавив перед его именем число или символ (например, !).

    ??? "Установка модов с файлами другого типа"
        !!! предупреждение "Примечание"
            Под файлами другого типа подрузамевается буквально любые файлы на замену, которые попадают в папки :material-folder: ==pc==, :material-folder: ==common==, :material-folder: ==TLAD== или :material-folder: ==TBoGT==. При условии, что это не файлы `.img`.

            Размещение файлов в папках модов не сработает. По крайней мере, на момент написания.
        1. Пересоздайте структуру папок из ванильной в :material-folder: ==update==.
        2. Разместите файлы замены точно так же, как и в ваниле, только сделайте это в :material-folder: ==update==.
        3. Если два мода заменяют одни и те же файлы, используйте тулзу для сравнения (лично я пользуюсь [WinMerge](https://winmerge.org/)), чтобы объединить их.

    ??? warning "Ожидаемая структура папок"
        В этом примере Mod 2 более приоритетнее, чем Mod 1.

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
                        * :material-file:`Mod 2.TBoGTOnly.img`
                * :material-folder: ==common==\
                    * :material-folder: ==data==\
                        * :material-file:`WeaponInfo.xml`
                * :material-folder: ==TLAD==\
                    * :material-folder: ==common==\
                        * :material-folder: ==data==\
                            * :material-file:`WeaponInfo.xml`
## [IV Tweaker](https://zolika1351.pages.dev/mods/ivtweaker)
!!! warning "Совместимость"
    Только поддерживает 1.0.8.0 и 1.0.7.0. Совершите [даунгрейд](../downgrading.md), если вы используете Complete Edition.
У этого модлоадера есть несколько преимуществ, например, возможность внедрять больше файлов, чем просто `.img`, при этом оригиналы остаются нетронутыми. Он также позволяет увеличить лимиты.

???+ note "Установка"
    * Перейдите на [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivtweaker)
    * Прогортайте до конца страницы и скачайте архив.
    * Распакуйте :material-zip-box:`IVTweaker_vx.x.zip` в папку с игрой.

???+ info "Использование"

    ??? "Установка модов"
        !!! warning "Примечание"
            Хотя вы *можете* обойтись без компиляции отдельных файлов (если, скажем, мод компилирует весь `vehicles.img`, а изменяет только одну машину), вы испортите любую совместимость с другими модами. Поэтому, пожалуйста, не делайте этого.

        1. Скомпилируйте все файлы, входящие в `.img`, в один архив `.img` (или несколько, если ваши архивы превышают `1.5GB`, чтобы избежать проблем), используя [OpenIV](openiv.md).
        2. Если мод объединяет эти файлы с файлами ванильной игры и нет возможности получить их отдельно, извлеките оба `.img` мода и ванильный `.img` и используйте любую тулзу для сравнения (лично я пользуюсь [WinMerge](https://winmerge.org/)), чтобы найти отличающиеся файлы. После этого вернитесь к пункту 1.
        3. Если у вас есть файлы, которые должны быть только в TLAD, TBoGT или IV, но не в другие длс, скомпилируйте для них отдельный файл `.img`.
        - Вы также можете просто использовать файлы напрямую.
        4. Создайте папку с названием вашего мода в :material-folder: ==modloader== (создайте папку, если она не существует).
        5. Закиньте скомпилированные файлы `.img` в эту папку.
        6. Если вам пришлось пройти через пункт 3, также создайте отдельные папки для IV, TLAD и TBoGT и бросьте туда соответствующие файлы `.img`.
        7. Вы можете добавить :material-file:`GTAIVOnly`, :material-file:`TLADOnly` или :material-file:`TBoGTOnly`, если вам не нужно, чтобы мод загружался в любом другом DLC. В противном случае отредактируйте :material-file-cog:`modloader.ini` для определения приоритета и того, когда мод должен или не должен загружаться.

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

    ??? "Настройка модлоадера"
        Чтобы настроить модлоадер, отредактируйте :material-file-cog:`modloader.ini` в :material-folder: ==modloader==. Убедитесь, что вы установили правильный приоритет(чем выше число, тем выше приоритет), чтобы нежелательные моды не перекрывали другие моды. Убедитесь, что моды, которые должны вводиться в TBoGT или TLAD, отключены для IV (Ep0), моды для TBoGT отключены для TLAD (Ep1), а моды для TLAD отключены для TBoGT(Ep2). ==Это необязательно если вы оставили файлы :material-file:`GTAIVOnly`, :material-file:`TLADOnly` или :material-file:`TBoGTOnly`.== Если у вас возникли проблемы - поэкспериментируйте с отключением модов.
        ??? warning "Ожидаемая настройка"
            В качестве примера будет использован мод Improved Animations.

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
    ??? "Увеличение лимитов"
        Чтобы увеличить лимиты, отредактируйте :material-file-cog:`IVTweaker.ini` - это может понадобиться, если вы устанавливаете моды, например, изменяющие текстуры транспортных средств, так как вы можете столкнуться с такси-багом.

[:material-page-first:Предыдущая страница <br>OpenIV</br>](openiv.md){ .md-button } [Следующая страница:material-page-last: <br>Моды</br>](mods.md){ .md-button .md-button--primary }