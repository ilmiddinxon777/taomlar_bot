from aiogram import types
from googletrans import Translator
from loader import dp

tarjima = Translator()


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    til = tarjima.detect(text=message.text).lang
    if til=='uz':
        tarjima_qilish = tarjima.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=tarjima_qilish)

    if til=='en':
        tarjima_qilish = tarjima.translate(text=message.text,dest='uz',src='en').text
        await message.answer(text=tarjima_qilish)