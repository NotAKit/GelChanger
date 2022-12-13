STATES: dict[str, str] = {
    'chosen_currency': 'gel'
}

CURRENCIES: dict[str, str] = {
                              'dollar': 'Доллар',
                              'gel': 'Лари',
                              'drum': 'Драмы'
                               }


LEXICON_RU: dict[str, str] = {'/start': f'Введите число для перевода в {CURRENCIES[STATES["chosen_currency"]]}',
                              '/help': '/хелп',
                              'currency': 'Выбор валюты',
                              }

