from aiogram import BaseMiddleware
from aiogram.types import Message


class OuterMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data):

        return await handler(event, data)



