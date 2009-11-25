import sys

def generate_sum(input):
    for m in xrange(2, input):
        for n in xrange(2, input):
            v = (m**2 - n**2, 2*m*n, m**2 + n**2)
            if (sum(v) == input) and all(i > 0 for i in v):
                return v, reduce(lambda t,n: t * n, v)

print generate_sum(1000)
                
