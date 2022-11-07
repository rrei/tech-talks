import random


def argmax1(values):
    i_max = 0
    i = 1
    while i < len(values):
        if values[i] > values[i_max]:
            i_max = i
        i += 1
    return i_max


def argmax2(values):
    i_max = 0
    for i, value in enumerate(values):
        if value > values[i_max]:
            i_max = i
    return i_max


def argmax3(values):
    indices = range(len(values))
    return max(indices, key=lambda i: values[i])


def test():
    for _ in range(1000):
        sample = random.sample(range(1000), k=100)
        assert argmax1(sample) == argmax2(sample) == argmax3(sample)
