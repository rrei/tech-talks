import curses
import statistics

from .base import TextUI

# Symbols used to represent alive/dead cells in the terminal.
# NOTE: make them 2 characters wide to approximate square shape.
ALIVE = "\u2593" * 2
DEAD = "\u2591" * 2


# Lines displayed at the bottom of the screen to let the user know the controls.
CONTROLS = (
    "(p)ause (s)lower (f)aster (t)ick (r)eset (q)uit",
    "(c)enter [arrow keys to scroll]",
)


class LifeTextUI(TextUI):
    def __init__(self, life, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_count = 0
        self.initial_life = life
        self.life = life
        self.generation = 0
        self.x, self.y = 0, 0

    def tick(self):
        self.life = self.life.tick()
        self.generation += 1
        if self.is_paused:
            self._draw()

    def reset(self):
        self.pause()
        self.life = self.initial_life
        self.generation = 0
        self.center_viewport()
        self._draw()

    def viewport(self):
        """Returns a 4-tuple `(x0, x1, y0, y1)` containing the coordinates of the
        currently visible region in our grid.
        """
        curses.update_lines_cols()
        width = (curses.COLS - 1) // 2  # cells are 2-char wide and -1 for line break
        height = curses.LINES - 3  # -1 for header and -2 for controls
        x0 = self.x - width // 2
        x1 = x0 + width
        y0 = self.y - height // 2
        y1 = y0 + height
        return x0, x1, y0, y1

    def scroll_viewport(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        if self.is_paused:
            self._draw()

    def center_viewport(self):
        if len(self.life) == 0:
            self.x = self.y = 0
        else:
            self.x = int(statistics.mean(x for x, _ in self.life))
            self.y = int(statistics.mean(y for _, y in self.life))
        if self.is_paused:
            self._draw()

    def adjust_refresh_rate(self, delta):
        self.refresh_rate = max(1, self.refresh_rate + delta)
        if self.is_paused:
            self._draw()

    def draw(self):
        if self.frame_count == 0:
            self.center_viewport()
            self._draw()
        elif self.frame_count % 10 == 0:
            self.tick()
            self._draw()
        self.frame_count += 1

    def _draw(self):
        x0, x1, y0, y1 = self.viewport()
        self.screen.clear()
        self.screen.addstr(
            f"x={self.x}  y={self.y}  "
            f"generation={self.generation}  alive={len(self.life)}  "
            f"{self.state.name}@{self.refresh_rate / 10:.02f}Hz\n"
        )
        for y in range(y0, y1):
            for x in range(x0, x1):
                self.screen.addstr(ALIVE if (x, y) in self.life else DEAD)
            self.screen.addstr("\n")
        self.screen.addstr("\n".join(line.center(curses.COLS - 1) for line in CONTROLS))
        self.screen.refresh()

    def input(self, key):
        if key == "KEY_DOWN":
            self.scroll_viewport(dy=+1)
        elif key == "KEY_UP":
            self.scroll_viewport(dy=-1)
        elif key == "KEY_RIGHT":
            self.scroll_viewport(dx=+1)
        elif key == "KEY_LEFT":
            self.scroll_viewport(dx=-1)
        elif key == "c":
            self.center_viewport()
        elif key == "p":
            self.pause() if self.is_running else self.unpause()
            self._draw()
        elif key == "s":
            self.adjust_refresh_rate(-1)
        elif key == "f":
            self.adjust_refresh_rate(+1)
        elif key == "t":
            self.tick()
        elif key == "r":
            self.reset()
        elif key == "q":
            self.stop()
