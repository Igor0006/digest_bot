import asyncio

from aiogram import Bot, Dispatcher
from config import config
from handlers import handler


async def main() -> None:
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_router(handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
