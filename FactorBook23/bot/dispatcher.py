from os import getenv

from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from utils.conf import Config as conf

TOKEN = conf.bot.BOT_TOKEN
redis = Redis()
dp = Dispatcher(storage=RedisStorage(redis))