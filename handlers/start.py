from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!\n"
                                      f"Я могу помочь тебе проверить правописание слов,"
                                      f"если ты вдруг сомневаешься в своих силах.\n"
                                      f"Для того, чтобы начать, просто отправь мне слово и я проверю,"
                                      f"правильно ли оно написано")