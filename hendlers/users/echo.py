from loader import dp, bot
from aiogram import types


@dp.message_handler(text='/start')
async def bot_start(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет')
