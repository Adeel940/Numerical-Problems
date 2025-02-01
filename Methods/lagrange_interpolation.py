
def lagrange_interpolation(x_values, y_values, x_target):
    """
    Perform Lagrange interpolation to estimate the value of f(x) at a given x_target.

    Args:
        x_values (list): List of x values.
        y_values (list): Corresponding list of f(x) values.
        x_target (float): The x value at which to estimate f(x).

    Returns:
        float: Interpolated value of f(x) at x_target.
    """
    n = len(x_values)
    result = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_target - x_values[j]) / (x_values[i] - x_values[j])

        result += y_values[i] * L_i

    return result


# Given data
x_values = [5, 10, 15, 25, 35, 45]
y_values = [3.4, 4.8, 6.2, 8.1, 9.0, 9.5]
x_target = 20


interpolated_value = lagrange_interpolation(x_values, y_values, x_target)


print(f"Estimated value of f(x) at x = {x_target}: {interpolated_value}")
