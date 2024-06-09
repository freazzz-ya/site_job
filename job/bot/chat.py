import telebot
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Загрузите токен для своей модели Hugging Face
TOKEN = "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"

# Инициализируйте токенизатор и модель
tokenizer = AutoTokenizer.from_pretrained("MODEL_NAME", token=TOKEN)
model = AutoModelForSeq2SeqLM.from_pretrained("MODEL_NAME", token=TOKEN)

# Инициализируйте бота Telegram
bot = telebot.TeleBot("641371098")

# Определите обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получите текст входящего сообщения
    input_text = message.text

    # Токенизируйте и сгенерируйте ответ с помощью нейросети
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=128)
    output_text = tokenizer.batch_decode(output, skip_special_tokens=True)

    # Отправьте ответ пользователю
    bot.send_message(message.chat.id, output_text[0])

# Запустите бота
bot.polling()