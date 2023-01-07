from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from dictionary.lexicon_ru import LEXICON_RU
from dictionary.lexicon_ru import CURRENCIES
from keyboards.keyboards import currency_kb
from keyboards.keyboards import change_currency_kb
from dictionary.lexicon_ru import STATES
from services.services import digit_check

# задается валюта по умолчанию
STATES['chosen_currency'] = 'gel'


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=currency_kb)


# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=currency_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
async def process_currency_answer(message: Message):
    await message.answer(text=LEXICON_RU['currency'], reply_markup=change_currency_kb)


async def process_choose_gel(message: Message):
    await message.answer(text=CURRENCIES['gel'], reply_markup=currency_kb)
    STATES['chosen_currency'] = 'gel'


async def process_choose_doll(message: Message):
    await message.answer(text=CURRENCIES['dollar'], reply_markup=currency_kb)
    STATES['chosen_currency'] = 'dollar'


async def process_choose_drum(message: Message):
    await message.answer(text=CURRENCIES['drum'], reply_markup=currency_kb)
    STATES['chosen_currency'] = 'drum'
    print(STATES)
    print(LEXICON_RU)


async def process_numbers_answer(message: Message):
    await digit_check(message)


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_currency_answer, text=LEXICON_RU['currency'])
    dp.register_message_handler(process_choose_gel, text=CURRENCIES['gel'])
    dp.register_message_handler(process_choose_doll, text=CURRENCIES['dollar'])
    dp.register_message_handler(process_choose_drum, text=CURRENCIES['drum'])
    dp.register_message_handler(process_numbers_answer)