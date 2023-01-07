from aiogram.types import Message
from dictionary.lexicon_ru import STATES
import requests
import random


def is_float(num):
    print(num)
    try:
        float(num)
        return True
    except ValueError:
        return False


def currency():
    if STATES['chosen_currency'] == 'gel':
        return 27
    if STATES['chosen_currency'] == 'dollar':
        return 72
    if STATES['chosen_currency'] == 'drum':
        return 0.18


def ending(number):
    if int(number) % 10 == 0 or int(number) % 10 == 5 or int(number) % 10 == 6 or int(number) % 10 == 7 or int(
            number) % 10 == 8 or int(number) % 10 == 9:
        return 'рублей'
    elif int(number) % 10 == 1:
        return 'рубль'
    elif int(number) % 10 == 2 or int(number) % 10 == 3 or int(number) % 10 == 4:
        return 'рубля'


async def calculate(message: Message):
    number = int(message.text) * float(currency())
    await message.answer(text=f'{number} {ending(number)}')


async def digit_check(message: Message):
    if is_float(message.text):
        await calculate(message)
    else:
        await message.answer(text='Введите число')
