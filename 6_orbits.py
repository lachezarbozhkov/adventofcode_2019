# https://adventofcode.com/2019/day/6 


with open("6_orbits.txt", "r") as f:
    lines = f.readlines()

print(len(lines))

# Solve the first question: 
# What is the total number of direct and indirect orbits in your map data?

orbits = dict()
for line in lines:
    A, B = line.strip().split(")")
    orbits[B] = A
print(len(orbits))

counter = 0
for i in orbits.keys():
    new_orbit = orbits[i]
    while new_orbit:
        counter += 1
        new_orbit = orbits.get(new_orbit, None)

print(counter)

# Solve the second question:
# What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting?

print("Start the search...")

def all_pointing_to_current(current_node):
    satellites = [k for k,v in orbits.items() if v == current_node]
    my_orbit = orbits[current_node]
    return satellites + [my_orbit]

used_nodes = set()
the_path = []

def search(current_node):
    used_nodes.add(current_node)
    nodes = all_pointing_to_current(current_node)
    for n in nodes:
        if n == search_node:
            the_path.append(n)
            the_path.append(current_node)
            return 1
        elif n in used_nodes:
            continue
        else:
            search_result = search(n)
            if search_result:
                the_path.append(current_node)
                return search_result + 1
    return 0

current_node = "YOU"
search_node = "SAN"

print(search(current_node))
print(len(the_path))
print(the_path)
print("Result:", len(the_path) - 2 - 1)
