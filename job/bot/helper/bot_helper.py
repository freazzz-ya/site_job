import os
import logging
from dotenv import load_dotenv
from .get_token import get_token, get_chat_completion

load_dotenv()
CLIENT_SECRET_GIGA = os.getenv('CLIENT_SECRET_GIGA', '')
AUTHORIZATION_GIGA = os.getenv('AUTHORIZATION_GIGA', '')
CLIENT_ID_GIGA = os.getenv('CLIENT_ID_GIGA', '')


def main_helper(message, parametres=None):
    response = get_token(AUTHORIZATION_GIGA)
    if response != -1:
        giga_token = response.json()['access_token']
    answer = get_chat_completion(giga_token, f'{message}')
    answer.json()
    return answer.json()['choices'][0]['message']['content']


if __name__ == '__main__':
    message = 'Расскажи стихотворение'
    print(main_helper(message))
