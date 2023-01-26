print('Задание 3')
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper_logger(arg):
        print(f'{calc_kube.__name__}({arg}: {type(arg)})')
        return func(arg)
    return wrapper_logger


@type_logger
def calc_kube(answer):
    return answer ** 3


a = calc_kube(5)
print(a)


print('Задание 4')
from functools import wraps


def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)
        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(9)
print(a)


