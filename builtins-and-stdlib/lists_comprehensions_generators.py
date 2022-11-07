import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for m in range(3, int(math.sqrt(n)), 2):
        if n % m == 0:
            return False
    return True


def primes_list(upper_bound):
    primes = []
    for n in range(2, upper_bound):
        if is_prime(n):
            primes.append(n)
    return primes


def primes_listcomp(upper_bound):
    return [n for n in range(2, upper_bound) if is_prime(n)]


def primes_gen(upper_bound):
    for n in range(2, upper_bound):
        if is_prime(n):
            yield n


def primes_genexpr(upper_bound):
    return (n for n in range(2, upper_bound) if is_prime(n))
