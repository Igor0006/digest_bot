from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU
import services
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

router = Router()


class FieldCallBackData(CallbackData, prefix='user_field'):
    x: int
    y: int


field: list[list[int]] = services.set_field()


def get_field(field: list[list[int]]) -> InlineKeyboardBuilder:
    game_field = InlineKeyboardBuilder()
    for x in range(len(field)):
        for y in range(len(field)):
            game_field.button(text=LEXICON_RU[field[x][y]], callback_data=FieldCallBackData(x=x, y=y))
    return game_field


@router.callback_query(FieldCallBackData.filter())
async def attack(callback: CallbackQuery, callback_data: FieldCallBackData):
    if field[callback_data.x][callback_data.y] == 1:
        field[callback_data.x][callback_data.y] = 3
    if field[callback_data.x][callback_data.y] == 0:
        field[callback_data.x][callback_data.y] = 2
    await callback.message.edit_text(text=")", reply_markup=get_field(field).as_markup())


@router.message(Command(commands='start'))
async def start(message: Message):
    await message.answer(text=LEXICON_RU['\start'],
                         reply_markup=get_field(field).as_markup())


@router.message(Command(commands='help'))
async def help(message: Message):
    await message.answer(text=LEXICON_RU['\help'])
