class Life(set):
    """A very simple set-based implementation of Conway's Game of Life (see
    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). The set contains only
    living cells, represented as `(x, y)` pairs. By subclassing `set` we get several
    things for free:

        for p in life:  # iteration over living cells
        len(life)  # number of living cells
        p in life  # checking the state of a cell
        life.add(p)  # setting a cell as alive
    """

    def __repr__(self):
        ...

    def repr(self, rect=None, alive="#", dead="."):
        """Build a string representation of the rectangular region defined by `rect`
        (a 4-tuple `(x0, x1, y0, y1)`) using symbols `alive` and `dead`. If omitted,
        `rect` defaults to the result of `.bbox()`.
        """
        ...

    def bbox(self):
        """Compute and return the (tightest) rectangular bounding box of all living
        cells in this grid as a 4-tuple `(x0, x1, y0, y1)`.
        """
        ...

    def tick(self):
        """Return a new state representing the next generation of this Game of Life.
        Note that this is done in one go for the whole grid, i.e. rules are applied
        simultaneously to all cells.
        """
        ...


def neighbors(p):
    """Generator of the eight neighbors of `p` (an `(x, y)` pair)."""
    ...
