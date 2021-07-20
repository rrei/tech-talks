import types

from .action import Action
from .delay import Delay
from .operators import *
from .process import Process


# from .request import Request


def coerce(val):
    if val is None:
        return Action()
    if isinstance(val, Action):
        return val
    if isinstance(val, types.GeneratorType):
        return Process(val)
    if isinstance(val, (int, float)):
        return Delay(val)
    raise TypeError(f"unable to coerce {val!r} to action")


def __and__(self, other):
    return And(self, other)


def __rand__(self, other):
    return And(other, self)


def __or__(self, other):
    return Or(self, other)


def __ror__(self, other):
    return Or(other, self)


def __xor__(self, other):
    return Xor(self, other)


def __rxor__(self, other):
    return Xor(other, self)


def __invert__(self):
    return Not(self)


Action.coerce = staticmethod(coerce)
Action.__and__ = __and__
Action.__rand__ = __rand__
Action.__or__ = __or__
Action.__ror__ = __ror__
Action.__xor__ = __xor__
Action.__rxor__ = __rxor__
Action.__invert__ = __invert__
