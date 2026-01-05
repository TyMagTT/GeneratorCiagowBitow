from components import (
    InvalidInputNumber, NotListError, NotFlipFlopError, NotBoolError,
    FlipFlop, Gate, MultiInputGate,
    NOT, AND, OR, XOR, NAND, NOR, XNOR
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


def test_Gate_create():
    G0 = Gate(None, True)
    assert G0.output()
    G0._output = False
    assert not G0.output()


def test_Gate_create_invalid_output():
    with pytest.raises(NotBoolError):
        Gate(None, 1)


def test_MultiInputGate_create_invalid_type():
    D0 = FlipFlop(None)
    with pytest.raises(NotListError):
        MultiInputGate(D0)


def test_MultiInputGate_create_invalid_input_number():
    D0 = FlipFlop(None)
    with pytest.raises(InvalidInputNumber):
        MultiInputGate([D0])


def test_NOT_create_invalid():
    inputs = [FlipFlop(None, True, True), FlipFlop(None)]
    with pytest.raises(NotFlipFlopError):
        NOT(inputs)


def test_NOT_calculate():
    D1 = FlipFlop(None, True, True)
    D2 = FlipFlop(None)
    G1 = NOT(D1)
    G2 = NOT(D2)
    assert not G1.calculate()
    assert G2.calculate()


def test_NOT_update():
    D1 = FlipFlop(None)
    G1 = NOT(D1)
    assert not G1.output()
    G1.update_output()
    assert G1.output()


def test_AND_calculate():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G0 = AND([D0, D0])
    G1 = AND([D0, D1])
    G2 = AND([D1, D1])
    assert not G0.calculate()
    assert not G1.calculate()
    assert G2.calculate()


def test_AND_update():
    D0 = FlipFlop(None, True, True)
    D1 = FlipFlop(None, True, True)
    G1 = AND([D0, D1], False)
    assert not G1.output()
    G1.update_output()
    assert G1.output()


def test_OR_calculate():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G0 = OR([D0, D0])
    G1 = OR([D0, D1])
    G2 = OR([D1, D1])
    assert not G0.calculate()
    assert G1.calculate()
    assert G2.calculate()


def test_OR_update():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G1 = OR([D0, D1], False)
    assert not G1.output()
    G1.update_output()
    assert G1.output()


def test_XOR_calculate():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G0 = XOR([D0, D0])
    G1 = XOR([D0, D1])
    G2 = XOR([D1, D1])
    assert not G0.calculate()
    assert G1.calculate()
    assert not G2.calculate()


def test_XOR_update():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G1 = XOR([D0, D1], False)
    assert not G1.output()
    G1.update_output()
    assert G1.output()


def test_NAND_calculate():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G0 = NAND([D0, D0])
    G1 = NAND([D0, D1])
    G2 = NAND([D1, D1])
    assert G0.calculate()
    assert G1.calculate()
    assert not G2.calculate()


def test_NAND_update():
    D0 = FlipFlop(None, True, True)
    D1 = FlipFlop(None, True, True)
    G1 = NAND([D0, D1], True)
    assert G1.output()
    G1.update_output()
    assert not G1.output()


def test_NOR_calculate():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G0 = NOR([D0, D0])
    G1 = NOR([D0, D1])
    G2 = NOR([D1, D1])
    assert G0.calculate()
    assert not G1.calculate()
    assert not G2.calculate()


def test_NOR_update():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None)
    G1 = NOR([D0, D1], False)
    assert not G1.output()
    G1.update_output()
    assert G1.output()


def test_XNOR_calculate():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None, True, True)
    G0 = XNOR([D0, D0])
    G1 = XNOR([D0, D1])
    G2 = XNOR([D1, D1])
    assert G0.calculate()
    assert not G1.calculate()
    assert G2.calculate()


def test_XNOR_update():
    D0 = FlipFlop(None)
    D1 = FlipFlop(None)
    G1 = XNOR([D0, D1], False)
    assert not G1.output()
    G1.update_output()
    assert G1.output()
