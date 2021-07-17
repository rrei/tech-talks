import curses
import enum
import time


class TextUIState(enum.Enum):
    RUNNING = enum.auto()
    PAUSED = enum.auto()
    STOPPED = enum.auto()

    def checker_property(self, attr):
        return property(lambda obj: getattr(obj, attr) is self)


class TextUI:
    State = TextUIState
    is_running = State.RUNNING.checker_property("state")
    is_paused = State.PAUSED.checker_property("state")
    is_stopped = State.STOPPED.checker_property("state")

    def __init__(self, refresh_rate=30):
        self.state = TextUIState.STOPPED
        self.screen = None
        self.refresh_rate = refresh_rate

    def start(self, paused=False):
        assert self.is_stopped
        assert self.screen is None
        self.state = TextUIState.PAUSED if paused else TextUIState.RUNNING
        return curses.wrapper(self.mainloop)

    def pause(self):
        assert not self.is_stopped
        self.state = TextUIState.PAUSED

    def unpause(self):
        assert not self.is_stopped
        self.state = TextUIState.RUNNING

    def stop(self):
        self.state = TextUIState.STOPPED

    def mainloop(self, stdscr):
        self.screen = stdscr
        self.screen.nodelay(True)
        self.draw()
        while not self.is_stopped:
            time.sleep(1 / self.refresh_rate)
            if self.is_running:
                self.draw()
            while True:
                try:
                    key = self.screen.getkey()
                except curses.error:
                    break
                self.input(key)
        self.screen = None

    def draw(self):
        raise NotImplementedError()

    def input(self, key):
        raise NotImplementedError()
