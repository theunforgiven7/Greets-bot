
from hendlers.choice_2 import *
from main111 import *
from aiogram.utils import keyboard
from aiogram import types, F
from hendlers.random_photo import *




@dp.callback_query(F.data == "feedback")
async def feedback(call: types.CallbackQuery):
    markup = keyboard.InlineKeyboardBuilder()
    markup.row(types.InlineKeyboardButton(text="Жінка", callback_data="answer_1"))
    markup.row(types.InlineKeyboardButton(text="Чоловік", callback_data="answer_2"))
    markup.row(types.InlineKeyboardButton(text="⬅", callback_data="choice_ukr"))
    await call.message.edit_text("Вибери стать:", reply_markup=markup.as_markup())






#Answear_1

from parse.Ukrain.pagesWuk import get_random_greeting_a_w, get_random_greeting_sister, get_random_greeting_mother, get_random_greeting_dother, get_random_greeting_friend_w


@dp.callback_query(F.data == "answer_1")
async def feedback(call: types.CallbackQuery):
    choice_women = keyboard.InlineKeyboardBuilder()
    choice_women.row(types.InlineKeyboardButton(text="Жінка", callback_data="Another_w"))
    choice_women.row(types.InlineKeyboardButton(text="Мама", callback_data="Mother"))
    choice_women.row(types.InlineKeyboardButton(text="Дочка", callback_data="Dother"))
    choice_women.row(types.InlineKeyboardButton(text="Сестра", callback_data="Sister"))
    choice_women.row(types.InlineKeyboardButton(text="Подруга", callback_data="Friend_w"))
    choice_women.row(types.InlineKeyboardButton(text="Знайти фото-привітання", callback_data="random_photo"))
    choice_women.row(types.InlineKeyboardButton(text="⬅", callback_data="feedback"))
    await call.message.edit_text("Вибери категорію:", reply_markup=choice_women.as_markup())


#
@dp.callback_query(F.data == "Another_w")
async def feedback(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Another_w"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
    greeting_a_w = get_random_greeting_a_w()
    # await call.message.edit_text('Тримай:')
    await call.message.edit_text(f"{str(greeting_a_w)}", reply_markup=bt1.as_markup())



@dp.callback_query(F.data == "Mother")
async def feedback(call: types.CallbackQuery):
    bt2 = keyboard.InlineKeyboardBuilder()
    bt2.row(types.InlineKeyboardButton(text="Інше", callback_data="Mother"))
    bt2.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
    greeting_w = get_random_greeting_mother()
    # await call.message.answer('Тримай:')
    await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt2.as_markup())
#


@dp.callback_query(F.data == "Dother")
async def feedback(call: types.CallbackQuery):
    bt3 = keyboard.InlineKeyboardBuilder()
    bt3.row(types.InlineKeyboardButton(text="Інше", callback_data="Mother"))
    bt3.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
    greeting_w = get_random_greeting_dother()
    await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt3.as_markup())
#


@dp.callback_query(F.data == "Sister")
async def feedback(call: types.CallbackQuery):
    bt4 = keyboard.InlineKeyboardBuilder()
    bt4.row(types.InlineKeyboardButton(text="Інше", callback_data="Sister"))
    bt4.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
    greeting_w = get_random_greeting_sister()
    # await call.message.edit_text(f" Тримай:\n{greeting_w}", reply_markup=bt4.as_markup())
    await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt4.as_markup())
#


@dp.callback_query(F.data == "Friend_w")
async def feedback(call: types.CallbackQuery):
    bt5 = keyboard.InlineKeyboardBuilder()
    bt5.row(types.InlineKeyboardButton(text="Інше", callback_data="Friend_w"))
    bt5.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
    greeting_w = get_random_greeting_friend_w()
    # await call.message.edit_text(f" Тримай: {greeting_w}", reply_markup=bt5.as_markup())
    await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt5.as_markup())



# About answer 2

from parse.Ukrain.pagesMuk import get_random_greeting_a_m, get_random_greeting_father, get_random_greeting_brother, get_random_greeting_son, get_random_greeting_friend_m



@dp.callback_query(F.data == "answer_2")
async def feedback(call: types.CallbackQuery):
    choice_man = keyboard.InlineKeyboardBuilder()
    choice_man.row(types.InlineKeyboardButton(text="Чоловік", callback_data="Another_m"))
    choice_man.row(types.InlineKeyboardButton(text="Батько", callback_data="Father"))
    choice_man.row(types.InlineKeyboardButton(text="Син", callback_data="Son"))
    choice_man.row(types.InlineKeyboardButton(text="Брат", callback_data="Brother"))
    choice_man.row(types.InlineKeyboardButton(text="Друг", callback_data="Friend_m"))
    choice_man.row(types.InlineKeyboardButton(text="Знайти фото-привітання", callback_data="random_photo"))
    choice_man.row(types.InlineKeyboardButton(text="⬅", callback_data="feedback"))
    await call.message.edit_text("Вибери категорію:", reply_markup=choice_man.as_markup())


@dp.callback_query(F.data == "Another_m")
async def feedback(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Another_m"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
    greeting_a_m = get_random_greeting_a_m()
    await call.message.edit_text(f"{str(greeting_a_m)}", reply_markup=bt1.as_markup())


@dp.callback_query(F.data == "Father")
async def feedback(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Father"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
    greeting_f = get_random_greeting_father() 
    await call.message.edit_text(f"{str(greeting_f)}", reply_markup=bt1.as_markup())


@dp.callback_query(F.data == "Son")
async def feedback(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Son"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
    greeting_s = get_random_greeting_son() 
    await call.message.edit_text(f"{str(greeting_s)}", reply_markup=bt1.as_markup())


@dp.callback_query(F.data == "Brother")
async def feedback(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Brother"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
    greeting_b = get_random_greeting_brother()
    await call.message.edit_text(f"{str(greeting_b)}", reply_markup=bt1.as_markup())


@dp.callback_query(F.data == "Friend_m")
async def feedback(call: types.CallbackQuery):
    bt1 = keyboard.InlineKeyboardBuilder()
    bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Friend_m"))
    bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
    greeting_f_m = get_random_greeting_friend_m()
    await call.message.edit_text(f"{str(greeting_f_m)}", reply_markup=bt1.as_markup())
