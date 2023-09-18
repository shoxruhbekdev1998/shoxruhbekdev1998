from aiogram import Bot
async def checking(user_id,kanal_link):
    user = Bot.get_current()
    azo = await user.get_chat_member(chat_id=kanal_link,user_id=user_id)
    return  azo.is_chat_member()
