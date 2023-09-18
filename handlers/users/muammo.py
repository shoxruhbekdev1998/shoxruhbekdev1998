from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove



from keyboards.default.menu_uchun_ru import menu_buttun_ru
from keyboards.default.menu_uchun_uz import menu_buttun
from keyboards.default.rekalma_buttun import tasdiqlashm_button, tasdiqlashm_buttonru
from states.holatlar import Shikoyat,Shikoyatru
from loader import dp,bot

#muammolar bo'limi
@dp.message_handler(text="Muammo")
async def bot_echo(message: types.Message):
     await message.answer(text="Ismingizni Kiriting--> ",reply_markup=ReplyKeyboardRemove())
     await Shikoyat.ism_qabul_qilish.set()

@dp.message_handler(state=Shikoyat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
     ism = message.text
     await state.update_data({'name':ism})
     await message.answer(text="Familyani  Kiriting--> ")
     await Shikoyat.fam_qabul_qilish.set()

@dp.message_handler(state=Shikoyat.fam_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
     fam = message.text
     await state.update_data({'fam':fam})
     await message.answer(text="Yoshingizni   Kiriting--> ")
     await Shikoyat.yosh_qabul_qilish.set()

@dp.message_handler(state=Shikoyat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
     yosh = message.text
     await state.update_data({'age': yosh})
     await message.answer(text="Telefon nomeringizni   Kiriting--> ")
     await Shikoyat.tel_qabul_qilish.set()

@dp.message_handler(state=Shikoyat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
     tel = message.text
     await state.update_data({'tel': tel})
     await message.answer(text="Sizni bezovta qilayotgan muammoni kiriting batafsil, Shifokorlarimiz tomonidan tekshiriladi--> ")
     await Shikoyat.shikoyat_qabul_qilish.set()

@dp.message_handler(state=Shikoyat.shikoyat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
     matn = message.text
     username = message.from_user.username
     user_id = message.from_user.id
     await state.update_data({'matn':matn})
     malumot = await state.get_data()
     ism = malumot.get("name")
     fam = malumot.get("fam")
     yosh = malumot.get("age")
     tel = malumot.get("tel")
     qmalumot = malumot.get("matn")
     s = f"Ismi : {ism}\n" \
         f"Familyasi : {fam}\n" \
         f"Yoshi : {yosh}\n" \
         f"Tel: {tel}\n" \
         f"Shikoyatlari : {qmalumot}\n" \


     await bot.send_message(chat_id=user_id,text=s,reply_markup=tasdiqlashm_button)
     await Shikoyat.shikoyatni_tasdiqlash.set()


@dp.message_handler(state=Shikoyat.shikoyatni_tasdiqlash,text='Muammoni jonatish')
async def bot_echo(message: types.Message,state:FSMContext):
     malumot = await state.get_data()
     username = message.from_user.username
     user_id = message.from_user.id
     ism = malumot.get("name")
     fam = malumot.get("fam")
     yosh = malumot.get("age")
     tel = malumot.get("tel")
     qmalumot = malumot.get("matn")
     s = f"Ismi : {ism}\n" \
         f"Familyasi : {fam}\n" \
         f"Yoshi : {yosh}\n" \
         f"Tel nomer: {tel}\n" \
         f"Shikoyatlari : {qmalumot}\n"\
         f"Tg_id: {user_id}\n"\
         f"username:{username}"

     await bot.send_message(chat_id="@ww3324",text=s)

     await bot.send_message(chat_id=user_id, text="Shifoxonaga Yuborildi",reply_markup=menu_buttun)
     await state.finish()

@dp.message_handler(state=Shikoyat.shikoyatni_tasdiqlash,text='Bekor qilish')
async def bot_echo(message: types.Message,state:FSMContext):
     await bot.send_message(chat_id=message.from_user.id,text='Bekor qilish',reply_markup=menu_buttun)
     await state.finish()





#rus tili muammo

@dp.message_handler(text="Проблема")
async def bot_echo(message: types.Message):
     await message.answer(text="Введите ваше имя--> ",reply_markup=ReplyKeyboardRemove())
     await Shikoyatru.ism_qabul_qilishru.set()

@dp.message_handler(state=Shikoyatru.ism_qabul_qilishru)
async def bot_echo(message: types.Message,state:FSMContext):
     ismru = message.text
     await state.update_data({'name':ismru})
     await message.answer(text="Введите вашу фамилию--> ")
     await Shikoyatru.fam_qabul_qilishru.set()

@dp.message_handler(state=Shikoyatru.fam_qabul_qilishru)
async def bot_echo(message: types.Message,state:FSMContext):
     famru = message.text
     await state.update_data({'fam':famru})
     await message.answer(text="Введите свой возраст--> ")
     await Shikoyatru.yosh_qabul_qilishru.set()

@dp.message_handler(state=Shikoyatru.yosh_qabul_qilishru)
async def bot_echo(message: types.Message,state:FSMContext):
     yoshru = message.text
     await state.update_data({'age': yoshru})
     await message.answer(text="Введите свой номер телефона--> ")
     await Shikoyatru.tel_qabul_qilishru.set()

@dp.message_handler(state=Shikoyatru.tel_qabul_qilishru)
async def bot_echo(message: types.Message,state:FSMContext):
     telru = message.text
     await state.update_data({'tel': telru})
     await message.answer(text="Пожалуйста, подробно опишите вашу проблему, она будет проверена нашими врачами--> ")
     await Shikoyatru.shikoyat_qabul_qilishru.set()

@dp.message_handler(state=Shikoyatru.shikoyat_qabul_qilishru)
async def bot_echo(message: types.Message,state:FSMContext):
     matn = message.text
     username = message.from_user.username
     user_id = message.from_user.id
     await state.update_data({'matn':matn})
     malumot = await state.get_data()
     ismru = malumot.get("name")
     famru = malumot.get("fam")
     yoshru = malumot.get("age")
     telru = malumot.get("tel")
     qmalumotru = malumot.get("matn")
     s = f"Имя : {ismru}\n" \
         f"Фамилия : {famru}\n" \
         f"Возраст : {yoshru}\n" \
         f"Номер телефона: {telru}\n" \
         f"Жалобы : {qmalumotru}\n" \


     await bot.send_message(chat_id=user_id,text=s,reply_markup=tasdiqlashm_buttonru)
     await Shikoyatru.shikoyatni_tasdiqlashru.set()


@dp.message_handler(state=Shikoyatru.shikoyatni_tasdiqlashru,text='проблема отправлять')
async def bot_echo(message: types.Message,state:FSMContext):
     malumot = await state.get_data()
     username = message.from_user.username
     user_id = message.from_user.id
     ismru = malumot.get("name")
     famru = malumot.get("fam")
     yoshru= malumot.get("age")
     telru = malumot.get("tel")
     qmalumotru = malumot.get("matn")
     s = f"Имя : {ismru}\n" \
         f"Фамилия : {famru}\n" \
         f"Возраст : {yoshru}\n" \
         f"Номер телефона: {telru}\n" \
         f"Жалобы : {qmalumotru}\n"\
         f"Tg_id: {user_id}\n"\
         f"username:{username}"

     await bot.send_message(chat_id="@ww3324",text=s)

     await bot.send_message(chat_id=user_id, text="Отправили в больницу",reply_markup=menu_buttun_ru)
     await state.finish()

@dp.message_handler(state=Shikoyatru.shikoyatni_tasdiqlashru,text='Отмена')
async def bot_echo(message: types.Message,state:FSMContext):
     await bot.send_message(chat_id=message.from_user.id,text='Oтмена',reply_markup=menu_buttun_ru)
     await state.finish()




