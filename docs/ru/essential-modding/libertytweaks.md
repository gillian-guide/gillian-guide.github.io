title: Liberty Tweaks
description: Один из неплохих желаемых модов для вашей установки GTA IV улучшающих несколько аспектов игры

# [Liberty Tweaks](https://gtaforums.com/topic/991160-liberty-tweaks/)
!!! warning "Совместимость"
    Этот мод на данный момент поддерживает только 1.0.8.0/1.0.7.0, но поддержка Complete Edition в планах. ==Использование IV-SDK .NET невозможно на Proton, по этому совместимость этого мода с Linux отпадает.==
Этот проект направлен на улучшение некоторых аспектов игры. Вы можете посмотреть функционал в [теме на GTAForums](https://gtaforums.com/topic/991160-liberty-tweaks/).

## Демонстрация { data-search-exclude }
<iframe width="560" height="315" src="https://www.youtube.com/embed/NnbC1-kv8q0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Установка { data-search-exclude }
* Установите [IV-SDK .NET и Clonk's Coding Library](../../mod-dependencies/#iv-sdk-net).
* В :material-file-cog:`IVSDKDotNet/config.ini` отключите `PauseExecutionWhenNotInFocus` чтобы избежать некоторых проблем.
* Перейдите на последний [релиз](https://github.com/catsmackaroo/LibertyTweaks/releases/latest).
* Скачайте :material-zip-box:`LibertyTweaksx.x.zip`.
* Распакуйте содержимое :material-folder: ==1. Install== в папку с игрой. Замените файлы если необходимо.
* Настройте :material-file-cog:`IVSDKDotNet/scripts/LibertyTweaks.ini` по желании.

???+ question "Почему этот мод использует IV-SDK .NET а не ScriptHookDotNet?"
    ScriptHookDotNet - старый API который уже не обновляется, имеющий большое количество проблем (производительность, проблемы с дождем) которые исправлены не будут. IV-SDK .NET - новый API построенным на IV-SDK от Zolika1351 который метит заметнить ScriptHookDotNet без его проблем.

[:material-page-first:Предудыщая страница <br>Various Fixes</br>](variousfixes.md){ .md-button } [Следующая страница:material-page-last: <br>Characters Fixes</br>](charactersfixes.md){ .md-button .md-button--primary }
