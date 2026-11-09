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
        self.mass = round(find_mass(
            MATERIALS[self.material], self.volume), 4)


my_new_cube = MakeACube(name="Jerry", side=5.0, material="oxygen")
print(my_new_cube)
