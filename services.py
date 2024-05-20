import random

dct: dict = {"\U0001F5FF": 1, "\U0001F4DC" : 2, "\U00002702" : 3}
rules: dict = {1 : 3, 3: 2, 2 : 1}


def bot_choose() -> str:
    return random.choice(["\U0001F5FF", "\U0001F4DC", "\U00002702"])


def get_winner(user_choice: str, bot_choice: str) -> str:
    bot_choice: int = dct[bot_choice]
    user_choice: int = dct[user_choice]
    if bot_choice == user_choice:
        return 'draw'
    if rules[bot_choice] == user_choice:
        return 'bot_won'
    return 'user_won'
