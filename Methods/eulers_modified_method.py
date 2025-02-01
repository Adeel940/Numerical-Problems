
def eulers_modified_method(f, x0, y0, h, x_target):
    x = x0
    y = y0

    while x < x_target:
        y_predictor = y + h * f(x, y)
        y_corrector = y + (h / 2) * (f(x, y) + f(x + h, y_predictor))
        y = y_corrector
        x += h

    return y

f = lambda x, y: (x - y) / 2
x0 = 0
y0 = 1
h = 0.1
x_target = 0.2

y_at_target = eulers_modified_method(f, x0, y0, h, x_target)
print(y_at_target)
