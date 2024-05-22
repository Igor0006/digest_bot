import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import config
from handlers import handler


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command='/start', description='для быстрого начала')]
    await bot.set_my_commands(main_menu_commands)


async def main() -> None:
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_router(handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
