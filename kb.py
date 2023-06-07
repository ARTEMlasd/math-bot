from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton('/S_круга')
button2 = KeyboardButton('/Discriminant')
button3 = KeyboardButton('/S_Треугольника')
markup3 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)