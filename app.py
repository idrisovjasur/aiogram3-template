import asyncio
import logging
import sys

from loader import dp, bot
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify

from handlers.users.start import start_router

async def main() -> None:
    dp.include_router(start_router)
    await set_default_commands()
    await on_startup_notify()
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    asyncio.run(main())








