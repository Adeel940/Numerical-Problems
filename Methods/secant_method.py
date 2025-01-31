import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x - 1) + np.cos(x - 1)


def secant_method(x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("Zero denominator. No solution found.")
            return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        print(f"Iteration {i+1}: x = {x2:.10f}, f(x) = {f(x2):.10f}")
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    print("Maximum iterations reached. No solution found.")
    return None

x0 = 1.3
x1 = 2

solution = secant_method(x0, x1)

x = np.linspace(1.3, 2, 400)
y = f(x)

plt.plot(x, y, label='f(x) = ln(x - 1) + cos(x - 1)')
plt.axhline(0, color='black', linewidth=0.5)
if solution is not None:
    plt.axvline(solution, color='red', linestyle='--', label=f'Solution at x = {solution:.5f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Secant Method: Finding the Root')
plt.legend()
plt.grid(True)
plt.show()

if solution is not None:
    print(f"Final solution: x = {solution:.5f}")