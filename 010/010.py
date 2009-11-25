import itertools
import math

def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return not any(n % y == 0 for y in xrange(3, int(math.sqrt(n)) + 1, 2))

def get_primes():
    yield 2 # special case
    for value in xrange(3, 2000000, 2):
        if is_prime(value): yield value

print sum(get_primes())


