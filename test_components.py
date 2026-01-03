from components import FlipFlop


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


test_FlipFlop_step()
