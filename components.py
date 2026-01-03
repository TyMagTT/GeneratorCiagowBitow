

class NotBoolError(TypeError):
    pass


class NotListError(TypeError):
    pass


class FlipFlop:
    """
    Synchronous D-type flip-flop,
    Contains attributes:

    :param input: logic gate or flip-flop output connecting to this input
    :type input: object

    :param stored: stored value
    :type stored: bool

    :param output: output value
    :type output: bool

    :param clock:
    :type clock: object
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

    def __str__(self):
        stored = self._stored
        output = self._output
        return f'I have {stored} stored and I am outputting {output}'


class Gate:
    """
    Class Gate,
    Contains attributes:

    :param input: input list of flip-flop outputs
    :type input: list of objects

    :param output: logic gate output
    :type output: bool

    :param enabled: enable working, defaults to False
    :type enabled: bool
    """
    def __init__(self, input, output, enabled=False):
        self._input = input
        self._output = output
        self._enabled = enabled

    def input(self):
        return self._input

    def output(self):
        return self._output

    def enabled(self):
        return self._enabled

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False


class NOT(Gate):
    """
    NOT gate, calculating one bool output based on a bool input
    when enabled
    """
    def calculate(self):
        return not self._input


class AND(Gate):
    """
    AND gate, calculating one bool output based on a list of inputs
    when enabled
    """
    def calculate(self):
        for input in self._input:
            if not input:
                return False
        return True


class OR(Gate):
    """
    OR gate, calculating one bool output based on a list of inputs
    when enabled
    """
    pass


class XOR(Gate):
    """
    XOR gate, calculating one bool output based on a list of inputs
    when enabled
    """
    pass


class NAND(Gate):
    """
    NAND gate, calculating one bool output based on a list of inputs
    when enabled
    """
    pass


class NOR(Gate):
    """
    NOR gate, calculating one bool output based on a list of inputs
    when enabled
    """
    pass


class NXOR(Gate):
    """
    NXOR gate, calculating one bool output based on a list of inputs
    when enabled
    """
    pass


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
        pass
