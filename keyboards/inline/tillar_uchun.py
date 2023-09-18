from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
tillar_buttun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data="til1"),
            InlineKeyboardButton(text="Rus tili",callback_data="til2")

        ],
        [
            InlineKeyboardButton(text="TG_SHIFOKOR",url="https://t.me/TG_SHIFOKOR"),
            InlineKeyboardButton(text="Botni Ulashish",switch_inline_query="Bu bot sizni sog'lom hayot kechirishingizda ko'maklashadi va sizda kuzatilishi mumkin bo'lgan kasalliklarni oldindan aniqlashga ko'maklashadi.")
        ]
    ]
)