from errors import (
    NotBoolError,
    NotFlipFlopError,
    NotListError,
    InvalidInputNumber,
    NotDictError
)


class FlipFlop:
    """
    Synchronous D-type flip-flop,
    Contains attributes:

    :param input: logic gate or flip-flop output connecting to this input
    :type input: object

    :param stored: stored value, defaults to False
    :type stored: bool

    :param output: output value, defaults to False
    :type output: bool
    """
    def __init__(self, input, stored=False, output=False):
        self._input = input
        self._stored = stored
        self._output = output

    def set_input(self, new_input):
        if type(new_input) is not FlipFlop and not isinstance(new_input, Gate):
            raise TypeError()
        self._input = new_input

    def output(self):
        return self._output

    def store_value(self):
        self._stored = self._input.output()

    def update_output(self):
        self._output = self._stored


class Gate:
    """
    Logic gate,
    Contains attributes:

    :param input: input list of flip-flop outputs
    :type input: list of objects

    :param output: logic gate output, defaults to False
    :type output: bool
    """
    def __init__(self, input, output=False):
        self._input = input
        if type(output) is not bool:
            raise NotBoolError()
        self._output = output

    def output(self):
        return self._output


class MultiInputGate(Gate):
    """
    Logic gate with 2 or more inputs,
    Contains attributes:

    :param input: input list of flip-flop outputs (2 or more)
    :type input: list of objects

    :param output: logic gate output, defaults to False
    :type output: bool
    """
    def __init__(self, input, output=False):
        if type(input) is not list:
            raise NotListError()
        if len(input) < 2:
            raise InvalidInputNumber()
        super().__init__(input, output)

    def set_input(self, new_input):
        if type(new_input) is not list:
            raise NotListError()
        if len(new_input) < 2:
            raise InvalidInputNumber()
        self._input = new_input


class NOT(Gate):
    """
    NOT gate
    Contains attributes:

    :param input: flip-flop output connecting to this input
    :type input: object

    :param output: logic gate output, defaults to False
    :type output: bool
    """
    def __init__(self, input, output=False):
        if type(input) is not FlipFlop:
            raise NotFlipFlopError()
        super().__init__(input, output)

    def set_input(self, new_input):
        if type(new_input) is not FlipFlop:
            raise NotFlipFlopError()
        self._input = new_input

    def calculate(self):
        return not self._input.output()

    def update_output(self):
        self._output = self.calculate()


class AND(MultiInputGate):
    """
    AND gate
    Contains attributes:

    :param input: list of flip-flop outputs connecting to this input
    :type input: list of objects

    :param output: logic gate output
    :type output: bool
    """
    def __init__(self, input, output=False):
        super().__init__(input, output)

    def calculate(self):
        for input in self._input:
            if not input.output():
                return False
        return True

    def update_output(self):
        self._output = self.calculate()


class OR(MultiInputGate):
    """
    OR gate
    Contains attributes:

    :param input: list of flip-flop outputs connecting to this input
    :type input: list of objects

    :param output: logic gate output
    :type output: bool
    """
    def __init__(self, input, output=False):
        super().__init__(input, output)

    def calculate(self):
        for input in self._input:
            if input.output():
                return True
        return False

    def update_output(self):
        self._output = self.calculate()


class XOR(MultiInputGate):
    """
    XOR gate
    Contains attributes:

    :param input: list of flip-flop outputs connecting to this input
    :type input: list of objects

    :param output: logic gate output
    :type output: bool
    """
    def __init__(self, input, output=False):
        super().__init__(input, output)

    def calculate(self):
        true_counter = 0
        for input in self._input:
            if input.output():
                true_counter += 1
        return true_counter % 2 == 1

    def update_output(self):
        self._output = self.calculate()


class NAND(MultiInputGate):
    """
    NAND gate
    Contains attributes:

    :param input: list of flip-flop outputs connecting to this input
    :type input: list of objects

    :param output: logic gate output
    :type output: bool
    """
    def __init__(self, input, output=False):
        super().__init__(input, output)

    def calculate(self):
        for input in self._input:
            if not input.output():
                return True
        return False

    def update_output(self):
        self._output = self.calculate()


class NOR(MultiInputGate):
    """
    NOR gate
    Contains attributes:

    :param input: list of flip-flop outputs connecting to this input
    :type input: list of objects

    :param output: logic gate output
    :type output: bool
    """
    def __init__(self, input, output=False):
        super().__init__(input, output)

    def calculate(self):
        for input in self._input:
            if input.output():
                return False
        return True

    def update_output(self):
        self._output = self.calculate()


class XNOR(MultiInputGate):
    """
    XNOR gate
    Contains attributes:

    :param input: list of flip-flop outputs connecting to this input
    :type input: list of objects

    :param output: logic gate output
    :type output: bool
    """
    def __init__(self, input, output=False):
        super().__init__(input, output)

    def calculate(self):
        true_counter = 0
        for input in self._input:
            if input.output():
                true_counter += 1
        return true_counter % 2 == 0

    def update_output(self):
        self._output = self.calculate()


class Register:
    """
    Register storing all flip-flop and gate objects
    and connections between them
    Contains attributes:

    :param flipflops: flipflop objects in the register
    :type flipflops: dict

    :param gates: gate objects in the register
    :type gates: dict
    """
    def __init__(self, flipflops, gates):
        if type(flipflops) is not dict:
            raise NotDictError
        if type(gates) is not dict:
            raise NotDictError
        self.flipflops = flipflops
        self.gates = gates

    def set_value(self, id, new_value):
        if type(new_value) is not bool:
            raise NotBoolError()
        self.flipflops[id]._output = new_value

    def output(self, id):
        return self.flipflops[id].output()

    def step(self):
        # 1. update gates
        # 2. store flipflop values
        # 3. update flipflops
        for gate in self.gates.values():
            gate.update_output()
        for flipflop in self.flipflops.values():
            flipflop.store_value()
        for flipflop in self.flipflops.values():
            flipflop.update_output()
