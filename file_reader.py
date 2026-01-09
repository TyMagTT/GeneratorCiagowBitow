from components import (
    FlipFlop, NOT, AND, OR, XOR, NAND, NOR, XNOR
)
import json


def read_from_json(file_handle):
    flipflops = []
    gates = []
    created_flipflops = {}
    created_gates = {}
    data = json.load(file_handle)
    for item in data:
        try:
            # create components
            # connect components
            id = item['id']
            inputs = item['input']
            placeholder_FlipFlop = FlipFlop(None)
            placeholder_list = [placeholder_FlipFlop, placeholder_FlipFlop]
            if 'gate' in item:
                # gate
                gate_type = item['gate']
                if gate_type == 'NOT':
                    # cannot create with none
                    created_gates[id] = NOT(placeholder_FlipFlop)
                elif gate_type == 'AND':
                    created_gates[id] = AND(placeholder_list)
                elif gate_type == 'OR':
                    created_gates[id] = OR(placeholder_list)
                elif gate_type == 'XOR':
                    created_gates[id] = XOR(placeholder_list)
                elif gate_type == 'NAND':
                    created_gates[id] = NAND(placeholder_list)
                elif gate_type == 'NOR':
                    created_gates[id] = NOR(placeholder_list)
                elif gate_type == 'XNOR':
                    created_gates[id] = XNOR(placeholder_list)
                created_flipflops[id] = FlipFlop(None)
            else:
                # no gate
                created_flipflops[id] = FlipFlop(None)
                pass
        except Exception as e:
            return e

    return flipflops, gates
