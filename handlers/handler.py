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
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from datetime import datetime, timedelta

logger = logging.getLogger()
router = Router()
user_id = 747110128
btn_send = KeyboardButton(text='Получить сообщения за последнюю неделю')
kp = ReplyKeyboardBuilder()
kp.add(btn_send)

@router.message(Command(commands='start'))
async def start(message: Message):
    global user_id
    logger.debug("in handler")
    await message.answer(text=LEXICON_RU['\start'], reply_markup=kp.as_markup())
    user_id = message.from_user.id

@router.message(F.text == btn_send.text)
async def send_messages(message: Message, session: AsyncSession):
    query = select(Post).where((Post.publication_date - timedelta(days=7) <= message.date))
    results = await session.execute(query)
    # result = (await session.execute(query)).scalar()
    for product in results.scalars().all():
        print("AAAAAAA", product.text)
        link = product.link
        await message.bot.send_message(user_id, text='[message{}]({})'.format(message.message_id, link),
                                parse_mode=ParseMode.MARKDOWN_V2)


@router.channel_post()
async def when_post(post: Message, session: AsyncSession):
    link: str = "https://t.me/" + str(post.chat.username) + '/' + str(post.message_id)
    session.add(Post(message_id=post.message_id, link=link, text=post.text, publication_date=post.date))
    await session.commit()
    print(post.date)
    # await post.answer(text='да что ты говришь' + " " + str(post.message_id))
    # await bot.send_message(user_id, post.text)
