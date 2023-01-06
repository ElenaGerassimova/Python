import datetime
import json
import requests
print('Задание 2')


url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
dict = json.loads(response.text)
print('USD', dict['Valute']['USD']['Value'])
print('EUR', dict['Valute']['EUR']['Value'])



print('Задание 4')

import utils

current_list = ['EUR', 'USD']
print('val')

for val in range(0, len(current_list)):
    print('Курс ', '"' + current_list[val] + '"', ' равен: ', utils.currency_rates(current_list[val]))
