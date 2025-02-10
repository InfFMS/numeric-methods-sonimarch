import math


def k(f, a, b):
    while abs(f(a) - f(b)) > 0.02:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
            continue
        elif f(b) * f(c) < 0:
            a = c
            continue
        else:
            return round(c, 2)
    else:
        return round((a + b) / 2, 2)


def f1(i):
    return i ** 3 - i + 1

print('1) x^3 - x + 1')
a = 0
b = -2
print(k(f1, a, b))



def f2(i):
    return i ** 3 - i + 1

print('2) x^3 - x^2 - 9x + 9')
a = -2
b = -4
print(k(f2, a, b))
a = 0
b = 2
print(k(f2, a, b))
a = 2
b = 4
print(k(f2, a, b))


def f3(i):
    return i ** 2 - math.e ** i

print('3) x^2 - e^x')
a = 2
b = -2
print(k(f3, a, b))
