import asyncio
import logging
import middlewares
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import config
from handlers import handler
from lexicon.lexicon import LEXICON_RU, LEXICON_EN
from database.engine import create_db, drop_db, session_maker


# Настраиваем базовую конфигурацию логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

translations = {
    'default': 'ru',
    'en': LEXICON_EN,
    'ru': LEXICON_RU,
}


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command='/start', description='для быстрого начала')]
    await bot.set_my_commands(main_menu_commands)


async def main() -> None:
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_router(handler.router)
    await create_db()

    handler.router.channel_post.middleware(middlewares.DataBaseSession(session_pool=session_maker))
    ##dp.update.outer_middleware(middlewares.TranslatorMiddleware())
    #await bot.delete_webhook(drop_pending_updates=True)
    #dp.startup.register(set_main_menu)
    #await bot.send_message(-1002205261693, "bugur")
    await dp.start_polling(bot, _bot=bot, _translations=translations)



if __name__ == '__main__':
    asyncio.run(main())
