import math
import random
import time

from . import actions
from .calendar import Calendar


class Simulation:
    def __init__(self, seed=None):
        self.seed = time.time() if seed is None else seed
        self.rng = random.Random(self.seed)
        self.calendar = Calendar()

    @property
    def time(self):
        return self.calendar.time

    def launch(self, action):
        action = actions.coerce(action)
        action.start(self)
        return action

    def run(self, dt=math.inf):
        return self.calendar.run(dt)

    def step(self, n=1):
        return self.calendar.step(n)
