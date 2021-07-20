import math
import random
import time

from . import actions
from .calendar import Calendar
from .caller import Caller


class Simulation:
    def __init__(self, seed=None):
        self.seed = time.time() if seed is None else seed
        self.rng = random.Random(self.seed)
        self.calendar = Calendar()

    @property
    def time(self):
        return self.calendar.time

    def run(self, dt=math.inf):
        return self.calendar.run(dt)

    def step(self, n=1):
        return self.calendar.step(n)

    def launch(self, action):
        action = actions.coerce(action)
        action.start(self)
        return action

    def launcher(self, func, *args, **kwargs):
        return self.caller(lambda: self.launch(func(*args, **kwargs)))

    def caller(self, func, *args, **kwargs):
        return Caller(self, func, *args, **kwargs)
