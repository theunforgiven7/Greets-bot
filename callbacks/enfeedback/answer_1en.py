
# from aiogram.utils import keyboard
# from aiogram import types, F, Dispatcher
# from parse.English.pagesWen import get_random_greeting_a_wen, get_random_greeting_friend_wen
# from hendlers.enfeedbackGreets import *
# dp = Dispatcher()

# #Answear_1е


# @dp.callback_query(F.data == "answer_1en")
# async def feedback(call: types.CallbackQuery):
#     choice_women = keyboard.InlineKeyboardBuilder()
#     choice_women.row(types.InlineKeyboardButton(text="For Woman", callback_data="EnAnother_w"))
#     choice_women.row(types.InlineKeyboardButton(text="For Friend", callback_data="EnFriend_w"))
#     choice_women.row(types.InlineKeyboardButton(text="⬅", callback_data="enfeedback"))
#     await call.message.edit_text("Choose a category:", reply_markup=choice_women.as_markup())

# @dp.callback_query(F.data == "EnAnother_w")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_w"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1en"))
#     greeting_a_w = get_random_greeting_a_wen()
#     # await call.message.edit_text('Тримай:')
#     await call.message.edit_text(f"{str(greeting_a_w)}", reply_markup=bt1.as_markup())

# @dp.callback_query(F.data == "EnFriend_w")
# async def feedback(call: types.CallbackQuery):
#     bt1 = keyboard.InlineKeyboardBuilder()
#     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_w"))
#     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1en"))
#     greeting_fried_w = get_random_greeting_friend_wen()
#     await call.message.edit_text(f"{str(greeting_fried_w)}", reply_markup=bt1.as_markup())




























# # #---------------------------------------------------------------
# # # @dp.callback_query(F.data == "answer_1en")
# # # async def feedback(call: types.CallbackQuery):
# # #     choice_women = keyboard.InlineKeyboardBuilder()
# # #     choice_women.row(types.InlineKeyboardButton(text="For Woman", callback_data="EnAnother_w"))
# # #     choice_women.row(types.InlineKeyboardButton(text="For Friend", callback_data="EnFriend_w"))
# # #     choice_women.row(types.InlineKeyboardButton(text="⬅", callback_data="enfeedback"))
# # #     await call.message.edit_text("Choose a category:", reply_markup=choice_women.as_markup())


# # # @dp.callback_query(F.data == "EnAnother_w")
# # # async def feedback(call: types.CallbackQuery):
# # #     bt1 = keyboard.InlineKeyboardBuilder()
# # #     bt1.row(types.InlineKeyboardButton(text="Інше", callback_data="EnAnother_w"))
# # #     bt1.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1en"))
# # #     greeting_a_w = get_random_greeting_a_w()
# # #     # await call.message.edit_text('Тримай:')
# # #     await call.message.edit_text(f"{str(greeting_a_w)}", reply_markup=bt1.as_markup())


# # # @dp.callback_query(F.data == "EnFriend_w")
# # # async def feedback(call: types.CallbackQuery):
# # #     bt5 = keyboard.InlineKeyboardBuilder()
# # #     bt5.row(types.InlineKeyboardButton(text="Інше", callback_data="EnFriend_w"))
# # #     bt5.row(types.InlineKeyboardButton(text="⬅", callback_data="answer_1en"))
# # #     greeting_w = get_random_greeting_friend_w()
# # #     # await call.message.edit_text(f" Тримай: {greeting_w}", reply_markup=bt5.as_markup())
# # #     await call.message.edit_text(f"{str(greeting_w)}", reply_markup=bt5.as_markup())