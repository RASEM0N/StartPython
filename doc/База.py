from functools import reduce

# region Ключевые слова

# import
# global, nonlocal

# Async, Await, yield
# class, def, return, lambda (() => {})

# try, finally, except,
# raise (throw), assert (throw если False)
# with, as -

# False, True, None
# del

# if, elif, else, and, or, not, in, is
# for, while, break, continue

# pass
# endregion

# region Типы данных
isEnd: bool = False
count: int = 10
money: float = 1_000_000
complexNumber: complex = 1 + 2j

text: str = f'''
IsEnd {isEnd}
count {count}
money {money}
complexNumber {complex}
'''

text = str(money)
count = int(money)
money = float(count)

# <class 'str'>
print(type(text))
# endregion

# region Арифметические операции
count /= 10
count *= 10
count += 10
count -= 10
count **= 2

# 11
count = round(10.5)
# endregion

# region Условные выражения
isTrue = 1 == 1
isFalse = 1 != 1

if isTrue and not isFalse:
    pass

if 'hello' in 'hello message':
    pass

if 'say hello' not in 'hello message':
    pass

# endregion

# region Циклы
count: int = 10

while count != 0:
    count -= 1

    if count > 100:
        break
else:
    print(f'Цикл завершился. Count: {count}')

for n in [1, 2, 3, 4, 5]:
    print(f'n: {n}')


# endregion

# region Функции

def sum_numbers(a: float = 0, b: float = 0, c: float = 0) -> float:
    return a + b + c


def sum_numbers_w(*, a=0, b=0, c=0) -> float:
    return a + b + c


def sum_array(*numbers: float) -> float:
    return reduce(lambda a, b: a + b, numbers)


def closures(a):
    def foo(b):
        nonlocal a
        a += b
        print(a)
        return foo

    return foo


print(sum_numbers(1, 2, 3))
print(sum_numbers_w(a=1, b=2, c=3))
print(sum_array(1, 2, 3, 4, 5, 6, 7, 8, 9))

closures(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)


# endregion

# region Декораторы

def log(input_f):
    def output_f(*args):
        print('start')
        input_f(*args)
        print('end')

    return output_f


@log
def hello(): print('hello')
# endregion
