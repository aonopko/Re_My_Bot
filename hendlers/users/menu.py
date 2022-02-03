from aiogram import types
from loader import dp
from keyboards.inline.choice_buttons import choice


@dp.message_handler(text="Ассортимент")
async def show_items(message: types.Message):
    await message.answer(text="Ваш ассортимент", reply_markup=choice)


@dp.message_handler(text="Доставка")
async def about_us(message: types.Message):
    await message.answer('1. Нова пошта - відправка щодено\n'
                         '3. Justin - відправка по суботах\n'
                         '2. Укрпошта - відправка пн-пт\n')
