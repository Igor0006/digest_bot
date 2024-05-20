from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import services

router = Router()
btn_start = KeyboardButton(text='Давай')
btn_pass = KeyboardButton(text='Впадлу \U0001F6AC')
btn_rock = KeyboardButton(text="\U0001F5FF")
btn_paper = KeyboardButton(text="\U0001F4DC")
btn_scissors = KeyboardButton(text="\U00002702")
btn_exit = KeyboardButton(text="\U0001f6d1")
kp_start_menu = ReplyKeyboardBuilder()
kp_start_menu.add(btn_start, btn_pass)
kp_game = ReplyKeyboardBuilder()
kp_game.add(btn_rock, btn_scissors, btn_paper, btn_exit)
kp_game.adjust(3, 1)


@router.message(F.text == btn_start.text)
async def btn_1_answer(message: Message):
    await message.answer(text=LEXICON_RU['player_choose'], reply_markup=kp_game.as_markup())


@router.message(F.text == btn_pass.text)
async def btn_2_answer(message: Message):
    await message.answer(text="....")


@router.message(F.text.in_([btn_rock.text, btn_paper.text, btn_scissors.text]))
async def bot_response(message: Message):
    bot_choice: str = services.bot_choose()
    await message.answer(text=bot_choice + " vs " + message.text + '\n' + LEXICON_RU[services.get_winner(message.text, bot_choice)]
                                                                                              + '\n Сыграем еще?',
                         reply_markup=kp_start_menu.as_markup())
@router.message(Command(commands='start'))
async def start(message: Message):
    await message.answer(text=LEXICON_RU['\start'],
                         reply_markup=kp_start_menu.as_markup())


@router.message(Command(commands='help'))
async def help(message: Message):
    await message.answer(text=LEXICON_RU['\help'])
