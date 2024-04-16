from hendlers.choice_2 import *
from hendlers.enfeedbackGreets import *
from hendlers.feedbackGreets import *

from main111 import *
from aiogram.utils import keyboard
from aiogram import types, F
import random

    # lang_kb.row(types.InlineKeyboardButton(text="Знайти фото-привітання/Find postcard", callback_data="random_photo"))
# 
# Список или словарь ваших ссылок на фото


@dp.callback_query(F.data == "random_photo")
async def send_random_photo(call: types.CallbackQuery):
    # Выберем случайную фотографию из списка
    photo_urls = ['https://i.pinimg.com/564x/5b/28/33/5b283333bb8188972225e74ea83cc141.jpg', 
            'https://i.pinimg.com/564x/2e/9f/e8/2e9fe88319a17cf6d773b57dd9d2656e.jpg', 
            'https://i.pinimg.com/564x/f1/50/68/f15068db985ea5cb9a8c323e0aeddf66.jpg',
            'https://i.pinimg.com/564x/78/e6/74/78e674c3852bf5f25830c8e5d2a11e50.jpg',
            'https://i.pinimg.com/564x/bd/8f/6e/bd8f6e4f2410f395964993843ffbe3ed.jpg',
            'https://i.pinimg.com/564x/28/53/e7/2853e722e80868c892e5cc3c7f0e194b.jpg',
            'https://i.pinimg.com/564x/02/b1/9a/02b19af3c56af9015972ba544c3da581.jpg',
            'https://i.pinimg.com/564x/a8/28/ad/a828ad44e126a32e0828ad6f6da48d20.jpg',
            'https://i.pinimg.com/564x/6e/84/89/6e8489042b6b3dc6bff9f783acf68cdc.jpg',
            'https://i.pinimg.com/736x/36/b4/62/36b4620b21888f3a8e73dbe1ca884938.jpg']

    photo_url = random.choice(photo_urls)
    await call.bot.send_photo(call.message.chat.id, photo_url)
