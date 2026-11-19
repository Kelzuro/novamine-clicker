import json
from aiogram import Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

WEB_APP_URL = "https://ваш-ник.github.io/novamine-clicker/"
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⚡ Играть в NovaMine", web_app=WebAppInfo(url=WEB_APP_URL))]],
        resize_keyboard=True
    )
    await message.answer("Запускай кликер кнопкой ниже:", reply_markup=kb)

@dp.message(F.web_app_data)
async def handle_stats(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(
        f"🏆 <b>Рекорд игрока {message.from_user.first_name}</b>\n\n"
        f"Лига: {data['league']}\n"
        f"🪙 Баланс: <b>{data['balance']}</b>\n"
        f"⚙️ Доход: <b>+{data['passivePerSec']}/сек</b>\n"
        f"👆 Кликов: {data['totalTaps']}",
        parse_mode="HTML"
    )