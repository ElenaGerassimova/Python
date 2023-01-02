print('1')


def add_to_n(n):
    for el in range(1, n+1, 2):
        yield el


num = add_to_n(15)
print(list(num))


print('3')

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def schedule(tutors, klasses):
    tutors_gen = (el for el in tutors)  # формирование генераторных списков
    klasses_gen = (el for el in klasses)
    for sch_gen in zip(klasses_gen, tutors_gen):  # "склеивание списков"
        yield sch_gen[::-1]
    for nomatch in tutors_gen:
        yield nomatch, None  # Для отсутствия соответствия


print(type(schedule(tutors, klasses)))  # класс
for i in schedule(tutors, klasses):    # вывод кортежей
    print(i)

print('4')
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


result = [elem for el, elem in zip(src, src[1:]) if elem > el]


print(result)


print('5')

src1 = [2, 5, 6, 4, 76, 7, 34, 3, 2, 90, 11, 2, 6, 4, 5, 3, 5]

res = {el: 0 for el in src1}

for el in src1:
    res[el] += 1

print([el for el in res if res[el] == 1])
