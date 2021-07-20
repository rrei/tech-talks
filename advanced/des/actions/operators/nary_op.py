from ..action import Action


class NaryOperator(Action):
    def __init__(self, *operands, simulation=None):
        super().__init__(simulation)
        self.operands = tuple(map(Action.coerce, operands))

    def _start(self):
        for operand in self.operands:
            self._setup(operand)
            operand.start(self.simulation)
            if self.has_ended:
                break

    def _end(self, state):
        for operand in self.operands:
            if operand.has_started and not operand.has_ended:
                operand.cancel()

    def _setup(self, operand):
        raise NotImplementedError()
