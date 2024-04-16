
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import keyboard
import requests
from bs4 import BeautifulSoup as BS
from decouple import config
TOKEN = config("TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN)


from hendlers.choice_2 import *


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    start_kb = keyboard.InlineKeyboardBuilder()
    start_kb.row(types.InlineKeyboardButton(text="🇺🇦", callback_data="choice_ukr"))
    start_kb.row(types.InlineKeyboardButton(text="🇬🇧", callback_data="choice_eng"))
    await message.reply("Для початку обери мову\nFor start choose your language", reply_markup=start_kb.as_markup())


async def main() -> None:
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())