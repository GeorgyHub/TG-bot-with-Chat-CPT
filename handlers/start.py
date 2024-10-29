from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard

async def start_get(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'👋 Привет, это бот создание макетов с помощью нейросетей 💻',
                           reply_markup=register_keyboard)
