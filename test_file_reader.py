from file_reader import create_from_json, create_components, connect_components
from errors import (
    NotListError,
    IncorrectGateType,
    MissingData,
    InvalidInputNumber
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


def test_create_components_invalid_gate():
    with open('test_invalid_gate.json') as file_handle:
        component_list = json.load(file_handle)
        with pytest.raises(IncorrectGateType):
            create_components(component_list)


def test_create_components_missing_keys():
    with open('test_missing_keys.json') as file_handle:
        component_list = json.load(file_handle)
        with pytest.raises(MissingData):
            create_components(component_list)


def test_connect_components():
    with open('test.json') as file_handle:
        component_list = json.load(file_handle)
        flipflops, gates = create_components(component_list)
        connect_components(component_list, flipflops, gates)
        assert flipflops['1']._input == flipflops['5']
        assert flipflops['2']._input == flipflops['1']
        assert flipflops['3']._input == gates['3']
        assert flipflops['4']._input == flipflops['2']
        assert flipflops['5']._input == gates['5']
        assert gates['3']._input == flipflops['1']
        assert gates['5']._input == [flipflops['3'], flipflops['4']]


def test_connect_components_invalid_input():
    with open('test_invalid_input.json') as file_handle:
        component_list = json.load(file_handle)
        flipflops, gates = create_components(component_list)
        with pytest.raises(KeyError):
            connect_components(component_list, flipflops, gates)


def test_connect_components_too_many_inputs():
    with open('test_too_many_inputs.json') as file_handle:
        component_list = json.load(file_handle)
        flipflops, gates = create_components(component_list)
        with pytest.raises(TypeError):
            connect_components(component_list, flipflops, gates)


def test_connect_components_too_few_inputs():
    with open('test_too_few_inputs.json') as file_handle:
        component_list = json.load(file_handle)
        flipflops, gates = create_components(component_list)
        with pytest.raises(InvalidInputNumber):
            connect_components(component_list, flipflops, gates)


def test_connect_components_input_not_list():
    with open('test_input_not_list.json') as file_handle:
        component_list = json.load(file_handle)
        flipflops, gates = create_components(component_list)
        with pytest.raises(NotListError):
            connect_components(component_list, flipflops, gates)


def test_create_from_json():
    with open('test.json') as file_handle:
        flipflops, gates = create_from_json(file_handle)
    assert len(flipflops) == 5
    assert len(gates) == 2


def test_create_from_json_no_file():
    with open('test.json'):
        with pytest.raises(AttributeError):
            create_from_json('not a handle')
