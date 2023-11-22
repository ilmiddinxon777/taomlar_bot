from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from loader import bot
from utils.chechking import checking
from data.config import kanallar



class Asosiy_chesking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        global holaat, kanal
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "quyidagi kanalga azo boling🔐\n"
        royxat = []
        daslabki_holati = True
        for k in kanallar:
            holaat = await checking(chat_id=user_id,kanal_link= k)
            daslabki_holati *= holaat

            kanal = await bot.get_chat(k)

        if not holaat:
            link = await kanal.export_invite_link()
            button = [InlineKeyboardButton(text="Obuna bolish✅",url=f"{link}")]
            royxat.append(button)
        royxat.append([InlineKeyboardButton(text="Tasdiqlash✅",callback_data='www')])
        if not daslabki_holati:
            await bot.send_message(chat_id=user_id, text=matn, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
            raise CancelHandler()

