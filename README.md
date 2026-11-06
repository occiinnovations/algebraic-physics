# algebraic-physics

A Python utility library for geometry and physics calculations based on the AP Physics 1 curriculum.

This library provides automated functions to solve for unknown variables using standard introductory mechanics equations. It accepts numerical inputs for known physical quantities to compute values across kinematics, dynamics, energy, momentum, and rotational motion.

## File Directory

```text
mathformulas/
│
├─ assets/... 
│
├─ src/                 
│   ├── geom.py  
│   └── mechanics.py
│    
├─ .gitignore
├─ LICENSE
├─ README.md
└─ requirements.txt
```

## Example

```python
import geom
import mechanics

# Geometry calculation
volume, surface_area = geom.sphere(radius=5)

# System calculation using object lists: ["Name", mass, position, force]
objects = [
    ["Ball", 2.0, 5.0, 10.0],
    ["Block", 4.0, 6.0, 8.0]
]

cm = mechanics.center_of_mass(objects)
```

## Note

Soon I will be merging this repo with shapeshift repo.

## Source Formulas

[**PDF Link**](https://apcentral.collegeboard.org/media/pdf/ap-physics-1-equations-sheet.pdf)

![Mechanics and Fluids](assets\formulas.png)

![Geometry/Conversion](assets\geometry.png)
