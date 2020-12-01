import numpy as np

# def get_positions():
#     return np.array([
#         [-1, 0, 2],
#         [2, -10, -7],
#         [4, -8, 8],
#         [3, 5, -1]
#         ]
#     )

def get_positions():
    return np.array([
        [5, 13, -3],
        [18, -7, 13],
        [16, 3, 4],
        [0, 8, 8]
        ]
    )

from collections import defaultdict

original_pos = get_positions()

def calculate_moons():
    positions = get_positions()
    velocity  = np.zeros_like(positions)
    moons = len(positions)
    dimensions = 3
       
    done_dimensions = np.array([0, 0, 0])
    for step in range(1_000_000_000_000):
        for i in range(dimensions):
            for j in range(moons):
                for z in range(moons):
                    if positions[j, i] > positions[z, i]:
                        velocity[j, i] -= 1
                    elif positions[j, i] < positions[z, i]:
                        velocity[j, i] += 1
        
        positions += velocity

        # part 2
        for i in range(dimensions):
            if (velocity[:, i] == [0, 0, 0, 0]).all() and (positions[:, i] == original_pos[:, i]).all():
                print(f"Step {step} for dimension {i}")
                done_dimensions[i] = step + 1
                if (done_dimensions > 0).all():
                    print(done_dimensions)
                    print("lcm:", np.lcm.reduce(done_dimensions))
                    return


    pot = np.abs(positions).sum(axis=1)
    kin = np.abs(velocity).sum(axis=1)
    total_energy = pot*kin

    print("step:", step + 1)
    print(positions)
    print(velocity)
    print(pot, kin, total_energy)
    print(total_energy.sum())

calculate_moons()


