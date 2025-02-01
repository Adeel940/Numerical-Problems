

import numpy as np

def bessel_interpolation(x, y, target):
    """
    Bessel's Interpolation Formula for a given target value.
    """
    n = len(x)
    h = x[1] - x[0]
    mid = n // 2 - 1
    u = (target - x[mid]) / h


    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for i in range(1, n):
        for j in range(n - i):
            diff_table[j, i] = diff_table[j + 1, i - 1] - diff_table[j, i - 1]


    result = (diff_table[mid, 0] + diff_table[mid + 1, 0]) / 2
    result += (u - 0.5) * diff_table[mid, 1]
    result += ((u - 0.5) * (u + 0.5) / 2) * diff_table[mid, 2]
    result += ((u - 0.5) * (u + 0.5) * (u - 1) / 6) * (
        diff_table[mid - 1, 3] + diff_table[mid, 3]
    ) / 2
    result += ((u - 0.5) * (u + 0.5) * (u - 1) * (u + 1) / 24) * diff_table[mid - 1, 4]

    return result


# Input data
x = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])
y = np.array([20.1, 18.7, 17.4, 16.1, 15.0, 14.1, 13.4, 12.8, 12.3])


predicted_temperature = bessel_interpolation(x, y, 275)
print(f"Predicted temperature at 275 meters: {predicted_temperature:.3f} °C")

