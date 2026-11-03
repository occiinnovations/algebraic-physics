# algebraic-physics

A Python utility library for geometry and physics calculations.

## Structure

* `geom.py` - Math constants and geometric calculations (area, volume, surface area).
* `mechanics.py` - Core mechanics formulas (kinematics, center of mass, system acceleration, gravity).

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
