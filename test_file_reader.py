from components import (
    FlipFlop, NOT, AND, OR, XOR, NAND, NOR, XNOR
)
from file_reader import create_from_json, create_components, connect_components
from errors import (
    NotListError
)
import pytest
import json


def test_create_components():
    with open('test.json') as file_handle:
        component_list = json.load(file_handle)
        flipflops, gates = create_components(component_list)
        assert len(flipflops) == 5
        assert len(gates) == 2


def test_create_components_not_list():
    component_list = 'I am not a list'
    with pytest.raises(NotListError):
        create_components(component_list)
