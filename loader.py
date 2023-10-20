from aiogram import Bot, Dispatcher
import redis
from aiogram.fsm.storage.redis import RedisStorage

import config

storage = RedisStorage(redis)
bot = Bot(token=config.token, parse_mode='json')
dp = Dispatcher(bot, storage=storage)