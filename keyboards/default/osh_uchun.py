from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

osh_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="katta osh"),
            KeyboardButton(text="Mini osh")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)