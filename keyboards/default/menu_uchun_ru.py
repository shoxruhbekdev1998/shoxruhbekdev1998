from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base

menular = base.select_all_menu_ru()
index = 0
i = 0
royxat = []
for menu in menular:
    if i % 2 == 0 and i != 0:
        index+=1
    if i%2==0:
        royxat.append([KeyboardButton(text=menu[1])])
    else:
        royxat[index].append(KeyboardButton(text=menu[1]))
    i+=1

royxat.append([KeyboardButton(text="Проблема")])
royxat.append([KeyboardButton(text='Главное меню')])


menu_buttun_ru = ReplyKeyboardMarkup(keyboard =royxat,resize_keyboard=True)

abcd_buttonr = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton("А"),
        KeyboardButton("Б"),


        ],
        [
        KeyboardButton("С"),
        KeyboardButton("Д"),

        ],
        [
        KeyboardButton("назад")
        ]

    ],
    resize_keyboard=True
)