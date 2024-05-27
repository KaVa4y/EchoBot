from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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