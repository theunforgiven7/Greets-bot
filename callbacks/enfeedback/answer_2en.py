# from aiogram.utils import keyboard
# from aiogram import Bot, Dispatcher, types, F
# from parse.English.pagesMen import get_random_greeting_a_m, get_random_greeting_friend_m
# from hendlers.enfeedbackGreets import *
# dp = Dispatcher()

# #Answear_2
# @dp.callback_query(F.data == "answer_2en")
# async def feedback(call: types.CallbackQuery):
#     choice_man = keyboard.InlineKeyboardBuilder()
#     choice_man.row(types.InlineKeyboardButton(text="For man", callback_data="EnAnother_m"))
#     choice_man.row(types.InlineKeyboardButton(text="For Friend", callback_data="EnFriend_m"))
#     choice_man.row(types.InlineKeyboardButton(text="⬅", callback_data="enfeedback"))
#     await call.message.edit_text("Choose a category:", reply_markup=choice_man.as_markup())


# @dp.callback_query(F.data == "EnAnother_m")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_m"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2en"))
#     greeting_a_m = get_random_greeting_a_m()
#     # await call.message.edit_text('Тримай:')
#     await call.message.edit_text(f"{str(greeting_a_m)}", reply_markup=bt1.as_markup())


# @dp.callback_query(F.data == "EnFriend_m")
# async def feedback(call: types.CallbackQuery):
#     bt5 = keyboard.InlineKeyboardBuilder()
#     bt5.row(types.InlineKeyboardButton(text="Інше", callback_data="EnFriend_m"))
#     bt5.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_2en"))
#     greeting_m = get_random_greeting_friend_m()
#     # await call.message.edit_text(f" Тримай: {greeting_w}", reply_markup=bt5.as_markup())
#     await call.message.edit_text(f"{str(greeting_m)}", reply_markup=bt5.as_markup())