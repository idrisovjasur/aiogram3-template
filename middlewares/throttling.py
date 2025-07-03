import time
from aiogram import BaseMiddleware
from aiogram.types import Message, Update
from typing import Callable, Dict, Any

class ManualThrottlingMiddleware(BaseMiddleware):
    def __init__(self, delay_seconds: float = 2.0):
        self.delay = delay_seconds
        self.user_last_time: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable,
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message):
            user_id = event.from_user.id
            now = time.time()

            last_time = self.user_last_time.get(user_id, 0)
            delta = now - last_time

            if delta < self.delay:
                await event.answer("Iltimos, sekinroq yozing 🕒")
                return

            self.user_last_time[user_id] = now

        return await handler(event, data)
