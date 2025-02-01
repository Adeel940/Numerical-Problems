
import sympy as sp

#  symbols
x, y = sp.symbols('x y')

# differential equation
dydx = 1 + x * y

# Initial condition
x0 = 0
y0 = 1

# Approximation order
order = 4

# Picard's Iteration Method
solutions = [y0]
for _ in range(order):
    integral = sp.integrate(dydx.subs(y, solutions[-1]), x)
    next_solution = y0 + integral.subs(x, x)
    solutions.append(next_solution)

for i, sol in enumerate(solutions[1:], start=1):
    print(f"Order {i}: {sol}")
