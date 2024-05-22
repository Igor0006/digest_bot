import random


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
