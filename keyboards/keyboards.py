from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton("Отправь фото кота.")
    button_2 = KeyboardButton("Перейти на след. клавиатуру.")
    keyboard.add(button_1, button_2)
    return keyboard


def get_keyboard_2():
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton("Отправь фото собаки.")
    button_4 = KeyboardButton("Вернуться на прошлую клавиатуру.")
    keyboard_1.add(button_3, button_4)
    return keyboard_1


def get_keyboard_inline_1():
    keyboard_inline_1 = InlineKeyboardMarkup(row_width=1)
    button_inline_1 = InlineKeyboardButton("Посмотреть", url="https://cattish.ru/breed/")
    button_inline_2 = InlineKeyboardButton("Отправь рандомное число", callback_data="send_random")
    button_inline_3 = InlineKeyboardButton("Переключиться на след. страницу", callback_data="go_2")
    keyboard_inline_1.add(button_inline_1, button_inline_2, button_inline_3,)
    return keyboard_inline_1


def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=1)
    button_inline_4 = InlineKeyboardButton("Посмотреть",url="https://www.youtube.com/watch?v=HIcSWuKMwOw")
    button_inline_5 = InlineKeyboardButton("Текущее время", callback_data="send_datatime")
    button_inline_6 = InlineKeyboardButton("Переключиться на пред. страницу", callback_data="go_1")
    keyboard_inline_2.add(button_inline_4, button_inline_5, button_inline_6)
    return keyboard_inline_2
