from aiogram.types import Message


def funny_dialogue(message: Message):
    return message.text.count(")") != 0;