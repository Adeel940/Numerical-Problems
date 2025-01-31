
import numpy as np

augmented_matrix = np.array([
    [9, 0, -3, 0, 0, 120],  # Equation 1
    [4, -4, 0, 0, 0, 0],    # Equation 2
    [0, -2, 9, 0, 0, 350],  # Equation 3
    [0, 1, 6, -9, 2, 0],    # Equation 4
    [5, 1, 0, 0, -6, 0]     # Equation 5
], dtype=float)


def gauss_jordan(mat):
    rows, cols = mat.shape

    for i in range(rows):
        if mat[i][i] == 0:
            for k in range(i+1, rows):
                if mat[k][i] != 0:
                    mat[[i, k]] = mat[[k, i]]
                    break

        mat[i] = mat[i] / mat[i][i]

        for j in range(rows):
            if i != j:
                mat[j] = mat[j] - mat[j][i] * mat[i]

    return mat


reduced_matrix = gauss_jordan(augmented_matrix)

solutions = reduced_matrix[:, -1]


print("Reduced Row Echelon Form (RREF):")
print(reduced_matrix)
print("\nSolutions for x1, x2, x3, x4, x5:")
print(solutions)
