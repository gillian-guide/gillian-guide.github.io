title: FusionFix & Shader Fixes
description: Один из важных модов для вашей установки GTA IV который исправляет множество проблем с графикой и физикой

# FusionFix & Shader Fixes
!!! warning "Совместимость"
    Этот мод официально поддерживает только Complete Edition, но учитывая некоторые вещи вы можете использовать его и с патчами 1.0.8.0 и 1.0.7.0.
Данный проект направлен на исправление или устранение некоторых проблем в Grand Theft Auto IV. Вы можете прочитать список изменений [здесь](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/blob/master/readme.md). Также в состав входит [Shader Fixes](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection) с переключателями для его опций.

???+ info "Shader Fixes"
    Этот проект направлен на исправление и восстановление сломанных и отсутствующих шейдеров на PC-порте (все [отсюда](https://uk.libertycity.net/gta-4/articles/4346-gta-iv-complete-edition-xbox-protiv-pc.html) и даже больше). Вы можете прочитать список изменений [здесь](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/blob/main/README.md#feature-list).

## Демонстрация { data-search-exclude }
<iframe width="560" height="315" src="https://www.youtube.com/embed/UuXVYUGJ45Y?si=gjuLgquNDoHyJeLq&amp;start=132" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Установка { data-search-exclude }
=== "1.0.8.0"
    !!! warning "Совместимость"
        Оффициальная поддержка может помешать использованию GFWL. Сначала установите мод, после чего примените наверх [GFWL Patch](https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL) если используете GFWL.
    * Перейдите на страницу [релизов](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/).
    * Скачайте последнюю версию.
    * Распакуйте :material-zip-box:`GTAIV.EFLC.FusionFix.zip` в папку с игрой.
    * Переименуйте :fontawesome-solid-gears:`dinput8.dll` в `xlive.dll` если даунгрейдились и не используете GFWL. По надобности, замените.
    !!! warning "Если используете ZolikaPatch..."
        Установите [GFWL Patch](https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL).

        Откройте :material-file-cog:`ZolikaPatch.ini` и отключите следующие опции:

        - BuildingAlphaFix
        - EmissiveLerpFix
        - BikePhoneAnimsFix
        - BorderlessWindowed
        - CutsceneFixes
        - HighFPSBikePhysicsFix
        - HighFPSSpeedupFix
        - ReversingLightFix
        - OutOfCommissionFix
        - SkipIntro
        - SkipMenu

        Учтите, что это не полностью отключает функционал - подобный уже присутствует в FusionFix.
=== "1.2.0.59"
    * Перейдите на страницу [релизов](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix).
    * Скачайте последнюю версию.
    * Распакуйте :material-zip-box:`GTAIV.EFLC.FusionFix.zip` в папку с игрой.
    !!! tip ""
        Для удобства можно переместить файлы из :material-folder:==plugins== в папку с игрой.
!!! warning "Обновление"
    Если вы обновляете мод, не распаковывайте :material-file-cog:`GTAIV.EFLC.FusionFix.ini`. Вместо этого обратите внимаение, есть ли какие-нибудь новые опции отличаются от существующих, перенесите их в этом случае.

!!! tip "Влияние на производительность"
    Сам по себе, FusionFix не влияет на производительность. Но, несколько новых опций *могут* увеличить само влияние - понизьте настройки ниже если вы хотите увеличить производительность:

    - SSAA 2x
    - Shadow Filter (PCSS)
    - Качество теней
    - Улучшенные ночные тени
    - Depth of Field
    - Distant Blur
    - Motion Blur
    - Дистанция обзора/глубина детализации
    - Разрешение отражений
    - Console Shadows

!!! tip "Модлоадинг"
    Этот мод может быть использован для целей модлоадинга. См. раздел [модлоадинг](extras/modloading.md).

## Настройка
Вы можете отредактировать :material-file-cog:`GTAIV.EFLC.FusionFix.ini` или :material-file-cog:`GTAIV.EFLC.FusionFix.cfg`, если вам по какой-то причине нужно отредактировать файл вне игры. См. [список неигровых опций](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix?tab=readme-ov-file#details), если вам нужно их изменить.

[:material-page-first:Предыдущая страница <br>Важные моды</br>](index.md){ .md-button } [Следующая страница:material-page-last: <br>ZolikaPatch</br>](zolikapatch.md){ .md-button .md-button--primary }