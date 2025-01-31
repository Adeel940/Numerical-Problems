

import numpy as np

A = np.array([
    [8, 2, 2, 5, 6],    # Equation 1
    [0, 1, 1, 2, 2],    # Equation 2
    [8, 6, 3, 1, 3],    # Equation 3
    [2, 8, 4, 9, 0],    # Equation 4
    [1, 7, 8, 4, 8]     # Equation 5
], dtype=float)

b = np.array([8, 4, 3, 7, 7], dtype=float)

def lu_decomposition(A):
    n = len(A)
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(n):
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_


        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U

def forward_substitution(L, b):
    n = len(L)
    y = np.zeros_like(b)

    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    return y

def back_substitution(U, y):
    n = len(U)
    x = np.zeros_like(y)

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x

L, U = lu_decomposition(A)

y = forward_substitution(L, b)

x = back_substitution(U, y)


print("Lower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)
print("\nSolution for x1, x2, x3, x4, x5:")
print(x)
