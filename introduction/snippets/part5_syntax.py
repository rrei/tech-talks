# assignment
x = 42  # regular
x += 1  # augmented
head, *tail = range(5, 15)  # unpacking
a = b = None  # chained

# boolean operations
p = False
q = True
not p or q

# bitwise operations
i = 42
i & (1 << 5)

# comparisons
x_min, x_max = 0, 100
x_min <= x <= x_max

# membership
10 in tail
head not in tail  # pythonic
not head in tail  # non-pythonic

# identity
a is None
x is not None  # pythonic
not x is None  # non-pythonic

# indexing and slicing
tail[0]
tail[-1]
tail[2:-2]

# ternary operator (?:)
y = "foo" if x is not None and x_min <= x <= x_max else "bar"

# deletion
del tail[-5:]

# f-strings
who = "world"
print(f"Hello {who.title()}! x is currently {x}")

# indentation-based blocks
if len(tail) == 4:
    tail.extend(reversed(tail))
    print(tail)

# truthyness and falsyness
falsy = None, 0, 0.0, "", (), [], {}, set()
all(bool(val) == False for val in falsy)

truthy = -1, 0.4, " ", (None,), [False], {"not": "empty"}, {0}
all(bool(val) == True for val in truthy)

# while, for, if-elif-else
i = 0
while i < 10:
    print(i)
    i += 1

for i in range(1, 33):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# break, continue
for n in range(2, 10):
    if n % 2 == 0:
        print(n, "is even")
        continue
    print(n, "is odd")
    if n == 7:
        print("pheeew, time for a break")
        break

# exceptions
try:
    y = x / (43 - x)
except ZeroDivisionError as error:
    y = "oops"
    raise RuntimeError("they came from... behind") from error
else:
    print("success!")
finally:
    print(y)

# assertions
assert head not in tail
assert x % 2 == 0, "x must be even"


# functions
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


# classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        print(math.hypot(dx, dy))


p0 = Point(0, 0)
p1 = Point(1, 1)
p0.distance_to(p1)

# imports
import math
from pprint import pprint as print
