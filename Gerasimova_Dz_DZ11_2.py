print('Задание 2')


class le_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input('Введите число - делимое: ')
num_2 = input('Введите число - делитель: ')
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise le_Error('Деление на 0!')
except le_Error as err:
    print(err)
else:
    res = num_1 / num_2
    print(f'Результат деления - {res}')
