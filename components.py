class InvalidInputNumber(Exception):
    pass


class NotListError(TypeError):
    pass


class NotFlipFlopError(TypeError):
    pass


class NotBoolError(TypeError):
    pass


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

    def value(self):
        return self._output

    def store_value(self):
        self._stored = self._input.value()

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
            raise NotFlipFlopError
        super().__init__(input, output)

    def calculate(self):
        return not self._input.value()

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
            if not input.value():
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
            if input.value():
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
            if input.value():
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
            if not input.value():
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
            if input.value():
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
            if input.value():
                true_counter += 1
        return true_counter % 2 == 0

    def update_output(self):
        self._output = self.calculate()


class Register:
    """
    Register storing all flip-flop and gate objects
    and connections between them
    """
    def __init__(self):
        pass

    def connect(self, first, second):
        """
        Connect function, simulates a connection between parts
        Contains attributes:

        :param first: object which output is to be connected
        :type first: object

        :param second: object which input is to be connected
        :type second: object
        """
        pass

    def disconnect(self, first, second):
        """
        Connect function, removes a connection between parts
        Contains attributes:

        :param first: object which output is to be disconnected
        :type first: object

        :param second: object which input is to be disconnected
        :type second: object
        """
        pass

    def next_step(self):
        # 1. update gates
        # 2. store flipflop values
        # 3. update flipflops
        pass
