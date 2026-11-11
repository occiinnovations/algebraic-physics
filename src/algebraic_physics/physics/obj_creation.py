from dataclasses import dataclass
from .mechanics import *
from .materials import *
from ..geometry.geom import *


@dataclass
class MakeACube:

    name: str
    material: str
    side: float = 0.0

    volume: float = 0.0
    mass: float = 0.0

    pos_x: float = 0.0
    pos_y: float = 0.0
    pos_z: float = 0.0

    velocity_x: float = 0.0
    velocity_y: float = 0.0
    velocity_z: float = 0.0

    def __post_init__(self):

        self.volume = cube_volume(self.side)
        self.mass = round(find_mass(MATERIALS[self.material], self.volume), 4)


@dataclass
class MakeASphere:
    name: str
    material: str
    radius: float = 0.0

    circumference: float = 0.0
    volume: float = 0.0
    mass: float = 0.0

    pos_x: float = 0.0
    pos_y: float = 0.0
    pos_z: float = 0.0

    velocity_x: float = 0.0
    velocity_y: float = 0.0
    velocity_z: float = 0.0

    def __post_init__(self):
        self.volume = sphere_volume(self.radius)
        self.mass = round(find_mass(MATERIALS[self.material], self.volume), 3)
        self.circumference = 2 * np.pi * self.radius


@dataclass
class MakeABox:
    name: str
    material: str

    volume: float = 0.0
    mass: float = 0.0

    side_1: float = 0.0
    side_2: float = 0.0
    side_3: float = 0.0

    pos_x: float = 0.0
    pos_y: float = 0.0
    pos_z: float = 0.0

    velocity_x: float = 0.0
    velocity_y: float = 0.0
    velocity_z: float = 0.0

    def __pos_init__(self):
        self.volume = rectangular_volume(self.side_1, self.side_2, self.side_3)
        self.mass = round(find_mass(MATERIALS[self.material], self.volume))
