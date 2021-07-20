from ..action import Action


class Not(Action):
    def __init__(self, operand, simulation=None):
        super().__init__(simulation)
        self.operand = Action.coerce(operand)

    def _start(self):
        self.operand.on_complete(self.fail)
        self.operand.on_fail(self.complete)
        self.operand.start(self.simulation)

    def _end(self):
        if not self.operand.has_ended:
            self.operand.cancel()
