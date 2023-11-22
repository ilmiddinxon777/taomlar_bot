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
from keyboards.default.menu_uchun import somsa_buttons
from keyboards.default.menu_uchun import kabob_buttons
from keyboards.default.menu_uchun import shorva_buttons
from keyboards.default.menu_uchun import chushvara_buttons
from keyboards.default.menu_uchun import manti_buttons
from keyboards.default.menu_uchun import oraman_buttons
from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.menu_uchun import joy_buttons
from keyboards.inline.til_uchun import tillar_buttons
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
    await message.answer(f"Hello and welcome to the bot",reply_markup=taomlar_buttons)

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


@dp.message_handler(text='soup')
async def bot_start(message: types.Message):
    await message.answer(f"you can choose pilaf dishes",reply_markup=osh_buttons)

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

@dp.message_handler(text='Somsalar')
async def bot_start(message: types.Message):
    await message.answer(f"Somsalar menusidasiz",reply_markup=somsa_buttons)


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

@dp.message_handler(text='kebabs')
async def bot_start(message: types.Message):
    await message.answer(f"Kaboblar menusidasiz",reply_markup=kabob_buttons)

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

@dp.message_handler(text='Soups')
async def bot_start(message: types.Message):
    await message.answer(f"shorvalar menusidasiz",reply_markup=shorva_buttons)

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

@dp.message_handler(text='Dumplings')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=chushvara_buttons)

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

@dp.message_handler(text='Mantis')
async def bot_start(message: types.Message):
    await message.answer(f"buyurtmangi qabul qilinadi",reply_markup=manti_buttons)

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

@dp.message_handler(text="Wrapping")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=oraman_buttons)


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

@dp.message_handler(text='fasfood')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=fastfood_buttons)

@dp.message_handler(text="lavash")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="shorma")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)


@dp.message_handler(text="hoddok")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="pizza")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#====================================================================================================================

@dp.message_handler(text='drinks')
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=ichimlik_buttons)

@dp.message_handler(text="pepsi")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=pepsi_buttons)

@dp.message_handler(text="coca cola")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="fanta")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="teas")
async def bot_start(message: types.Message):
     await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
     await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

#=====================================================================================================================

@dp.message_handler(text='pepsi')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=ichimlik_buttons)

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

@dp.message_handler(text='=coca cola')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=cola_buttons)

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

@dp.message_handler(text='fanta')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=fanta_buttons)

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

@dp.message_handler(text='mexitto')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=mexito_buttons)

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

@dp.message_handler(text='choylar')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=choy_buttons)

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


@dp.message_handler(text='Sweets')
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=shirinlik_buttons)

@dp.message_handler(text="cake")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Chocolate cake")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="banana cake")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="cream cake")
async def bot_start(message: types.Message):
    await message.answer(f"Your order has been accepted you are in the main menu",reply_markup=menu_buttons)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"you are in the main menu",reply_markup=menu_buttons)

