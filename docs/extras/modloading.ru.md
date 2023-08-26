title: Модлоадинг
description: Методы установки модов в GTA IV, позволяющие избежать замены внутренних файлов

# Модлоадинг
Большинство модов требуют замены внутренних файлов с помощью [OpenIV](openiv.md). Мы можем обойти это, используя модлоадер - или два!

## В чем разница между ними?
Хотя они и отличаются в некоторых отношениях, вы можете использовать оба, если вы используете 1.0.8.0 или 1.0.7.0. Например, UAL'овский может покрыть то, что не поддерживает IV Tweaker.
???+ question "Сравнение"
    * :material-plus-minus: означает "Частично" или "Не так хорошо".

    | Преимущества | IV Tweaker | UAL'овский |
    | :--------: | :--------: | :---: |
    | Поддержка 1.0.8.0 и 1.0.7.0 | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Поддержка Complete Edition | :material-cancel: | :material-checkbox-marked-circle: |
    | Возможность внедрения файлов .img | :material-checkbox-marked-circle: | :material-checkbox-marked-circle: |
    | Возможность внедрения других файлов без замены | :material-checkbox-marked-circle: | :material-cancel: |
    | Есть возможность заменить большинство файлов не изменяя оригиналы | :material-cancel: | :material-checkbox-marked-circle: |
    | Простой .ini для настройки | :material-checkbox-marked-circle: | :material-cancel: |

## IV Tweaker
!!! warning "Совместимость"
    Только поддерживает 1.0.8.0 и 1.0.7.0. Совершите [даунгрейд](../downgrading.md), если вы используете Complete Edition.
Этот модлоадер превосходит UAL'овский по многим параметрам - особенно по возможности объединения различных файлов и наличию простого .ini файла для настройки. Он также позволяет увеличить лимиты для различных вещей - например, VehicleBudget, чтобы избежать такси-бага.

???+ note "Установка"
    * Перейдите на [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivtweaker)
    * Прогортайте до конца страницы и скачайте архив.
    * Распакуйте :material-zip-box:`IVTweaker_vx.x.zip` в папку с игрой.

???+ info "Использование"

    ??? "Установка модов"
        Для установки модов создайте папку с названием вашего мода в :material-folder:==modloader==. Затем создайте (с помощью OpenIV) или поместите `.img` или другие [поддерживаемые файлы](https://zolika1351.pages.dev/mods/ivtweaker) в эту папку. Вы также можете добавить :material-file:`GTAIVOnly`, :material-file:`TLADOnly` или :material-file:`TBoGTOnly` чтобы не морочиться с конфигом. ==Не используйте вложенные папки. Используйте разные папки для файлов, которые могут быть использованы как для IV, так и для EFLC DLC, чтобы избежать проблем с совместимостью==.
        ??? warning "Ожидаемая структура папок"
            В качестве примера будет использован мод Improved Animations.

            * :material-folder:==GTAIV==\
                * :material-folder:==modloader==\
                    * :material-folder:==IVImprovedAnimations==\
                        * :material-file:`IVAnims.img`
                        * :material-file:`WeaponInfo.xml`
                    * :material-folder:==TLADImprovedAnimations==\
                        * :material-file:`TLADOnly`
                        * :material-file:`TLADAnims.img`
                        * :material-file:`WeaponInfo.xml`
                    * :material-folder:==TBoGTImprovedAnimations==\
                        * :material-file:`TBoGTOnly`
                        * :material-file:`TBoGTAnims.img`
                            
    ??? "Настройка модлоадера"
        Чтобы настроить модлоадер, отредактируйте :material-file-cog:`modloader.ini` в :material-folder:==modloader==. Убедитесь, что вы установили правильный приоритет(чем выше число, тем выше приоритет), чтобы нежелательные моды не перекрывали другие моды. Убедитесь, что моды, которые должны вводиться в TBoGT или TLAD, отключены для IV (Ep0), моды для TBoGT отключены для TLAD (Ep1), а моды для TLAD отключены для TBoGT(Ep2). ==Это необязательно если вы оставили файлы :material-file:`GTAIVOnly`, :material-file:`TLADOnly` или :material-file:`TBoGTOnly`.== Если у вас возникли проблемы - поэкспериментируйте с отключением модов.
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
        Чтобы увеличить лимиты, отредактируйте :material-file-cog:`IVTweaker.ini` - это может понадобиться, если вы устанавливаете моды, например, изменяющие текстуры транспортных средств, так как вы можете столкнуться с ошибкой такси.

## Ultimate ASI Loader
!!! warning ""
    Для установки см. раздел [Ultimate ASI Loader](../../mod-dependencies/#ultimate-asi-loader).

!!! warning "Совместимость"
    Поддерживает Complete Edition. Может поддерживать 1.0.8.0/1.0.7.0 при использовании последней версии [ZolikaPatch](../essential-modding/zolikapatch.md).

Этот модлоадер не такой продвинутый, как IV Tweaker, но может заменять большее количество файлов.

???+ info "Использование"

    ??? "Установка модов"
        * Для модов `.img`, создайте папку с названием вашего мода в :material-folder:==update==. Затем создайте (с помощью OpenIV) или поместите `.img` в эту папку. ==Если ваш мод содержит файлы, которые могут быть использованы для IV и EFLC DLC, создайте подпапки :material-folder:`IV`, :material-folder:`TLAD` и :material-folder:`TBoGT` и поместите файлы .img отдельно, чтобы избежать проблем совместимости==.

        * Для модов, заменяющих другие файлы, создайте структуру папок, идентичную игровой, в :material-folder:==update== для заменяющих файлов и поместите заменяющие файлы в соответствующие папки. ==Не используйте папки модов==.
        ??? warning "Ожидаемая структура папок"
            В качестве примера будет использован мод Improved Animations.

            * :material-folder:==GTAIV==\
                * :material-folder:==update==\
                    * :material-folder:==ImprovedAnimations==\
                        * :material-folder:==IV==\
                            * :material-file:`IVAnims.img`
                        * :material-folder:==TLAD==\
                            * :material-file:`TLADAnims.img`
                        * :material-folder:==TBoGT==\
                            * :material-file:`TBoGTAnims.img`
                    * :material-folder:==common==\
                        * :material-folder:==data==\
                            * :material-file:`WeaponInfo.xml`
                    * :material-folder:==TLAD==\
                        * :material-folder:==common==\
                            * :material-folder:==data==\
                                * :material-file:`WeaponInfo.xml`

    ??? "Настройка модлоадера"
        Если вы хотите настроить приоритет, поставьте число в начале названия папки. Чем ниже число, тем выше приоритет.

        В настоящее время я не знаю других способов настройки модлоадера. [Свяжитесь со мной](../contact-me.md), если вы знаете другие способы.

[:material-page-first:Предыдущая страница <br>OpenIV</br>](openiv.md){ .md-button } [Следующая страница:material-page-last: <br>Моды</br>](mods.md){ .md-button .md-button--primary }