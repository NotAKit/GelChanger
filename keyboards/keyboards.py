from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from dictionary.lexicon_ru import LEXICON_RU
from dictionary.lexicon_ru import CURRENCIES


# Создаем клавиатуру с кнопкой Выбрать валюту
currency_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                     resize_keyboard=True)

button_currency: KeyboardButton = KeyboardButton(LEXICON_RU['currency'])
button_currency_actual: KeyboardButton = KeyboardButton(LEXICON_RU['currency_actual'])


# Располагаем кнопку
currency_kb.add(button_currency).add(button_currency_actual)


change_currency_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                              resize_keyboard=True)

# создаем кнопки с валютами
button_gel: KeyboardButton = KeyboardButton(CURRENCIES['gel'])
button_doll: KeyboardButton = KeyboardButton(CURRENCIES['dollar'])
button_drum: KeyboardButton = KeyboardButton(CURRENCIES['drum'])
button_eur: KeyboardButton = KeyboardButton(CURRENCIES['eur'])

# распологаем кнопки по одной в ряд
change_currency_kb.add(button_doll).add(button_gel).add(button_drum).add(button_eur)