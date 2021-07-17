import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y})"

    def __iter__(self):
        return iter((self.x, self.y))

    def __neg__(self):
        return type(self)(-self.x, -self.y)

    def __add__(self, p):
        px, py = p
        return type(self)(self.x + px, self.y + py)

    def __sub__(self, p):
        return self + (-p)

    def norm(self):
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        return (self - p).norm()


p0 = Point(1, 1)
p1 = Point(4, 5)
p0.distance_to(p1)
