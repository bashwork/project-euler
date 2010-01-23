'''
9 and 8 cannot be prime because
>>> any(a for a in [9,8] if (sum(range(a)) % 3) != 0)
False
'''
import math
from itertools import permutations

def compose(n):
    result = 0
    for k,v in enumerate(n):
        result += v*10**k
    return result

def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return not any(n % y == 0 for y in xrange(3, int(math.sqrt(n)) + 1, 2))

def compute(n):
    for n in permutations(n):
        v = compose(n)
        if is_prime(v): yield v

print max(compute([7,6,5,4,3,2,1]))
