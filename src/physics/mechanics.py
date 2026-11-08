import numpy as np
import geometry.geom as geom

# #1


def find_instantaneous_velocity(initial_velocity, acceleration, time):

    v_x = initial_velocity + (acceleration * time)
    return v_x

# #2


def find_position(inital_position, initial_velocity, time, current_acceleration):

    x = inital_position + (initial_velocity*time) + \
        ((1/2)*current_acceleration*(time**2))
    return x

# #3


def find_velocity_squared(initial_velocity, acceleration, current_position, initial_position=0):
    v_x_squared = initial_velocity**2 + 2 * \
        acceleration * (current_position - initial_position)
    return v_x_squared

# example: [["Ball", 2, 5, forceof10righthere],["Block", 4, 6, forceof8righthere]]

# #4


def center_of_mass(list_of_object_lists):
    top_part = 0
    total_mass = 0
    for obj in list_of_object_lists:
        top_part += (obj[1]*obj[2])
        total_mass += obj[1]

    center_of_mass = float(top_part/total_mass)
    return center_of_mass

# #5


def total_acceleration(list_of_object_lists):
    top_part = 0
    bottom_part = 0

    for obj in list_of_object_lists:
        top_part += obj[3]
        bottom_part += obj[1]

    total_acceleration = top_part/bottom_part
    return total_acceleration

# #6


def newtons_law_of_universal_gravitation(mass1, mass2, radius):
    attractive_force = geom.gravity_m3 * ((mass1 * mass2)/(radius**2))
    return attractive_force

# #10


def kinetic_energy(mass, velocity):
    KE = (1/2) * mass * (velocity**2)
    return KE

# #11


def work(force, distance, angle):

    if isinstance(angle, float) or isinstance(angle, int):
        angle = np.radians(angle)

    work = (force * distance) * np.cos(angle)
    return work

# #12


def delta_ke(*work):
    return sum(work)

# #16


def momentum(mass, velocity):
    momentum = mass * velocity

    return momentum

# #9


def centripetal_acceleration(velocity, radius):
    centripetal_acceleration = (velocity**2)/radius
    return centripetal_acceleration


def density(mass, volume):
    density = mass/volume
    return density


def speed_booster(scalar):
    if scalar < 1000:
        scalar += 1
    return scalar
