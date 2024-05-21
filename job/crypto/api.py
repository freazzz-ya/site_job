import aiohttp
import asyncio

from max_site.settings import API_SHARES, API_BINANCE


async def get_value_binance():
    """Получает данные апи первых 30 монет на бинансе"""
    async with aiohttp.ClientSession() as session:
        async with session.get(API_BINANCE) as response:
            data = await response.json()
    return data[:30 ]


async def get_shares():
    """Получает поля данные 30 крупнейших компаний мосбиржи
    поля: Краткое наименование ценной бумаги,
    Цена закрытия предыдущей торговой сессии,
    Средневзвешенная цена предыдущей торговой сессии,
    Полное наименование ценной бумаги, Размер лота,
    Статус ценной бумаги, Тип ценной бумаги."""
    async with aiohttp.ClientSession() as session:
        async with session.get(API_SHARES) as response:
            data = await response.json()
    current_prices = []
    for item in data['securities']['data']:
        current_prices.append(
            [item[2], item[3], item[15], item[9], item[4], item[6],],
        )
    return current_prices[:30]


async def main():
    return [await get_value_binance(), await get_shares()]


def return_api():
    return asyncio.run(main())
