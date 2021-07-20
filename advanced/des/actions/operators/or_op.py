from .nary_op import NaryOperator


class Or(NaryOperator):
    def _setup(self, operand):
        operand.on_complete(self.complete)
        operand.on_fail(self._check)

    def _check(self):
        if all(operand.is_failed for operand in self.operands):
            self.fail()
