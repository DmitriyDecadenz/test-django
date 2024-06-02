from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/all')],
                                     [KeyboardButton(text='/find')],
                                     [KeyboardButton(text='/my')],
                                     ],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')
