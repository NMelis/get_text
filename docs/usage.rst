=============
Использование
=============

Чтобы скачать данные с сайта, нужно ввести в консоль команду::

    get_text <ссылка>

Пример::

    get_text https://habr.com/ru/post/444130/

На выход получим папка `habr.com/ru/post` и файл в нем `444130.txt` где будет заголовок и тело статьи

Запуск программы со своими настройками::

    get_text -s <yaml файл> https://habr.com/ru/post/444130/

<yaml файл> - в нем можно указать правила оформление и получение информации со страниц для каждого сайта отдельно

Пример yaml файла (settings.yaml) где будет указан параметр width (ширина строки)::

    # settings.yaml
    width: 100

Запускаем::

    get_text -s settings.yaml https://habr.com/ru/post/444130/

На выход получим файл 444130.txt в соответствующем папке на основе urla в котором строки не привышают в ширину 100 символов:


Возможные параметры для настройки::

    width: 100
    show_link: true\false
    sites:
        1tv.ru:
            title: h1.title,
            content: div.w_row>div>div
    template: |
        {{ news_title }}
        {% for _ in range(0, config['width']) %}-{% endfor %}
        {{ news_content }}
        {% for _ in range(0, config['width']) %}-{% endfor %}


Определение:
width - Ширина строчки в символах
show_link - Показывать ли ссылки (true - показывать, false - не показывать)
sites - пользовательские списки сайтов для которых стандарный парсинг не выдает нужный результат
    1tv.ru - (пример) - правила для сайта `https://1tv.ru`
        title - точный css селектор на заголовок статьи
        content - точный css селектор на содержимое статьи\новостя или на что то другое)



Алгоритм работы утилиты:
    1. Получение страницы с помощью библиотеки `requests`
    2. Получение объекта Beautiful Soup. Парсингом занимаеться библиотека `Beautiful Soup` (bs4)
    3. Удаление тегов, id и тегов с классами которые указаны в DEFAULT_SETTINGS (пример DEFAULT_SETTING указан ниже)
    4. Если программа запущена с пользовательскими настройкам и где указаны правила получение Заголовка и Содержимое статьи для сайта - будет получены содержимое указанных css селекторов
    5. Если в пользовательских настройках указан `template` - будет отредрирован информация на этом `template` иначе на `template` по умолчение
    6. Сохранение файла

DEFAULT_SETTINGS::

    "exclude_elements": {
            'class': [
                'header',
                'footer',
                'nav',
                'menu',
                'push',
                'socials',
                'sharing',
                'topics',
                '^hidden$'
                'hidden',
                'banner',
                '^ad$',
                'sidebar',
                'footer',
                'sidebars',
            ],
            'css_selectors': [
                'div.hidden'
            ],
            'tags': [
                'nav',
                'footer',
                'iframe',
                'canvas',
                '^header$',
                'footer',
            ],
            'id': ['footer', '^header', 'header'],
        },
