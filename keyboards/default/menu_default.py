from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ассортимент"),
            KeyboardButton(text="Корзина")
        ],
        [
            KeyboardButton(text="Заказы"),
            KeyboardButton(text="Доставка")

        ],
        [
            KeyboardButton(text="Про нас")
        ]

    ],
    resize_keyboard=True
)
