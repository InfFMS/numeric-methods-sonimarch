import math
import matplotlib.pyplot as plt


def s(f1, f2, a, b):
    su = 0
    for i in range(a * 10, b * 10 + 10):
        d = (f1(i * 0.1) - f2(i * 0.1)) * 0.1
        su += d
    return su

def f1(x):
    return math.e ** (-1 * x ** 2) + 1
def f2(x):
    return -0.3 * x ** 3 + 0.5

def f3(x):
    return math.e ** (-1 * x ** 2) + 0.5
def f4(x):
    return 0.2 * math.sin(3 * x) - 0.5

def f5(x):
    return math.e ** (-1 * (x - 1) ** 2) + math.e ** (-1 * (x + 1) ** 2) + 0.5
def f6(x):
    return -0.3 * x ** 2

# x = [i * 0.01 for i in range(0, 100)]
# y = [f1(i) for i in x]
# fig, ax = plt.subplots()
# plt.plot(x, y)
# x1 = [i * 0.01 for i in range(0, 100)]
# y1 = [f2(i) for i in x1]
# plt.plot(x1, y1)
#
# plt.show()

print('1)', s(f1, f2, -2, 2))
print('2)', s(f3, f4, -2, 2))
print('3)', s(f5, f6, -2, 2))