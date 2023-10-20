from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext


async def bot_echo_message(message: types.Message):
    """
    :param message: it is a result for user
    :return:
    """
    text = [
        """Курс доллара к рублю сегодня один к одному"""
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo_message, state="*", content_types=types.ContentTypes.ANY)
