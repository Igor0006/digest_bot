from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    token: str


env: Env = Env()
env.read_env()
config = Config(token=env("BOT_TOKEN"))
