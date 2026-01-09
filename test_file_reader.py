from components import (
    FlipFlop, NOT, AND, OR, XOR, NAND, NOR, XNOR
)
from file_reader import read_from_json


def test_read_from_json():
    with open('test.json', 'r') as file_handle:
        read_from_json(file_handle)


test_read_from_json()
