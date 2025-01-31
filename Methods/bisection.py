# part a

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x + np.log(x)

def bisection_method(a, b, tol=1e-5, plot_steps=True):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    iteration = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        iteration += 1
        print(f"Iteration {iteration}: Interval = [{a:.5f}, {b:.5f}], Midpoint = {c:.5f}, f(c) = {f(c):.5f}")

        if plot_steps:
            plot_bisection(a, b, c, iteration)

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def plot_bisection(a, b, c, iteration):
    x = np.linspace(1, 4, 400)
    y = f(x)

    plt.plot(x, y, label='f(x) = x^2 - 4x + ln(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(a, color='green', linestyle='--', label=f'a = {a:.5f}')
    plt.axvline(b, color='orange', linestyle='--', label=f'b = {b:.5f}')
    plt.axvline(c, color='red', linestyle='--', label=f'c = {c:.5f}')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Bisection Method: Iteration {iteration}')
    plt.legend()
    plt.grid(True)
    plt.show()

intervals = [(1, 2), (2, 4)]
roots = []


for interval in intervals:
    a, b = interval
    root = bisection_method(a, b)
    if root is not None:
        roots.append(root)
        print(f"Root found in interval [{a}, {b}]: x = {root:.5f}")


#part b

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)

def bisection_method(a, b, tol=1e-5, plot_steps=True):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    iteration = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        iteration += 1
        print(f"Iteration {iteration}: Interval = [{a:.5f}, {b:.5f}], Midpoint = {c:.5f}, f(c) = {f(c):.5f}")

        if plot_steps:
            plot_bisection(a, b, c, iteration)

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def plot_bisection(a, b, c, iteration):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)

    plt.plot(x, y, label='f(x) = e^x - 2 - cos(e^x - 2)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(a, color='green', linestyle='--', label=f'a = {a:.5f}')
    plt.axvline(b, color='orange', linestyle='--', label=f'b = {b:.5f}')
    plt.axvline(c, color='red', linestyle='--', label=f'c = {c:.5f}')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Bisection Method: Iteration {iteration}')
    plt.legend()
    plt.grid(True)
    plt.show()


intervals = [(0.5, 1.5)]
roots = []

for interval in intervals:
    a, b = interval
    root = bisection_method(a, b)
    if root is not None:
        roots.append(root)
        print(f"Root found in interval [{a}, {b}]: x = {root:.5f}")

import numpy as np
import matplotlib.pyplot as plt

def g1(x):
    return np.sqrt((x**4 - 3) / 3)

def g2(x):
    return np.sqrt(3*x**2 + 3)

def g3(x):
    return (3*x**2 + 3)**0.25

def g4(x):
    return np.sqrt((x**4 - 3) / 3)

def fixed_point_iteration(g, p0, tol=1e-2, max_iter=100):
    p = p0
    iteration = 0
    p_values = [p0]

    for i in range(max_iter):
        p_next = g(p)
        iteration += 1
        p_values.append(p_next)

        print(f"Iteration {iteration}: p = {p_next:.5f}")

        if abs(p_next - p) < tol:
            break

        p = p_next

    return p_values

p0 = 1


g_functions = [g1, g2, g3, g4]
g_labels = ['g1(x)', 'g2(x)', 'g3(x)', 'g4(x)']
roots = []


for i, g in enumerate(g_functions):
    print(f"Testing {g_labels[i]}")
    p_values = fixed_point_iteration(g, p0)


    x = np.linspace(1, 2, 400)
    y = g(x)

    plt.plot(x, y, label=f'{g_labels[i]}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.plot(p_values, g(np.array(p_values)), 'ro-', label='Iterations')
    plt.xlabel('x')
    plt.ylabel(g_labels[i])
    plt.title(f'Fixed-Point Iteration for {g_labels[i]}')
    plt.legend()
    plt.grid(True)
    plt.show()


    final_solution = p_values[-1]
    roots.append(final_solution)
    print(f"Final solution for {g_labels[i]}: x = {final_solution:.5f}\n")


for i, root in enumerate(roots):
    print(f"Final solution for {g_labels[i]}: x = {root:.5f}")
    