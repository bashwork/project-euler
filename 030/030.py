
def get_base_array(n, b):
    '''
    given a number n and base b, return an
    array of each nueric element in that base

    >>> get_base_array(1234, 10)
    [1,2,3,4]
    '''
    r = []
    while n > 0:
        r.append(n % b)
        n /= b
    return r

def get_max_num(p):
    ''' Basically, we know that:

    1. 1*9**5 = 59049  (5 digits > 1)
    2. 2*9**5 = 118098 (6 digits > 2)
    9. 9*9**5 = 531441 (6 digits < 9)

    >>> get_max_num(5)
    354294 
    '''
    r,t,a = 0,0,9**p
    while r < len(str(t)):
        r,t = r + 1,t+a
    return t

def sum_of_power(p):
    '''
    given a power p, this returns an iterator for
    each number that equals the sum of its powers

    >>> sum_of_power(4)
    [1634, 8208, 9474]
    '''
    powers = [a**p for a in xrange(10)]
    for i in xrange(2, get_max_num(p)):
        if i == sum(powers[a] for a in get_base_array(i, 10)):
            yield i

print sum(sum_of_power(5))

