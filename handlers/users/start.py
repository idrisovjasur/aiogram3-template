from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}")




