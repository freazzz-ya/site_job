import requests
from max_site.settings import API_BINANCE, API_SHARES


def get_value_binance():
    """Получает данные апи первых 30 монет на бинансе"""
    response = requests.get(API_BINANCE)
    data = response.json()[:30]
    return data


def get_shares():
    """Получает поля данные 30 крупнейших компаний мосбиржи
    поля: Краткое наименование ценной бумаги,
    Цена закрытия предыдущей торговой сессии,
    Средневзвешенная цена предыдущей торговой сессии,
    Полное наименование ценной бумаги, Размер лота,
    Статус ценной бумаги, Тип ценной бумаги."""
    response = requests.get(API_SHARES)
    data = response.json()
    current_prices = []
    for item in data['securities']['data']:
        current_prices.append(
            [item[2], item[3], item[15], item[9], item[4], item[6],]
        )
    return current_prices[:30]
