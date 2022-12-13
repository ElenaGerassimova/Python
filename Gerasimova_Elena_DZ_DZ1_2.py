summ = 0
dvd = 0
summ2 = 0
cube = [a ** 3 for a in range(1001) if a % 2 != 0] #вычисляем последовательность кубов
print(cube)
for dvd in range(len(cube)): #для новой последовательности ищем числа, делящиеся на 7
    if cube[dvd] % 7 ==0:
        summ = summ + cube[dvd] # вычисляем сумму
print(summ,'- сумма кубов, кратных 7')
cube_plus_17 = [(a ** 3 + 17) for a in range(1001) if a % 2 != 0] #новая последовательность на основе предыдущей
print(cube_plus_17)
for dvd in range(len(cube_plus_17)): #ищем числа, делящиеся на 7
    if cube_plus_17[dvd] % 7 ==0:
        summ2 = summ2 + cube_plus_17[dvd] # вычисляем сумму
print(summ2,'- сумма кубов, увеличенных на 17, кратных 7')