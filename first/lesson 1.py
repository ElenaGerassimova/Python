#age = int(input())
#print(age-2)

milk = False
cereal = False
egg = False

print('У тебя есть молоко')
reg = input()
if reg == 'да':
    milk = True

print('У тебя есть хлопья')
reg = input()
if reg == 'да':
    cereal = True

print('У тебя есть яйца')
reg = input()
if reg == 'да':
    egg = True
print(milk,cereal,egg)
