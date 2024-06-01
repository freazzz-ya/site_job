import asyncio

import aiohttp
import aiohttp_socks
from max_site.settings import API_BINANCE, API_SHARES

proxy_url = '51.145.176.250'
proxy_port = '8080'
proxies = f"http://{proxy_url}:{proxy_port}"


async def get_data(url):
    connector = aiohttp_socks.ProxyConnector.from_url(
        proxies, rdns=True, limit=1000
    )
    async with aiohttp.ClientSession(
        connector=connector, timeout=aiohttp.ClientTimeout(total=100)
    ) as session:
        async with session.get(url) as response:
            data = await response.json()
    return data


async def get_value_binance():
    data = await get_data(API_BINANCE)
    return data[:30]


async def get_shares():
    data = await get_data(API_SHARES)
    current_prices = []
    for item in data['securities']['data']:
        current_prices.append(
            [item[2], item[3], item[15], item[9], item[4], item[6]]
        )
    return current_prices[:30]


async def main():
    return await asyncio.gather(get_value_binance(), get_shares())


def return_api():
    return asyncio.run(main())
