import collections
import enum


class ActionState(enum.Enum):
    PENDING = enum.auto()
    STARTING = enum.auto()
    ONGOING = enum.auto()
    ENDING = enum.auto()
    COMPLETED = enum.auto()
    FAILED = enum.auto()
    CANCELED = enum.auto()

    def checker_property(self, attr):
        return property(lambda obj: getattr(obj, attr) is self)


class Action:
    State = ActionState  # set up alias to `ActionState`
    is_pending = ActionState.PENDING.checker_property("state")
    is_starting = ActionState.STARTING.checker_property("state")
    is_ongoing = ActionState.ONGOING.checker_property("state")
    is_ending = ActionState.ENDING.checker_property("state")
    is_completed = ActionState.COMPLETED.checker_property("state")
    is_failed = ActionState.FAILED.checker_property("state")
    is_canceled = ActionState.CANCELED.checker_property("state")

    def __init__(self, simulation=None):
        self.simulation = simulation
        self.state = ActionState.PENDING
        self.callbacks = collections.defaultdict(list)
        self.start_time = None
        self.end_time = None

    @property
    def elapsed_time(self):
        if self.end_time is None:
            return self.simulation.time - self.start_time
        return self.end_time - self.start_time

    @property
    def has_started(self):
        return self.start_time is not None

    @property
    def has_ended(self):
        return self.end_time is not None

    def on_complete(self, func, *args, **kwargs):
        self.callbacks[ActionState.COMPLETED].append((func, args, kwargs))

    def on_fail(self, func, *args, **kwargs):
        self.callbacks[ActionState.FAILED].append((func, args, kwargs))

    def start(self, simulation=None):
        assert not self.has_started
        if simulation is not None:
            self.simulation = simulation
        self.start_time = self.simulation.time
        self.state = ActionState.STARTING
        self._start()
        if self.state is ActionState.STARTING:
            self.state = ActionState.ONGOING

    def _start(self):
        pass

    def end(self, state):
        assert self.has_started and not self.has_ended
        self.end_time = self.simulation.time
        self.state = ActionState.ENDING
        self._end(state)
        self.state = state
        for func, args, kwargs in self.callbacks.get(state, ()):
            func(*args, **kwargs)

    def _end(self, state):
        pass

    def complete(self):
        self.end(ActionState.COMPLETED)

    def fail(self):
        self.end(ActionState.FAILED)

    def cancel(self):
        self.end(ActionState.CANCELED)
