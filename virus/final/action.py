import collections
import enum


class ActionState(enum):
    PENDING = enum.auto()
    ONGOING = enum.auto()
    COMPLETED = enum.auto()
    FAILED = enum.auto()


class Action:
    State = ActionState  # set up alias to `ActionState`
    counter = 0  # instance counter to generate unique sequential ids

    def __init__(self):
        Action.counter += 1
        self.id = Action.counter
        self.state = ActionState.PENDING
        self.callbacks = collections.defaultdict(list)

    @property
    def is_pending(self):
        return self.state is ActionState.PENDING

    @property
    def is_ongoing(self):
        return self.state is ActionState.ONGOING

    @property
    def is_completed(self):
        return self.state is ActionState.COMPLETED

    @property
    def is_failed(self):
        return self.state is ActionState.FAILED

    def set_state(self, state):
        self.state = ActionState(state)
        for func, args, kwargs in self.callbacks[self.state]:
            func(*args, **kwargs)

    def add_callback(self, state, func, *args, **kwargs):
        self.callbacks[ActionState(state)].append((func, args, kwargs))

    def on_start(self, func, *args, **kwargs):
        self.add_callback(ActionState.ONGOING, func, *args, **kwargs)

    def on_stop(self, func, *args, **kwargs):
        self.add_callback(ActionState.PENDING, func, *args, **kwargs)

    def on_complete(self, func, *args, **kwargs):
        self.add_callback(ActionState.COMPLETED, func, *args, **kwargs)

    def on_fail(self, func, *args, **kwargs):
        self.add_callback(ActionState.FAILED, func, *args, **kwargs)

    def start(self, *args, **kwargs):
        assert self.is_pending
        self._start(*args, **kwargs)
        self.set_state(ActionState.ONGOING)

    def _start(self, *args, **kwargs):
        raise NotImplementedError()

    def stop(self):
        assert self.is_ongoing
        self._stop()
        self.set_state(ActionState.PENDING)

    def _stop(self):
        raise NotImplementedError()

    def complete(self):
        self._finish(ActionState.COMPLETED)

    def fail(self):
        self._finish(ActionState.FAILED)

    def _finish(self, state):
        assert state in (ActionState.COMPLETED, ActionState.FAILED)
        self.stop()
        self.set_state(state)
