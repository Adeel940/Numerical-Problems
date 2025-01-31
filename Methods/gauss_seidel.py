
import numpy as np

A = np.array([
    [12, 3, -5],   # Equation 1
    [1, 5, 3],     # Equation 2
    [3, 7, 13]     # Equation 3
], dtype=float)

b = np.array([1, 28, 76], dtype=float)

def gauss_seidel(A, b, initial_guess, tolerance, max_iterations):
    n = len(b)
    x = initial_guess.copy()

    for iteration in range(max_iterations):
        x_new = np.copy(x)

        for i in range(n):
            sum_ = sum(A[i][j] * x_new[j] for j in range(n) if j != i)

            x_new[i] = (b[i] - sum_) / A[i][i]

        if np.allclose(x, x_new, atol=tolerance):
            print(f"Converged after {iteration + 1} iterations")
            return x_new


        x = x_new

    print(f"Reached max iterations ({max_iterations}) without full convergence")
    return x

initial_guess = np.array([0, 0, 0], dtype=float)

tolerance = 1e-6

max_iterations = 100


solution = gauss_seidel(A, b, initial_guess, tolerance, max_iterations)

print("\nSolution for x1, x2, x3:")
print(solution)
