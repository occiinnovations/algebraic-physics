import numpy as np
from . import vector_ops as vp


def matrix_addition(matrix_a, matrix_b):
    new_matrix = []
    for i in range(len(matrix_a)):

        new_matrix.append(vp.add_2_vectors(matrix_a[i], matrix_b[i]))

    return np.array(new_matrix)


def matrix_subtraction(matrix_a, matrix_b):
    new_matrix = []
    for i in range(len(matrix_a)):

        new_matrix.append(vp.sub_2_vectors(matrix_a[i], matrix_b[i]))

    return np.array(new_matrix)


def scalar_on_matrix(scalar, matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append(vp.scalar_on_vector(scalar, row))
    return np.array(new_matrix)


def matrix_multiplication(matrix_a, matrix_b):

    return np.matmul(matrix_a, matrix_b)


def count_columns(matrix):
    return vp.count_axis(matrix[0])


def count_rows(matrix):
    return len(matrix)


def check_matrix_symetrical(matrix):
    if count_rows(matrix) != count_columns(matrix):
        return False

    new_matrix = []
    for i in range(count_columns(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)

    return matrix == new_matrix


def matrix_transpose(matrix):

    new_matrix = []
    for i in range(count_columns(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix
