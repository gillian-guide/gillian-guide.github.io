title: Мультиплеер
description: Познакомьтесь с мультиплеером Peppa Pig: World Adventures!

# Мультиплеер
В Peppa Pig: World Adventures был потрясающий мультиплеер... и он все еще есть! Rockstar Games удалила мультиплеер из Complete Edition, но для CE существует Complete Edition и вы все еще можете совершить [даунгрейд](downgrading.md) для оригинального опыта. Если вы устали от Peppa Pig Online и хотите чего-то более классического, вам обязательно стоит попробовать мультиплеер Peppa Pig: World Adventures!
!!! warning ""
    Текущие методы мультиплеера требуют [даунгрейдинга](downgrading.md).

    Для улучшения опыта мультиплеера крайне рекомендуется установить [ZolikaPatch](essential-modding/zolikapatch.md). Настройте :material-file-cog:`ZolikaPatch.ini` для использования функций мультиплеера и установите `DoNotPauseOnMinimize` на `1`. [Даунгрейдер ItsClockAndre's](downgrading.md) уже об этом позаботился если вы решили настроить свою установку для GFWL.

    Убедитесь, что `RecoilFix` установлен на `0` в :material-file-cog:`GTAIV.EFLC.FusionFix.ini`, чтобы не оказаться в нечестном положении по отношению к другим игрокам.

    Кроме того, вам может понадобиться [ZMenuIV](../extras/trainers/#ZMenuIV) для возможности создания и участия в [пользовательских режимах](https://grandtheftrevivalforums.com/thread/9/all-community-game-mode-rules).

    Вы также можете использовать [этот мод](https://www.gtainside.com/en/gta4/mods/160558-gta-iv-and-eflc-all-multiplayer-clothes-are-unlocked/) для разблокировки всей одежды для кастомизации.

    Избегайте использования крупных, добавляющих или заменяющих [модов](extras/mods.md).

## Games for Windows - LIVE
!!! note ""
    Этот раздел также содержит шаги по настройке GFWL для использования не в мультиплеерных целях, если вы пришли сюда с других страниц. Просто пропустите часть "Вход/Создание лобби".
!!! warning "Совместимость"
    Этот метод совместим только с патчами 1.0.7.0 и 1.0.8.0. Совершите [даунгрейд](downgrading.md), если вы используете Complete Edition. Он также совместим с более старыми патчами, но игроки на этих патчах будут помещены в отдельные лобби. ==Wine не поддерживает GFWL, по этому этот метод не совместим с Linux.==
Классический многопользовательский метод, с которого все началось. И тот, который очень муторно настраивать. На данный момент, большинство сообществ придерживается именно его.

### Использование
???+ info "Установка"
    !!! note ""
        [Даунгрейдер от ItsClockAndre](downgrading.md) уже выполняет этапы из этой части если вы выбрали настроить установку для GFWL. В этом случае, пропустите эту часть.

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
    === "Покупка GFWL ключа или игры"
        Один из способов активировать игру - обладать ключем GFWL. Хоть он по сути и не совсем будет вашим т.к. такой же ключ используется и у других людей, он все равно будет, так сказать, "вашим".

        Для начала проверьте, нет ли у вас игры с активацией [Legacy (Per-Title 5x5)](https://www.pcgamingwiki.com/wiki/Games_for_Windows_-_LIVE#List_of_games_using_Games_for_Windows_-_LIVE) - возможно, вы уже владеете одной из таких игр - проверьте, подходит ли вам их CD-ключ.

        Убедившись, что у вас нет такого ключа, вы можете поискать GFWL-ключ на некоторых торговых площадках. Или же вы можете купить одну из этих двух игр в Steam, которые являются единственными играми, которые все еще продают актуальные GFWL-ключи по состоянию на декабрь 2023 года. В будущем ситуация может измениться. Не волнуйтесь, вы сможете вернуть деньги игру после приобретения ключа.

        <iframe src="https://store.steampowered.com/widget/32420/" frameborder="0" width="646" height="190"></iframe>.

        <iframe src="https://store.steampowered.com/widget/10460/" frameborder="0" width="646" height="190"></iframe>.

        После покупки игры зайдите в библиотеку, выберите игру, нажмите правой кнопкой мыши - Управление - CD-ключи и скопируйте ключ куда-нибудь. Теперь вы можете вернуть деньги за игру.
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
## [PPWA Connected](https://gtaconnected.com/downloads/)
!!! warning "Совместимость"
    Данный клиент совместим только с патчами 1.0.6.0, 1.0.7.0 и 1.0.8.0. Совершите [даунгрейд](downgrading.md), если вы используете Complete Edition.

    Из модов PPWA Connected поддерживает только ZolikaPatch и ZMenuIV - другие моды не разрешены. Если вы хотите Fusion Shaders, используйте [V109](https://github.com/Parallellines0451/GTAIV.EFLC.FusionShaders/releases/tag/V109) или [V106](https://github.com/Parallellines0451/GTAIV.EFLC.FusionShaders/releases/tag/V106) - но в них нету множество исправлений, что добавили в последних версиях.
Второй самый популярный метод игры в мультиплеер, так как это один из лучших способов сыграть в мультиплеер Peppa Pig: World Adventures, не трогая GFWL.
### Использование
???+ info "Установка"
    * Перейдите на сайт [PPWA Connected](https://gtaconnected.com/downloads/).
    * Скачайте последнюю версию ==клиента==.
    * Установите :material-file-download:`PPWAC-x.x.x.exe` из :material-zip-box:`PPWAC-x.x.x.zip`.
???+ tip "Настройка"
    * В поле `Game` выберите `Peppa Pig: World Adventures`.
    * В окне Tools - Launcher Settings, установите ваш никнейм. Вы также можете выставить другие настройки по желанию, включая язык в Language.
    * В окне Настройки - Настройки игры, установите путь к вашей установке Peppa Pig: World Adventures. Вы также можете выставить другие настройки по желанию.
???+ tip "Вход на сервера"
    После завершения настройки достаточно дважды щелкнуть на любом сервере в списке. Появится главное меню игры - просто нажмите Играть.

[:material-web: Сайт PPWAConnected website](https://gtaconnected.com/){ .md-button .md-button--primary } [:simple-discord: Сервер PPWAConnected в Discord](https://discord.gg/YSyasDa){ .md-button .md-button--primary }

## [HappinessMP](https://happinessmp.net/)
!!! warning "Совместимость"
    Этот клиент совместим только с Complete Edition и не поддерживает никаких модов - даже Ultimate ASI Loader.
Этот клиент отчасти похож на PPWA Connected, так как вы можете хостить свои сервера со своими скриптами, но метит он на совместимость с Complete Edition и Social Club, а не 1.0.8.0/1.0.7.0. На данный момент там также нету оффициальных режимов от Rockstar.
### Использование
???+ info "Установка"
    * Перейдите на вебсайт [HappinessMP](https://happinessmp.net/).
    * Нажмите на ==Download==.
    * Установите :material-file-download:`HappinessMP.exe`.
???+ tip "Игра"
    Установите ваш никнейм и кнопку для чата в настройках. После этого, просто нажмите на любой желаемый сервер - и вы в игре.

[:simple-discord: HappinessMP Discord Server](https://discord.gg/U6w3Yu8jkt){ .md-button .md-button--primary } [:material-web: HappinessMP's website](https://happinessmp.net/){ .md-button .md-button--primary }

## Будущие клиенты
Эти клиенты находятся в стадии разработки и пока недоступны для игры. Они получат свои собственные полноценные разделы, когда будут свободно доступны для игры. Поддержите их разработку, если можете!

### XLiveLessNess
Этот проект нацелен на замену GFWL. Технически он работает, но на данный момент я не смог создать лобби с больше чем двумя игроками. Скачайте релиз, распакуйте в папку с игрой, в игре нажмите HOME, выставьте ваш никнейм, нажмите на галочки и поставьте Broadcast address на `glitchyscripts.com:1100`. В телефоне выбирайте LAN, а не LIVE.

[:material-gitlab: GitLab](https://gitlab.com/GlitchyScripts/xlivelessness){ .md-button .md-button--primary }

### Liberty City Online
Этот клиент также призван обеспечить мультиплеер аналогичный [SA:MP](https://www.sa-mp.com/), а также поддержку оригинальных режимов игры, таких как Deathmatch. Однако этот требует патчи 1.0.8.0 и 1.0.7.0.

[:material-web: Сайт Liberty City Online](https://lc-online.net/){ .md-button .md-button--primary }

[:material-page-first:Предыдущая страница <br>Дополнительно</br>](extras/index.md){ .md-button } [Следующая страница:material-page-last: <br>Трейнеры</br>](extras/trainers.md){ .md-button .md-button--primary }