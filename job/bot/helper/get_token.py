import requests
import uuid
import json
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='main_helper.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    encoding='utf-8'
)


def get_token(auth_token, scope='GIGACHAT_API_PERS'):
    """
      Выполняет POST-запрос к эндпоинту, который выдает токен.
      Параметры:
      - auth_token (str): токен авторизации, необходимый для запроса.
      - область (str): область действия запроса API. По умолчанию — «GIGACHAT_API_PERS».
      Возвращает:
      - ответ API, где токен и срок его "годности".
      """
    # Создадим идентификатор UUID (36 знаков)
    rq_uid = str(uuid.uuid4())
    # API URL
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    # Заголовки
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth_token}'
    }
    # Тело запроса
    payload = {
        'scope': scope
    }
    try:
        # Делаем POST запрос с отключенной SSL верификацией
        # (можно скачать сертификаты Минцифры, тогда отключать проверку не надо)
        logging.info('Делает пост запрос на получение токена')
        response = requests.post(url, headers=headers, data=payload, verify=False)
        logging.info('Успешный пост запрос на получение токена')
        return response
    except requests.RequestException as e:
        logging.error(
            f'{e} ошибка, не удалось выполнить пост запрос.'
            f'Токен не получен')
        return -1


def get_chat_completion(giga_token, user_message):
    """
    Отправляет POST-запрос к API чата для получения ответа от модели GigaChat.
    Параметры:
    - giga_token (str): Токен для авторизации в API.
    - user_message (str): Сообщение от пользователя, для которого нужно получить ответ.

    Возвращает:
    - str: Ответ от API в виде текстовой строки.
    """
    # URL API, к которому мы обращаемся
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    # Подготовка данных запроса в формате JSON
    payload = json.dumps({
        "model": "GigaChat",  # Используемая модель
        "messages": [
            {
                "role": "user",  # Роль отправителя (пользователь)
                "content": user_message  # Содержание сообщения
            }
        ],
        "temperature": 1,  # Температура генерации
        "top_p": 0.1,  # Параметр top_p для контроля разнообразия ответов
        "n": 1,  # Количество возвращаемых ответов
        "stream": False,  # Потоковая ли передача ответов
        "max_tokens": 400,  # Максимальное количество токенов в ответе
        "repetition_penalty": 1,  # Штраф за повторения
        "update_interval": 0  # Интервал обновления (для потоковой передачи)
    })

    # Заголовки запроса
    headers = {
        'Content-Type': 'application/json',  # Тип содержимого - JSON
        'Accept': 'application/json',  # Принимаем ответ в формате JSON
        'Authorization': f'Bearer {giga_token}'  # Токен авторизации
    }

    # Выполнение POST-запроса и возвращение ответа
    try:
        logging.info('Отправка запроса на сообщение')
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        logging.info('Успешная отправка запроса')
        return response
    except requests.RequestException as e:
        logging.error(f'Ошибка запроса {e}')
        # Обработка исключения в случае ошибки запроса
        return -1
