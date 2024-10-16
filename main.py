import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from app.handler import router
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print(52)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit()')









