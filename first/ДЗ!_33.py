a= int(input())
prn1 = 'процент'
prn2 = 'процентов'
prn3 = 'процента'

while a <100:
    a=a+1
if 5 <= a <= 20:
    prn = prn2
elif a % 10 == 1:
    prn = prn1
    a=a+1
elif 2 >= a % 10 <=4:
    prn = prn3
    a=a+1
else:
    prn=prn2
    print(a,prn)
a = a+1