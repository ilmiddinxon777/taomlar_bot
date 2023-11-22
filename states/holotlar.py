from aiogram.dispatcher.filters.state import State,StatesGroup

class Adminga_murojat(StatesGroup):
    ism_qabul_qilish = State()
    fam_qabul_qilish = State()
    yosh_qabul_qilish = State()
    tel_qabul_qilish = State()
    manzil_qabul_qilish = State()
    murojat_qabul_qilish = State()
    tasdiqlash_qabul_qilish = State()


class Adminga_murojatlar(StatesGroup):
    isme_qabul = State()
    fame_qabul = State()
    yoshe_qabul = State()
    tele_qabul = State()
    manzile_qabul = State()
    murojate_qabul = State()
    tasdiqelashe_qabul = State()


class Adminga_murojatlarru(StatesGroup):
    ismr_qabul = State()
    famr_qabul = State()
    yoshr_qabul = State()
    telr_qabul = State()
    manzilr_qabul = State()
    murojatr_qabul = State()
    tasdiqelashr_qabul = State()