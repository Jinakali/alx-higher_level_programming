#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    matrix_squared = []
    for i in range(len(matrix)):
        list_copy = matrix[i].copy()
        matrix_squared.append(list(map((lambda x: x ** 2), list_copy)))
    return matrix_squared
