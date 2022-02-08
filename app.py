from aiogram import executor
from loguru import logger
from loader import dp, db
import hendlers
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    await db.create_table_items()
    await db.create()
    logger.info(f"База анніх подключена")
    await on_startup_notify(dp)
    logger.info(f"Бот запущен")




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
