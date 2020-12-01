from computer import Computer

quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
assert(Computer(quine).calculate() == quine)

with open("9_input.txt") as _file:
    program = [int(num) for num in _file.read().split(",")]
    print(f"Part 1: {Computer(program, inputs=[1]).calculate()}")
    print(f"Part 2: {Computer(program, inputs=[2]).calculate()}")
