#!python
import curses
import itertools
import random
import shutil
import sys
import time

# Symbols used to represent alive/dead cells in the terminal.
# NOTE: make them 2 characters wide to approximate square shape.
ALIVE = "\u2593" * 2
DEAD = "\u2591" * 2

# This constant represents the deltas `(dx, dy)` for each of the eight neighbors
# of a cell. Since we're wrapping coordinates, all cells will have exactly eight
# neighbors.
NEIGHBOR_DELTAS = (
    (-1, -1),
    (-1, +0),
    (-1, +1),
    (+0, -1),
    (+0, +1),
    (+1, -1),
    (+1, +0),
    (+1, +1),
)


class InfiniteGrid(set):
    def __getitem__(self, coords):
        return coords in self

    def __setitem__(self, coords, alive):
        if alive:
            self.add(coords)
        else:
            self.discard(coords)

    def neighbors(self, coords):
        x, y = coords
        return ((x + dx, y + dy) for dx, dy in NEIGHBOR_DELTAS)

    def as_string(self, x_min=None, x_max=None, y_min=None, y_max=None):
        grid = []
        for y in range(y_min, y_max):
            row = []
            for x in range(x_min, x_max):
                row.append(ALIVE if (x, y) in self else DEAD)
            grid.append("".join(row))
        return "\n".join(grid)


class FiniteGrid:
    def __init__(self, n_rows, n_cols, wrap_x=False, wrap_y=False):

        self.range_x = range(0, n_cols)
        self.range_y = range(0, n_rows)
        self.wrap_x = wrap_x
        self.wrap_y = wrap_y
        self.cells = [[False for _ in range(n_cols)] for _ in range(n_rows)]

    def __getitem__(self, coords):
        x, y = coords
        return self.cells[y][x]

    def __setitem__(self, coords, alive):
        x, y = coords
        self.cells[y][x] = alive

    def normalized(self, coords):
        x, y = coords
        if self.wrap_x:
            x %= self.x_range.min
        if self.wrap_y:
            y %= self.n_rows
        if 0 <= x <= self.n_cols and 0 <= y <= self.n_rows:
            return x, y
        raise ValueError(f"coordinates {(x, y)} are out of bounds")

    def neighbors(self, coords):
        x, y = coords
        for dx, dy in NEIGHBOR_DELTAS:
            try:
                xn, yn = self.normalized(x + dx, y + dy)
            except ValueError:
                continue

            if not (self.wrap_x or 0 <= xn <= self.n_cols) or not (
                self.wrap_y or 0 <= yn <= self.n_rows
            ):
                continue


class Life:
    def __init__(self, grid):
        self.grid = grid
        self.generation = 0

    def __str__(self):
        return self.grid.as_string()

    def __repr__(self):
        n_alive = sum(sum(row) for row in self.grid)
        return (
            f"<{type(self).__name__}"
            f" {self.n_rows}x{self.n_cols} cells"
            f" ({n_alive} alive), generation #{self.generation}>"
        )

    def __getitem__(self, coords):
        """Implement subscripting magic method with wrapping on both axes."""
        x, y = coords
        return self.grid[y % self.n_rows][x % self.n_cols]

    def randomize(self, p=0.25):
        for row in self.grid:
            for x in range(self.n_cols):
                row[x] = bool(random.random() < p)
        self.generation = 0

    def tick(self):
        """Simulate one tick by replacing the current grid w/ a new grid representing
        the next generation of this game of life. Note that this is done in one go
        for the whole grid, i.e. rules are applied simultaneously to all cells.
        """
        points = set()
        for point in self.grid:
            points.add(point)
            points.update(self.grid.neighbors(point))

        grid = self.grid.copy()
        for p in points:
            alive = p in self.grid
            n_neighbors = sum(n in self.grid for n in self.grid.neighbors(p))
            grid[p] = (alive and 2 <= n_neighbors <= 3) or (
                not alive and n_neighbors == 3
            )
        self.grid = grid
        self.generation += 1

    def run(self):
        return curses.wrapper(self._run)

    def _run(self, stdscr):
        stdscr.nodelay(True)
        paused = False
        interval = 4
        for i in itertools.count():
            time.sleep(0.25)
            if not paused and i % interval == 0:
                self.tick()
            stdscr.clear()
            stdscr.addstr(f"{self!r} @ {1.0 / (0.25 * interval)}Hz")
            if paused:
                stdscr.addstr(" PAUSED")
            stdscr.addstr(f"\n{self}\n")
            stdscr.addstr("(p)ause (s)lower (f)aster (t)ick (r)andomize (q)uit")
            stdscr.refresh()
            try:
                key = stdscr.getkey()
            except curses.error:
                continue
            if key == "p":
                paused = not paused
            elif key == "s":
                interval = min(16, interval * 2)
            elif key == "f":
                interval = max(1, interval / 2)
            elif key == "t":
                self.tick()
            elif key == "r":
                self.randomize()
            elif key == "q":
                return


class TextUI:
    def __init__(self, refresh_rate=1):
        self.running = False
        self.screen = None
        self.refresh_rate = refresh_rate

    def run(self):
        return curses.wrapper(self.mainloop)

    def mainloop(self, stdscr):
        assert not self.running
        self.running = True
        self.screen = stdscr
        stdscr.nodelay(True)
        while self.running:
            time.sleep(1 / self.refresh_rate)
            stdscr.clear()
            self.draw(stdscr)
            stdscr.refresh()
            try:
                key = stdscr.getkey()
            except curses.error:
                continue
            self.input(stdscr, key)
        self.screen = None

    def draw(self, stdscr):
        pass

    def input(self, stdscr, key):
        pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        term_size = shutil.get_terminal_size()
        n_rows = term_size.lines - 2  # subtract 2 lines for status and controls
        n_cols = (term_size.columns - 1) // 2  # because each cell is 2-characters long
    elif len(sys.argv) == 3:
        n_rows, n_cols = map(int, sys.argv[1:])
    else:
        print(f"Usage: {sys.argv[0]} [n_rows ncols]")
        sys.exit(1)
    life = Life(n_rows, n_cols)
    life.randomize()
    life.run()
    sys.exit(0)
