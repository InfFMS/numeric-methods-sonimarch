import math


def l(f):
    s = 0
    for i in range(0, 314):
        d = ((f(i * 0.01 + 0.01) - f(i * 0.01)) ** 2 + 0.00001) ** 0.5
        s += abs(d)
    return s

def f1(x):
    return math.cos(x) + 0.1 * x ** 2
def f2(x):
    return -1 * math.tanh(x - math.pi / 2)
def f3(x):
    return -0.2 * (x - math.pi) ** 3 + 0.5 * (x - math.pi) ** 2 + 1

print('1) cos(x) + 0.1x^2')
print(l(f1))
print('2) -tanh(x - pi/2)')
print(l(f2))
print('3) -0.2(x - pi)^3 + 0.5(x - pi)^2 + 1')
print(l(f3))