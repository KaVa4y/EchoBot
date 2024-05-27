import types
from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= "/start", description="Комманда для запуска бота."),
        types.BotCommand(command="/help", description="Комманда для получения помощи."),
        types.BotCommand(command="/about", description="Комманда для получения информации."),
        types.BotCommand(command="/contacts", description="Комманда для получения контактной информации."),
        types.BotCommand(command="/black_lives_not_matter", description="Комманда для..."),
        types.BotCommand(command="/say_gex", description="Комманда для получения gexa.")
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет!")

@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer("Если что-то не работает, то это только твои проблеммы.")

@dp.message_handler(commands="about")
async def start(message: types.Message):
    await message.answer("В разработке.")

@dp.message_handler(commands="contacts")
async def start(message: types.Message):
    await message.answer("В разработке.")

@dp.message_handler(commands="black_lives_not_matter")
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