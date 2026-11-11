# algebraic-physics

A Python utility library for geometry and physics calculations based on the AP Physics 1 curriculum.

This library provides automated functions to solve for unknown variables using standard introductory mechanics equations. It accepts numerical inputs for known physical quantities to compute values across kinematics, dynamics, energy, momentum, and rotational motion.

The file 'make_cube.py' under tests/ utilizes a while loop for creating a new cube every second. There is an 'active_objects' list for holding shapes. 'aps' is used for accessing library functions. The library does contain a materials list.

## Installation

Install the library via [PyPI](https://pypi.org):

```bash
pip install algebraic-physics
```

## File Directory

```text
mathformulas/
│
├── .github/
│   └── workflows/
│
├── assets/
├── dist/
│
├── src/
│   └── algebraic_physics/
│       ├── geometry/
│       ├── physics/
│       └── __init__.py
│
├── tests/
│   └── make_cube.py
│
├── .env
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Tests Example

### Example 1 - Object Creation

```python
@dataclass # Dataclass system
class MakeACube:

    name: str               # Naming
    material: str           # Material choice; each choice gives a density
    side: float = 0.0       # side_length used for volume calculation

    volume: float = 0.0
    mass: float = 0.0

    pos_x: float = 0.0
    pos_y: float = 0.0
    pos_z: float = 0.0 # Z Axis Added

    velocity_x: float = 0.0
    velocity_y: float = 0.0
    velocity_z: float = 0.0

    def __post_init__(self):

        self.volume = cube_volume(self.side)            # Cube Volume is side_length **3
        self.mass = round(
            find_mass(MATERIALS[self.material], self.volume) # find_mass = material density * volume
                            ,4)
```

### Example 2 - Logic of Simulation in 'make_cube.py'

```python
#make_cube.py
import algebraic_physics as aps

active_objects = []

... 

while time < max_time:

    if round(time, 1) % 1.0 == 0.0:
        unique_name = f"cube {cube_id_counter}"

        my_new_cube = aps.MakeACube(   #<<<------ Cube Named 'my_new_cube' 
            name=unique_name, 
            side=5.0, 
            material="oxygen"
            )

        active_objects.append(my_new_cube)   #Added to 'active_objects', which undergoes a for loop for physics calculations
        print(f"Spawned: {my_new_cube.name}")
...
```

## Source Formulas

![Mechanics and Fluids](assets/formulas.png)

![Geometry/Conversion](assets/geometry.png)
