import os

import telebot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

# Создаем экземпляр бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Отправляем эхо-ответ пользователю
    bot.send_message(message.chat.id, message.text)

# Запускаем бота
bot.polling()
