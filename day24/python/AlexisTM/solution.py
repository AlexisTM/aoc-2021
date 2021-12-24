#!/usr/env python3
from alu import ALU
from alu_to_math import MathALU
import json
from copy import deepcopy

POSSIBLE_VALUES = list("89")
alu = ALU()
default_internals = alu.get()
tree = {"i": default_internals}
program_steps = []

def runner(steps, internals, input):
    alu = ALU()
    alu.reset()
    alu.set_input(str(input))
    alu.set_internals(deepcopy(internals))
    for instruction in steps:
        alu.run(instruction)
    return alu.get()

def do_subtree(subtree, from_step, to_step):
    if from_step >= to_step: return
    for val in POSSIBLE_VALUES:
        internal = runner(program_steps[from_step], subtree['i'], val)
        subtree[val] = {"i": internal}
        do_subtree(subtree[val], from_step + 1, to_step)

if __name__ == "__main__":
    with open("program.alu") as file:
        program = file.read().splitlines()


    # split program in steps
    step = []
    for instruction in program:
        if instruction.startswith("inp"):
            if(step):
                program_steps.append(step)
                step = []
        step.append(instruction)
    program_steps.append(step)

    # node = { val: "1", internal: {}}

    """
        tree["i"] = default_internals
        for val in POSSIBLE_VALUES:
            internal = runner(steps[0], default_internals, val)
            tree[val] = {"internal": internal}
    """

    do_subtree(tree, 0, 14)

    print(json.dumps(tree, indent=4))

    """
        for instruction in program:
            alu.run(instruction)
            print("Index: ", index)
            print("val: ", alu.get())
            index += 1
    """
