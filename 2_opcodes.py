# https://adventofcode.com/2019/day/2 
# Solve the opcodes.

def run_program(opcode):
    for i in range(0, len(opcode), 4):
        code = opcode[i]

        if code == 1:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
        elif code == 2:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
        elif code == 99:
            break
        else:
            raise Exception(f"What code is that {code}?")

    return opcode

assert(run_program([1,0,0,0,99]) == [2,0,0,0,99])
assert(run_program([2,3,0,3,99]) == [2,3,0,6,99])
assert(run_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
assert(run_program([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])

code_to_solve = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]
result_code = run_program([i for i in code_to_solve])
print(result_code)



# second part:
print("second part")
ans = 0
for noun in range(100):
    for verb in range(100):
        code_to_solve = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]
        code_to_solve[1] = noun
        code_to_solve[2] = verb

        result_code = run_program(code_to_solve)
        if result_code[0] == 19690720:
            ans = 100*noun + verb
            print(ans)
            break

    if ans > 0:
        break
