import bisect
import collections
import math
import random


class Action:
    def __init__(self, callback):
        self.callback = callback

    def success(self):
        self.callback()

    def cancel(self):
        pass


class Delay(Action):
    def __init__(self, duration, priority=0):
        super().__init__()
        self.duration = duration
        self.priority = priority


class Calendar:
    def __init__(self, rng=random):
        self.rng = rng
        self.events = collections.deque()
        self.time = 0

    def step(self):
        key, delay = self.events.popleft()
        delay.success()

    def run(self, n=math.inf):
        i = 0
        while i < n:
            self.step()
            i += 1

    def run_until(self, t):
        delay = Delay(t - self.time)
        delay.on_success(self.stop)
        self.add(delay)

    def add(self, delay):
        key = (self.time + delay.duration, delay.priority, self.rng.random())
        delay.on_cancel(self.remove, key)
        bisect.insort_right(self.events, (key, delay))
        return key

    def remove(self, key):
        index = bisect.bisect_left(self.events, (key, None))
        k, delay = self.events[index]
        assert k == key
        return delay
