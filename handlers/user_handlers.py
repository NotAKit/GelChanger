from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from dictionary.lexicon_ru import LEXICON_RU
from dictionary.lexicon_ru import CURRENCIES
from keyboards.keyboards import currency_kb
from keyboards.keyboards import change_currency_kb
from dictionary.lexicon_ru import STATES
from services.services import digit_check
import requests
from lxml import html
from lxml import etree

# задается валюта по умолчанию
STATES['chosen_currency'] = 'gel'


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=f'Введите число для перевода в {CURRENCIES[STATES["chosen_currency"]]}', reply_markup=currency_kb)


# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=currency_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
async def process_currency_answer(message: Message):
    await message.answer(text=f'Выбранная валюта {CURRENCIES[STATES["chosen_currency"]]}', reply_markup=change_currency_kb)


async def process_choose_gel(message: Message):
    await message.answer(text=f"Выбранная валюта: {CURRENCIES['gel']}", reply_markup=currency_kb)
    STATES['chosen_currency'] = 'gel'


async def process_choose_doll(message: Message):
    await message.answer(text=f"Выбранная валюта: {CURRENCIES['dollar']}", reply_markup=currency_kb)
    STATES['chosen_currency'] = 'dollar'


async def process_choose_drum(message: Message):
    await message.answer(text=f'Выбранная валюта: {CURRENCIES["drum"]}', reply_markup=currency_kb)
    STATES['chosen_currency'] = 'drum'

async def process_choose_eur(message: Message):
    await message.answer(text=f'Выбранная валюта: {CURRENCIES["eur"]}', reply_markup=currency_kb)
    STATES['chosen_currency'] = 'eur'


async def process_numbers_answer(message: Message):
    await digit_check(message)

async def process_currency_actual_answer(message: Message):
    url = "http://www.finmarket.ru/currency/rates/"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_ym_uid=1681144816958865930; _ym_d=1681144816; _ym_visorc=w; adtech_uid=d9a94228-c5cd-4e3b-aea8-1dde3e0e4fa7%3Afinmarket.ru; top100_id=t1.7919.724931502.1681144815722; last_visit=1681130415725%3A%3A1681144815725; t3_sid_7919=s1.1362791205.1681144815724.1681144815728.1.2; _ym_isad=1; tmr_lvid=c304bba83abeee660bc1ab447d43559b; tmr_lvidTS=1681144815966; tmr_detect=1%7C1681144815985',
        'If-Modified-Since': 'Sun, 10 Apr 2023 13:40:14 GMT',
        'Referer': 'https://www.google.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    tree = html.fromstring(response.text)
    usd = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[14]/td[4]')[0])[4:11].decode('utf-8').replace(',', '.')
    eur = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[15]/td[4]')[0])[4:11].decode('utf-8').replace(',', '.')
    gel = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[11]/td[4]')[0])[4:11].decode('utf-8').replace(',', '.')
    drum = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[3]/td[4]')[0])[4:11].decode('utf-8').replace(',', '.')

    # в строке вылезал лишний символ, пришлось его удалять
    usd = usd.replace('<', '')
    eur = eur.replace('<', '')
    gel = gel.replace('<', '')
    drum = drum.replace('<', '')


    await message.answer(text=f'Доллар: {round(float(usd), 2)}')
    await message.answer(text=f'Евро: {round(float(eur), 2)}')
    await message.answer(text=f'Лари: {round(float(gel), 2)}')
    await message.answer(text=f'Драммы: {round(float(drum)/100, 2)}', reply_markup=currency_kb)



# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_currency_answer, text=LEXICON_RU['currency'])
    dp.register_message_handler(process_choose_gel, text=CURRENCIES['gel'])
    dp.register_message_handler(process_choose_doll, text=CURRENCIES['dollar'])
    dp.register_message_handler(process_choose_drum, text=CURRENCIES['drum'])
    dp.register_message_handler(process_choose_eur, text=CURRENCIES['eur'])
    dp.register_message_handler(process_currency_actual_answer, text=LEXICON_RU['currency_actual'])
    dp.register_message_handler(process_numbers_answer)