from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Женские",
                                          callback_data=buy_callback.new(item_name="women_socks")
                                      ),
                                      InlineKeyboardButton(
                                          text="Мужские",
                                          callback_data="buy:men_socks"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )

                                  ]
                              ])

deep_choice = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="Зимние",
                                               callback_data="buy:winter_socks"

                                           )
                                       ]
                                   ])
