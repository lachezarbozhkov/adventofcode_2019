from enum import Enum
class AddressMode(Enum):
    POSITIONAL = 0
    IMMEDIATE = 1
    RELATIVE = 2

class Computer:
    def __init__(self, data, inputs=[], manual_inputs=False, print_outputs=False):
        self.idx = 0
        self.data = data[:] + [0] * 3000
        self.done = False
        self.pause = False
        self.output = []
        self.inputs = inputs
        self.manual_inputs = manual_inputs
        self.print_outputs = print_outputs
        self.relative_base = 0
        self.instructions_dict = {
            1: lambda addresses: self.add(*addresses),
            2: lambda addresses: self.multiply(*addresses),
            3: lambda addresses: self.take_input(*addresses),
            4: lambda addresses: self.create_output(*addresses),
            5: lambda addresses: self.jump_if_true(*addresses),
            6: lambda addresses: self.jump_if_false(*addresses),
            7: lambda addresses: self.less_than(*addresses),
            8: lambda addresses: self.equals(*addresses),
            9: lambda addresses: self.relative_offset(*addresses),
            99: lambda addresses: self.exit()
        }

    def read_next_instruction(self):
        # ABCDE
        # 21002
        # DE - two-digit opcode,      02 == opcode 2
        # C - mode of 1st parameter,  0 == position mode
        # B - mode of 2nd parameter,  1 == immediate mode
        # A - mode of 3rd parameter,  2 == relative mode
        code = f"{self.data[self.idx]:05}"
        return [AddressMode(int(address_mode)) for address_mode in [code[2], code[1], code[0]]] + [int(code[3:])]

    def get_addresses(self, address1_mode, address2_mode, address3_mode):
        return self.calculate_address(address1_mode, 1), self.calculate_address(address2_mode, 2), self.calculate_address(address3_mode, 3)

    def calculate_address(self, address_mode, increment):
        if address_mode == AddressMode.POSITIONAL:
            return self.data[self.idx + increment]
        elif address_mode == AddressMode.IMMEDIATE:
            return self.idx + increment
        elif address_mode == AddressMode.RELATIVE:
            return self.relative_base + self.data[self.idx + increment]
        else:
            raise Exception(f"Not supported address mode: {address_mode}")

    def add(self, address1, address2, address3):
        self.data[address3] = self.data[address1] + self.data[address2]
        self.idx += 4

    def multiply(self, address1, address2, address3):
        self.data[address3] = self.data[address1] * self.data[address2]
        self.idx += 4

    def take_input(self, address1, *args):
        if self.manual_inputs:
            print("Enter command:")
            self.data[address1] = int(input())
        elif len(self.inputs) > 0:
            self.data[address1] = self.inputs.pop(0)
        else:
            self.pause = True
            return

        self.idx += 2

    def create_output(self, address1, *args):
        if self.print_outputs:
            print(self.data[address1])
        self.output.append(self.data[address1])
        self.idx += 2
        return self.output

    def less_than(self, address1, address2, address3):
        self.data[address3] = 1 if self.data[address1] < self.data[address2] else 0
        self.idx += 4

    def equals(self, address1, address2, address3):
        self.data[address3] = 1 if self.data[address1] == self.data[address2] else 0
        self.idx += 4

    def jump_if_true(self, address1, address2, address3):
        self.idx = self.data[address2] if self.data[address1] != 0 else self.idx + 3

    def jump_if_false(self, address1, address2, address3):
        self.idx = self.data[address2] if self.data[address1] == 0 else self.idx + 3

    def relative_offset(self, address1, *args):
        self.relative_base += self.data[address1]
        self.idx += 2

    def exit(self):
        self.done = True
        return self.output

    def clear_output(self):
        self.output = []

    def calculate(self, inputs=[]):
        self.pause = False
        self.inputs += inputs
        while not self.done and not self.pause:
            address1_mode, address2_mode, address3_mode, opcode = self.read_next_instruction()
            address1, address2, address3 = self.get_addresses(address1_mode, address2_mode, address3_mode)
            self.instructions_dict[opcode]([address1, address2, address3])

        return self.output              

# self test
quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
assert(Computer(quine).calculate() == quine)
