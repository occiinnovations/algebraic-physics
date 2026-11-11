import algebraic_physics as aps

dt = 0.1
time = 0.0
max_time = 5.0
current_acceleration = 1.0
speedy_boost = aps.speed_booster(1)

cube_id_counter = 1
active_objects = []

print("Starting Sim")

while time < max_time:

    if round(time, 1) % 1.0 == 0.0:
        unique_name = f"cube {cube_id_counter}"

        my_new_cube = aps.MakeACube(
            name=unique_name, side=5.0, material="oxygen")
        print(my_new_cube)

        active_objects.append(my_new_cube)
        print(f"Spawned: {my_new_cube.name}")

        cube_id_counter += 1

    current_acceleration = aps.speed_booster(current_acceleration)

    for obj in active_objects:
        obj.pos_x = round(aps.find_position(
            obj.pos_x, obj.velocity_x, dt, current_acceleration), 3)

        obj.velocity_x = round(aps.find_instantaneous_velocity(
            obj.velocity_x, current_acceleration, dt), 3)

    time += dt

print("Final Items:")
for item in active_objects:
    print(item)
