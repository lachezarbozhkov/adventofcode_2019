# https://adventofcode.com/2019/day/10

import numpy as np
from scipy import sparse
import math as m

the_map = """##.#..#..###.####...######
#..#####...###.###..#.###.
..#.#####....####.#.#...##
.##..#.#....##..##.#.#....
#.####...#.###..#.##.#..#.
..#..#.#######.####...#.##
#...####.#...#.#####..#.#.
.#..#.##.#....########..##
......##.####.#.##....####
.##.#....#####.####.#.####
..#.#.#.#....#....##.#....
....#######..#.##.#.##.###
###.#######.#..#########..
###.#.#..#....#..#.##..##.
#####.#..#.#..###.#.##.###
.#####.#####....#..###...#
##.#.......###.##.#.##....
...#.#.#.###.#.#..##..####
#....#####.##.###...####.#
#.##.#.######.##..#####.##
#.###.##..##.##.#.###..###
#.####..######...#...#####
#..#..########.#.#...#..##
.##..#.####....#..#..#....
.###.##..#####...###.#.#.#
.##..######...###..#####.#"""

# the_map = """.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##"""


# Part 1

def get_locations(s):
    array = np.array([[int(i=="#") for i in line ]for line in s.splitlines()])
    sparse_array = sparse.coo_matrix(array)
    coords = list(zip(sparse_array.col, sparse_array.row))
    return array, coords

def calculate_angle(a, b):
    theta = m.atan2(b[1]-a[1], b[0]-a[0]) * 180 / m.pi

    # Rotate map, so angles of coordinates are suitable for the laser gun rotation calculation. (part 2)
    theta = theta + 90
    if theta < 0:
        theta = 270 + (90 - abs(theta))
    return theta

array, locations = get_locations(the_map)

solutions= []
for i in locations:
    check = set()
    solutions.append(len(locations) - 1)
    for j in locations:
        if i == j:
            continue

        if calculate_angle(i, j) in check:
            solutions[-1] -= 1

        check.add(calculate_angle(i, j))

print(max(solutions))
pos = locations[np.argmax(solutions)]
print(pos)

# part 2
print("Part 2")

def calculate_distance(a, b):  
    dist = m.sqrt((b[1] - a[1])**2 + (b[0] - b[1])**2)  
    return dist  

def debug_angles(array, pos):
    array = array.copy()
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            theta = calculate_angle(pos, (j,i))
            array[i, j] = theta
        
    array[pos[1], pos[0]] = 10000
    return array

print(debug_angles(array, pos)[:, 8:])

vectors = []
for i in locations:
    if i == pos:
        continue

    distance = calculate_distance(pos, i)
    angle = calculate_angle(pos, i)
    vectors.append((angle, distance, i))

vectors = sorted(vectors)

print(vectors[:20])
index, steps = 0, 0
previous_angle = vectors[-1][0]

while len(vectors):
    angle, dist, pos = vectors[index]
    if angle != previous_angle:
        steps += 1
        del vectors[index]
        if steps in set([1, 2, 3, 10, 20, 50, 100, 199, 200, 201, 299]):
            print(f"At {steps} we deleted:", angle, dist, pos)
            
        if steps > 220:
            break
    else:
        index += 1

    previous_angle = angle
    if index >= len(vectors):
        index = 0
