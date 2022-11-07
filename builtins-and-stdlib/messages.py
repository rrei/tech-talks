import collections
import json
import math
import pathlib
import random
import typing


class Vector(typing.NamedTuple):
    """A barebones three-dimensional vector/point class."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y, self.z - other.z)

    @property
    def norm(self):
        """Euclidean vector norm."""
        return math.sqrt(sum(val * val for val in self))


def encode(text, noise_ratio=10):
    """Translate a given `text` message into a list of vectors and an character
    encoding map. The message data is mixed in with random noise and shuffled.
    """
    chars = set(text)
    encoding = {char: i for i, char in enumerate(chars)}
    payload = [
        Vector(x=col, y=row, z=encoding[char])
        for row, line in enumerate(text.splitlines(keepends=True))
        for col, char in enumerate(line)
    ]
    noise = [
        Vector(x=point.x, y=point.y, z=point.z + random.randint(1, noise_ratio))
        for point in payload
        for _ in range(noise_ratio)
    ]
    data = payload + noise
    random.shuffle(data)
    return data, encoding


def decode(data, encoding):
    """Reconstruct the original message text from `data` and `encoding`."""
    reverse_encoding = {code: char for char, code in encoding.items()}
    return "".join(
        reverse_encoding[point.z]
        for point in sorted(extract_payload(data), key=lambda p: (p.y, p.x))
    )


def dump(data, encoding, filepath):
    """Save the given `data` and `encoding` (i.e. an encoded message) to a JSON file."""
    with open(filepath, "wt") as ostream:
        json.dump({"data": data, "encoding": encoding}, ostream)


def load(filepath):
    """Load an encoded message (data + encoding) from a JSON file."""
    message = json.loads(pathlib.Path(filepath).read_text())
    return [Vector(*xyz) for xyz in message["data"]], message["encoding"]


def has_zero(data):
    """Determine if any point in `data` is a zero vector."""
    return any(p.x == p.y == p.z == 0 for p in data)


def check_noise_ratio(data, noise_ratio):
    """Verify whether the number of points in `data` for each (x, y) position is
    equal to `1 + noise_ratio`.
    """
    counts = collections.Counter((p.x, p.y) for p in data)
    return all(c == noise_ratio + 1 for c in counts.values())


def extract_payload(data):
    """Extract the subset of `data` corresponding to the vectors that actually
    represent characters in the original message.
    """
    grid = collections.defaultdict(list)
    for point in data:
        grid[point.x, point.y].append(point.z)
    return [Vector(x, y, min(zs)) for (x, y), zs in grid.items()]


def find_nearest_point(origin, payload):
    """Find the element in `payload` closest to `origin`."""
    return min(payload, key=lambda p: (p - origin).norm)


def get_checksum(payload):
    """Compute the checksum for the given `payload`."""
    return sum(math.prod(p) for p in payload) % len(payload)


def find_message(dirpath="./messages/"):
    """Find a valid message file in the given `dirpath`."""
    for filepath in pathlib.Path(dirpath).glob("*.json"):
        data, encoding = load(filepath)
        payload = extract_payload(data)
        if (
            not has_zero(data)
            and check_noise_ratio(data, 10)
            and find_nearest_point(Vector(10, 20, 30), payload) == Vector(10, 20, 47)
            and get_checksum(payload) == 12627
        ):
            return filepath, data, encoding
    raise LookupError(f"unable to find valid message file in {dirpath!r}")


def check_messages(dirpath="./messages/"):
    for filepath in pathlib.Path(dirpath).glob("*.json"):
        print(f"{filepath.name}:")
        data, encoding = load(filepath)
        payload = extract_payload(data)
        print("\thas_zero:", not has_zero(data))
        print("\tcheck_noise_ratio:", check_noise_ratio(data, 10))
        print(
            "\tfind_nearest_point:",
            find_nearest_point(Vector(10, 20, 30), payload) == Vector(10, 20, 47),
        )
        print("\tget_checksum:", get_checksum(payload) == 12627)
