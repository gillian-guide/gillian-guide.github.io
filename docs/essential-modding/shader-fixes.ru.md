title: Shader Fixes
description: Один из важных модов для вашей установки GTA IV

# Shader Fixes

Этот проект направлен на исправление и восстановление сломанных и отсутствующих шейдеров на PC-порте (все [отсюда](https://uk.libertycity.net/gta-4/articles/4346-gta-iv-complete-edition-xbox-protiv-pc.html)). Вы можете прочитать список изменений [здесь](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/blob/main/README.md#feature-list).

## Установка
Вы можете установить этот мод отдельно, как часть [IV Tweaker](../../modloading/#iv-tweaker), как часть [модлоадера UAL](../../modloading/#ultimate-asi-loader) или обновить файлы в [FusionFix](fusionfix.md), который уже содержит этот мод

=== "Отдельно"
    - Инструкции:
        * Перейдите на страницу [релизов](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/releases).
        * Скачайте последнюю версию.
        * Распакуйте файлы из :material-folder:==1. Main== в папку с игрой, заменяя все файлы.
        ???+ tip "Консольная гамма"
            Если вы также хотите иметь консольную гамму, распакуйте файлы из :material-folder:==2. Addons\Console-like Gamma== в папку с игрой, заменяя все файлы.
            <figure markdown>
                ![Image title](assets/console-gamma.png)
                <figcaption></figcaption>
            </figure>

=== "Как часть модлоадера UAL | Обновление файлов FusionFix"
    - Инструкции:
        * Перейдите на страницу [релизов](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/releases).
        * Скачайте последнюю версию.
        * Распакуйте файлы из :material-folder:==1. Main== в :material-folder:==update==, заменяя все файлы.
        ??? tip "Консольная гамма"
            Если вы также хотите иметь консольную гамму ==не используя FusionFix==, распакуйте :material-folder:==2. Addons\Console-like Gamma== в :material-folder:==update==, заменяя все файлы.
            <figure markdown>
                ![Image title](assets/console-gamma.png)
                <figcaption></figcaption>
            </figure>

=== "Как часть IV Tweaker"
    !!! warning ""
        Это не рекомендуется из-за потенциальной несовместимости. Вместо этого используйте метод модлоадера UAL или [порт последнего FusionFix](fusionfix.md).

    - Инструкции:
        * Перейдите на страницу [релизов](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/releases).
        * Скачайте последнюю версию.
        * Создайте папку для мода в :material-folder:==modloader==.
        * Распакуйте файлы из :material-folder:==1. Main\common\shaders\win32-30== (или любой другой папки от туда) в папку для мода.
        !!! info ""
            Также вы можете скачать папку с модом [отсюда](https://zolika1351.pages.dev/mods/ivtweaker/downgrading) из optional mods и просто распаковать её.
        * Настройте :material-file-cog:`modloader.ini` по необходимости.

[:material-page-first:Предыдущая страница <br>ZolikaPatch</br>](fusionfix.md){ .md-button } [Следующая страница:material-page-last: <br>Мультиплеер</br>](../../multiplayer){ .md-button .md-button--primary }