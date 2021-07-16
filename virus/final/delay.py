from .action import Action


class Delay(Action):
    def __init__(self, duration, priority=0):
        super().__init__()
        self.duration = duration
        self.priority = priority
        self.calendar = None
        self.calendar_key = None

    def _start(self, calendar):
        self.calendar = calendar
        self.calendar_key = (calendar.time + self.duration, self.priority, self.id)
        self.calendar.add(self)

    def _stop(self):
        self.calendar.remove(self)
        self.calendar = None
