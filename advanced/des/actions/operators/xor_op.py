from .nary_op import NaryOperator


class Xor(NaryOperator):
    def _setup(self, operand):
        operand.on_complete(self._check)
        operand.on_fail(self._check)

    def _check(self):
        n_completed = 0
        for operand in self.operands:
            if operand.is_completed:
                n_completed += 1
                if n_completed > 1:
                    self.fail()
                    break
            elif not operand.is_failed:
                return
        self.complete()
