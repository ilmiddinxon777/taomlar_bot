from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_uchun import tasdiqlash_buttons
from keyboards.default.menu_uchun import meny_buttons
from states.holotlar import Adminga_murojat
from loader import dp, bot


# Echo bot
@dp.message_handler(text="Adminga murojat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismingizni kiriting")
    await Adminga_murojat.ism_qabul_qilish.set()




@dp.message_handler(state=Adminga_murojat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"ismi":ism})
    await message.answer(text="Familyangizni  kiriting")
    await Adminga_murojat.fam_qabul_qilish.set()


@dp.message_handler(state=Adminga_murojat.fam_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    famila = message.text
    await state.update_data({"fam":famila})
    await message.answer(text="yoshni kiriting")
    await Adminga_murojat.yosh_qabul_qilish.set()


@dp.message_handler(state=Adminga_murojat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data({"age":yoshi})
    await message.answer(text="Telni kiriting")
    await Adminga_murojat.tel_qabul_qilish.set()



@dp.message_handler(state=Adminga_murojat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    nomer = message.text
    await state.update_data({"number":nomer})
    await message.answer(text="Manzilni kirinting kiriting")
    await Adminga_murojat.manzil_qabul_qilish.set()


@dp.message_handler(state=Adminga_murojat.manzil_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    manzil = message.text
    await state.update_data({"Manzil":manzil})
    await message.answer(text="Murojatni kirinting kiriting")
    await Adminga_murojat.murojat_qabul_qilish.set()


@dp.message_handler(state=Adminga_murojat.murojat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    murojjat = message.text
    await state.update_data({"text":murojjat})
    malumot = await state.get_data()
    ism = malumot.get("ismi")
    familyasi = malumot.get("fam")
    yoshi = malumot.get("age")
    tel = malumot.get("number")
    manzil = malumot.get("Manzil")
    matn = malumot.get("text")

    text= f"🙋🏻 Ism : {ism}\n" \
          f"✅ Familyasi : {familyasi}\n" \
          f"✅ Yoshi : {yoshi}\n" \
          f"✅ tel : {tel}\n" \
          f"✅ Manzili : {manzil}\n" \
          f"✅ Murojat : {matn}\n" \

    await message.answer(text=text,reply_markup=tasdiqlash_buttons)
    await Adminga_murojat.tasdiqlash_qabul_qilish.set()


@dp.message_handler(state=Adminga_murojat.tasdiqlash_qabul_qilish,text="Tasdiqlash")
async def bot_echo(message: types.Message,state:FSMContext):

    malumot = await state.get_data()
    ism = malumot.get("ismi")
    familyasi = malumot.get("fam")
    yoshi = malumot.get("age")
    tel = malumot.get("number")
    manzil = malumot.get("Manzil")
    matn = malumot.get("text")

    text= f"🙋🏻‍Ism : {ism}\n" \
          f"✅Familyasi : {familyasi}\n" \
          f"✅Yoshi : {yoshi}\n" \
          f"✅tel : {tel}\n" \
          f"✅Manzili : {manzil}\n" \
          f"✅Murojat : {matn}\n" \

    await bot.send_message(chat_id=5110814400,text=text,)
    await message.answer(text="Adminga yuborildi", reply_markup=meny_buttons)
    await state.finish()


@dp.message_handler(state=Adminga_murojat.tasdiqlash_qabul_qilish,text="Bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Bekor qilindi", reply_markup=meny_buttons)
    await state.finish()




#===============================================================================================================













from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.taomlar_uchun import tasdiqlashli_buttons
from keyboards.default.taomlar_uchun import menu_buttons
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

    text= f"🙋🏻Name : {ism}\n" \
          f"✅Family : {familyasi}\n" \
          f"✅Age : {yoshi}\n" \
          f"✅tel : {tel}\n" \
          f"✅Address : {manzil}\n" \
          f"✅Appeal : {matn}\n" \

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

    text= f"🙋🏻Name : {ism}\n" \
          f"✅Family : {familyasi}\n" \
          f"✅Age : {yoshi}\n" \
          f"✅tel : {tel}\n" \
          f"✅Address : {manzil}\n" \
          f"✅Appeal : {matn}\n" \

    await bot.send_message(chat_id=5110814400,text=text,)
    await message.answer(text="Sent to admin", reply_markup=menu_buttons)
    await state.finish()


@dp.message_handler(state=Adminga_murojatlar.tasdiqelashe_qabul,text="cancel")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Canceled", reply_markup=menu_buttons)
    await state.finish()

#====================================================================================================================================


from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.taomlar_uchun import tasdiqlashr_buttons
from keyboards.default.taomlar_uchun import menyu_buttons
from states.holotlar import Adminga_murojatlarru
from loader import dp, bot


# Echo bot
@dp.message_handler(text="Свяжитесь с администратором")
async def bot_echo(message: types.Message):
    await message.answer(text="Введите ваше имя")
    await Adminga_murojatlarru.ismr_qabul.set()




@dp.message_handler(state=Adminga_murojatlarru.ismr_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"Имя":ism})
    await message.answer(text="Введите свою фамилию")
    await Adminga_murojatlarru.famr_qabul.set()


@dp.message_handler(state=Adminga_murojatlarru.famr_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    famila = message.text
    await state.update_data({"семья":famila})
    await message.answer(text="введите возраст")
    await Adminga_murojatlarru.yoshr_qabul.set()


@dp.message_handler(state=Adminga_murojatlarru.yoshr_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data({"возраст":yoshi})
    await message.answer(text="Введите телефон")
    await Adminga_murojatlarru.telr_qabul.set()



@dp.message_handler(state=Adminga_murojatlarru.telr_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    nomer = message.text
    await state.update_data({"число":nomer})
    await message.answer(text="Введите адрес")
    await Adminga_murojatlarru.manzilr_qabul.set()


@dp.message_handler(state=Adminga_murojatlarru.manzilr_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    manzil = message.text
    await state.update_data({"Адрес":manzil})
    await message.answer(text="Пожалуйста, введите ваш адрес")
    await Adminga_murojatlarru.murojatr_qabul.set()


@dp.message_handler(state=Adminga_murojatlarru.murojatr_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    murojjat = message.text
    await state.update_data({"text":murojjat})
    malumot = await state.get_data()
    ism = malumot.get("Имя")
    familyasi = malumot.get("семья")
    yoshi = malumot.get("возраст")
    tel = malumot.get("число")
    manzil = malumot.get("Адрес")
    matn = malumot.get("text")

    text= f"🙋🏻Имя : {ism}\n" \
          f"✅Семья : {familyasi}\n" \
          f"✅Возраст : {yoshi}\n" \
          f"✅тел : {tel}\n" \
          f"✅Адрес : {manzil}\n" \
          f"Б✅ращаться : {matn}\n" \

    await message.answer(text=text,reply_markup=tasdiqlashr_buttons)
    await Adminga_murojatlarru.tasdiqelashr_qabul.set()


@dp.message_handler(state=Adminga_murojatlarru.tasdiqelashr_qabul,text="Подтверждение")
async def bot_echo(message: types.Message,state:FSMContext):

    murojjat = message.text
    await state.update_data({"text":murojjat})
    malumot = await state.get_data()
    ism = malumot.get("Имя")
    familyasi = malumot.get("семья")
    yoshi = malumot.get("возраст")
    tel = malumot.get("число")
    manzil = malumot.get("Адрес")
    matn = malumot.get("text")

    text= f"🙋🏻Имя : {ism}\n" \
          f"✅Семья : {familyasi}\n" \
          f"✅Возраст : {yoshi}\n" \
          f"✅тел : {tel}\n" \
          f"✅Адрес : {manzil}\n" \
          f"✅Бращаться : {matn}\n" \




    await bot.send_message(chat_id=5110814400,text=text,)
    await message.answer(text="Отправлено администратору", reply_markup=menyu_buttons)
    await state.finish()


@dp.message_handler(state=Adminga_murojatlarru.tasdiqelashr_qabul,text="Отмена")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Отменено", reply_markup=menyu_buttons)
    await state.finish()

