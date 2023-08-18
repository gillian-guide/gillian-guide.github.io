title: Shader Fixes
description: Один из важных модов для вашей установки GTA IV

# Shader Fixes
!!! warning "Compatibility" 
    Этот мод совместим с Complete Edition, а также патчами 1.0.7.0 и 1.0.8.0.

Этот проект направлен на исправление и восстановление сломанных и отсутствующих шейдеров на PC-порте (все [отсюда](https://uk.libertycity.net/gta-4/articles/4346-gta-iv-complete-edition-xbox-protiv-pc.html)). Вы можете прочитать список изменений [здесь](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/blob/main/README.md#feature-list).

## Установка { data-search-exclude }
Вы можете установить этот мод отдельно, как часть [IV Tweaker](../../extras/modloading/#iv-tweaker), как часть [модлоадера UAL](../../extras/modloading/#ultimate-asi-loader) или обновить файлы в [FusionFix](fusionfix.md), который уже содержит этот мод.

=== "Отдельно"
    * Перейдите на страницу [релизов](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/releases).
    * Скачайте последнюю версию.
    * Распакуйте файлы из :material-folder:==1. Main== в папку с игрой, заменяя все файлы.
    ???+ tip "Консольная гамма"
        Если вы также хотите иметь консольную гамму, распакуйте файлы из :material-folder:==2. Addons\Console-like Gamma== в папку с игрой, заменяя все файлы.
        <figure markdown>
            ![Консольная гамма](assets/console-gamma.png)
            <figcaption></figcaption>
         </figure>

=== "Как часть модлоадера UAL | Обновление файлов FusionFix"
    * Перейдите на страницу [релизов](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/releases).
    * Скачайте последнюю версию.
    * Распакуйте файлы из :material-folder:==1. Main== в :material-folder:==update==, заменяя все файлы.
    ??? tip "Консольная гамма"
        Если вы также хотите иметь консольную гамму ==не используя FusionFix==, распакуйте :material-folder:==2. Addons\Console-like Gamma== в :material-folder:==update==, заменяя все файлы.
        <figure markdown>
            ![Консольная гамма](assets/console-gamma.png)
            <figcaption></figcaption>
        </figure>

=== "Как часть IV Tweaker"
    !!! warning ""
        Это не рекомендуется из-за потенциальной несовместимости. Вместо этого используйте метод части модлоадера UAL или [порт последнего FusionFix](fusionfix.md).

    * Перейдите на страницу [релизов](https://github.com/Parallellines0451/GTAIV.ShaderFixesCollection/releases).
    * Скачайте последнюю версию.
    * Создайте папку для мода в :material-folder:==modloader==.
    * Распакуйте файлы из :material-folder:==1. Main\common\shaders\win32-30== (или любой другой папки от туда) в папку для мода.
    * Настройте :material-file-cog:`modloader.ini` по необходимости.

??? tip "Восстановление вида ванильного шума в TLAD"
    Если вам не нравится шум TLAD, который Shader Fixes исправляет, чтобы сделать его похожим на консольную версию, вы можете извлечь [этот архив](https://drive.google.com/file/d/1zxCWhWQ4qP4rJvUablTGjfqpFUp3UOS3/view?usp=sharing) поверх, чтобы вернуть ванильный вид. Файлы собраны для модлоадера UAL, но вы можете пересобрать их вручную.

[:material-page-first:Предыдущая страница <br>FusionFix</br>](fusionfix.md){ .md-button } [Следующая страница:material-page-last: <br>Мультиплеер</br>](../multiplayer.md){ .md-button .md-button--primary }