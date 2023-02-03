print('Задание 3')


import re

class correct_list(Exception):
    def __init__(self, txt):
        self.txt = txt


list = []
print('Формирование списка: введите число или stop для вывода результата')
while True:
    num = input('Введите число: ')
    if num == 'stop':
        print(list)
        break
    try:
        if re.compile(r'[^0-9, .]').search(num):
            raise correct_list('Данный символ не является числом')
    except correct_list as n:
        print(n)
    else:
        num = float(num)
        list.append(num)