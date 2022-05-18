import requests
import pprint
import time

TOKEN = '5350081937:AAGbkMsecOR0d7mKTTUa7y8SqQYXsR8i0T0'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# Информация о боте
url = f'{MAIN_URL}/getMe'

print(url)

# proxies = {
#     'http': 'http://167.86.96.4:3128',
#     'https': 'http://167.86.96.4:3128',
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

# result = requests.get(url, proxies=proxies, headers=headers)

# pprint.pprint(result.json())

# Как понять что нам написали сообщение
# Обновления
while True:
    time.sleep(5)
    url = f'{MAIN_URL}/getUpdates'

    result = requests.get(url,  headers=headers)

    pprint.pprint(result.json())

    messages = result.json()['result']

    for message in messages:
        # Как ответить на сообщение
        chat_id = message['message']['chat']['id']
        url = f'{MAIN_URL}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': 'Привет User!'
        }

        result = requests.post(url, headers=headers, params=params)