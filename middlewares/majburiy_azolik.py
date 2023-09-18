from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from data.config import kanallar
from data.tekshirish import checking
from loader import bot

class Asosiy_cheking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "Quyidagi kanallarga a'zo bo'ling-->"
        royhat =[]
        dastlabki_holati = True
        for k in kanallar:
            holat = await checking(user_id=user_id,kanal_link=k)
            dastlabki_holati *= holat

            kanal = await bot.get_chat(k)
            if not holat:
                link = await kanal.export_invite_link()
                button = [InlineKeyboardButton(text=f"Obuna bo'lish",url=f'{link}')]
                royhat.append(button)
        royhat.append([InlineKeyboardButton(text="Tasdiqlash",callback_data='www')])
        if not dastlabki_holati:
            await bot.send_message(chat_id=user_id,text=matn,disable_web_page_preview=True,
                                   reply_markup=InlineKeyboardMarkup(inline_keyboard=royhat))
            raise CancelHandler()