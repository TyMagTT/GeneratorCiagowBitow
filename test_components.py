from components import FlipFlop


def test_FlipFlop_create():
    D1 = FlipFlop(None, True)
    D2 = FlipFlop(D1, False)
    D3 = FlipFlop(D2, False)
    D1._input = D3

    assert D1.value()
    assert not D2.value()
    assert not D3.value()


def test_FlipFlop_step():
    D1 = FlipFlop(None, True)
    D2 = FlipFlop(D1, False)
    D3 = FlipFlop(D2, False)
    D1._input = D3

    D1.step()
    D2.step()
    D3.step()

    assert not D1.value()
    assert D2.value()
    assert not D3.value()
