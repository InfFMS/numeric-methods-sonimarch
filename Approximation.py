import matplotlib.pyplot as plt


x = [i * 0.01 for i in range(-200, 200)]
y = [i ** 3 - i + 1 for i in x]
plt.plot(x, y)

plt.show()
def f(i):
    return i ** 3 - i + 1
a = -2
b = 0
c = (a + b) / 2
if f(c) * f(a) < 0: