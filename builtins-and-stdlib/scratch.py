import json
import random


class Vector:
    """A barebones three-dimensional vector/point class."""


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


def dump(data, encoding, filepath):
    """Save the given `data` and `encoding` (i.e. an encoded message) to a JSON file."""
    with open(filepath, "wt") as ostream:
        json.dump({"data": data, "encoding": encoding}, ostream)


def load(filepath):
    """Load an encoded message (data + encoding) from a JSON file."""


def find_message(dirpath="./messages/"):
    """Find a valid message file in the given `dirpath`."""


def has_zero(data):
    """Determine if any point in `data` is a zero vector."""


def check_noise_ratio(data, noise_ratio):
    """Verify whether the number of points in `data` for each (x, y) position is
    equal to `1 + noise_ratio`.
    """


def extract_payload(data):
    """Extract the subset of `data` corresponding to the vectors that actually
    represent characters in the original message.
    """


def find_nearest_point(origin, payload):
    """Find the element in `payload` closest to `origin`."""


def get_checksum(payload):
    """Compute the checksum for the given `payload`."""


def decode(data, encoding):
    """Reconstruct the original message text from `data` and `encoding`."""
