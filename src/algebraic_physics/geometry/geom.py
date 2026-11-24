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


def side_amounts(angle_points):
    side_lengths_of_shape = []
    count = 0
    first_point = angle_points[0]
    final_point = ()
    for point in angle_points:
        this_side_length = 0

        if count > 0:
            this_side_length = xyz_distance_formula(using_point, point)
        count += 1

        try:
            side_lengths_of_shape.append(
                f"Side {count}; Joins {using_point} to {point}; Length = {this_side_length}")
        except:
            pass
        using_point = point
        final_point = point

    if angle_points[0] != angle_points[-1]:

        final_side = xyz_distance_formula(final_point, first_point)
        count += 1
        side_lengths_of_shape.append(
            f"Final Side {count}; Joins {final_point} to {first_point}; Length = {final_side}")
    return side_lengths_of_shape
