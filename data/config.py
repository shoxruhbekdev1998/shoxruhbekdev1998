from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

import  os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = os.environ.get("ADMINS")
IP = os.environ.get("ip")

kanallar = ['@TG_SHIFOKOR']