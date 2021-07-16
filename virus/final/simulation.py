import random
from .calendar import Calendar


class Simulation:
    def __init__(self, seed=None):
        self.calendar = Calendar()
        # self.channel = Channel()
        self.rng = random.Random()
        if seed is not None:
            self.rng.seed(seed)


s = Simulation()
