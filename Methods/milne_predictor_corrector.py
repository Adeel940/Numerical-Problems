
def milne_predictor_corrector(x_values, y_values, f, target_x, h):
    # Milne Predictor formula
    y_predicted = y_values[-4] + (4 * h / 3) * (
        2 * f(x_values[-3], y_values[-3]) - f(x_values[-2], y_values[-2]) + 2 * f(x_values[-1], y_values[-1])
    )

    # Corrector formula
    x_new = target_x
    y_corrected = y_values[-2] + (h / 3) * (
        f(x_values[-2], y_values[-2]) + 4 * f(x_values[-1], y_values[-1]) + f(x_new, y_predicted)
    )

    return y_corrected

#  dy/dx = f(x, y) from the equation
f = lambda x, y: (2 - y**2) / (5 * x + y)  # Rearranged from 5xy + y^2 - 2 = 0

# Initial values
x_values = [4.0, 4.1, 4.2, 4.3]
y_values = [1.0, 1.0049, 1.0097, 1.0143]
target_x = 4.4
h = 0.1

# Predictor-Corrector
y_at_target = milne_predictor_corrector(x_values, y_values, f, target_x, h)
print(y_at_target)
