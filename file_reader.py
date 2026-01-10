from components import (
    FlipFlop, NOT, AND, OR, XOR, NAND, NOR, XNOR, MultiInputGate
)
import json
from errors import (
    IncorrectGateType,
    NotListError,
    MissingData,
    NotJsonError
)
from os.path import splitext


def create_components(component_list):
    """
    Reads connections from a list,
    and creates dicts of unconnected flipflops and gates

    :param component_list: list with objects from file
    :type component_list: list
    """
    if type(component_list) is not list:
        raise NotListError()
    created_flipflops = {}
    created_gates = {}
    for component in component_list:
        if 'id' not in component or 'input' not in component:
            raise MissingData()
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
                raise IncorrectGateType()
        created_flipflops[id] = FlipFlop(None)
    return created_flipflops, created_gates


def connect_components(component_list, flipflops, gates):
    """
    Connects components in dictionaries,
    based on data from a list from a file

    :param component_list: list with objects from file
    :type component_list: list

    :param flipflops: dict with ids as keys and FlipFlop objects as values
    :type flipflops: dict

    :param gates: dict with ids as keys and Gate objects as values
    :type gates: dict
    """
    for component in component_list:
        id = component['id']
        input = component['input']
        if 'gate' in component:
            current_flipflop = flipflops[id]
            current_gate = gates[id]
            if isinstance(current_gate, MultiInputGate):
                if type(input) is not list:
                    raise NotListError()
                current_input = []
                for input_part in input:
                    current_input.append(flipflops[input_part])
            else:
                current_input = flipflops[input]

            current_flipflop.set_input(current_gate)
            current_gate.set_input(current_input)
        else:
            current_flipflop = flipflops[id]
            current_input = flipflops[input]

            current_flipflop.set_input(current_input)

    return flipflops, gates


def create_from_json(file_handle):
    flipflops = {}
    gates = {}
    component_list = json.load(file_handle)
    created_flipflops, created_gates = create_components(component_list)
    flipflops, gates = connect_components(component_list,
                                          created_flipflops,
                                          created_gates)

    return flipflops, gates


def open_file(path):
    extension = splitext(path)[1]
    if extension != '.json':
        raise NotJsonError()
    with open(path) as file_handle:
        flipflops, gates = create_from_json(file_handle)
    return flipflops, gates
