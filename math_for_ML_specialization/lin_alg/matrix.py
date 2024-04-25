import numpy as np


#Ar = s

A = [[1, 1.5, 0.5],
     [0, 1, 1],
     [0, 0, 2]]

s = [2.25, -0.5, 0]


r = np.linalg.solve(A, s)

print(r)

# Define a function to convert a matrix into echelon form
# def to_echelon_form(A, s):
#     """
#     Convert matrix A into echelon form with respect to vector s.

#     Parameters:
#     A (numpy.ndarray): The matrix to be converted.
#     s (numpy.ndarray): The vector to be used for the conversion.

#     Returns:
#     numpy.ndarray: The matrix in echelon form.
#     numpy.ndarray: The transformed vector s.
#     """
#     # Form the augmented matrix with the right-side vector
#     augmented = np.column_stack((A, s))
#     r, c = A.shape

#     # Loop over each row
#     for i in range(r):
#         # Make the diagonal contain all 1s
#         # Find the pivot
#         pivot = augmented[i, i]
#         if pivot == 0:
#             # If pivot is zero, find a non-zero element and swap rows
#             for j in range(i+1, r):
#                 if augmented[j, i] != 0:
#                     augmented[[i, j]] = augmented[[j, i]]
#                     pivot = augmented[i, i]
#                     break
#         # Skip if no pivot is found
#         if pivot == 0:
#             continue
#         # Scale the pivot row
#         augmented[i] = augmented[i] / pivot
#         # Eliminate all other entries in the current column
#         for j in range(r):
#             if j != i:
#                 ratio = augmented[j, i]
#                 augmented[j] = augmented[j] - ratio * augmented[i]

#     # Separate the matrix and the vector
#     echelon_A = augmented[:, :-1]
#     transformed_s = augmented[:, -1]

#     return echelon_A, transformed_s

# # Example matrix A and vector s
# A_example = np.array([[1, 1, 1], [3, 2, 1], [2, 1, 2]])
# s_example = np.array([15, 28, 23])

# # Convert to echelon form
# echelon_A, transformed_s = to_echelon_form(A_example, s_example)

# print(echelon_A, transformed_s)


A = [[1, 1, 1],
     [3, 2, 1],
     [2, 1, 2]]

A_inv = np.linalg.inv(A)

print(A_inv)