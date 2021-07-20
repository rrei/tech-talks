import functools
import itertools
from collections.abc import Iterable

from .actions import Process


class Caller:
    def __init__(self, simulation, func, *args, **kwargs):
        self.simulation = simulation
        self.target = functools.partial(func, *args, **kwargs)
        self.process = None

    def interval(self, span, *args, **kwargs):
        intervals = _intervals(self.simulation.rng, span, args, kwargs)
        return Process(generator=self._run(intervals), simulation=self.simulation)

    def _run(self, intervals):
        for interval in intervals:
            yield interval
            self.target()


def _intervals(rng, span, args, kwargs):
    # If `span` is a string, we use it to look up a method on the rng.
    if isinstance(span, str):
        return iter(functools.partial(getattr(rng, span), *args, **kwargs), None)
    # If `span` is a callable, we pass the rng as the first positional argument.
    if callable(span):
        return iter(functools.partial(span, rng, *args, **kwargs), None)
    # If `span` is an iterable (non-string, because we handled strings above),
    # we simply return it; otherwise we assume it is a number and repeat it forever.
    assert not args and not kwargs
    return span if isinstance(span, Iterable) else itertools.repeat(span)
