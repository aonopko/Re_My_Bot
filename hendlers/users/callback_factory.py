from loguru import logger

from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import deep_choice

from loader import dp


@dp.callback_query_handler(buy_callback.filter(item_name="women_socks"))
async def buying_women_socks(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logger.info(f"callback_data = {call.data}")
    logger.info(f"callback_data dict = {callback_data}")
    await call.message.answer(text="Выбери сезонность",reply_markup=deep_choice)