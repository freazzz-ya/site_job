import requests
proxies = {
    'http': 'http://223.135.156.183:8080'
}
url = 'https://httpbin.org/get'
response = requests.get(url, proxies=proxies)

print("Параметры запроса по умолчанию:")
print("URL:", response.url)
print("Метод запроса:", response.request.method)
print("User-Agent:", response.request.headers['User-Agent'])
print(response.json)