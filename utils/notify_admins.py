import logging

from data.config import ADMINS
from loader import bot

async def on_startup_notify():
    try:
        await bot.send_message(ADMINS, 'Bot Running!')
    except Exception as e:
        logging.error(e)
