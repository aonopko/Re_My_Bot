from aiogram import executor

from loader import dp
import hendlers
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
