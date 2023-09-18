from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
reklama_jonatish_button = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton("Reklama jo'natish"),
        KeyboardButton("Bekor qilish")
        ]

    ],
    resize_keyboard=True
)

video_jonatish_button = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton('reklama jonatish'),
        KeyboardButton('bekor qilish'),

        ]
    ],
    resize_keyboard=True

)


tasdiqlashm_button = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton('Muammoni jonatish'),
        KeyboardButton('Bekor qilish'),

        ],

    ],
    resize_keyboard=True

)

tasdiqlashm_buttonru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('проблема отправлять'),
            KeyboardButton('Отмена'),

        ],

    ],
    resize_keyboard=True

)
