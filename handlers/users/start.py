from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from keyboards.default.taomlar_uchun import taomlar_buttons
from keyboards.default.taomlar_uchun import fastfood_buttons
from keyboards.default.taomlar_uchun import ichimlik_buttons
from keyboards.default.taomlar_uchun import shirinlik_buttons
from keyboards.default.taomlar_uchun import pepsi_buttons
from keyboards.default.taomlar_uchun import cola_buttons
from keyboards.default.taomlar_uchun import fanta_buttons
from keyboards.default.taomlar_uchun import mexito_buttons

from keyboards.default.taomlar_uchun import choy_buttons
from keyboards.default.taomlar_uchun import osh_buttons
from keyboards.default.menu_uchun import somsali_buttons
from keyboards.default.menu_uchun import kabobli_buttons
from keyboards.default.menu_uchun import shorvali_buttons
from keyboards.default.menu_uchun import chushvarali_buttons
from keyboards.default.menu_uchun import mantili_buttons
from keyboards.default.menu_uchun import oramanli_buttons
from keyboards.default.menu_uchun import meny_buttons
from keyboards.default.menu_uchun import joyli_buttons
from keyboards.inline.til_uchun import tillar_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum botimizga hush kelibsiz")

@dp.callback_query_handler(text='til1')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu aleykum botimizga hush kelibsiz",reply_markup=meny_buttons, )

@dp.message_handler(text='Milliy taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum botimizga hush kelibsiz",reply_markup=taomlar_buttons)

@dp.message_handler(text="O'rqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="buyurtmani bekor qilish")
async def bot_start(message: types.Message):
    await message.answer(f"Buyurtmalar bekor boldi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Buyurtmani yetkazish")
async def bot_start(message: types.Message):
    await message.answer(f"Buyurtma yetkaziladi, joyni toldiring",reply_markup=joyli_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)

#======================================================================================================================


# @dp.message_handler(text='Osh')
# async def bot_start(message: types.Message):
#     await message.answer(f"Osh taomlarini tanlashingiz mumkin",reply_markup=osh_buttons)

@dp.message_handler(text="dvaynoy osh")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="mini osh")
async def bot_start(message: types.Message):


    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="kavatak osh")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="hammsi birda")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#===================================================================================================================

@dp.message_handler(text='Somsalar')
async def bot_start(message: types.Message):
    await message.answer(f"Somsalar menu sidasiz",reply_markup=somsali_buttons)


# @dp.message_handler(text="Go'shtli somsa")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="ashqavoq somsa")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="kartochka")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="kokatli somsalar")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

# @dp.message_handler(text="Orqaga")
# async def bot_start(message: types.Message):
#     await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#======================================================================================================================

# @dp.message_handler(text='kaboblar')
# async def bot_start(message: types.Message):
#     await message.answer(f"Kaboblar menusidasiz",reply_markup=kabobli_buttons)

@dp.message_handler(text="ravon shashlik")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="kuskavoy shashlik")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="ravon qiyma shashlik")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="toviq g'oshti shashlik")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):

    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#====================================================================================================================

# @dp.message_handler(text='Shorvalar')
# async def bot_start(message: types.Message):
#     await message.answer(f"shorvalar menusidasiz",reply_markup=shorvali_buttons)

@dp.message_handler(text="dolma shorva")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="suvak skorva")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#=====================================================================================================================

# @dp.message_handler(text='Chuchvara')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=chushvarali_buttons)

@dp.message_handler(text="25 tali katta chuchvara")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)


@dp.message_handler(text="15 talik mini chuchvarar")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#====================================================================================================================

# @dp.message_handler(text='Manti')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=mantili_buttons)

@dp.message_handler(text="gosgtli monti")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="kartojkali monti")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="ashqavoqli monti")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="ko'katli")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#=====================================================================================================================

# @dp.message_handler(text="O'rama")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=oramanli_buttons)


@dp.message_handler(text="g'oshtli orama")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="kartoshkali oraman")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)
#======================================================================================================================

# @dp.message_handler(text='fasfood')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=fastfood_buttons)
#
# @dp.message_handler(text="lavash")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="shourma")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
#
# @dp.message_handler(text="hoddok")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)
#
# @dp.message_handler(text="pizza")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"Asosiy menudasiz",reply_markup=meny_buttons)

#====================================================================================================================

# @dp.message_handler(text='ichimliklar')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=ichimlik_buttons)
#
# @dp.message_handler(text="pepsi")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=pepsi_buttons)
#
# @dp.message_handler(text="coca cola")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="fanta")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="choylar")
# async def bot_start(message: types.Message):
#      await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"asosiy menudasiz",reply_markup=meny_buttons)

#=====================================================================================================================

# @dp.message_handler(text='pepsi')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=ichimlik_buttons)

@dp.message_handler(text="2.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1,5.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="0,5.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"asosiy menudasiz",reply_markup=meny_buttons)

#=====================================================================================================================

# @dp.message_handler(text='=coca cola')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=cola_buttons)

@dp.message_handler(text="2.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1,5.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="0,5.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"asosiy menudasiz",reply_markup=meny_buttons)

#=====================================================================================================================

# @dp.message_handler(text='fanta')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=fanta_buttons)

@dp.message_handler(text="2.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1,5.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="0,5.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"asosiy menudasiz",reply_markup=meny_buttons)

#=====================================================================================================================

# @dp.message_handler(text='mexitto')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=mexito_buttons)

@dp.message_handler(text="2.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1,5.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="1.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="0,5.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"asosiy menudasiz",reply_markup=meny_buttons)

#=====================================================================================================================
#
# @dp.message_handler(text='choylar')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=choy_buttons)

@dp.message_handler(text="1,choy")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="2,choy")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="limonli choy")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="novotli choy")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
     await message.answer(f"asosiy menudasiz",reply_markup=meny_buttons)

#===================================================================================================================


# @dp.message_handler(text='shirinliklar')
# async def bot_start(message: types.Message):
#     await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=shirinlik_buttons)
#
# @dp.message_handler(text="tort")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="shkaladniy tort")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="bananli tort")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)
#
# @dp.message_handler(text="qaymoqli tort")
# async def bot_start(message: types.Message):
#     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=meny_buttons)

#=======================================================================================================================================================



from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from keyboards.default.taomlar_uchun import taomlarli_buttons
from keyboards.default.taomlar_uchun import fastfoodli_buttons
from keyboards.default.taomlar_uchun import ichimlikli_buttons
from keyboards.default.taomlar_uchun import shirinlikli_buttons
from keyboards.default.taomlar_uchun import pepsili_buttons
from keyboards.default.taomlar_uchun import colali_buttons
from keyboards.default.taomlar_uchun import fantali_buttons
from keyboards.default.taomlar_uchun import mexitoli_buttons
from keyboards.default.taomlar_uchun import choyli_buttons
from keyboards.default.taomlar_uchun import oshli_buttons
from keyboards.default.taomlar_uchun import somsajon_buttons
from keyboards.default.taomlar_uchun import kabob_buttons
from keyboards.default.taomlar_uchun import shorva_buttons
from keyboards.default.taomlar_uchun import chushvara_buttons
from keyboards.default.taomlar_uchun import manti_buttons
from keyboards.default.taomlar_uchun import oraman_buttons
from keyboards.default.taomlar_uchun import menu_buttons
from keyboards.default.taomlar_uchun import joy_buttons
# # from keyboards.inline.til_uchun import tillar_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"hello, {message.from_user.full_name}!",reply_markup=tillar_buttons)

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Hello and welcome to the bot ")

@dp.callback_query_handler(text='til2')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Hello and welcome to the bot",reply_markup=menu_buttons)

@dp.message_handler(text='National foods')
async def bot_start(message: types.Message):
    await message.answer(f"Hello and welcome to the bot",reply_markup=taomlarli_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu ",reply_markup=menu_buttons)

@dp.message_handler(text="Cancellation of order")
async def bot_start(message: types.Message):
    await message.answer(f"Orders canceled are not in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Order delivery")
async def bot_start(message: types.Message):
    await message.answer(f"Fill in the place where your order will be delivered",reply_markup=joy_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#======================================================================================================================


# @dp.message_handler(text='soup')
# async def bot_start(message: types.Message):
#     await message.answer(f"you can choose pilaf dishes",reply_markup=oshli_buttons)

@dp.message_handler(text="dvaynoy osh")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="mini osh")
async def bot_start(message: types.Message):


    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="kavatak osh")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="hammsi birda")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)
#===================================================================================================================

# @dp.message_handler(text='Somsalar')
# async def bot_start(message: types.Message):
#     await message.answer(f"You are in the somsal menu",reply_markup=somsajon_buttons)


@dp.message_handler(text="Somsa with meat")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="pumkin somsa")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="somsa with potatoes")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Somsa with cockade")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#======================================================================================================================

# @dp.message_handler(text='kebabs')
# async def bot_start(message: types.Message):
#     await message.answer(f"You are on the kebab menu",reply_markup=kabob_buttons)

@dp.message_handler(text="Fluent shashlik")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="kuskavoy shashlik")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="smooth minced meat")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="chicken skewers")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):

    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)
#====================================================================================================================

# @dp.message_handler(text='Soups')
# async def bot_start(message: types.Message):
#     await message.answer(f"you are on the soup menu",reply_markup=shorva_buttons)

@dp.message_handler(text="dolma soup")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="plaster skorva")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)
#=====================================================================================================================

# @dp.message_handler(text='Dumplings')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=chushvara_buttons)

@dp.message_handler(text="25 large dumplings")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)


@dp.message_handler(text="15 mini dumplings")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#====================================================================================================================

# @dp.message_handler(text='Mantis')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=manti_buttons)

@dp.message_handler(text="meat monty")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="card mount")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="poppy monty")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="green")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)
#=====================================================================================================================

# @dp.message_handler(text="Wrapping")
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=oraman_buttons)


@dp.message_handler(text="meat roll")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="potato roll")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)
#======================================================================================================================

# @dp.message_handler(text='fasfood')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=fastfoodli_buttons)
#
# @dp.message_handler(text="lavash")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
# @dp.message_handler(text="shorma")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
#
# @dp.message_handler(text="hoddok")
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)
#
# @dp.message_handler(text="pizza")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#====================================================================================================================

# @dp.message_handler(text='drinks')
# async def bot_start(message: types.Message):
#     await message.answer(f"you are in the main menu",reply_markup=ichimlikli_buttons)

# @dp.message_handler(text="pepsi")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=pepsi_buttons)
#
# @dp.message_handler(text="coca cola")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
# @dp.message_handler(text="fanta")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
# @dp.message_handler(text="teas")
# async def bot_start(message: types.Message):
#      await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='pepsi')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=pepsili_buttons)

@dp.message_handler(text="2.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1,5.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="0,5.l pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='=coca cola')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=colali_buttons)

@dp.message_handler(text="2.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1,5.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="0,5.l coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu ",reply_markup=menu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='fanta')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=fantali_buttons)

@dp.message_handler(text="2.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1,5.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="0,5.l fanta")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='mexitto')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=mexitoli_buttons)

@dp.message_handler(text="2.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1,5.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="1.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="0,5.l mexito")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='choylar')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=choyli_buttons)

@dp.message_handler(text="1,choy")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="2,choy")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="limonli choy")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="novotli choy")
async def bot_start(message: types.Message):
    await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#===================================================================================================================


# @dp.message_handler(text='Sweets')
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=shirinlikli_buttons)
#
# @dp.message_handler(text="cake")
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
# @dp.message_handler(text="Chocolate cake")
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
# @dp.message_handler(text="banana cake")
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)
#
# @dp.message_handler(text="cream cake")
# async def bot_start(message: types.Message):
#     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#===================================================================================================================================================================














from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from keyboards.default.taomlar_uchun import taomlarbek_buttons
from keyboards.default.taomlar_uchun import fastfoodbek_buttons
from keyboards.default.taomlar_uchun import ichimlikbek_buttons
from keyboards.default.taomlar_uchun import shirinlikbek_buttons
from keyboards.default.taomlar_uchun import pepsibek_buttons
from keyboards.default.taomlar_uchun import colabek_buttons
from keyboards.default.taomlar_uchun import fantabek_buttons
from keyboards.default.taomlar_uchun import mexitobek_buttons
from keyboards.default.taomlar_uchun import choybek_buttons
from keyboards.default.taomlar_uchun import oshbek_buttons
from keyboards.default.taomlar_uchun import somsabek_buttons
from keyboards.default.taomlar_uchun import kabobbek_buttons
from keyboards.default.taomlar_uchun import shorvabek_buttons
from keyboards.default.taomlar_uchun import chushvarabek_buttons
from keyboards.default.taomlar_uchun import mantibek_buttons
from keyboards.default.taomlar_uchun import oramanbek_buttons
from keyboards.default.taomlar_uchun import menyu_buttons
from keyboards.default.taomlar_uchun import joybek_buttons
# from keyboards.inline.til_uchun import tillar_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!",reply_markup=tillar_buttons)

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте и добро пожаловать в наш бот")

@dp.callback_query_handler(text='til3')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Здравствуйте и добро пожаловать в наш бот",reply_markup=menyu_buttons)

@dp.message_handler(text='Национальные блюда')
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте и добро пожаловать в наш бот",reply_markup=taomlarbek_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="аннулирование заказа")
async def bot_start(message: types.Message):
    await message.answer(f"Заказы отменены, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Доставка заказа")
async def bot_start(message: types.Message):
    await message.answer(f"Заказ будет доставлен, заполните поле",reply_markup=joybek_buttons)

@dp.message_handler(text="назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#======================================================================================================================


# @dp.message_handler(text='Суп')
# async def bot_start(message: types.Message):
#     await message.answer(f"Вы можете выбрать суповые блюда",reply_markup=oshbek_buttons)

@dp.message_handler(text="Двайной Ош")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="мини-суп")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="суп каватак")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="все в одном")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)
#===================================================================================================================

# @dp.message_handler(text='Сомса')
# async def bot_start(message: types.Message):
#     await message.answer(f"Вы находитесь в меню сомсал",reply_markup=somsabek_buttons)


@dp.message_handler(text="Сомса с мясом")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="тыквенная сомса")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="карта")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="кокетливая сомса")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)
#======================================================================================================================

# @dp.message_handler(text='шашлыки')
# async def bot_start(message: types.Message):
#     await message.answer(f"Вы находитесь в шашлычном меню",reply_markup=kabobbek_buttons)

@dp.message_handler(text="беглый шашлык")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="кускавой шашлык")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="гладкий фарш")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="куриные шашлычки")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):

    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)
#====================================================================================================================

# @dp.message_handler(text='Супы')
# async def bot_start(message: types.Message):
#     await message.answer(f"ты в суповом меню",reply_markup=shorvabek_buttons)

@dp.message_handler(text="суп долма")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="штукатурка скорва")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)


#=====================================================================================================================



# @dp.message_handler(text='хучвара')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=chushvarabek_buttons)

@dp.message_handler(text="25 больших пельменей")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)


@dp.message_handler(text="15 мини-пельменей")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню", reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)


#====================================================================================================================

# @dp.message_handler(text='Богомол')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=mantibek_buttons)

@dp.message_handler(text="госгтли монти")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню", reply_markup=menyu_buttons)

@dp.message_handler(text="крепление карты")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню", reply_markup=menyu_buttons)

@dp.message_handler(text="Поппи Монти")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню", reply_markup=menyu_buttons)

@dp.message_handler(text="зеленый")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принят, вы в главном меню", reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)


#=====================================================================================================================

# @dp.message_handler(text="Оберточная бумага")
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=oramanbek_buttons)


@dp.message_handler(text="мясной рулет")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="я катаюсь с картошкой")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#======================================================================================================================

# @dp.message_handler(text='фастфуд')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=fastfoodbek_buttons)

# @dp.message_handler(text="лаваш")
# async def bot_start(message: types.Message):
#      await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)
#
# @dp.message_handler(text="шорма")
# async def bot_start(message: types.Message):
#      await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)
#
#
# @dp.message_handler(text="Ходдок")
# async def bot_start(message: types.Message):
#     await message.answer(f"Ваш заказ принят, вы в главном меню", reply_markup=menyu_buttons)
#
# @dp.message_handler(text="пицца")
# async def bot_start(message: types.Message):
#      await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)
#
@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)


#====================================================================================================================

# @dp.message_handler(text='напитки')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=ichimlikbek_buttons)


@dp.message_handler(text="пепси")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=pepsibek_buttons)

@dp.message_handler(text="Кока-Кола")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="фанта")
async def bot_start(message: types.Message):
     await message.answer(f"buyirtmangiz qabul qilindi, Asosiy menudasiz",reply_markup=menyu_buttons)

@dp.message_handler(text="чаи")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)


#=====================================================================================================================


# @dp.message_handler(text='пепси')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=ichimlikbek_buttons)

@dp.message_handler(text="2.л пепси")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1,5 л пепси")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1.л пепси")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="0,5 л пепси")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='кока-кола')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=colabek_buttons)

@dp.message_handler(text="2.л кока-колы")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1,5 л кока-колы")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1.л кока-колы")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="0,5 л кока-колы")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принят, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='фанта')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=fantabek_buttons)

@dp.message_handler(text="2.л фанта")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1,5 л вентилятор")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1. л фанта")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="0,5 л фанта")
async def bot_start(message: types.Message):
     await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='Мексика')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=mexitobek_buttons)

@dp.message_handler(text="2. л Мексикато")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1,5 л Мексикато")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="1. л Мексикато")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="0,5 л Мексикато")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#=====================================================================================================================

# @dp.message_handler(text='чаи')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=choybek_buttons)

@dp.message_handler(text="1, чай")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="2, чай")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="чай и лимон")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="новостной чай")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
     await message.answer(f"Вы находитесь в главном меню",reply_markup=menyu_buttons)

#===================================================================================================================


# @dp.message_handler(text='сладости')
# async def bot_start(message: types.Message):
#     await message.answer(f"заказ принят!",reply_markup=shirinlikbek_buttons)

@dp.message_handler(text="торт")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Шоколадный торт")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="банановый пирог")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="крем для торта")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Ваш заказ принимают, вы в главном меню",reply_markup=menyu_buttons)

