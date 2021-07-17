import bisect
import collections
import math

from .action import ActionState
from .delay import Delay


class Calendar:
    def __init__(self):
        self.events = collections.deque()
        self.keys = {}
        self.time = 0

    def add(self, delay):
        key = (self.time + delay.duration, delay.priority, delay.id)
        self.keys[delay] = key
        bisect.insort_right(self.events, (key, delay))

    def remove(self, delay):
        if delay.calendar is not self:
            return
        index = bisect.bisect_left(self.events, (key, None))
        delay_key, delay = self.events[index]
        if delay_key == key:
            del self.events[index]

    def step(self):
        key, delay = self.events.popleft()
        delay.state = ActionState.PENDING
        delay.complete()

    def run(self, n=math.inf):
        i = 0
        while i < n:
            self.step()
            i += 1

    def run_until(self, t):
        delay = Delay(t - self.time)
        delay.on_success(self.stop)
        self.add(delay)
