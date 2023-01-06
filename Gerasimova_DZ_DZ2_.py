# 1
type_1 = 15 * 3
type_2 = 15 / 3
type_3 = 15 * 2
type_4 = 15 ** 2

print('15 * 3 =', type_1, type(type_1))
print('15 / 3 =', type_2, type(type_2))
print('15 * 2 =', type_3, type(type_3))
print('15 ** 2 =', type_4, type(type_4))

# 2

list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

lenght: int = len(list1)
store_id = id(list1)
for i in range(lenght):
    entity = list1.pop(0)
    if entity.isdigit():
        list1.append(F'"{int(entity):02d}"')
    elif entity[0] == "+" and entity[1].isdigit():
        list1.append(F'"+{int(entity):02d}"')
    else:
        list1.append(entity)
print(' '.join(list1))

# 4

hello = 'Привет, {}!'

wrong_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name in wrong_name:
    print(hello.format(name.split()[-1].title()))

# 5

price = [13.6, 24.18, 88, 45.03, 16, 49, 65.13, 24, 8, 50]

price_id = id(price)

end_word: str = ", "

for i, num in enumerate(price):

    new_price = str(f"{float(num):.2f}").split(".")

    if i == len(price) - 1:
        end_word = "\n"

    print(f"{new_price[0]} руб {new_price[1]} коп", end=end_word)


print(f"id перед сортировкой {price_id}")
price.sort()
print(price)
print(f"id после сортировки {id(price)}")

price2 = price.copy()
print(id(price2))
price2.sort(reverse=True)

print(price2)
print(id(price2))


print("5 самых дорогих товаров", price2[:5])
