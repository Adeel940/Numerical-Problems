
import numpy as np

def newton_forward(x, y, target, order=3):
    """
    Newton's Forward Interpolation
    """
    n = len(y)
    h = x[1] - x[0]
    u = (target - x[0]) / h


    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for i in range(1, n):
        for j in range(n - i):
            diff_table[j, i] = diff_table[j + 1, i - 1] - diff_table[j, i - 1]


    result = y[0]
    u_term = 1
    for i in range(1, order + 1):
        u_term *= (u - (i - 1)) / i
        result += u_term * diff_table[0, i]

    return result


def newton_backward(x, y, target, order=4):
    """
    Newton's Backward Interpolation
    """
    n = len(y)
    h = x[1] - x[0]
    u = (target - x[-1]) / h


    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            diff_table[j, i] = diff_table[j, i - 1] - diff_table[j - 1, i - 1]


    result = y[-1]
    u_term = 1
    for i in range(1, order + 1):
        u_term *= (u + (i - 1)) / i
        result += u_term * diff_table[n - 1, i]

    return result



x = np.array([1910, 1915, 1920, 1925, 1930, 1935, 1940, 1945, 1950, 1955])
y = np.array([1, 4, 10, 22, 41, 68, 105, 153, 215, 292])

predicted_1919_forward = newton_forward(x, y, 1919)
print(f"Predicted population in 1919 (Forward Interpolation): {predicted_1919_forward}")

predicted_1948_backward = newton_backward(x, y, 1948)
print(f"Predicted population in 1948 (Backward Interpolation): {predicted_1948_backward}")
