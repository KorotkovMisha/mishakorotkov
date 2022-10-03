from telebot.types import Message
from loader import bot, speller


@bot.message_handler(state=None)
def bot_echo(message: Message):
    text_list = message.text.lower().split()
    text = ''
    for word in text_list:
        if not speller.check(word):
            correct_word = '\n'.join([cor_word.capitalize() for cor_word in speller.suggest(word)])
            text += f'Слово {word} написано не правильно.\n' \
                    f'Возможно ты имел ввиду одно из этих слов:\n{correct_word}\n' \
        # if speller.autocorrect_word(word) != word:
        #     cor_word = speller.autocorrect_word(word)
        #     text += f'Слово {word} написано не правильно.\n' \
        #             f'Возможно ты имел ввиду: {cor_word}\n' \

    if len(text) > 0:
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, 'Ты написал все правильно! Продолжай в том же духе!')
