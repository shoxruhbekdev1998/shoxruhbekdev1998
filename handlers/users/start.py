from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart



#tillar
from aiogram.types import CallbackQuery

from keyboards.inline.tillar_uchun import tillar_buttun
from keyboards.default.menu_uchun_ru import menu_buttun_ru
from keyboards.default.menu_uchun_uz import menu_buttun
from loader import dp, base, bot


# Tillar uchun

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism,fam=fam,username=message.from_user.username,tg_id=user_id)
    except Exception:
        pass
    await message.answer(f'Tillarni tanlang-->\n'
                         f'Выберите языки-->\n'
                         f"Bu bot sizdagi uralogik  kassaliklarni erta aniqlashga va shifoxonalarga yo'naltirishga ko'rsatmalar beradi. \n"
                         f"Этот бот проведет вас к раннему выявлению и направлению в больницу для урологических заболеваний.",reply_markup=tillar_buttun)



#uz

@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Ixtiyoriy bo'limni tanlang\n"
                               f"Test_1 bo'limi ---- Siydik yo'llari kasalliklari bo'yicha savolnoma.\n"
                               f"Test_2 bo'limi ----  Prostata bezi adenomasi bo'yicha savolnoma.\n"
                               f"Test_3 bo'limi ---- Jinsiy zaiflik bo'yicha savolnoma\n"
                               f" Muammo bo'limi ---- O'zingizni qiynayotgan kasalliklar va muammolaringiz bo'yicha shifoxonamizga murojat bo'limi ",reply_markup=menu_buttun)


#ru

@dp.callback_query_handler(text="til2")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Выберите необязательный раздел \n"
                               f"Раздел Test_1r ---- Анкета по заболеваниям мочевыводящих путей.\n"
                               f"Раздел Test_2r ---- Анкета по аденоме предстательной железы.\n"
                               f"Раздел Test_3r ---- Анкета по половому бессилию\n"
                               f"Проблемное отделение ---- Отдел направления в нашу больницу для лечения заболеваний и проблем, от которых вы страдаете",reply_markup=menu_buttun_ru)

@dp.callback_query_handler(text="www")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f'Tillarni tanlang-->\n'
                         f'Выберите языки-->\n'
                         f"Bu bot sizdagi uralogik  kassaliklarni erta aniqlashga va shifoxonalarga yo'naltirishga ko'rsatmalar beradi. \n"
                         f"Этот бот проведет вас к раннему выявлению и направлению в больницу для урологических заболеваний.",reply_markup=tillar_buttun)


#orqaga
@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Ixtiyoriy bo'limni tanlang\n"
                               f"Test1 bo'limi ---- Siydik yo'llari kasalliklari bo'yicha savolnoma.\n"
                               f"Test2 bo'limi ----  Prostata bezi adenomasi bo'yicha savolnoma.\n"
                               f"Test3 bo'limi ---- Jinsiy zaiflik bo'yicha savolnoma\n"
                               f" Muammo bo'limi ---- O'zingizni qiynayotgan kasalliklar va muammolaringiz bo'yicha shifoxonamizga murojat bo'limi ",
                               reply_markup=menu_buttun)


@dp.message_handler(text="назад")
async def bot_start(message: types.Message):
          await message.answer(f"Выберите необязательный раздел \n"
                               f"Раздел Test1r ---- Анкета по заболеваниям мочевыводящих путей.\n"
                               f"Раздел Test2r ---- Анкета по аденоме предстательной железы.\n"
                               f"Раздел Test3 ---- Анкета по половому бессилию\n"
                               f"Проблемное отделение ---- Отдел направления в нашу больницу для лечения заболеваний и проблем, от которых вы страдаете",
                               reply_markup=menu_buttun_ru)

#bosh menu

@dp.message_handler(text="Bosh menu")
async def bot_start(message: types.Message):
    await message.answer(f'Tillarni tanlang-->\n'
                         f'Выберите языки-->\n'
                         f"Bu bot sizdagi uralogik  kassaliklarni erta aniqlashga va shifoxonalarga yo'naltirishga ko'rsatmalar beradi. \n"
                         f"Этот бот проведет вас к раннему выявлению и направлению в больницу для урологических заболеваний.",reply_markup=tillar_buttun)

@dp.message_handler(text="Главное меню")
async def bot_start(message: types.Message):
    await message.answer(f'Tillarni tanlang-->\n'
                         f'Выберите языки-->\n'
                         f"Bu bot sizdagi uralogik  kassaliklarni erta aniqlashga va shifoxonalarga yo'naltirishga ko'rsatmalar beradi. \n"
                         f"Этот бот проведет вас к раннему выявлению и направлению в больницу для урологических заболеваний.",reply_markup=tillar_buttun)


#statistika
@dp.message_handler(commands="obuna",chat_id= '1961871634')
async def bot_start(message: types.Message):
    userlar = base.count_users()
    a = ((userlar))
    await bot.send_message(chat_id=1961871634,text=f" Umumiy obunachilar soni   {a} ta   {message.from_user.full_name}!")





