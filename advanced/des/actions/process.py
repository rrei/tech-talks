import functools
import types

from .action import Action


class ProcessFail(Exception):
    """Exception raised within a `Process`s generator function to cause it to fail."""


class ProcessActionFailed(Exception):
    """Exception automatically raised by a `Process` object and thrown into its
    generator function when the process' current action has failed.
    """


class ProcessGetSimulation(Action):
    """Action used exclusively within a `Process`s generator function to instruct the
    process to send the `Simulation` object into the generator. Note that this class
    simply implements an action that completes immediately on start, and the rest is
    handled by the `Process` class.
    """

    def _start(self):
        self.complete()


class Process(Action):
    Fail = ProcessFail
    ActionFailed = ProcessActionFailed
    GetSimulation = ProcessGetSimulation

    def __new__(cls, generator, simulation=None):
        if isinstance(generator, types.GeneratorType):
            return super().__new__(cls)

        @functools.wraps(generator)
        def wrapper(*args, **kwargs):
            return cls(generator(*args, **kwargs), simulation)

        return wrapper

    def __init__(self, generator, simulation=None):
        super().__init__(simulation)
        self.generator = generator
        self.action = None
        self.result = None

    def _start(self):
        self._step()

    def _end(self, state):
        if self.action is not None and not self.action.has_ended:
            self.action.cancel()

    def _step(self):
        try:
            if self.action is None or self.action.is_completed:
                value = self.generator.send(
                    self.simulation
                    if isinstance(self.action, ProcessGetSimulation)
                    else self.action
                )
            else:
                assert self.action.is_failed
                value = self.generator.throw(ProcessActionFailed(self.action))
        except StopIteration as stop:
            self.result = stop.value
            self.complete()
        except ProcessFail:
            self.fail()
        else:
            self.action = Action.coerce(value)
            self.action.on_complete(self._step)
            self.action.on_fail(self._step)
            self.action.start(self.simulation)
