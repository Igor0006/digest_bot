from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from typing import Any, Awaitable, Callable, Dict
import logging
from aiogram.types.update import Update
from typing import Any, Awaitable, Callable, Dict
from sqlalchemy.ext.asyncio import async_sessionmaker


class DataBaseSession(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            data['session'] = session
            return await handler(event, data)


logger = logging.getLogger(__name__)


class TranslatorMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        user: User = data.get('event_from_user')
        if user is None:
            return await handler(event, data)
        user_lang = user.language_code
        translations = data.get('_translations')
        i18n = translations.get(user_lang)
        if i18n is None:
            data['i18n'] = translations[translations['default']]
        else:
            data['i18n'] = i18n
        return await handler(event, data)


class OuterMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        logger.debug("In outer middleware")
        result = await handler(event, data)
        bot = data.get("_bot")
        update: Update = data.get('event_update')
        await bot.send_message(747110128, update.channel_post.text)
        logger.debug("Out inner middleware")
        return result
