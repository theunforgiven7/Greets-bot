import asyncio
from decouple import config
from aiogram import Bot, Dispatcher, Router, types,F
from aiogram.filters import CommandStart, Command
from datetime import datetime

TOKEN = config("TOKEN")
TOKEN = '7060816343:AAFzz0hHHcDxkIFN1v8CWCVF5JHqZxE7FUg'
dp = Dispatcher() 
bot = Bot(TOKEN)

@dp.message(Command("time"))
async def command_timenow(message: types.Message):
    current_time = datetime.now()
    await message.answer(f"Поточний час:{current_time}")

@dp.message(Command('hello'))
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")
@dp.message()
async def error(massage: types.Message):
    await massage.answer('Я вас don\'t understand.Доступні команди: /hello, /time')

async def main() -> None:
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
