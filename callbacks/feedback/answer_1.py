# from aiogram.utils import keyboard
# from aiogram import Dispatcher, types, F
# from parse.Ukrain.pagesWuk import get_random_greeting_a_w
# from parse.Ukrain.pagesWuk import get_random_greeting_mother
# from parse.Ukrain.pagesWuk import get_random_greeting_dother
# from parse.Ukrain.pagesWuk import get_random_greeting_friend_w

# from hendlers.feedbackGreets import *

# dp = Dispatcher()

# #Answear_1
# @dp.callback_query(F.data == "answer_1")
# async def feedback(call: types.CallbackQuery):
#     choice_women = keyboard.InlineKeyboardBuilder()
#     choice_women.row(types.InlineKeyboardButton(text="Жінка", callback_data="Another_w"))
#     choice_women.row(types.InlineKeyboardButton(text="Мама", callback_data="Mother"))
#     choice_women.row(types.InlineKeyboardButton(text="Дочка", callback_data="Dother"))
#     choice_women.row(types.InlineKeyboardButton(text="Сестра", callback_data="Sister"))
#     choice_women.row(types.InlineKeyboardButton(text="Подруга", callback_data="Friend_w"))
#     choice_women.row(types.InlineKeyboardButton(text="⬅", callback_data="feedback"))
#     await call.message.edit_text("Вибери категорію:", reply_markup=choice_women.as_markup())


# #
# @dp.callback_query(F.data == "Another_w")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="Another_w"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
#     greeting_a_w = get_random_greeting_a_w()
#     # await call.message.edit_text('Тримай:')
#     await call.message.edit_text(f"{str(greeting_a_w)}", reply_markup=bt1.as_markup())



# @dp.callback_query(F.data == "Mother")
# async def feedback(call: types.CallbackQuery):
#     bt2 = keyboard.InlineKeyboardBuilder()
#     bt2.row(types.InlineKeyboardButton(text="Інше", callback_data="Mother"))
#     bt2.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
#     greeting_w = get_random_greeting_mother()
#     # await call.message.answer('Тримай:')
#     await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt2.as_markup())
# #


# @dp.callback_query(F.data == "Dother")
# async def feedback(call: types.CallbackQuery):
#     bt3 = keyboard.InlineKeyboardBuilder()
#     bt3.row(types.InlineKeyboardButton(text="Інше", callback_data="Mother"))
#     bt3.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
#     greeting_w = get_random_greeting_dother()
#     await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt3.as_markup())
# #


# @dp.callback_query(F.data == "Sister")
# async def feedback(call: types.CallbackQuery):
#     bt4 = keyboard.InlineKeyboardBuilder()
#     bt4.row(types.InlineKeyboardButton(text="Інше", callback_data="Sister"))
#     bt4.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
#     greeting_w = get_random_greeting_sister()
#     # await call.message.edit_text(f" Тримай:\n{greeting_w}", reply_markup=bt4.as_markup())
#     await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt4.as_markup())
# #


# @dp.callback_query(F.data == "Friend_w")
# async def feedback(call: types.CallbackQuery):
#     bt5 = keyboard.InlineKeyboardBuilder()
#     bt5.row(types.InlineKeyboardButton(text="Інше", callback_data="Friend_w"))
#     bt5.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1"))
#     greeting_w = get_random_greeting_friend_w()
#     # await call.message.edit_text(f" Тримай: {greeting_w}", reply_markup=bt5.as_markup())
#     await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt5.as_markup())