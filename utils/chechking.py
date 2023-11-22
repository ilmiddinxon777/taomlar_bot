import typing
from aiogram import Bot
async def checking(chat_id,kanal_link):
    bot = Bot.get_current()
    user = await bot.get_chat_member(chat_id=kanal_link,user_id=chat_id)
    return user.is_chat_member()

