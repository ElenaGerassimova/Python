print('Задача 1')

num_translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
    }
print('Введите число по-английски:')
item = num_translate.get(input())
print(item)

print('Задача 3')


def thesaurus(*names):  # Задаем функцию
    lst = {}
    for name in names:  # Определяем ключ как первый символ слова
        key = name[0].capitalize()
        if key not in lst:
            lst[key] = []
        lst[key].append(name)
    return lst


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


print('Задача 5')

from random import choice  # задаем случайный выбор для списков

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbes = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    for i in range(n):  # Присваиваем переменным случайные значения из списков
        r_nouns = choice(nouns)
        r_adverbes = choice(adverbes)
        r_adjectives = choice(adjectives)
        joke = f'{r_nouns} {r_adverbes} {r_adjectives}'
        print(joke)
        if flag:  # Исключаем повтояющиеся слова
            res_1 = joke.split()
            for noun in nouns:
                for jk in res_1:
                    if noun == jk:
                        nouns.remove(noun)

            for adverb in adverbes:
                for jk in res_1:
                    if adverb == jk:
                        adverbes.remove(adverb)

            for adjective in adjectives:
                for jk in res_1:
                    if adjective == jk:
                        adjectives.remove(adjective)


get_jokes(n=5, flag=True)  # задаем условия вывода аргументов функции
