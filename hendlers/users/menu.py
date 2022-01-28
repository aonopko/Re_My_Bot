from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import menu
from loader import dp
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Ваше меню", reply_markup=menu)


@dp.message_handler(text="Доставка")
async def about_us(message: types.Message):
    await message.answer('1. Нова пошта - відправка щодено\n'
                         '3. Justin - відправка по суботах\n'
                         '2. Укрпошта - відправка пн-пт\n')
