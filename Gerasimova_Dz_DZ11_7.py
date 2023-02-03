print('Задание 7')


class Complex_Number:
    def __init__(self, real, im):
        self.real = real
        self.im = im
        if self.real == 0:
            print(f'Комплексное число {self.im} * i')
        elif self.im == 0:
            print(f'Вещественное число {self.real}')
        else:
            print(f'Комплексное число {self.real} + {self.im} * i')

    def __add__(self, other):
        a = self.real + other.real
        b = self.im + other.im
        return Complex_Number(a, b)

    def __mul__(self, other):
        a = (self.real * other.real) - (self.im * other.im)
        b = (self.real * other. im) + (self.im * other.real)
        return Complex_Number(a, b)

i_1 = Complex_Number(1, 12)
i_2 = Complex_Number(2, 14)
i_3 = i_1 + i_2

