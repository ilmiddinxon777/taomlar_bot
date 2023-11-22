from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text="O'zbek tili ",callback_data="til1"),
        ],
        [
            InlineKeyboardButton(text="English tili", callback_data="til2"),
        ],
        [
            InlineKeyboardButton(text="Rus tili",callback_data="til3"),
        ],
        [
            InlineKeyboardButton(text="kanalga azo bolin",url='https://t.me/insta_dunyo_ilmiddin'),
            InlineKeyboardButton(text="botni ulashish",switch_inline_query="shu bot zor ekan tavsiya beraman")
        ]
    ]
)