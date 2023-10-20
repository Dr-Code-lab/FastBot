from fastapi import FastAPI
import uvicorn
import logging
import aiogram

import loader
from telegram.middlewares.middlemodule import OuterMiddleware
from telegram.filters.filter import MyFilter
from telegram.handlers.admin import register_admin
from telegram.handlers.echo import register_echo
from telegram.handlers.user import register_user


logger = logging.getLogger(__name__)
app = FastAPI()


def register_middlewares(dp, config):
    dp.setup_middleware(OuterMiddleware)


def register_filters(dp):
    dp.filters_factory.bind(MyFilter)


def register_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_echo(dp)


@app.get('/')
async def main():
    logger.info("Bot now starting...")
    bot['config'] = config
    register_middleware(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)
    start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

    return "some json"

if __name__ == '__main__':
    try:
        uvicorn.run("bot:app", reload=True)
    except (KeyboardInterrupt, SystemExit):
        logger.error("Done!")


#%%
