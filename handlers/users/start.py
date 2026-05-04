from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from loader import db

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}")
    try:
        db.add_user(
            id = message.from_user.id,
            name = message.from_user.full_name,
            username = message.from_user.username,
        )
    except Exception as e:
        print(e)





