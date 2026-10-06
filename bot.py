import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Profilim"),
            KeyboardButton(text="🔎 Tanishuvni boshlash")
        ],
        [
            KeyboardButton(text="💬 Suhbatlarim"),
            KeyboardButton(text="⚙️ Sozlamalar")
        ],
        [
            KeyboardButton(text="🚨 Shikoyat")
        ]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "💗 AnonChat'ga xush kelibsiz!\n\n"
        "Anonim suhbat va yangi tanishuvlarni boshlang 👇",
        reply_markup=main_menu
    )

@dp.message(lambda message: message.text == "👤 Profilim")
async def profile(message: types.Message):
    await message.answer("👤 Profilim bo‘limi tez orada ishga tushadi.")

@dp.message(lambda message: message.text == "🔎 Tanishuvni boshlash")
async def dating(message: types.Message):
    await message.answer("🔎 Tanishuv qidirilmoqda...")

@dp.message(lambda message: message.text == "💬 Suhbatlarim")
async def chats(message: types.Message):
    await message.answer("💬 Hozircha suhbatlaringiz yo‘q.")

@dp.message(lambda message: message.text == "⚙️ Sozlamalar")
async def settings(message: types.Message):
    await message.answer("⚙️ Sozlamalar bo‘limi tez orada ishga tushadi.")

@dp.message(lambda message: message.text == "🚨 Shikoyat")
async def report(message: types.Message):
    await message.answer("🚨 Shikoyat yuborish bo‘limi tez orada ishga tushadi.")

async def main():
    print("✅ AnonChat ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main)
