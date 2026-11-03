# algebraic-physics

A Python utility library for geometry and physics calculations.

## File Directory

```text
mathformulas/
│
├── src/                 
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

## Requirements

* NumPy
