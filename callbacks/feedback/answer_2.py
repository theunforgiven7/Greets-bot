# from aiogram.utils import keyboard
# from aiogram import Dispatcher, types, F
# from parse.Ukrain.pagesMuk import get_random_greeting_a_m
# from parse.Ukrain.pagesMuk import get_random_greeting_father
# from parse.Ukrain.pagesMuk import get_random_greeting_son
# from parse.Ukrain.pagesMuk import get_random_greeting_friend_m

# # from main111 import *
# from hendlers.feedbackGreets import *

# dp = Dispatcher()
# # About answer 2

# @dp.callback_query(F.data == "answer_2")
# async def feedback(call: types.CallbackQuery):
#     choice_man = keyboard.InlineKeyboardBuilder()
#     choice_man.row(types.InlineKeyboardButton(text="Чоловік", callback_data="Another_m"))
#     choice_man.row(types.InlineKeyboardButton(text="Батько", callback_data="Father"))
#     choice_man.row(types.InlineKeyboardButton(text="Син", callback_data="Son"))
#     choice_man.row(types.InlineKeyboardButton(text="Брат", callback_data="Brother"))
#     choice_man.row(types.InlineKeyboardButton(text="Друг", callback_data="Friend_m"))
#     choice_man.row(types.InlineKeyboardButton(text="⬅", callback_data="feedback"))
#     await call.message.edit_text("Вибери категорію:", reply_markup=choice_man.as_markup())


# @dp.callback_query(F.data == "Another_m")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Another_m"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
#     greeting_a_m = get_random_greeting_a_m()
#     await call.message.edit_text(f"{str(greeting_a_m)}", reply_markup=bt1.as_markup())


# @dp.callback_query(F.data == "Father")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Father"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
#     greeting_f = get_random_greeting_father() 
#     await call.message.edit_text(f"{str(greeting_f)}", reply_markup=bt1.as_markup())


# @dp.callback_query(F.data == "Son")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Son"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
#     greeting_s = get_random_greeting_son() 
#     await call.message.edit_text(f"{str(greeting_s)}", reply_markup=bt1.as_markup())


# @dp.callback_query(F.data == "Brother")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Brother"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
#     greeting_b = get_random_greeting_brother()
#     await call.message.edit_text(f"{str(greeting_b)}", reply_markup=bt1.as_markup())


# @dp.callback_query(F.data == "Friend_m")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Friend_m"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2"))
#     greeting_f_m = get_random_greeting_friend_m()
#     await call.message.edit_text(f"{str(greeting_f_m)}", reply_markup=bt1.as_markup())
