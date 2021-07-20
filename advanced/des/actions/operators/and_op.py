from .nary_op import NaryOperator


class And(NaryOperator):
    def _setup(self, operand):
        operand.on_complete(self._check)
        operand.on_fail(self.fail)

    def _check(self):
        if all(operand.is_completed for operand in self.operands):
            self.complete()
