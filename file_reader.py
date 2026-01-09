from components import (
    FlipFlop, NOT, AND, OR, XOR, NAND, NOR, XNOR, MultiInputGate
)
import json


class IncorrectGateType(Exception):
    pass


def create_components(component_list):
    created_flipflops = {}
    created_gates = {}
    for component in component_list:
        id = component['id']
        placeholder_FlipFlop = FlipFlop(None)
        placeholder_list = [placeholder_FlipFlop, placeholder_FlipFlop]
        if 'gate' in component:
            gate_type = component['gate']
            if gate_type == 'NOT':
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
            else:
                raise IncorrectGateType
        created_flipflops[id] = FlipFlop(None)
    return created_flipflops, created_gates


def connect_components(component_list, flipflops, gates):
    connected_flipflops = []
    connected_gates = []
    for component in component_list:
        id = component['id']
        input = component['input']
        if 'gate' in component:
            current_flipflop = flipflops[id]
            current_gate = gates[id]
            if isinstance(current_gate, MultiInputGate):
                current_input = []
                for input_part in input:
                    current_input.append(flipflops[input_part])
            else:
                current_input = flipflops[input]

            current_flipflop._input = current_gate
            current_gate._input = current_input
            connected_flipflops.append(current_flipflop)
            connected_gates.append(current_gate)
        else:
            current_flipflop = flipflops[id]
            current_input = flipflops[input]

            current_flipflop._input = current_input
            connected_flipflops.append(current_flipflop)

    return connected_flipflops, connected_gates


def read_from_json(file_handle):
    flipflops = []
    gates = []
    component_list = json.load(file_handle)
    created_flipflops, created_gates = create_components(component_list)
    flipflops, gates = connect_components(component_list, created_flipflops, created_gates)

    return flipflops, gates
