
from main111 import *
from aiogram.utils import keyboard
from aiogram import types, F

# from callbacks.feedback.answer_1 import *
# from callbacks.feedback.answer_2 import *
# from hendlers.enfeedbackGreets import*

from hendlers.feedbackGreets import *
# from hendlers.rmb import *
from hendlers.enfeedbackGreets import *
from hendlers.random_photo import *


@dp.callback_query(F.data == "choice_ukr")
async def greet_lan(call: types.CallbackQuery):
    lang_uk = keyboard.InlineKeyboardBuilder()
    lang_uk.row(types.InlineKeyboardButton(text="Зробити нагадування знайди бота: @RememmberPost_bot", callback_data="rmb"))
    lang_uk.row(types.InlineKeyboardButton(text="Знайти те саме привітання", callback_data="feedback"))
    await call.message.answer("(/start)Обери, що тобі потрібно:", reply_markup=lang_uk.as_markup())


@dp.callback_query(F.data == "choice_eng")
async def greet_lan(call: types.CallbackQuery):
    lang_uk = keyboard.InlineKeyboardBuilder()
    lang_uk.row(types.InlineKeyboardButton(text="Find a Happy Birthday Greeting", callback_data="enfeedback"))
    await call.message.answer("(/start)Click on the button to continue:", reply_markup=lang_uk.as_markup())