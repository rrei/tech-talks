import bisect
import collections
import math
import random
import typing


class Event(typing.NamedTuple):
    time: float
    random: float
    id: int
    delay: object


class Calendar:
    def __init__(self, rng=random):
        self.time = 0.0  # simulation time
        self.rng = rng  # used for primary tie breaker
        self.event_counter = 0  # used for secondary tie breaker
        self.event_sequence = collections.deque()  # [Event]
        self.event_mapping = {}  # {Delay: Event}

    def add(self, delay):
        assert delay.duration >= 0
        event = Event(
            time=self.time + delay.duration,
            random=self.rng.random(),
            id=self.event_counter,
            delay=delay,
        )
        bisect.insort_right(self.event_sequence, event)
        self.event_mapping[delay] = event
        self.event_counter += 1

    def remove(self, delay):
        event = self.event_mapping.pop(delay, None)
        if event is None:
            return
        index = bisect.bisect_left(self.event_sequence, event)
        assert self.event_sequence[index] is event
        del self.event_sequence[index]

    def run(self, dt=math.inf):
        end_time = self.time + dt
        while len(self.event_sequence) > 0:
            event = self.event_sequence[0]
            if event.time > end_time:
                break
            self._step()
        if not math.isinf(end_time):
            self.time = end_time

    def step(self, n=1):
        for _ in range(n):
            self._step()

    def _step(self):
        event = self.event_sequence.popleft()
        del self.event_mapping[event.delay]
        self.time = event.time
        event.delay.complete()
