title: Мультиплеер
description: Познакомьтесь с мультиплеером GTA IV!

# Мультиплеер
В GTA IV был потрясающий мультиплеер... и он все еще есть! По крайней мере, для тех, кто [даунгрейдиться](downgrading.md), поскольку Rockstar Games удалила мультиплеер из Complete Edition. Если вы устали от GTA Online и хотите чего-то более классического, вам обязательно стоит попробовать мультиплеер GTA IV!
!!! warning ""
    Текущие методы мультиплеера требуют [даунгрейдинга](downgrading.md).

    Для улучшения опыта мультиплеера крайне рекомендуется установить [ZolikaPatch](essential-modding/zolikapatch.md). Настройте :material-file-cog:`ZolikaPatch.ini` для использования функций мультиплеера и установите `DoNotPauseOnMinimize` на `1`. [Даунгрейдер ItsClockAndre's](../downgrading/#itsclockandres) уже об этом позаботился если вы решили настроить свою установку для GFWL.

    Убедитесь, что `RecoilFix` установлен на `0` в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`, чтобы не оказаться в нечестном положении по отношению к другим игрокам.

    Используйте [JacksIVFixes](https://drive.google.com/file/d/1-qTmg28S6lHNI2qoYtCwdECOMb4hh9f2/view?usp=sharing), чтобы игра не считала ввод при сворачивании.

    Кроме того, вам может понадобиться [ZMenuIV](../extras/trainers/#ZMenuIV) для возможности создания и участия в [пользовательских режимах](https://grandtheftrevivalforums.com/thread/9/all-community-game-mode-rules).

    Вы также можете использовать [этот мод](https://www.gtainside.com/en/gta4/mods/160558-gta-iv-and-eflc-all-multiplayer-clothes-are-unlocked/) для разблокировки всей одежды для кастомизации.

    Избегайте использования крупных, добавляющих или заменяющих [модов](extras/mods.md).

## Games for Windows - LIVE
!!! note ""
    Этот раздел также содержит шаги по настройке GFWL для использования не в мультиплеерных целях, если вы пришли сюда с других страниц. Просто пропустите часть "Вход/Создание лобби".
!!! warning "Совместимость"
    Этот метод совместим только с патчами 1.0.7.0 и 1.0.8.0. Совершите [даунгрейд](downgrading.md), если вы используете Complete Edition. Он также совместим с более старыми патчами, но игроки на этих патчах будут помещены в отдельные лобби.
Классический многопользовательский метод, с которого все началось. И тот, который очень муторно настраивать. На данный момент, большинство сообществ придерживается именно его.

### Использование
???+ info "Установка"
    !!! note ""
        [Даунгрейдер от ItsClockAndre](../downgrading/#itsclockandre) уже выполняет этапы из этой части если вы выбрали настроить установку для GFWL. В этом случае, пропустите эту часть.

    * Убедитесь, что у вас нет устаревшей установки GFWL Marketplace и LIVE. Удалите их, если они есть.
    * Установите [Microsoft Visual C++ 2005 Redistributable **x86**](https://www.microsoft.com/en-us/download/details.aspx?id=26347).
    * Скачайте последний [GFWL Redistributables](https://community.pcgamingwiki.com/files/file/1012-microsoft-games-for-windows-live/).
    * Установите :material-file-download:`gfwllivesetup.exe`, :material-file-download:`wllogin_64.msi` и :material-file-download:`xliveredist.msi`.
    !!! question "Что такое Marketplace?"
        Вы получаете Marketplace, но не стоит открывать его или пытаться заставить его работать. Marketplace не является функциональным, но все же должен быть установлен для работы самого GFWL.
???+ info "Вход в аккаунт"
    !!! warning ""
        Используйте тот же аккаунт, что и для [Microsoft](https://microsoft.com/account) или [Xbox](https://xbox.com/account). Создайте его, если у вас его еще нет.

        [Полностью отключите 2FA на вашем аккаунте](https://account.microsoft.com/security) чтобы иметь возможность войти в аккаунт. Вы сможете включить его обратно после того, как войдете в систему и настроите автоматический вход.

    * Убедитесь, что в папке с игрой нет :fontawesome-solid-gears:`xlive.dll` переименуйте его в :fontawesome-solid-gears:`dinput8.dll` если есть.
    * Откройте игру.
    * Нажмите ++home++. Появится начальный экран.
    !!! note ""
        Если начальный экран не появился или у вас ошибка при запуске игры, перечитайте инструкции с самого начала.
    * Нажмите `Use Existing LIVE Profile` для перехода на окно входа в аккаунт.
    * Снимите флажки с `Save my e-mail address` и `Save my e-mail address and password`.
    * Введите данные от вашего [Microsoft](https://microsoft.com/account) или [Xbox](https://xbox.com/account) аккаунта для входа.  ==Для удобства и чтобы иметь возможность снова включить 2FA, установите флажок `Sign me in automatically`.==
    * Сделайте себе чашку чая или займитесь чем угодно в течение следующих 5-10 минут. Я не шучу - вход может занять столько времени. ==Не думайте, что зависло - это не так.==
    * Об активации читайте в следующей части.
???+ tip "Активация"
    Теперь у нас есть несколько способов активации игры.
    === "Покупка другой игры с GFWL"
        Как ни странно, это самый простой способ. Не волнуйтесь - впоследствии вы сможете вернуть деньги за игру, так что деньги не будут потрачены. Я рекомендую `FlatOut: Ultimate Carnage`, но подойдет и любая другая игра с GFWL с [Legacy (Per-Title 5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE).

        <iframe style="background: transparent; background-color: transparent;" allowtransparency="true" src="https://store.steampowered.com/widget/12360/943/" frameborder="0" width="646" height="190"></iframe>

        После покупки игры зайдите в библиотеку, выберите игру, нажмите правой кнопкой мыши - Управление - CD ключи и скопируйте ключ куда-нибудь. Теперь вы можете вернуть деньги за игру.
    === "Пробовать случайные ключи GFWL онлайн"
        Этот пункт не требует пояснений - просто поищите онлайн случайные ключи для GFWL - желательно от игр с [Legacy (Per-Title 5x5) activation](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) - они имеют несколько использований, так что вам может повезти. Эти два сервера в Discord могут вам помочь:

        [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary } [:simple-discord: Games For Windows Live Hub](https://discord.gg/d97u73k2TV){ .md-button .md-button--primary }
    === "Метод коммьюнити RevIVal"
        Канал с методом активации - `#gfwl-keys` (из соображений продвижения и уважения я не буду давать здесь прямую ссылку на него), но загляньте и на сам сервер, мы рады всем(однако, уважайте то, что сервер является англоязычным)!

        [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }
    После того, как вы приобрели ключ и активировали игру (опять же, это может занять еще 5-10 минут, так что сделайте чаю или что-нибудь еще), вы готовы играть!
???+ tip "Вход/Создание лобби"
    Либо воспользуйтесь опцией Сетевая игра - Похожие игроки - LIVE в игровом телефоне чтобы присоединиться к или создать лобби, либо добавьте друзей в оверлее ++home++ и присоединитесь к их лобби.

    - Обьяснение пунктов меню:
        * ==Быстрая игра== позволяет присоединиться к случайному существующему лобби *конкретного* режима.
        * ==Точный поиск== позволяет найти существующее лобби *любой* режима.
        * ==Создать игру== позволяет создать лобби самостоятельно.
    
    Если вы ищете людей для игры, посетите этот сервер в Discord(англо-язычный):

    [:simple-discord: Grand Theft RevIVal](https://discord.gg/Wn5eCWGcpb){ .md-button .md-button--primary }
???+ warning "Переадресация портов"
    Если у вас возникают проблемы с подключением к лобби (кикбаг, присоединение к пустому лобби), возможно, у вас проблемы с автоматической переадресацией портов (UPnP). Настройте проброс портов для следующих портов в настройках маршрутизатора (поищите в Интернете инструкции для конкретного маршрутизатора или провайдера, либо обратитесь к провайдеру):

    * TCP: `3074`, `80`, `88`
    * UDP: `3074`, `80`, `88`

    Если вы не можете выполнить проброс портов, используйте вместо этого VPN-сервис. Я рекомендую [Mullvad VPN](https://mullvad.net/en) (мне за это не платят).
## Grand Theft Auto Connected
!!! warning "Совместимость"
    Данный метод совместим только с патчами 1.0.7.0 и 1.0.8.0. Совершите [даунгрейд](downgrading.md), если вы используете Complete Edition.
Этот клиент не даст того же опыта, что и оригинальный мультиплеер, но на данный момент это один из лучших способов сыграть в мультиплеер GTA IV, не трогая GFWL.
### Использование
???+ info "Установка"
    * Перейдите на сайт [GTA Connected](https://gtaconnected.com/downloads/).
    * Скачайте последнюю версию ==клиента==.
    * Установите :material-file-download:`GTAC-x.x.x.exe` из :material-zip-box:`GTAC-x.x.x.zip`.
???+ tip "Настройка"
    * В поле `Game` выберите `Grand Theft Auto IV`.
    * В окне Tools - Launcher Settings, установите ваш никнейм. Вы также можете выставить другие настройки по желанию, включая язык в Language.
    * В окне Настройки - Настройки игры, установите путь к вашей установке GTA IV. Вы также можете выставить другие настройки по желанию.
???+ tip "Вход на сервера"
    После завершения настройки достаточно дважды щелкнуть на любом сервере в списке. Появится главное меню игры - просто нажмите Играть.
??? tip "Создание сервера"
    !!! warning ""
        Выполняйте все эти действия только в том случае, если у вас есть опыт работы с серверами.
    * Скачайте последнюю версию сервера с сайта [GTA Connected](https://gtaconnected.com/downloads/).
    * Распакуйте `GTAC-Server-Winxx-x.x.x.zip` в папку на выбор.
    * Настройте :material-file-cog:`server.xml` как необходимо. Используйте [эту страницу](https://wiki.gtaconnected.com/ServerConfiguration) для инструкций.
    * Запустите :material-file:`Server.exe` или :material-file:`Server` если ваш сервер на Linux.

## Будущие клиенты
Эти клиенты находятся в стадии разработки и пока недоступны для игры. Они получат свои собственные полноценные разделы, когда будут свободно доступны для игры. Поддержите их разработку, если можете!
### HappinessMP
Этот клиент призван обеспечить мультиплеер аналогичный [SA:MP](https://www.sa-mp.com/), а также поддержку оригинальных режимов игры, таких как Deathmatch. Для его работы потребуется Complete Edition и Social Club.

[:simple-discord: Сервер HappinessMP в Discord](https://discord.gg/U6w3Yu8jkt){ .md-button .md-button--primary } [:material-web: Сайт HappinessMP](https://happinessmp.net/){ .md-button .md-button--primary }

### Liberty City Online
Этот клиент также призван обеспечить мультиплеер аналогичный [SA:MP](https://www.sa-mp.com/), а также поддержку оригинальных режимов игры, таких как Deathmatch. Однако этот требует патчи 1.0.8.0 и 1.0.7.0.

[:material-web: Сайт Liberty City Online](https://lc-online.net/){ .md-button .md-button--primary }

[:material-page-first:Предыдущая страница <br>Дополнительно</br>](extras/index.md){ .md-button } [Следующая страница:material-page-last: <br>Трейнеры</br>](extras/trainers.md){ .md-button .md-button--primary }