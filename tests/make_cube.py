import geometry.geom as gm
import physics.mechanics as pm

dt = 0.1
time = 0.0
max_time = 5.0
current_acceleration = 1.0
speedy_boost = pm.speed_booster(1)

my_cube = {
    "side": 4,
    "mass": 10,
    "volume": 0,

    "pos_x": 0.0,
    "pos_y": 0.0,

    "velocity_x": 0.0,
    "velocity_y": 0.0,



}

print("Simulation Begin:")

my_cube["volume"] = gm.cube_volume(my_cube["side"])
print(f'The volume is {my_cube["volume"]}')

while time < max_time:
    current_acceleration = pm.speed_booster(current_acceleration)

    my_cube["velocity_x"] = pm.find_instantaneous_velocity(
        my_cube["velocity_x"],
        speedy_boost,
        dt
    )

    my_cube["pos_x"] = pm.find_position(
        my_cube["pos_x"],
        my_cube["velocity_x"],
        time,
        current_acceleration
    )

    print(
        f'Position of object: {my_cube["pos_x"]}; Velocity of object: {my_cube["velocity_x"]}'
    )
    time += dt

print("Simulation Done")
print(my_cube)
