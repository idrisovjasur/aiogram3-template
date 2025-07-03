from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.enums import ParseMode
from data import config

bot = Bot(token = config.BOT_TOKEN, default = DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage = storage, fsm = FSMStrategy.CHAT, events_isolation = None)