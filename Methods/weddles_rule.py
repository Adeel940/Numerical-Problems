
import numpy as np

def weddles_rule(f, a, b, n=6):
    if n != 6:
        raise ValueError("Weddle's Rule requires n = 6 intervals (7 points).")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    coefficients = [1, 5, 1, 6, 1, 5, 1]  # Weddle's specific weights
    result = (3 * h / 10) * np.dot(coefficients, y)
    return result

f = lambda x: np.exp(x)* np.sin(2*x)
a = 0.2
b = 0.5

integral_value = weddles_rule(f, a, b)
print(integral_value)

