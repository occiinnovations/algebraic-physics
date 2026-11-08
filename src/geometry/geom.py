import numpy as np

gravity_m3 = 6.67 * 10**-11

one_atm = 1.0 * 10**5


def rectangleArea(length, width):
    return length * width


def cube_volume(side_length):
    volume = side_length**3
    return volume


def triangleArea(base, height):
    return 0.5 * base * height


def circle(radius):
    area = np.pi * (radius**2)
    circumference = 2 * np.pi * radius

    return area, circumference


def rectangular_solid(length, width, height):
    volume = length * width * height

    return volume


def cylinder(radius, length):
    volume = np.pi * (radius**2) * length
    surface_area = (2 * np.pi * radius * length) + (2 * np.pi * (radius**2))

    return volume, surface_area


def sphere(radius):
    volume = 4/3 * np.pi * (radius**3)
    surface_area = 4 * np.pi * (radius**2)
    return volume, surface_area


def arc_relations(r, theta):
    s = r*theta
    return s


def pythag(side1, side2):
    side3 = (side1**2 + side2**2)**(1/2)
    return side3
