from loguru import logger

from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from loader import dp


@dp.callback_query_handler(buy_callback.filter(item_name="women_socks"))
async def buying_women_socks(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logger.info(f"callback_data = {call.data}")
    logger.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали женские носки, их всего {quantity}")