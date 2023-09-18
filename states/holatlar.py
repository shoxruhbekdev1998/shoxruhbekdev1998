from aiogram.dispatcher.filters.state import State,StatesGroup

class Test(StatesGroup):
    savol_qabul_qilish = State()
    tur_qabul_qilish = State()
    tasdiqlash = State()
    savol_qabul_qilish_ru = State()
    tur_qabul_qilish_ru = State()
    tasdiqlash_ru=State()

class Reklama(StatesGroup):
     rasm_qabul_qilish = State()
     nom_qabul_qilish = State()
     tavsif_qabul_qilish = State()
     reklamani_tasdiqlash = State()


class Videorek(StatesGroup):
    video_qabul_qilish = State()
    nom_qabul_qilish = State()
    tavsif_qabul_qilish = State()
    viderekni_tasdiqlash = State()

class Shikoyat(StatesGroup):
    ism_qabul_qilish = State()
    fam_qabul_qilish = State()
    yosh_qabul_qilish = State()
    tel_qabul_qilish =State()
    shikoyat_qabul_qilish = State()
    shikoyatni_tasdiqlash = State()

class Shikoyatru(StatesGroup):
    ism_qabul_qilishru = State()
    fam_qabul_qilishru = State()
    yosh_qabul_qilishru = State()
    tel_qabul_qilishru =State()
    shikoyat_qabul_qilishru = State()
    shikoyatni_tasdiqlashru = State()

