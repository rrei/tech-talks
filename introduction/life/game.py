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

    def tick(self):
        """Return a new state representing the next generation of this Game of Life.
        Note that this is done in one go for the whole grid, i.e. rules are applied
        simultaneously to all cells.
        """
        # First we collect a set of all points that might be alive in the next tick.
        # This includes all cells that are currently alive as well as their neighbors.
        points = set()
        for p in self:
            points.add(p)
            points.update(neighbors(p))
        # Now we make a new empty grid and populate it by evaluating the rules (using
        # the current state of the grid) on each of the points collected above.
        next = type(self)()
        for p in points:
            alive = p in self
            n_neighbors = sum(1 for n in neighbors(p) if n in self)
            if (alive and 2 <= n_neighbors <= 3) or (not alive and n_neighbors == 3):
                next.add(p)
        return next


def neighbors(p):
    """Generator of the eight neighbors of `p` (an `(x, y)` pair)."""
    x, y = p
    return (
        (x + dx, y + dy)
        for dx, dy in (
            (-1, -1),
            (-1, +0),
            (-1, +1),
            (+0, -1),
            (+0, +1),
            (+1, -1),
            (+1, +0),
            (+1, +1),
        )
    )
