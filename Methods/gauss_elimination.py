#Question 2(b)

import numpy as np

augmented_matrix = np.array([
    [9, 2, 0, 0, 90],    # Equation 1
    [0, 3, 4, 0, 0],     # Equation 2
    [0, 5, -1, 1, 25],   # Equation 3
    [-2, 0, 4, 0, 0]     # Equation 4
], dtype=float)

def gauss_elimination(mat):
    rows, cols = mat.shape

    for i in range(rows):
        if mat[i][i] == 0:
            for k in range(i + 1, rows):
                if mat[k][i] != 0:
                    mat[[i, k]] = mat[[k, i]]  # Swap rows
                    break

        mat[i] = mat[i] / mat[i][i]

        for j in range(i + 1, rows):
            mat[j] = mat[j] - mat[j][i] * mat[i]

    return mat

def back_substitution(mat):
    rows, cols = mat.shape
    x = np.zeros(rows)


    for i in range(rows - 1, -1, -1):
        x[i] = mat[i][-1] - np.sum(mat[i][i + 1:cols - 1] * x[i + 1:])

    return x

upper_triangular_matrix = gauss_elimination(augmented_matrix)

solutions = back_substitution(upper_triangular_matrix)

print("Upper Triangular Matrix:")
print(upper_triangular_matrix)
print("\nSolutions for x1, x2, x3, x4:")
print(solutions)
