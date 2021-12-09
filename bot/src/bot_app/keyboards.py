from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

keyboard_der = InlineKeyboardButton('Мужской', callback_data='мужской')
keyboard_die = InlineKeyboardButton('Женский', callback_data='женский')
keyboard_das = InlineKeyboardButton('Средный', callback_data='средный')
markup = InlineKeyboardMarkup(row_width=3)
markup.add(keyboard_der, keyboard_das, keyboard_die)
