from components import (
    FlipFlop, NOT, AND, OR, XOR, NAND, NOR, XNOR
)
import json


def read_from_json(file_handle):
    flipflops = []
    gates = []
    data = json.load(file_handle)
    objects = {}
    for item in data:
        try:
            # create components
            # connect components
            id = item['id']
            inputs = item['input']
            if 'gate' in item:
                # gate
                gate_type = item['gate']
                gate_name = f'gate{id}'
                if gate_type == 'NOT':
                    objects[gate_name] = NOT(None)
                elif gate_type == 'AND':
                    objects[gate_name] = AND(None)
                elif gate_type == 'OR':
                    objects[gate_name] = OR(None)
                elif gate_type == 'XOR':
                    objects[gate_name] = XOR(None)
                elif gate_type == 'NAND':
                    objects[gate_name] = NAND(None)
                elif gate_type == 'NOR':
                    objects[gate_name] = NOR(None)
                elif gate_type == 'XNOR':
                    objects[gate_name] = XNOR(None)
                objects[id] = FlipFlop(None)
            else:
                # no gate
                objects[id] = FlipFlop(None)
                pass
        except Exception:
            pass

    return flipflops, gates
