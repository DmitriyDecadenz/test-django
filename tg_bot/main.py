import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from handlers import router


async def main() -> None:
    """Program entry point"""
    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')