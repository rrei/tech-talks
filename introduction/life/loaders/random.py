import itertools
import random

from ..game import Life


def load(x0, x1, y0, y1, p=0.25):
    """Create a new `Life` object with random living cells (with probability `p`)
    in the rectangular region defined by `(x0, x1, y0, y1)`.
    """
    return Life(
        point
        for point in itertools.product(range(x0, x1), range(y0, y1))
        if random.random() < p
    )
