from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config
from autocorrect import Speller
import enchant


storage = StateMemoryStorage()
speller = enchant.Dict('ru_RU')
# speller = Speller('ru')
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)