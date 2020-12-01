# https://adventofcode.com/2019/day/7

def run_program(opcode, stack, i=0):

    def get_val(i, immediate_mode):
        return opcode[i] if immediate_mode else opcode[opcode[i]]

    while i < len(opcode):

        code = opcode[i]
        code_A = code // 10000 # 3rd param
        code = code % 10000
        code_B = code // 1000 # 2nd param
        code = code % 1000
        code_C = code // 100 # 1st param
        code = code % 100

        if code == 1:
            opcode[opcode[i+3]] = get_val(i+1, code_C) + get_val(i+2, code_B)
            i += 4

        elif code == 2:
            opcode[opcode[i+3]] = get_val(i+1, code_C) * get_val(i+2, code_B)
            i += 4

        elif code == 3:
            # input a value
            opcode[opcode[i+1]] = int(stack.pop())
            i += 2

        elif code == 4: 
            # output the value
            stack.append(get_val(i+1, code_C))
            i += 2
            return i

        elif code == 5:
            # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if get_val(i+1, code_C):
                i = get_val(i+2, code_B)
            else:
                i += 3

        elif code == 6:
            # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if get_val(i+1, code_C) == 0:
                i = get_val(i+2, code_B)
            else:
                i += 3

        elif code == 7:
            # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            opcode[opcode[i+3]] = int(get_val(i+1, code_C) < get_val(i+2, code_B))
            i += 4

        elif code == 8:
            # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            opcode[opcode[i+3]] = int(get_val(i+1, code_C) == get_val(i+2, code_B))
            i += 4

        elif code == 99:
            return
            
        else:
            raise Exception(f"What code is that {code}?")

    return i


def calculate_amp(phases, code):
    stack = [0]
    for phase in phases:
        stack.append(phase)
        run_program(code.copy(), stack) 
    return stack.pop()

phases = [4,3,2,1,0]
code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
result = calculate_amp(phases, code)
assert (result == 43210)


phases = [0,1,2,3,4]
code = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
result = calculate_amp(phases, code)
assert (result == 54321)

phases = [1,0,4,3,2]
code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
result = calculate_amp(phases, code)
assert (result == 65210)



# # First part of the program:
import itertools
results = []
code = [3,8,1001,8,10,8,105,1,0,0,21,46,55,72,85,110,191,272,353,434,99999,3,9,1002,9,5,9,1001,9,2,9,102,3,9,9,101,2,9,9,102,4,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]

for phase in itertools.permutations([0, 1, 2, 3, 4]):
    result = calculate_amp(phase, code)
    results.append((result, phase))

print(sorted(results)[-5:])



# Second part
print("Second part")

def calculate_amp_loop(phases, code):
    codes = [code.copy() for i in range(len(phases))]
    indexes = [0 for i in range(len(phases))]
    stack = [0]
    for i, phase in enumerate(phases):
        stack.append(phase)
        indexes[i] = run_program(codes[i], stack, indexes[i]) 

    while True:
        for i, phase in enumerate(phases):
            try:
                indexes[i] = run_program(codes[i], stack, indexes[i])             
            except:
                return stack.pop()
        
    return stack.pop()


phases = [9,8,7,6,5]
code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
result = calculate_amp_loop(phases, code)
print(result)
assert (result == 139629729)

phases = [9,7,8,5,6]
code = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
result = calculate_amp_loop(phases, code)
print(result)
assert (result == 18216)





results = []
code = [3,8,1001,8,10,8,105,1,0,0,21,46,55,72,85,110,191,272,353,434,99999,3,9,1002,9,5,9,1001,9,2,9,102,3,9,9,101,2,9,9,102,4,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]

for phase in itertools.permutations([5, 6, 7, 8, 9]):
    result = calculate_amp_loop(phase, code)
    results.append((result, phase))

print(sorted(results)[-5:])
