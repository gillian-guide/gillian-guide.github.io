---
title: OpenPreCEPatch
description: Некоторые исправления для вашей даунгрейднутой копии, в основном для комфортной игры в мультиплеере.
---

# [OpenPreCEPatch](https://github.com/gillian-guide/IV.EFLC.OpenPreCEPatch)

!!! warning "Совместимость"
    Этот мод совместим со всеми даунгрейднутыми версиями, но не с Complete Edition. Пропустите этот мод, если не собираетесь делать даунгрейд - без [мультиплеера](../extras/multiplayer.md) улучшения незначительны.

Этот проект **улучшает основной опыт игры в мультиплеере, добавляет поддержку DLC в патчи PreCE и считается обязательным для даунгрейднутых версий**. Список изменений можно прочитать [здесь](https://zolika1351.pages.dev/mods/ivpatch).

---

<h2>Установка</h2> <a id="_2"></a>

1. Перейдите на страницу [релизов](https://github.com/gillian-guide/IV.EFLC.OpenPreCEPatch/releases/latest).
2. Скачайте последний релиз.
3. Распакуйте :material-zip-box:`OpenPreCEPatch.zip` в папку с игрой.

??? tip "ZolikaPatch"
    OpenPreCEPatch - экспериментальный преемник ZolikaPatch с открытым исходным кодом, который уже включает все его значимые функции, а также совместимость с FusionFix и патчи для известных проблем ZolikaPatch.

    Если же вы по каким-то причинам хотите установить именно ZolikaPatch, инструкция ниже:

    1. Перейдите на [Zolika1351's Zone](https://zolika1351.pages.dev/mods/ivpatch).
    2. Прокрутите страницу до конца и скачайте последнюю версию.
    3. Распакуйте :material-zip-box:`ZolikaPatch_vx_x.zip` в папку с игрой.
        - Компиляция мода с открытым исходным кодом доступна [здесь](https://github.com/gillian-guide/ZolikaPatch/releases/latest) - по поведению она ничем не отличается.
        - Если вы использовали Setup Utility на страницах [оптимизации](../optimization.md) или [второстепенной настройки](../additional-setup.md), лучше запустите его заново.
        - **НЕ** распаковывайте :material-file:`PlayGTAIV.exe` и :material-file:`IVMenuAPI.asi`. Второй удалите, если уже распаковали.

    <a id="incompatible-options"></a>

    !!! warning "Если используется FusionFix..."
        !!! tip "Setup Utility (**Только для Windows**)"
            [Setup Utility](../optimization.md#setup-utility) может сделать все это за вас автоматически.

        Откройте :material-file-cog:`ZolikaPatch.ini` и отключите следующие настройки:

        - BenchmarkFix
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
        - NoLODLightHeightCutoff
        - OutOfCommissionFix
        - PoliceEpisodicWeaponSupport
        - RemoveBoundingBoxCulling
        - RemoveUselessChecks
        - ReversingLightFix
        - SkipIntro
        - SkipMenu
        - SCOSignatureFix

        Учтите, что это ничего не ломает и не отключает, т.к. эти функции реализованы в FusionFix.

    !!! question "Что такое :material-file:`GFWLProtectionDisabler2019.asi`?"
        Этот файл нужен, чтобы GFWL не блокировал :material-file:`.asi` моды.

---

<h2>Настройка</h2> <a id="_3"></a>

Откройте :material-file-cog:`IV.EFLC.OpenPreCEPatch.ini` или :material-file-cog:`XLivelessAddon.ini` и настройте файл как нужно. У всех опций рядом есть пояснения.

---

<h2>Навигация</h2> <a id="_4"></a>

[:material-page-first:Предыдущая страница <br>FusionFix</br>](fusionfix.md){ .md-button } [Следующая страница:material-page-last: <br>Various Fixes</br>](various-fixes.md){ .md-button .md-button--primary }
