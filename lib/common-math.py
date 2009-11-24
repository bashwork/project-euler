import itertools

def get_primes():
    yield 2 # special case
    for value in itertools.count(3):
        if all(value % a for a in xrange(2, value)):
            yield value

def is_prime(input):
    if input == 1:
        return False
    return all(input % a for a in xrange(2,input))

def gcd(a,b):
    ''' using euclids algorithm '''
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a*b / gdc(a,b)

def factor(input, start=2):
    result = []
    while input != 1:
        while input % start == 0:
            input /= start
            result.append(start)
        start += 1
    return result

def factor_list(input):
    return [factor(a) for a in input]
