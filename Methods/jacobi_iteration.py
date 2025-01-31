
import numpy as np

A = np.array([
    [10, -1, 2, 0],   # Coefficients from E1
    [-1, 11, -1, 3],  # Coefficients from E2
    [2, -1, 10, -1],  # Coefficients from E3
    [0, 3, -1, 8]     # Coefficients from E4
], dtype=float)

b = np.array([6, 25, -11, 15], dtype=float)

def jacobi_iteration(A, b, initial_guess, tolerance, max_iterations):
    n = len(b)
    x = initial_guess.copy()

    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i][i]

        if np.allclose(x, x_new, atol=tolerance):
            print(f"Converged after {iteration + 1} iterations")
            return x_new

        x = x_new

    print(f"Reached maximum iterations ({max_iterations}) without full convergence")
    return x

initial_guess = np.zeros(4)

tolerance = 1e-6

max_iterations = 100

solution = jacobi_iteration(A, b, initial_guess, tolerance, max_iterations)

print("\nSolution for x1, x2, x3, x4:")
print(solution)
