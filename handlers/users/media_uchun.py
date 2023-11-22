from aiogram import types

from keyboards.default.menu_uchun import chushvarali_buttons
from keyboards.default.menu_uchun import kabobli_buttons
from keyboards.default.menu_uchun import mantili_buttons
from keyboards.default.menu_uchun import meny_buttons
from keyboards.default.menu_uchun import oramanli_buttons
from keyboards.default.menu_uchun import shorvali_buttons
from keyboards.default.menu_uchun import somsali_buttons
from keyboards.default.taomlar_uchun import cola_buttons
from keyboards.default.taomlar_uchun import fanta_buttons
from keyboards.default.taomlar_uchun import fastfood_buttons
from keyboards.default.taomlar_uchun import ichimlik_buttons
from keyboards.default.taomlar_uchun import osh_buttons
from keyboards.default.taomlar_uchun import pepsi_buttons
from keyboards.default.taomlar_uchun import shirinlik_buttons

from loader import dp,bot


# from keyboards.inline.til_uchun import tillar_buttons


@dp.message_handler(text="Osh")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Osh menusidasiz", reply_markup=osh_buttons)

@dp.message_handler(text="Somsalar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Somsa menusidasiz", reply_markup=somsali_buttons)

@dp.message_handler(text="kaboblar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Kabob menusadasiz", reply_markup=kabobli_buttons)

@dp.message_handler(text="Shorvalar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Shorva menusidsiz ", reply_markup=shorvali_buttons)


@dp.message_handler(text="Chuchvara")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Chuchvaralar menusidasiz,", reply_markup=chushvarali_buttons)

@dp.message_handler(text="Manti")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Manti menusidasiz,", reply_markup=mantili_buttons)

@dp.message_handler(text="O'rama")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("O'rama menusidasiz", reply_markup=oramanli_buttons)

@dp.message_handler(text="fasfood")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Fastfood menusidasiz", reply_markup=fastfood_buttons)

@dp.message_handler(text="lavash")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buyurtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="shourma")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buyurtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="hoddok")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buyurtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="pizza")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buyurtmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="ichimliklar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Ichimlik menusidasiz ", reply_markup=ichimlik_buttons)

@dp.message_handler(text="pepsi")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("pepsi menu", reply_markup=pepsi_buttons)

@dp.message_handler(text="fanta")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Fanta menu", reply_markup=fanta_buttons)

@dp.message_handler(text="coca cola")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/18"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("cola menu", reply_markup=cola_buttons)


@dp.message_handler(text="choylar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/19"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buritrmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)


@dp.message_handler(text="mexitto")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/20"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buritrmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)


@dp.message_handler(text="shirinliklar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/21"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Shirinliklar menu", reply_markup=shirinlik_buttons)


@dp.message_handler(text="tort")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/22"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buritrmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)


@dp.message_handler(text="shkaladniy tort")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/23"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buritrmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="bananli tort")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/24"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buritrmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

@dp.message_handler(text="qaymoqli tort")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/26"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("Buritrmangiz qabul qilindi, Asosiy menudasiz", reply_markup=meny_buttons)

#=====================================================================================================================


from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
# from aiogram.types import CallbackQuery
# from keyboards.default.taomlar_uchun import taomlarli_buttons
from keyboards.default.taomlar_uchun import fastfoodli_buttons
from keyboards.default.taomlar_uchun import ichimlikli_buttons
from keyboards.default.taomlar_uchun import shirinlikli_buttons
from keyboards.default.taomlar_uchun import pepsili_buttons
from keyboards.default.taomlar_uchun import colali_buttons
from keyboards.default.taomlar_uchun import fantali_buttons
from keyboards.default.taomlar_uchun import mexitoli_buttons
# from keyboards.default.taomlar_uchun import choyli_buttons
from keyboards.default.taomlar_uchun import oshli_buttons
from keyboards.default.taomlar_uchun import somsajon_buttons
from keyboards.default.taomlar_uchun import kabob_buttons
from keyboards.default.taomlar_uchun import shorva_buttons
from keyboards.default.taomlar_uchun import chushvara_buttons
from keyboards.default.taomlar_uchun import manti_buttons
from keyboards.default.taomlar_uchun import oraman_buttons
from keyboards.default.taomlar_uchun import menu_buttons
# from keyboards.default.taomlar_uchun import joy_buttons


@dp.message_handler(text="soup")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=oshli_buttons)

@dp.message_handler(text="Somsalar")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=somsajon_buttons)

@dp.message_handler(text="kebabs")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=kabob_buttons)

@dp.message_handler(text="Soups")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=shorva_buttons)


@dp.message_handler(text="Dumplings")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=chushvara_buttons)

@dp.message_handler(text="Mantis")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=manti_buttons)

@dp.message_handler(text="Wrapping")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=oraman_buttons)

@dp.message_handler(text="fasfood")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=fastfoodli_buttons)

@dp.message_handler(text="lavash")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="shourma")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="hoddok")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="pizza")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="drinks")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=ichimlikli_buttons)

@dp.message_handler(text="pepsi")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=pepsili_buttons)

@dp.message_handler(text="fanta")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=fantali_buttons)

@dp.message_handler(text="coca cola")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/18"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=colali_buttons)


@dp.message_handler(text="teas")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/19"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)


@dp.message_handler(text="mexitto")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/20"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=mexitoli_buttons)


@dp.message_handler(text="Sweets")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/21"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=shirinlikli_buttons)


@dp.message_handler(text="cake")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/22"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)


@dp.message_handler(text="Chocolate tort")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/23"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="banana cake")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/24"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

@dp.message_handler(text="cream cake3")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/26"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("you are in the main menu", reply_markup=menu_buttons)

#+=====================================================================================================================================









from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
# from aiogram.types import CallbackQuery
# from keyboards.default.taomlar_uchun import taomlarbek_buttons
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








@dp.message_handler(text="Суп")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=oshbek_buttons)

@dp.message_handler(text="Сомса")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=somsabek_buttons)

@dp.message_handler(text="шашлыки")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=kabobbek_buttons)

@dp.message_handler(text="Супы")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=shorvabek_buttons)


@dp.message_handler(text="хучвара")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=chushvarabek_buttons)

@dp.message_handler(text="Богомол")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=mantibek_buttons)

@dp.message_handler(text="Оберточная")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=oramanbek_buttons)

@dp.message_handler(text="фастфуд")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=fastfoodbek_buttons)

@dp.message_handler(text="лаваш")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="шорма")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="Ходдок")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="пицца")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="напитки")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=ichimlikbek_buttons)

@dp.message_handler(text="пепси")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=pepsibek_buttons)

@dp.message_handler(text="фанта")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=fantabek_buttons)

@dp.message_handler(text="Кока-Кола")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/18"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=colabek_buttons)


@dp.message_handler(text="чаи")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/19"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=choybek_buttons)


@dp.message_handler(text="Мексика")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/20"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=mexitobek_buttons)


@dp.message_handler(text="сладости")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/21"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=shirinlikbek_buttons)


@dp.message_handler(text="торт")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/22"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)


@dp.message_handler(text="Шоколадный торт")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/23"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="банановый пирог")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/24"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="крем для торта")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/26"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)

@dp.message_handler(text="Go'shtli somsa")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/malumotlar_bot_uchun/26"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)
    await message.answer("ты в суповом меню", reply_markup=menyu_buttons)