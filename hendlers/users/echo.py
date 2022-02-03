from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("start"))
async def show_menu(message: types.Message):
    await message.answer("Ваше меню", reply_markup=menu)
