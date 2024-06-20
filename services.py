import random
from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject
import logging

logger = logging.getLogger(__name__)


def set_field() -> list[[]]:
    lst = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, 8):
        for j in range(0, 8):
            lst[i][j] = random.randint(0, 1)
    return lst


def check_field(field: list[list[int]]) -> bool:
    cnt = 0
    for i in field:
        for j in i:
            cnt += j
    return cnt == 0


class TrueFilter(BaseFilter):
    async def __call__(self, event: TelegramObject):
        logger.debug("true filter in")
        return True


class FalseFilter(BaseFilter):
    async def __call__(self, event: TelegramObject):
        logger.debug("false filter in")
        return False