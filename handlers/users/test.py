from aiogram import types
from aiogram.dispatcher import FSMContext



#tillar
from aiogram.types import ReplyKeyboardMarkup
from keyboards.default.menu_uchun_uz import menu_buttun
from keyboards.default.menu_uchun_ru import abcd_buttonr
from keyboards.default.menu_uchun_uz import abcd_button
from states.holatlar import Test
from loader import dp,base,bot





menular = base.select_all_menu_uz()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_echo(message: types.Message,state:FSMContext):
    typee =message.text
    qator = base.select_test_savollar(tur=typee)[0]
    print(qator)

    qator_savol = qator[1]
    savol_id = qator[0]
    qator_tur=qator[6]
    qator_variant1 = qator[2]
    qator_variant2 = qator[3]
    qator_variant3 = qator[4]
    qator_variant4 = qator[5]
    user_id = message.from_user.id
    await state.update_data({"Savol": savol_id})
    await state.update_data({"tur":qator_tur})

    menu_buttun = ReplyKeyboardMarkup( resize_keyboard=True)

    await message.answer(f"Assalomu alaykum. {message.from_user.full_name}! Sizga berilayotgan test topshiriqlari kassalliklarni aniqlashning boshlang'ich yo'li hisoblanadi. Bu testlarni yechish orqali siz o'zingizda kuzatilashi mumkin bo'lgan kasalliklarni oldindan aniqlab erta davollashga erishishingiz mumkin. \n Testlarni yechish davomida o'z holatingizga mos bo'lgan test javoblarini  belgilang \n Eslatma: Bu testlar boshlang'ich holatni aniqlovchi testlar bo'lib test natijalaridan vaximaga tushmang. ",reply_markup=menu_buttun)
    await bot.send_message(chat_id=user_id, text=f" Savol :  {qator_savol} \n"
                                                 f" A : {qator_variant1}\n"
                                                 f" B : {qator_variant2}\n"
                                                 f" C : {qator_variant3}\n"
                                                 f" D : {qator_variant4}\n",reply_markup=abcd_button)
    await  Test.savol_qabul_qilish.set()
   # await  Test.tur_qabul_qilish.set()

@dp.message_handler(state=Test.savol_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    javob =message.text
    if not javob in ['a','b','c','d','A','B','D',"C","а","б","с","д","А","Б","С","Д"]:
        await message.answer(text="Bunday jabob mavjud emas. Iltimos javoblarni quyidagi hariflardan birini belgilsh orqali kiriting (A,B,C,D,a,b,c,d)")
        await Test.savol_qabul_qilish.set()
    else:
        if javob == 'a' or javob == 'A' or javob == 'а' or javob == 'А':
            javob = 5
        elif javob == 'b' or javob == 'B' or javob == 'б' or javob == 'Б':
            javob = 10
        elif javob == 'c' or javob == 'C' or javob == 'с' or javob == 'С':
            javob = 15
        elif javob == 'd' or javob == 'D' or javob == 'д' or javob == 'Д':
            javob = 20
        else:
            await message.answer(
                text="Bunday jabob mavjud emas. Iltimos javoblarni quyidagi hariflardan birini belgilsh orqali kiriting (A,B,C,D,a,b,c,d)")
            await Test.savol_qabul_qilish.set()
        malumot = await state.get_data()
        qator_tur = malumot.get("tur")
        uzunlik = len(base.select_test_savollar(tur=qator_tur))
        max_id =base.select_test_savollar(tur=qator_tur)[-1][0]
        print(uzunlik,max_id)
        savol_id = int(malumot.get('Savol'))
        if savol_id == max_id:
            savol_id = int(malumot.get('Savol'))

        else:

            savol_id = int(malumot.get('Savol')) + 1

        print(savol_id,'**************************')
        base.natija_qoshish(savol_id=savol_id, savol='s', javob=javob, tg_id=message.from_user.id, tur=qator_tur,
                            status=True)

        if max_id <= savol_id :
                ism = message.from_user.first_name
                fam = message.from_user.last_name
                username = message.from_user.username
                user_id = message.from_user.id
                await message.answer(text="Test yakunlandi")
                javoblar = base.select_javob(tg_id=message.from_user.id,tur=qator_tur,status=True)
                print(javoblar,'++++++++++++++++')
                yigindi = 0
                for i in javoblar:
                    yigindi= yigindi +int(i[0])
                    base.update_test_savollar(tg_id=message.from_user.id,tur=qator_tur,status=True)
                await message.answer(text=f"Sizning ballingiz {yigindi}")
                if 45 < yigindi <= 90:

                    await bot.send_message(chat_id="@ww3324", text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")
                    await bot.send_message(chat_id=message.from_user.id,
                                           text="Sizning holatingiz o'rta darajada.\n"" Maslahat:Yuqoridagi test natijasiga ko'ra sizdan O'zingiz joylashgan hududdagi QVP da tibbiy  Ko'rikdan o'tishinngizni so'raymiz.\n""Eslatma: O'z sog'lig'ingiz o'z qo'lingizda.\n Kasallikni davolagandan ko'ra oldini olgan maqul. \n Muammolar bo'limiga ayni vaqtda sizni qiynayotgan muammolaringizni ya'ni o'zingizdagi o'zgarishlarni jo'natishingiz mumkin. Muammolaringiz shifokorlarimiz tomonidan ko'rib chiqiladi va sizga aloqaga chiqiladi")
                    # await bot.send_photo(chat_id=message.from_user.id,photo="https://t.me/meningkanalim1898/14",caption=" Farg'ona Uralogiya markazi\n"
                    #                                                                                                   "Manzil: Shakarqishloq MFY")

                elif 90 < yigindi <= 135:
                    await bot.send_message(chat_id="@ww3324", text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")
                    await bot.send_message(chat_id=message.from_user.id,text="Sizning holatingiz qoniqarli.\n"" Maslahat:Yuqoridagi test natijasiga ko'ra sizdan Quyidagi keltirilgan shifoxonalarga tashrif buyurishingiz so'raladi. \n""Eslatma: O'z sog'lig'ingiz o'z qo'lingizda.\n Kasallikni davolagandan ko'ra oldini olgan maqul.\n Muammolar bo'limiga ayni vaqtda sizni qiynayotgan muammolaringizni ya'ni o'zingizdagi o'zgarishlarni jo'natishingiz mumkin. Muammolaringiz shifokorlarimiz tomonidan ko'rib chiqiladi va sizga aloqaga chiqiladi")
                    await bot.send_photo(chat_id=message.from_user.id, photo="https://t.me/meningkanalim1898/21",
                                         caption=" Respublika Ixtisoslashtirilgan Urologiya Ilmiy Amaliy Tibbiyot Markazi Farg'ona Filiali \n")
                    await bot.send_location(chat_id=message.from_user.id, longitude=71.81342607963862,
                                            latitude=40.360527378049284)
                    #await bot.send_location()

                elif 135 < yigindi <= 180:
                    await bot.send_message(chat_id="@ww3324", text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")
                    await bot.send_message(chat_id=message.from_user.id,
                                           text="Sizning holatingiz qoniqarsiz darajada. \n""Maslahat: Yuqoridagi test natijasiga ko'ra sizdan Quyidagi keltirilgan shifoxonalarga tashrif buyurishingiz so'raladi. \n""Eslatma: O'z sog'lig'ingiz o'z qo'lingizda.\n Kasallikni davolagandan ko'ra oldini olgan maqul.\n Muammolar bo'limiga ayni vaqtda sizni qiynayotgan muammolaringizni ya'ni o'zingizdagi o'zgarishlarni jo'natishingiz mumkin. Muammolaringiz shifokorlarimiz tomonidan ko'rib chiqiladi va sizga aloqaga chiqiladi")
                    await bot.send_photo(chat_id=message.from_user.id, photo="https://t.me/meningkanalim1898/21",
                                         caption=" Respublika Ixtisoslashtirilgan Urologiya Ilmiy Amaliy Tibbiyot Markazi Farg'ona Filiali\n")
                    await bot.send_location(chat_id=message.from_user.id, longitude=71.81342607963862,
                                            latitude=40.360527378049284)
                    # await bot.send_location()

                    await Test.tasdiqlash.set()
                else:
                    await bot.send_message(chat_id="@ww3324", text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")
                    await bot.send_message(chat_id=message.from_user.id,
                                           text="Sizning holatingiz yaxshi.\n"" Maslahat:Yuqoridagi test natijasiga ko'ra sizdan  Har 3 oyda tibbiy ko'rikdan o'tishingizni so'rab qolamiz.\n"" Eslatma: O'z sog'lig'ingiz o'z qo'lingizda.\n Kasallikni davolagandan ko'ra oldini olgan maqul.\n Muammolar bo'limiga ayni vaqtda sizni qiynayotgan muammolaringizni ya'ni o'zingizdagi o'zgarishlarni jo'natishingiz mumkin. Muammolaringiz shifokorlarimiz tomonidan ko'rib chiqiladi va sizga aloqaga chiqiladi")

                await state.finish()




        else:

                qator = base.select_test_savollar(id=savol_id)[0]

                qator_savol = qator[1]
                savol_id = qator[0]

                qator_variant1 = qator[2]
                qator_variant2 = qator[3]
                qator_variant3 = qator[4]
                qator_variant4 = qator[5]
                user_id = message.from_user.id
                await state.update_data({"Savol": savol_id})


                menu_buttun = ReplyKeyboardMarkup( resize_keyboard=True)

                await message.answer(f"{message.from_user.full_name}! Testlarni yechish davomida o'z holatingizga mos bo'lgan test javoblarini  belgilang , ",reply_markup=menu_buttun)
                await bot.send_message(chat_id=user_id, text=f" Savol :  {qator_savol} \n"
                                                             f" A : {qator_variant1}\n"
                                                             f" B : {qator_variant2}\n"
                                                             f" C : {qator_variant3}\n"
                                                             f" D : {qator_variant4}\n",reply_markup=abcd_button)
                await  Test.savol_qabul_qilish.set()















#ru

menular = base.select_all_menu_ru()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message,state:FSMContext):
    typee =message.text
    qator_ru = base.select_test_savollarru(turru=typee)[0]

    qator_savol = qator_ru[1]
    savol_id = qator_ru[0]
    qator_tur = qator_ru[6]
    qator_variant1 = qator_ru[2]
    qator_variant2 = qator_ru[3]
    qator_variant3 = qator_ru[4]
    qator_variant4 = qator_ru[5]
    user_id = message.from_user.id
    await state.update_data({"Savol": savol_id})
    await state.update_data({"turru": qator_tur})

    menu_buttun_ru = ReplyKeyboardMarkup(resize_keyboard=True)

    await message.answer(f"Привет. {message.from_user.full_name}!  Анализы, которые вам дают, являются первым способом выявления заболеваний. Решая эти тесты, вы можете обнаружить признаки заболевания, которые не являются диагнозом. При решении тестов отмечайте ответы тестов, подходящие под вашей ситуации.\n  ",reply_markup=menu_buttun_ru)
    await bot.send_message(chat_id=user_id, text=f" Вопрос :  {qator_savol} \n"
                                                 f" A : {qator_variant1}\n"
                                                 f" Б : {qator_variant2}\n"
                                                 f" C : {qator_variant3}\n"
                                                 f" Д : {qator_variant4}\n",reply_markup=abcd_buttonr)
    await  Test.savol_qabul_qilish_ru.set()
@dp.message_handler(state=Test.savol_qabul_qilish_ru)
async def bot_echo(message: types.Message,state:FSMContext):
    javob =message.text
    if not javob in ['a','b','c','d','A','B','D',"C","а","б","с","д","А","Б","С","Д"]:
        await message.answer(text="Такого ответа нет. Пожалуйста, введите ответы, отметив одну из следующих букв (A,B,C,D,a,b,c,d)")
        await Test.savol_qabul_qilish_ru.set()
    else:
        if javob =='a' or javob=='A' or javob=='а' or javob=='А':
            javob=5
        elif javob=='b' or javob=='B' or javob=='б' or javob=='Б':
            javob=10
        elif javob== 'c' or javob=='C'or javob== 'с' or javob=='С':
            javob = 15
        elif javob == 'd' or javob == 'D' or javob =='д' or javob=='Д':
            javob = 20
        else:
            await message.answer(
                text="Такого ответа нет. Пожалуйста, введите ответы, отметив одну из следующих букв (A,B,C,D,a,b,c,d)")
            await Test.savol_qabul_qilish_ru.set()
        malumot_ru = await state.get_data()
        qator_tur_ru = malumot_ru.get("turru")
        uzunlik = len(base.select_test_savollarru(turru=qator_tur_ru))
        max_id = base.select_test_savollarru(turru=qator_tur_ru)[-1][0]
        print(uzunlik, max_id)
        savol_id = int(malumot_ru.get('Savol'))
        if savol_id == max_id:
            savol_id = int(malumot_ru.get('Savol'))

        else:

            savol_id = int(malumot_ru.get('Savol')) + 1

        print(savol_id, '**************************')
        base.natija_qoshishru(savol_id=savol_id, savol='s', javob=javob, tg_id=message.from_user.id, turru=qator_tur_ru,
                            status=True)

        if max_id <= savol_id:
            ism = message.from_user.first_name
            fam = message.from_user.last_name
            username = message.from_user.username
            user_id = message.from_user.id
            await message.answer(text="Тест завершен")
            javoblar = base.select_javobru(tg_id=message.from_user.id,turru=qator_tur_ru,status=True)
            print(javoblar,'++++++++++++++++')
            yigindi = 0
            for i in javoblar:
                yigindi= yigindi +int(i[0])
                base.update_test_savollarru(tg_id=message.from_user.id,turru=qator_tur_ru,status=True)
            await message.answer(text=f"Общий результат {yigindi}")
            if 45 < yigindi <= 90:

                await bot.send_message(chat_id="@ww3324",text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")

                await bot.send_message(chat_id=message.from_user.id,
                                       text="Ваше состояние средней степени тяжести.\n"" Совет: На основании приведенных выше результатов анализов просим вас пройти медицинское обследование в СВП в вашем районе.\n""Примечание: Ваше здоровье в ваших руках.\n Профилактика лучше лечения \n В разделе Проблемы вы можете отправлять ваши вопросы и симптомы для своевременной профилактике")
                # await bot.send_photo(chat_id=message.from_user.id,photo="https://t.me/meningkanalim1898/14",caption=" Farg'ona Uralogiya markazi\n"
                #                                                                                                   "Manzil: Shakarqishloq MFY")

            elif 90 <= yigindi < 135:
                await bot.send_message(chat_id="@ww3324",
                                       text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")

                await bot.send_message(chat_id=message.from_user.id,
                                       text="Ваше состояние удовлетворительное.\n"" Совет: На основании приведенных выше результатов теста вам будет предложено посетить вышеуказанные мероприятия. \n""Примечание: Ваше здоровье в ваших руках.\n Профилактика лучше лечения \n В разделе Проблемы вы можете отправлять ваши вопросы и симптомы для своевременной профилактике")
                await bot.send_photo(chat_id=message.from_user.id, photo="https://t.me/meningkanalim1898/21",
                                     caption=" Ферганский филиал Республиканского центра специализированной урологии научно-исследовательской медицины\n")
                await bot.send_location(chat_id=message.from_user.id, longitude=71.81342607963862,
                                        latitude=40.360527378049284)
                #await bot.send_location()


            elif 135 <= yigindi <= 180:
                await bot.send_message(chat_id="@ww3324",
                                       text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")

                await bot.send_message(chat_id=message.from_user.id,
                                       text="Ваше состояние неудовлетворительное. \n""Совет: На основании приведенных выше результатов теста вам будет предложено посетить вышеуказанные медицинские заведение. \n""Примечание: Ваше здоровье в ваших руках.\n Профилактика лучше лечения \n В разделе Проблемы вы можете отправлять ваши вопросы и симптомы для своевременной профилактике")
                await bot.send_photo(chat_id=message.from_user.id, photo="https://t.me/meningkanalim1898/21",
                                     caption=" Ферганский филиал Республиканского центра специализированной урологии научно-исследовательской медицины\n")
                await bot.send_location(chat_id=message.from_user.id, longitude=71.81342607963862,
                                        latitude=40.360527378049284)
                # await bot.send_location()

                await Test.tasdiqlash_ru.set()
            else:
                await bot.send_message(chat_id="@ww3324",
                                       text=f"Test ishlandi.\n Foydalanuvchi_nomi={ism}.\n Foydalanuvchi_familyasi={fam}.\n Foydalanuvchi_username={username}.\n Foydalanuvchi_id={user_id}.\n Foydalanuvchi_bali={yigindi}")

                await bot.send_message(chat_id=message.from_user.id,
                                       text="Ваше состояние хорошее.\n"" Совет: На основании вышеприведенных результатов анализов просим Вас проходить диспансеризацию каждые 3 месяца.\n"" Примечание: Ваше здоровье в ваших руках.\n Профилактика лучше лечения\n В разделе Проблемы вы можете отправлять ваши вопросы и симптомы для своевременной профилактике ")

            await state.finish()




        else:

            qator_ru = base.select_test_savollarru(id=savol_id)[0]

            qator_savol = qator_ru[1]
            savol_id = qator_ru[0]
            qator_variant1 = qator_ru[2]
            qator_variant2 = qator_ru[3]
            qator_variant3 = qator_ru[4]
            qator_variant4 = qator_ru[5]
            user_id = message.from_user.id
            await state.update_data({"Savol": savol_id})

            menu_buttun_ru = ReplyKeyboardMarkup( resize_keyboard=True)

            await message.answer(f" {message.from_user.full_name}! При решении тестов отмечайте ответы тестов, подходящие под ваше состояние. ",reply_markup=menu_buttun)
            await bot.send_message(chat_id=user_id, text=f" Вопрос :  {qator_savol} \n"
                                                         f" A : {qator_variant1}\n"
                                                         f" Б  : {qator_variant2}\n"
                                                         f" C : {qator_variant3}\n"
                                                         f" Д  : {qator_variant4}\n",reply_markup=abcd_buttonr)
            await  Test.savol_qabul_qilish_ru.set()







