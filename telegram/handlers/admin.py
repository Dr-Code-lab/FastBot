from aiogram import Dispatcher
from aiogram.types import Message


async def message_to_admin(message: Message):
    await message.reply(message)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(message_to_admin, commands=["start"], state="*", is_admin=True)
