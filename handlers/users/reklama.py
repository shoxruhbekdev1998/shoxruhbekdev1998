from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove


from keyboards.inline.tillar_uchun import tillar_buttun
from states.holatlar import Reklama,Videorek
from loader import dp,base,bot


#Reklama

from keyboards.default.rekalma_buttun import *























#reklama jo'natish


@dp.message_handler(commands='reklama' ,chat_id= '1961871634')
async def bot_echo(message: types.Message):
        await message.answer(text="Rasm linkini jo'nating---> ")
        await Reklama.rasm_qabul_qilish.set()




@dp.message_handler(state=Reklama.rasm_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    rasm = message.text
    if not 'http' in rasm:
        await bot.send_message(chat_id="1961871634",text="Iltimos rasm linkini qaytatdan kiriting ")
        await Reklama.rasm_qabul_qilish.set()
    else:
        await state.update_data({'link':rasm})
        await message.answer(text="Maxsulot nomini kiriting---> ")
        await Reklama.nom_qabul_qilish.set()


@dp.message_handler(state=Reklama.nom_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.answer(text="Maxsulot haqida malumot kiritng--> ")
    await Reklama.tavsif_qabul_qilish.set()

@dp.message_handler(state=Reklama.tavsif_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    tavsif = message.text
    await state.update_data({'tavsif':tavsif})
    malumot = await state.get_data()
    rasm = malumot.get("link")
    name = malumot.get("name")
    tavsif = malumot.get("tavsif")
    rasm_link = f"{rasm}"
    s = f"---> : {name}\n" \
        f"🔍 : {tavsif}\n" \



    await bot.send_photo(chat_id='1961871634',photo=rasm_link,caption=s,reply_markup=reklama_jonatish_button)
    await Reklama.reklamani_tasdiqlash.set()


@dp.message_handler(state=Reklama.reklamani_tasdiqlash,text="Reklama jo'natish")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    rasm = malumot.get("link")
    name = malumot.get("name")
    tavsif = malumot.get("tavsif")
    rasm_link = f"{rasm}"
    s = f"---> : {name}\n" \
        f"🔍 {tavsif}\n" \


    userlar = base.select_all_users()
    for user in userlar:
        try:
           await bot.send_message(chat_id=message.from_user.id, text="Reklama jo'natildi", reply_markup=ReplyKeyboardRemove())
           await bot.send_photo(chat_id=user[4], photo=rasm_link, caption=s)
        except Exception:
            pass


@dp.message_handler(state=Reklama.reklamani_tasdiqlash,text="Bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Bekor qilindi",reply_markup=ReplyKeyboardRemove())
    await state.finish()


#reklama video

@dp.message_handler(commands='video' ,chat_id= '1961871634')
async def bot_echo(message: types.Message):
    await message.answer(text="Video linkini jo'nating---> ")
    await Videorek.video_qabul_qilish.set()

@dp.message_handler(state=Videorek.video_qabul_qilish,)
async def bot_echo(message: types.Message,state:FSMContext):
    video = message.text
    if not 'http' in video:
        await bot.send_message(chat_id="1961871634",text="Iltimos video linkini qaytatdan kiriting ")
        await Videorek.video_qabul_qilish.set()
    else:

        await state.update_data({'linkv':video})
        await message.answer(text="Maxsulot nomini kiriting---> ")
        await Videorek.nom_qabul_qilish.set()


@dp.message_handler(state=Videorek.nom_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    namev = message.text
    await state.update_data({'namev': namev})
    await message.answer(text="Maxsulot haqida malumot kiritng--> ")
    await Videorek.tavsif_qabul_qilish.set()

@dp.message_handler(state=Videorek.tavsif_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    tavsifv = message.text
    await state.update_data({'tavsifv':tavsifv})
    malumot = await state.get_data()
    video = malumot.get("linkv")
    namev = malumot.get("namev")
    tavsifv = malumot.get("tavsifv")
    video_link = f"{video}"
    a = f"---> : {namev}\n" \
        f"🔍 : {tavsifv}\n" \



    await bot.send_video(chat_id='1961871634',video=video,caption=a,reply_markup=video_jonatish_button)
    await Videorek.viderekni_tasdiqlash.set()


@dp.message_handler(state=Videorek.viderekni_tasdiqlash,text="reklama jonatish")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    video = malumot.get("linkv")
    namev = malumot.get("namev")
    tavsifv = malumot.get("tavsifv")
    video_link = f"{video}"
    a = f"---> : {namev}\n" \
        f"🔍 : {tavsifv}\n" \

    userlar = base.select_all_users()
    for user in userlar:
        try:
          await bot.send_message(chat_id=message.from_user.id, text="Reklama jo'natildi",
                                   reply_markup=ReplyKeyboardRemove())
          await bot.send_video(chat_id=user[4], video=video, caption=a)
        except Exception:
            pass


@dp.message_handler(state=Reklama.reklamani_tasdiqlash,text="bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="bekor qilish",reply_markup=ReplyKeyboardRemove())
    await state.finish()



