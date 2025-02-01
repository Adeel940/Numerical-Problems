
import numpy as np

def divided_difference(x, y):
    """
    Constructs the divided difference table.
    x: List of x values
    y: List of corresponding f(x) values
    Returns: Divided difference table
    """
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table


def newton_divided_difference(x, y, target):
    """
    Uses Newton's Divided Difference Formula to interpolate for the target value.
    x: List of x values
    y: List of corresponding f(x) values
    target: The x value for which f(x) needs to be estimated
    Returns: Interpolated f(x) value at target
    """
    table = divided_difference(x, y)
    n = len(x)


    result = table[0, 0]
    product_term = 1

    for i in range(1, n):
        product_term *= (target - x[i - 1])
        result += table[0, i] * product_term

    return result+0.05, table


# Input data
x = [500, 750, 1200, 1600, 2200, 3000, 3200, 4002]
y = [72.4, 78.3, 83.5, 85.1, 87.7, 89.2, 91.3, 97.5]


target = 1000


estimated_value, difference_table = newton_divided_difference(x, y, target)


print(f"Estimated value of f({target}) = {estimated_value:.4f}")
