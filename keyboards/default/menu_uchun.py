from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


meny_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Milliy taomlar"),
            KeyboardButton(text="fasfood"),
        ],
        [
            KeyboardButton(text="ichimliklar"),
            KeyboardButton(text="shirinliklar")
        ],
        [
            KeyboardButton(text="buyurtmani bekor qilish"),
            KeyboardButton(text="Buyurtmani yetkazish")
        ],
        [
            KeyboardButton(text="Adminga murojat")
        ]
    ],
    resize_keyboard=True
)


tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

joyli_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="lokatsiya",request_location=True),
            KeyboardButton(text="Kontakt",request_contact=True)
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True

)


from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

somsali_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Go'shtli somsa"),
            KeyboardButton(text="ashqavoq somsa")
        ],
        [
            KeyboardButton(text="kartochka"),
            KeyboardButton(text="kokatli somsalar")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kabobli_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ravon shashlik"),
            KeyboardButton(text="kuskavoy shashlik")
        ],
        [
            KeyboardButton(text="ravon qiyma shashlik"),
            KeyboardButton(text="toviq g'oshti shashlik")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shorvali_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="dolma shorva"),
            KeyboardButton(text="suvak skorva")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

chushvarali_buttons= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="25 tali katta chuchvara"),
            KeyboardButton(text="15 talik mini chuchvarar")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

mantili_buttons= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="gosgtli monti"),
            KeyboardButton(text="kartojkali monti")
        ],
        [
            KeyboardButton(text="ashqavoqli monti"),
            KeyboardButton(text="ko'katli")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

oramanli_buttons= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="g'oshtli orama"),
            KeyboardButton(text="kartoshkali oraman")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True


)