import telebot
from teleg import pas
from main import HTMLparser
TOKEN = pas()
#
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")

# Обработка команд
@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, 'Будет произведен поиск статей на сайте https://pythondigest.ru')
    bot.send_message(message.chat.id, 'Введите текст запроса:')


@bot.message_handler(content_types=['text'])
def serch(message):
    print(message.text.lower())
    serc = HTMLparser(message.text.lower())
    for h in serc:
        bot.send_message(chat_id=message.from_user.id, text=h)

bot.polling()