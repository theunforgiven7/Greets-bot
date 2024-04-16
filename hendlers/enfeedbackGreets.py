
from hendlers.choice_2 import *
from main111 import *
from hendlers.random_photo import *
from aiogram.utils import keyboard
from aiogram import types, F




@dp.callback_query(F.data == "enfeedback")
async def enfeedback(call: types.CallbackQuery):
    markup = keyboard.InlineKeyboardBuilder()
    markup.row(types.InlineKeyboardButton(text="Woman", callback_data="answer_1en"))
    markup.row(types.InlineKeyboardButton(text="Man", callback_data="answer_2en"))
    markup.row(types.InlineKeyboardButton(text="⬅", callback_data="choice_eng"))
    await call.message.edit_text("Choose a gender:", reply_markup=markup.as_markup())

#Answear_1е
from parse.English.pagesWen import get_random_greeting_a_wen, get_random_greeting_friend_wen


@dp.callback_query(F.data == "answer_1en")
async def feedback4(call: types.CallbackQuery):
    choice_women = keyboard.InlineKeyboardBuilder()
    choice_women.row(types.InlineKeyboardButton(text="For Woman", callback_data="EnAnother_w"))
    choice_women.row(types.InlineKeyboardButton(text="For Friend", callback_data="EnFriend_w"))
    choice_women.row(types.InlineKeyboardButton(text="Find postcard", callback_data="random_photo"))
    choice_women.row(types.InlineKeyboardButton(text="⬅", callback_data="enfeedback"))
    await call.message.edit_text("Choose a category:", reply_markup=choice_women.as_markup())


@dp.callback_query(F.data == "EnAnother_w")
async def feedback5(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_w"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1en"))
    greeting_a_w = get_random_greeting_a_wen()
    await call.message.edit_text(f"{str(greeting_a_w)}", reply_markup=bt1.as_markup())


@dp.callback_query(F.data == "EnFriend_w")
async def feedback6(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_w"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1en"))
    greeting_fried_w = get_random_greeting_friend_wen()
    await call.message.edit_text(f"{str(greeting_fried_w)}", reply_markup=bt1.as_markup())


#
#Answear_2

from parse.English.pagesMen import get_random_greeting_a_m, get_random_greeting_friend_m


@dp.callback_query(F.data == "answer_2en")
async def feedback1(call: types.CallbackQuery):
    choice_man = keyboard.InlineKeyboardBuilder()
    choice_man.row(types.InlineKeyboardButton(text="For man", callback_data="EnAnother_m"))
    choice_man.row(types.InlineKeyboardButton(text="For Friend", callback_data="EnFriend_m"))
    choice_man.row(types.InlineKeyboardButton(text="Find postcard", callback_data="random_photo"))
    choice_man.row(types.InlineKeyboardButton(text="⬅", callback_data="enfeedback"))
    await call.message.edit_text("Choose a category:", reply_markup=choice_man.as_markup())


@dp.callback_query(F.data == "EnAnother_m")
async def feedback2(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_m"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2en"))
    greeting_a_m = get_random_greeting_a_m()
    await call.message.edit_text(f"{str(greeting_a_m)}", reply_markup=bt1.as_markup())


@dp.callback_query(F.data == "EnFriend_m")
async def feedback3(call: types.CallbackQuery):
    bt5 = keyboard.InlineKeyboardBuilder()
    bt5.row(types.InlineKeyboardButton(text="Інше", callback_data="EnFriend_m"))
    bt5.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2en"))
    greeting_m = get_random_greeting_friend_m()
    await call.message.edit_text(f"{str(greeting_m)}", reply_markup=bt5.as_markup())