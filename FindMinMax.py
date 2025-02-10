import math


def f(n1, n2, a, b, c, d):
    s = []
    g = []
    for i in range(3141, -1, -1):
        sb1 = round(math.sin(i * 0.001) * n2 / n1, 3)
        x = b * math.tan(i) + a
        sb2 = round(abs(c - x) / ((c - x) ** 2 + d ** 2), 3)
        if sb1 == sb2:
            s.append(math.asin(sb2) * 180 / 3.1415)
            g.append(n1 * (b ** 2 + x ** 2) ** 0.5 + n2 * (d ** 2 + (c - x) ** 2) ** 0.5)

    return s[g.index(min(g))]

