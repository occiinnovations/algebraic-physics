import numpy as np

gravity_m3 = 6.67 * 10**-11

one_atm = 1.0 * 10**5


def rectangle_area(length, width):
    return length * width


def cube_volume(side_length):
    volume = side_length**3
    return volume


def triangle_area(base, height):
    return 0.5 * base * height


def circle(radius):
    area = np.pi * (radius**2)
    circumference = 2 * np.pi * radius

    return area, circumference


def rectangular_volume(length, width, height):
    volume = length * width * height

    return volume


def cylinder(radius, length):
    volume = np.pi * (radius**2) * length
    surface_area = (2 * np.pi * radius * length) + (2 * np.pi * (radius**2))

    return volume, surface_area


def sphere_volume(radius):
    volume = 4/3 * np.pi * (radius**3)
    surface_area = 4 * np.pi * (radius**2)
    return volume, surface_area


def arc_relations(r, theta):
    s = r*theta
    return s


def pythag(side1, side2):
    side3 = (side1**2 + side2**2)**(1/2)
    return side3


def xy_distance_formula(point1, point2):  # use tuples or lists for this

    distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return distance


def xyz_distance_formula(point1, point2):
    distance = np.sqrt((point2[0] - point1[0])**2 +
                       (point2[1] - point1[1])**2 +
                       (point2[2] - point1[2])**2
                       )
    return distance
