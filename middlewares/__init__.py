from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .majburiy_azolik import Asosiy_cheking

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
   # dp.middleware.setup(Asosiy_cheking())
