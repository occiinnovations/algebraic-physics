import numpy as np


def add_2_vectors(vector1, vector2):

    new_vector = []
    for i in range(len(vector1)):
        new_vector.append(vector1[i] + vector2[i])

    return np.array(new_vector)


def sub_2_vectors(vector1, vector2):

    new_vector = []
    for i in range(len(vector1)):
        new_vector.append(vector1[i] - vector2[i])

    return np.array(new_vector)


def scalar_on_vector(scalar, vector):
    new_vec = []
    for i in vector:
        i *= scalar
        new_vec.append(i)

    return np.array(new_vec)


def vector_magnitude(vector):
    total = 0

    for i in vector:
        total += i**2

    total **= (1/2)
    return total


def dot_product(vector1, vector2):
    total = 0
    for i in range(len(vector1)):
        total += vector1[i] * vector2[i]

    return total


def cross_product(vector_a, vector_b):

    x = vector_a[2]*vector_b[3] - vector_a[3]*vector_b[2]
    y = vector_a[3]*vector_b[1] - vector_a[1]*vector_b[3]
    z = vector_a[1]*vector_b[2] - vector_a[2]*vector_a[1]

    return np.array([x, y, z])


def find_unit_vector(vector):
    new_vec = []

    for i in vector:
        new_vec.append(i/vector_magnitude(vector))

    return new_vec


def count_axis(vector):
    return len(vector)
