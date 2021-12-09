from aiogram import types
from app import bot, dp
from messages import start_message
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply(text=start_message, reply_markup=ReplyKeyboardRemove())
