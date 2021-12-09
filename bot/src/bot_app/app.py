from aiogram import Bot, Dispatcher
from local_settings import token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


