import types
from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN
from keyboards.keyboards import get_keyboard_1, get_keyboard_2, get_keyboard_inline_1, get_keyboard_inline_2
import random
from datetime import datetime

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Комманда для запуска бота."),
        types.BotCommand(command="/help", description="Комманда для получения помощи."),
        types.BotCommand(command="/about", description="Комманда для получения информации."),
        types.BotCommand(command="/contacts", description="Комманда для получения контактной информации."),
        types.BotCommand(command="/dev_info", description="Информация для разработчиков."),
        types.BotCommand(command="/say_gex", description="Комманда для получения gexa."),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == "Отправь фото кота.")
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo="https://img.goodfon.com/original/1600x1200/e/e6/zhivotnoe-kot-bolshie-glaza.jpg", caption= "Вот тебе кот.", reply_markup=get_keyboard_inline_1())

@dp.message_handler(lambda message: message.text == "Перейти на след. клавиатуру.")
async def button_2_click(message: types.Message):
    await message.answer("Тут ты можешь попросить бота отправить фото собаки.", reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == "Отправь фото собаки.")
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo="https://w.forfun.com/fetch/2b/2b370a552f767dce12a4e612e2711c76.jpeg", caption= "Вот тебе собака.")

@dp.message_handler(lambda message: message.text == "Вернуться на прошлую клавиатуру.")
async def button_4_click(message: types.Message):
    await message.answer("Тут ты можешь попросить бота отправить фото кота.", reply_markup=get_keyboard_1())

@dp.callback_query_handler(lambda c: c.data == "go_2")
async def go_2(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Пароды кошек.", reply_markup=get_keyboard_inline_2())
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda c: c.data == "send_random")
async def send_random(callback_query: types.CallbackQuery):
    random_number = random.randint(1,1000)
    await callback_query.message.answer(f"Ваше случайное число от 1 до 1000: {random_number}")

@dp.callback_query_handler(lambda c: c.data == "send_datatime")
async def send_datatime(callback_query: types.CallbackQuery):
    current_time = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.answer(f"Время по МСК: {current_time}")

@dp.callback_query_handler(lambda c: c.data == "go_1")
async def go_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Пароды кошек.", reply_markup=get_keyboard_inline_1())

@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer("Если что-то не работает, то это только твои проблеммы.")

@dp.message_handler(commands="about")
async def start(message: types.Message):
    await message.answer("В разработке.")

@dp.message_handler(commands="contacts")
async def start(message: types.Message):
    await message.answer("В разработке.")

@dp.message_handler(commands="dev_info")
async def start(message: types.Message):
    await message.answer("В разработке.")

@dp.message_handler(commands="say_gex")
async def start(message: types.Message):
    await message.answer("GEX")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)