# [FusionFix](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix>)

Этот проект нацелен на исправление большинства **графических и геймплейных проблем** и добавляет новые настройки графики. Список изменений можно прочитать в [репозитории](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/tree/master#coregameplay-changelog>).

---

## Демо

---

## Установка

1. Перейдите на [страницу последнего релиза](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest>).
2. Скачайте архив `GTAIV.EFLC.FusionFix.zip`.
3. Распакуйте архив в папку с игрой.

   - Если вы использовали Setup Utility на страницах [оптимизации](<https://gillian-guide.github.io/ru/optimization/index.md>) или [второстепенной настройки](<https://gillian-guide.github.io/ru/additional-setup/index.md>), лучше запустите его заново.
   - Посмотрите [оптимальные настройки графики для FusionFix](<https://gillian-guide.github.io/ru/additional-setup/#__tabbed_2_2>).

> [!NOTE]
>
> **Недостающие исправления**
>
> Устанавливая FusionFix на 1.0.8.0, вы лишаетесь части исправлений, а официальной поддержки от Fusion Team при возникновении проблем не будет. Имейте это в виду.

1. Перейдите на [страницу последнего релиза](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases/latest>).
2. Скачайте `GTAIV.EFLC.FusionFix.zip`.
3. Распакуйте архив в папку с игрой.
4. Переместите файлы из папки <mark>plugins</mark> в папку с игрой (не спрашивайте почему - так обычно повышается стабильность).

   - Переименуйте `dinput8.dll` в `xlive.dll`, **если не используете GFWL**. Замените файл, если потребуется.
   - Если вы использовали Setup Utility на страницах [оптимизации](<https://gillian-guide.github.io/ru/optimization/index.md>) или [второстепенной настройки](<https://gillian-guide.github.io/ru/additional-setup/index.md>), лучше запустите его заново.
   - Посмотрите [оптимальные настройки графики для FusionFix](<https://gillian-guide.github.io/ru/additional-setup/#__tabbed_2_2>).
   - **Не включайте `Check For Fusion Fix Updates`.**

> [!TIP]
>
> **Если для мультиплеера используется GFWL...**
>
> Сверху примените этот [патч](<https://github.com/gillian-guide/GTAIV.EFLC.FusionFix-GFWL/releases/latest>).
>
> Если вы играете **только в мультиплеер**, вместо него рассмотрите [патч только для мультиплеера](<https://github.com/SandeMC/GTAIV.EFLC.FusionFix-GFWLMin/releases/latest>) - он стабильнее.

### Дополнительные действия для пользователей Linux

1. Установите [Protontricks](<https://github.com/Matoking/protontricks>)
2. Откройте терминал и выполните следующую команду в префиксе GTA IV:

   ```bash
   protontricks 12210 -q d3dx9_43
   ```

   Если Protontricks установлен через Flatpak (а он так установлен, если вы запускаете Steam через Flatpak), выполните вместо нее эту:

   ```bash
   flatpak run com.github.Matoking.protontricks 12210 -q d3dx9_43
   ```
3. Дождитесь установки DirectX (это может занять несколько минут).

> [!TIP]
>
> **Модлоадинг**
>
> Этот мод можно использовать для модлоадинга. Подробности смотрите в разделе [Fusion Overloader](<https://gillian-guide.github.io/ru/extras/modloading/#fusion-overloader>).

---

## Настройка

Большая часть настроек доступна в настройках самой игры.

Если вам зачем-то нужно менять настройки вне игры, отредактируйте `GTAIV.EFLC.FusionFix.ini` или `GTAIV.EFLC.FusionFix.cfg`. Если нужно что-то подкрутить, смотрите [список настроек вне игры](<https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix?tab=readme-ov-file#details>).

---

## Навигация

- Если ваша **игра даунгрейднута**, продолжите с OpenPreCEPatch:
- Если нет, вместо него продолжите с Various Fixes:
