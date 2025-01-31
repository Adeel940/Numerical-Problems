import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) + 2**(-x) + 2 * np.cos(x) - 6

def df(x):
    return np.exp(x) - np.log(2) * 2**(-x) - 2 * np.sin(x)

def newtons_method(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None
        x_next = x - fx / dfx
        print(f"Iteration {i+1}: x = {x_next:.10f}, f(x) = {f(x_next):.10f}")
        if abs(x_next - x) < tol:
            break
        x = x_next
    return x

x0 = 3

solution = newtons_method(x0)
x = np.linspace(1, 2, 400)
y = f(x)

plt.plot(x, y, label='f(x) = e^x + 2^(-x) + 2cos(x) - 6')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(solution, color='red', linestyle='--', label=f'Solution at x = {solution:.5f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton\'s Method: Finding the Root')
plt.legend()
plt.grid(True)
plt.show()
print(f"Final solution: x = {solution:.5f}")