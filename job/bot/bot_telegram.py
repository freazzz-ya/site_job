import logging
import os
import sqlite3
from io import BytesIO
import datetime

import requests
import telebot
from dotenv import load_dotenv
from PIL import Image
from telebot import types

CURRENT_MONTH = datetime.datetime.now().month
CURRENT_YEAR = datetime.datetime.now().year

API_USERS = 'http://127.0.0.1:8000/api/v1/users'
API_NEURAL_NETWORKS = 'http://127.0.0.1:8000/api/v1/neuronet'
API_EARNING_CHEME = 'http://127.0.0.1:8000/api/v1/earning_scheme'
API_EXPENSES = 'http://127.0.0.1:8000/api/v1/epxenses'
API_OTHER_PAYMENT = 'http://127.0.0.1:8000/api/v1/other_payment'
API_JOB_PAYMENT = 'http://127.0.0.1:8000/api/v1/job_payment'
API_NETWORK_PAYMENT = 'http://127.0.0.1:8000/api/v1/network_payment'

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

CONSTANTS_FOR_START = 'Всем привет, это бот ' \
                      'помощник для сайта PIGGY BANK. '\
                      'Здесь вы можете осуществить часть '\
                      'Огромного потенциала нашего приложения'

CONSTANTS_FOR_HELP = f'\nЕсли вам необходима помощь, то вы можете '\
                      f'написать руководству id:{TELEGRAM_CHAT_ID}'

CONSTANTS_FOR_UNKNOWN_COMMAND = 'Я вас не понимаю, чтобы узнать '\
                                'весь список комманд, наберите: '

CONSTANTS_FOR_COMMANDS = '\n/start - для приветсвтия \n'\
                         '/help - для помощи во взаимодействии \n'\
                         '/site - для перехода на сайт \n'\
                         '/commands - список комманд \n'\
                         '/profile - профиль пользователя \n'\
                         '/neural_networks - все существуюшие' \
                         'на сайте нейросети \n'\
                         '/earning_cheme - схемы заработка'

CONSTANTS_FOR_SITE = 'Перейти на сайт'

CONSTANTS_FOR_NEURAL_NETWORK = 'Актуалбные новости о самых свежих нейросетях.'\
                            ' Данные представлены лишь о последних 5 ' \
                            'нейросетях, чтобы узнать подробнее,' \
                            ' вы можете с ними ознакомиться тут: ' \
                            'http://max1475.pythonanywhere.com/job/neuronet/' \

CONSTANTS_FOR_NEURAL_NETWORK = 'Здесь описываются актуальные схемы зарабаотка'\
                            '. Данные представлены лишь в 5 записях.'\
                            'Чтобы полностью ознакомиться вы можете '\
                            'посмотреть тут: '\
                            'http://max1475.pythonanywhere.com/job/scheme/'

URL = 'http://max1475.pythonanywhere.com/job/'

load_dotenv()

# Здесь задана глобальная конфигурация для логирования
logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    encoding='utf-8'
)

data_base = sqlite3.connect('data_base.db')
cur = data_base.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        username TEXT NOT NULL UNIQUE,
        first_name TEXT,
        last_name TEXT,
        image BLOB NOT NULL
        )
""")
logging.info('База данных создана при старте')
data_base.commit()
cur.close()
data_base.close()

# Создаем экземпляр бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)


def search_profit(id: int) -> dict:
    """Находит общий доход
       за все время"""
    respone_profit_job = requests.get(API_JOB_PAYMENT).json()
    respone_profit_network = requests.get(API_NETWORK_PAYMENT).json()
    respone_profit_other_source = requests.get(API_OTHER_PAYMENT).json()
    user_profit_job = sum(
        [profit['payment_in_money'] for profit in
         respone_profit_job if profit['worker'] == id])
    user_profit_network = sum(
        [profit['payment_in_money'] for profit in
         respone_profit_network if profit['worker'] == id])
    user_profit_other = sum(
        [profit['payment_in_money'] for profit in
         respone_profit_other_source if profit['worker'] == id])
    total_profit = user_profit_job + user_profit_network + user_profit_other
    context = {
                'total_profit': total_profit,
    }
    return context


def search_profit_month(id: int) -> list:
    """Находит общий доход
       за текущий месяц"""
    respone_job = requests.get(API_JOB_PAYMENT).json()
    respone_network = requests.get(API_NETWORK_PAYMENT).json()
    respone_other = requests.get(API_OTHER_PAYMENT).json()
    user_job_month = sum(
            [profit['payment_in_money'] for profit in
             respone_job if profit['worker'] == id
             and datetime.datetime.strptime(profit['date'],
             '%Y-%m-%dT%H:%M:%SZ').month == CURRENT_MONTH
             and datetime.datetime.strptime(profit['date'],
             '%Y-%m-%dT%H:%M:%SZ').year == CURRENT_YEAR])
    user_network_month = sum(
            [profit['payment_in_money'] for profit in
             respone_network if profit['worker'] == id
             and datetime.datetime.strptime(profit['date'],
             '%Y-%m-%dT%H:%M:%SZ').month == CURRENT_MONTH
             and datetime.datetime.strptime(profit['date'],
             '%Y-%m-%dT%H:%M:%SZ').year == CURRENT_YEAR])
    user_other_month = sum(
            [profit['payment_in_money'] for profit in
             respone_other if profit['worker'] == id
             and datetime.datetime.strptime(profit['date'],
             '%Y-%m-%dT%H:%M:%SZ').month == CURRENT_MONTH
             and datetime.datetime.strptime(profit['date'],
             '%Y-%m-%dT%H:%M:%SZ').year == CURRENT_YEAR])
    profit_month = user_job_month + user_network_month + user_other_month
    context = {
        'profit_month': profit_month,
    }
    return context


def about_user(message: dict) -> dict:
    """Данные профиля пользователя."""
    user = message.from_user
    return user


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обрабатывает кнопку старт."""
    logging.info('Обработка кнопки старт')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Профиль пользователя')
    markup.row(btn1)
    bt2 = types.KeyboardButton('Переход на сайт')
    bt3 = types.KeyboardButton('Нейросети')
    markup.row(bt2, bt3)
    bot.send_message(
        message.chat.id, CONSTANTS_FOR_START, reply_markup=markup
    )
    logging.info('Конец Обработки кнопки старт')


@bot.message_handler(commands=['site', 'website'])
def send_site(message):
    """Обрабатывает кнопку site."""
    logging.info('Обработка кнопки сайт')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        f'{CONSTANTS_FOR_SITE}', url=URL)
    )
    photo = open('media/piggy.png', 'rb')
    bot.send_photo(
        message.chat.id, photo,
        caption='Сайт про финансы - PIGGY BANK', reply_markup=markup,
    )
    logging.info('Конец бработки кнопки сайт')


@bot.message_handler(commands=['profile'])
def send_profile(message):
    """Обрабатывает кнопку profile"""
    logging.info('Начало обработки кнопки профиль')
    user = about_user(message)
    try:
        response = requests.get(API_USERS).json()
        user_site = [
            user1 for user1 in response if user1['telegram_id'] == user.id
        ][0]
        try:
            image_response = requests.get(user_site['image'])
            image = Image.open(BytesIO(image_response.content))
            # Отправка изображения
            photo = BytesIO()
            image.save(photo, 'PNG')
            photo.seek(0)
            logging.info('Фото сайта открывается')
        except (FileNotFoundError, OSError) as error:
            photo = open('media/nouname.jpg', 'rb')
            logging.error(f'Открылось запасное фото. Ошибка {error}')
        logging.info('Совпадение с профилем сайта')
        with sqlite3.connect('data_base.db') as data_base:
            logging.info('Загрузка из базы данных сайта')
            cur = data_base.cursor()
            # Check if user exists
            cur.execute("SELECT 1 FROM users WHERE user_id = ?", (user.id,))
            exists = cur.fetchone()
            if not exists:
                cur.execute(
                    "INSERT INTO users (user_id, username, "
                    "first_name, last_name, image) VALUES (?, ?, ?, ?, ?)",
                    (user.id, user_site['username'], user_site['first_name'],
                     user_site['last_name'], photo.read()))
                data_base.commit()  # Commit the transaction
                logging.info('Пользователь добавлен в базу с сайта')
                cur.close()
            else:
                # Update if user exists
                cur.execute(
                    "UPDATE users SET username = ?, first_name = ?, last_name = ?, image = ? WHERE user_id = ?",
                    (user_site['username'], user_site['first_name'],
                     user_site['last_name'], photo.read(), user.id))
                data_base.commit()  # Commit the transaction
                logging.info('Пользователь обновлен данными с сайта')
                cur.close()
        respone_expenses = requests.get(API_EXPENSES).json()
        user_expenses = sum(
            [expense['price'] for expense in
             respone_expenses if expense['author'] == user_site['id']])
        user_expenses_month = sum(
            [expense['price'] for expense in
             respone_expenses if expense['author'] == user_site['id']
             and datetime.datetime.strptime(expense['date'],
             '%Y-%m-%dT%H:%M:%SZ').month == CURRENT_MONTH
             and datetime.datetime.strptime(expense['date'],
             '%Y-%m-%dT%H:%M:%SZ').year == CURRENT_YEAR])
        user_profit = search_profit(user_site['id'])
        user_profit_month = search_profit_month(user_site['id'])
        cur = data_base.cursor()
        cur.execute(
            "SELECT * FROM users WHERE user_id = ?", (user.id,)
        )
        user_db = cur.fetchone()
        bot.send_photo(
            message.chat.id,
            photo=image,
            caption=f'<b>Добро пожаловать {user_db[2]} 🤫</b>\n'
                    f'<em>id: {user_db[1]}</em>\n'
                    f'<em>Имя: {user_db[3]}</em>\n'
                    f'<em>Фамилия: {user_db[4]}</em>\n'
                    f'<em>Сумма общих расходов: {user_expenses} рублей</em>\n'
                    f'<em>Сумма расходов за текущий месяц:'
                    f' {user_expenses_month} рублей</em>\n'
                    f'<em>Сумма доходов за все время: '
                    f'{user_profit["total_profit"]} рублей</em>\n'
                    f'<em>Сумма доходов за текущий месяц: '
                    f'{user_profit_month["profit_month"]} рублей</em>',

            parse_mode='html'
        )
        cur.close()
        photo.close()
    except IndexError:
        logging.info('Не совпадение с профилем сайта')
        try:
            photo = open('media/nouname.jpg', 'rb')
            logging.info('Фото основное открывается')
        except FileNotFoundError:
            photo = open('media/piggy.png', 'rb')
            logging.error('Открылось запасное фото')
        with sqlite3.connect('data_base.db') as data_base:
            cur = data_base.cursor()
            # Check if user exists
            cur.execute("SELECT 1 FROM users WHERE user_id = ?", (user.id,))
            exists = cur.fetchone()
            if not exists:
                # Insert if user doesn't exist
                cur.execute(
                    "INSERT INTO users (user_id, username, "
                    "first_name, last_name, image) VALUES (?, ?, ?, ?, ?)",
                    (user.id, user.username, user.first_name,
                     user.last_name, photo.read()))
                data_base.commit()  # Commit the transaction
                logging.info('Новый пользователь добавлен в базу')
                cur.close()
    # Send photo
        bot.send_photo(
            message.chat.id,
            open('media/nouname.jpg', 'rb'),
            caption=f'<b>Добро пожаловать {user.username} 🤫</b>\n'
                    f'<em>id: {user.id}</em>\n'
                    f'<em>Имя: {user.first_name}</em>\n'
                    f'<em>Фамилия: {user.last_name}</em> \n'
                    f'<em>Чтобы увидеть профиль, который на сайте,</em> \n'
                    f'<em>Регистрируйтест тут: {URL}</em> \n'
                    f'И обязаетльно укажите свой teltgram id в профиле \n'
                    f'в таком формате - 6823805231 \n',
            parse_mode='html'
        )
        logging.info('Конец обработки кнопки профиль')
        # Close the file
        photo.close()


@bot.message_handler(commands=['help'])
def send_help(message):
    """Обрабатывает кнопку help"""
    logging.info('Начало обработки кнопки хелп')
    bot.send_message(message.chat.id,
                     f'<b>help</b> <em>{CONSTANTS_FOR_HELP}</em>',
                     parse_mode='html')
    logging.info('Конец обработки кнопки хелп')


@bot.message_handler(commands=['commands'])
def send_command(message):
    """Обрабатывает кнопку commands."""
    logging.info('Начало обработки кнопки командс')
    bot.send_message(message.chat.id,
                     f'<b>commands</b> <em>{CONSTANTS_FOR_COMMANDS}</em>',
                     parse_mode='html')
    logging.info('Конец обработки кнопки командс')


@bot.message_handler(commands=['neural_networks'])
def send_neural_networks(message):
    """Обрабатывает кнопку neural networks."""
    logging.info('Обработка кнопки neural networks')
    response = requests.get(API_NEURAL_NETWORKS).json()[:5]
    if response:
        for network in response:
            message_text = f"*Название:* {network['title']}\n"
            message_text += f"*Описание:* {network['description']}\n"
            message_text += f"*Ссылка:* {network['url']}\n"
            # Форматирование даты создания
            create_date = datetime.datetime.strptime(
                network['date_joined'], '%Y-%m-%dT%H:%M:%S.%fZ'
            )
            message_text += f"*Дата создания:*" \
                            f"{create_date.strftime('%Y-%m-%d')}"
            try:
                # Загрузка изображения
                image_response = requests.get(network['image'])
                image = Image.open(BytesIO(image_response.content))
                # Отправка изображения
                bio = BytesIO()
                image.save(bio, 'PNG')
                bio.seek(0)
                bot.send_photo(
                    chat_id=message.chat.id,
                    photo=bio, caption=message_text,
                    parse_mode="Markdown")
                logging.info('Отправка данных о нейросети')
            except Exception as e:
                logging.error(f"Ошибка при отправке фото: {e}")
                bot.send_message(
                    chat_id=message.chat.id,
                    text=message_text,
                    parse_mode="Markdown")
        bot.send_message(
            message.chat.id,
            f'<b>NEURAL NETWORKS</b> <em>{CONSTANTS_FOR_NEURAL_NETWORK}</em>',
            parse_mode='html')
    else:
        message_text = f"{CONSTANTS_FOR_NEURAL_NETWORK} Извините, " \
                       f"в данный момент нет доступных нейросетей."
        bot.send_message(chat_id=message.chat.id, text=message_text)
        logging.critical('Отсутсвтие данных в запросе')
    logging.info('Конец Обработки кнопки neural networks')


@bot.message_handler(commands=['earning_cheme'])
def send_earning_cheme(message):
    """Обрабатывает кнопку earning cheme."""
    logging.info('Обработка кнопки neural earning_cheme')
    response = requests.get(API_EARNING_CHEME).json()[:5]
    if response:
        for network in response:
            message_text = f"Автор: {network['worker']}\n"
            message_text = f"Название: {network['title']}\n"
            message_text += f"Описание: {network['discription']}\n"
            message_text += f"Нейросеть: {network['network']}\n"
            message_text += f"Источник заработка:{network['other_source']}\n"
            message_text += f"Ссылка: {network['url']}\n"
            # Форматирование даты создания
            create_date = datetime.datetime.strptime(
                network['date_joined'], '%Y-%m-%dT%H:%M:%S.%fZ'
            )
            message_text += f"Дата создания:" \
                            f"{create_date.strftime('%Y-%m-%d')}"
            try:
                # Загрузка изображения
                image_response = requests.get(network['image'])
                image = Image.open(BytesIO(image_response.content))
                # Отправка изображения
                bio = BytesIO()
                # Сохраняем изображение в формате PNG
                image.save(bio, 'PNG')
                bio.seek(0)
                bot.send_photo(
                    chat_id=message.chat.id,
                    photo=bio, caption=message_text,
                    parse_mode="Markdown")
                logging.info('Отправка данных о другом источнике')
            except Exception as e:
                logging.error(f"Ошибка при отправке фото: {e}")
                bot.send_message(
                    chat_id=message.chat.id,
                    text=message_text,
                    parse_mode="Markdown")
        bot.send_message(
            message.chat.id,
            f'<b>EARNING CHEME</b> <em>{CONSTANTS_FOR_NEURAL_NETWORK}</em>',
            parse_mode='html')
    else:
        message_text = f"{CONSTANTS_FOR_NEURAL_NETWORK} Извините, " \
                        f"в данный момент нет доступных нейросетей."
        bot.send_message(chat_id=message.chat.id, text=message_text)
        logging.critical('Отсутсвтие данных в запросе')
    logging.info('Конец Обработки кнопки earning_cheme')


# обрабатывает фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    pass


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
    if message.text == 'Профиль пользователя':
        send_profile(message)
    elif message.text == 'Переход на сайт':
        send_site(message)
    elif message.text == 'Нейросети':
        send_neural_networks(message)
    else:
        bot.reply_to(
            message,
            f'<em>{CONSTANTS_FOR_UNKNOWN_COMMAND}</em> <b>/commands</b>',
            parse_mode='html'
        )
        logging.info('Отправка неизвестного сообщения')


# Запускаем бота
bot.polling()
