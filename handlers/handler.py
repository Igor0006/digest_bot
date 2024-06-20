from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Post
from lexicon.lexicon import LEXICON_RU
import services
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

logger = logging.getLogger()
router = Router()
user_id = 747110128


@router.message(Command(commands='start'))
async def start(message: Message):
    global user_id
    logger.debug("in handler")
    await message.answer(text=LEXICON_RU['\start'])
    user_id = message.from_user.id


@router.channel_post()
async def when_post(post: Message, session: AsyncSession):
    link: str = "https://t.me/" + str(post.chat.username) + '/' + str(post.message_id)
    session.add(Post(message_id=post.message_id, link=link, description=post.text, publication_date=post.date))
    await session.commit()
    print(post.date)
    query = select(Post).where(Post.message_id == post.message_id)
    result = (await session.execute(query)).scalar()
    print("!", result.description, result.data)
    #for product in result.scalars().all():
    #    print("AAAAAAA", product.data)

    await post.bot.send_message(user_id, text='[message]({})'.format(link),
                                parse_mode=ParseMode.MARKDOWN_V2)
    # await post.answer(text='да что ты говришь' + " " + str(post.message_id))
    # await bot.send_message(user_id, post.text)
