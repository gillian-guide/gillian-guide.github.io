title: ZolikaPatch
description: Несколько исправлений для даунгрейднутых версий, в основном ради мультиплеера.

# [ZolikaPatch](https://zolika1351.pages.dev/mods/ivpatch)

!!! warning "Совместимость"
    Этот мод совместим со всеми даунгрейднутыми версиями, но не Complete Edition. Пропустите этот мод если вы не собираетесь даунгрейдиться - его улучшения того не стоят если вы не играете в [мультиплеер](../extras/multiplayer.md).

Этот проект **улучшает работоспособность мультиплеера и считается обязательным для даунгрейднутых версией**. Обо всех изменениях можете почитать [здесь](https://zolika1351.pages.dev/mods/ivpatch).

---

<h2>Установка</h2> <a id="_2"></a>

1. Перейдите на [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch).
2. Прокрутите до конца страницы и скачайте последнюю версию.
3. Распакуйте :material-zip-box:`ZolikaPatch_vx_x.zip` в папку с игрой.
    - Рекомендуется заново использовать Setup Utility если вы использовали утилиту на страницах [оптимизации](../../optimization.md) или [второстепенной настройки](../../additional-setup.md).

<a id="incompatible-options"></a>

!!! warning "Если используется FusionFix..."
    !!! tip "Setup Utility (**Только для Windows**)"
        [Setup Utility](../optimization.md/#setup-utility-automatic-installation) может автоматически сделать все это за вас.

    Откройте :material-file-cog:`ZolikaPatch.ini` и отключите следующие настройки:

    - BikePhoneAnimsFix
    - BorderlessWindowed
    - BuildingAlphaFix
    - BuildingDynamicShadows
    - CarDynamicShadowFix
    - CarPartsShadowFix
    - CutsceneFixes
    - DoNotPauseOnMinimize
    - DualVehicleHeadlights
    - EmissiveLerpFix
    - EpisodicVehicleSupport
    - EpisodicWeaponSupport
    - ForceCarHeadlightShadows
    - ForceDynamicShadowsEverywhere
    - ForceShadowsOnObjects
    - HighFPSBikePhysicsFix
    - HighFPSSpeedupFix
    - HighQualityReflections
    - ImprovedShaderStreaming
    - MouseFix
    - NewMemorySystem
    - NoLiveryLimit
    - OutOfCommissionFix
    - PoliceEpisodicWeaponSupport
    - RemoveBoundingBoxCulling
    - ReversingLightFix
    - SkipIntro
    - SkipMenu

    Имейте ввиду, что это на самом деле не отключает и не ломает ничего, т.к. эти настройки уже встроены в FusionFix.

!!! question "Что за :material-file:`GFWLProtectionDisabler2019.asi`?"
    Этот файл является обязательным для предотвращения GFWL от блокировки модов :material-file:`.asi`.

---

<h2>Настройка</h2> <a id="_3"></a>

Откройте :material-file-cog:`ZolikaPatch.ini` и настройте файл по надобности. Все настройки имеют обьяснения рядом с ними.

---

<h2>Навигация</h2> <a id="_4"></a>

[:material-page-first:Предыдущая страница <br>FusionFix</br>](fusionfix.md){ .md-button } [Следующая страница:material-page-last: <br>Various Fixes</br>](various-fixes.md){ .md-button .md-button--primary }
