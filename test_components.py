from components import (
    InvalidInputNumber, NotListError,
    FlipFlop,
    NOT, AND, OR, XOR, NAND, NOR, NXOR
)
import pytest

def test_FlipFlop_create():
    D1 = FlipFlop(None, True, True)
    D2 = FlipFlop(D1, False, False)
    D3 = FlipFlop(D2, False, False)
    D1._input = D3

    assert D1.value()
    assert not D2.value()
    assert not D3.value()


def test_FlipFlop_step():
    D1 = FlipFlop(None, True, True)
    D2 = FlipFlop(D1)
    D3 = FlipFlop(D2)
    D1._input = D3

    D1.store_value()
    D2.store_value()
    D3.store_value()

    D1.update_output()
    D2.update_output()
    D3.update_output()

    assert not D1.value()
    assert D2.value()
    assert not D3.value()


def test_NOT_create_invalid():
    pass


def test_AND_calculate():
    D1 = FlipFlop(None, True, True)
    D2 = FlipFlop(None, True, False)
    inputs = [D1, D2]
    G1 = AND(inputs)

    assert not G1.calculate()


def test_AND_create_invalid_type():
    D1 = FlipFlop(None)
    with pytest.raises(NotListError):
        AND(D1)


def test_AND_create_invalid_input_number():
    D1 = FlipFlop(None)
    with pytest.raises(InvalidInputNumber):
        AND([D1])


def test_OR_calculate():
    D1 = FlipFlop(None, True, True)
    D2 = FlipFlop(None, True, False)
    inputs = [D1, D2]
    G1 = OR(inputs)

    assert G1.calculate()
