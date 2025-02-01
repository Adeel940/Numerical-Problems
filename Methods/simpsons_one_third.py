
import numpy as np

def simpsons_one_third(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])
    return result

f = lambda x: 1 / (2 * x**2 + 1)
a = 0
b = 6
n = 6

integral_value = simpsons_one_third(f, a, b, n)
print(integral_value)
