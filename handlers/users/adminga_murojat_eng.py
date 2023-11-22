from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.taomlar_uchun import tasdiqlashli_buttons
from keyboards.default.menu_uchun import meny_buttons
from states.holotlar import Adminga_murojatlar
from loader import dp, bot

# Echo bot
@dp.message_handler(text="Contact the admin")
async def bot_echo(message: types.Message):
    await message.answer(text="Enter your name")
    await Adminga_murojatlar.isme_qabul.set()




@dp.message_handler(state=Adminga_murojatlar.isme_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"name":ism})
    await message.answer(text="Enter your last name")
    await Adminga_murojatlar.fame_qabul.set()


@dp.message_handler(state=Adminga_murojatlar.fame_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    famila = message.text
    await state.update_data({"fam":famila})
    await message.answer(text="enter age")
    await Adminga_murojatlar.yoshe_qabul.set()


@dp.message_handler(state=Adminga_murojatlar.yoshe_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data({"age":yoshi})
    await message.answer(text="Enter the phone")
    await Adminga_murojatlar.tele_qabul.set()



@dp.message_handler(state=Adminga_murojatlar.tele_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    nomer = message.text
    await state.update_data({"number":nomer})
    await message.answer(text="Enter the address")
    await Adminga_murojatlar.manzile_qabul.set()


@dp.message_handler(state=Adminga_murojatlar.manzile_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    manzil = message.text
    await state.update_data({"Address":manzil})
    await message.answer(text="Please enter your address")
    await Adminga_murojatlar.murojate_qabul.set()


@dp.message_handler(state=Adminga_murojatlar.murojate_qabul)
async def bot_echo(message: types.Message,state:FSMContext):

    malumot = await state.get_data()
    ism = malumot.get("Name")
    familyasi = malumot.get("fam")
    yoshi = malumot.get("age")
    tel = malumot.get("number")
    manzil = malumot.get("Address")
    matn = malumot.get("text")

    text= f"Name : {ism}\n" \
          f"Family : {familyasi}\n" \
          f"Age : {yoshi}\n" \
          f"tel : {tel}\n" \
          f"Address : {manzil}\n" \
          f"Appeal : {matn}\n" \

    await message.answer(text=text,reply_markup=tasdiqlashli_buttons)
    await Adminga_murojatlar.tasdiqelashe_qabul.set()


@dp.message_handler(state=Adminga_murojatlar.tasdiqelashe_qabul,text="Confirmation")
async def bot_echo(message: types.Message,state:FSMContext):

    malumot = await state.get_data()
    ism = malumot.get("Name")
    familyasi = malumot.get("fam")
    yoshi = malumot.get("age")
    tel = malumot.get("number")
    manzil = malumot.get("Address")
    matn = malumot.get("text")

    text= f"Name : {ism}\n" \
          f"Family : {familyasi}\n" \
          f"Age : {yoshi}\n" \
          f"tel : {tel}\n" \
          f"Address : {manzil}\n" \
          f"Appeal : {matn}\n" \

    await bot.send_message(chat_id=5110814400,text=text,)
    await message.answer(text="Sent to admin", reply_markup=meny_buttons)
    await state.finish()


@dp.message_handler(state=Adminga_murojatlar.tasdiqelashe_qabul,text="cancel")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Canceled", reply_markup=meny_buttons)
    await state.finish()
