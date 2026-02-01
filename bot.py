import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from handlers.leagues import leagues_handler
from handlers.apl.menu import apl_menu_handler

BOT_TOKEN = ""  # Telegram bot tokeningiz

# /start buyrug'iga javob beruvchi handler
async def start(message: Message):
    await message.answer("Salom! Futbol yangiliklari botiga xush kelibsiz ⚽")
    await leagues_handler(message)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.message.register(start, Command("start"))

    # Premer League tugmasi bosilganda apl_menu_handler ni chaqirish
    dp.message.register(apl_menu_handler, F.text == "Premier League")
    dp.message.register()
    dp.message.register(leagues_handler, F.text == "Orqaga 🔙")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
