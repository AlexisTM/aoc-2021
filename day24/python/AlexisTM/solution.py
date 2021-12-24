#!/usr/env python3
from alu import ALU


processor = ALU()
program = []

def test_value(x):
    processor.reset()
    processor.set_input(str(x))

    for instruction in program:
        processor.run(instruction)

    return processor.get('z') == 0


if __name__ == "__main__":
    with open("program.alu") as file:
        program = file.read().splitlines()

    val = 99999999999999
    while(True):
        # print(val)
        if val % 10000 == 0:
            print(val)
        if(test_value(val)):
            print("SUCCESS: ", val)
            break
        val = val - 1
