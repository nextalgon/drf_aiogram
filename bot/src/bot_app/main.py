from aiogram import executor
from app import dp
import logging
import commands
import random_ten

logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
