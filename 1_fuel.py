# https://adventofcode.com/2019/day/1
# Calculate fuel needed for the mass

def calc_fuel(mass):
    fuel =  mass // 3 - 2
    if fuel < 0: 
        fuel = 0
    
    return fuel

def calc_fuel_including(mass):
    fuel = calc_fuel(mass)
    fuel_list = []
    while fuel > 0:
        fuel_list.append(fuel)
        fuel = calc_fuel(fuel)

    return(sum(fuel_list))


assert(calc_fuel(12) == 2)
assert(calc_fuel(14) == 2)
assert(calc_fuel(1969) == 654)
assert(calc_fuel(100756) == 33583)

assert(calc_fuel_including(12) == 2)
assert(calc_fuel_including(1969) == 966)
assert(calc_fuel_including(100756) == 50346)


with open("1_input.txt", "r") as f:
    total_fuel = sum(calc_fuel_including(int(line)) for line in f.readlines())

print("fuel required:", total_fuel)

