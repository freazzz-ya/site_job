import os

import telebot
from dotenv import load_dotenv

CONSTANTS_FOR_START = 'Всем привет, это бот ' \
                      'помощник для сайта PIGGY BANK. '\
                      'Здесь вы можете осуществить часть '\
                      'Огромного потенциала нашего приложения'

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

# Создаем экземпляр бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, CONSTANTS_FOR_START)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
""")


# обрабатывает документы и аудио
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


# Обрабатывает все текстовые сообщения
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
    pass


# Это означает, что он обрабатывает только документы с текстовым содержимым.
@bot.message_handler(
    func=lambda message: message.document.mime_type == 'text/plain',
    content_types=['document'])
def handle_text_doc(message):
    pass


# Handle all other messages with content_type
# 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


# Запускаем бота
bot.polling()
