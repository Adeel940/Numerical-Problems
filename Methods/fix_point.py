import numpy as np
import matplotlib.pyplot as plt

def g1(x):
    return np.cbrt(x + 1)

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

g_functions = [g1]
g_labels = ['g1(x)']
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
    