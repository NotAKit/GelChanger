from aiogram.types import Message
import random


async def digit_check(message: Message):
    flag = False
    mess = message.text
    for i in range(len(mess)):
        if mess[i] in '1234567890.':
            flag = True
        else:
            flag = False
    if flag == True:
        dots = message.text.replace(',','.')
        dots = dots.replace(' ','')

        # умножаю введенное число на 23
        gel = float(dots) * 23
        if int(gel)%10 == 0 or int(gel)%10 == 5 or int(gel)%10 == 6 or int(gel)%10 == 7 or int(gel)%10 == 8 or int(gel)%10 == 9:
            await message.answer(text=f'{gel} рублей')
        elif int(gel)%10 == 1 :
            await message.answer(text=f'{gel} рубль')
        elif int(gel)%10 == 2 or int(gel)%10 == 3 or int(gel)%10 == 4:
            await message.answer(text=f'{gel} рубля')

    else:
       await message.answer(text='Введите число')