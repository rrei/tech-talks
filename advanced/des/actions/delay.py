from .action import Action


class Delay(Action):
    def __init__(self, duration, simulation=None):
        super().__init__(simulation)
        self.duration = duration

    def _start(self):
        self.simulation.calendar.add(self)

    def _end(self, state):
        self.simulation.calendar.remove(self)
