import psyco
psyco.full() # a little boost :D
import math

def get_triangles():
    s, c = 0, 1
    while True:
        s,c = s + c, c + 1
        yield s

def factor_count(input):
    result = 1
    for i in xrange(2,int(math.sqrt(input))):
        if input % i == 0: result += 1
    return result * 2

def get_answer(answer):
    for result in get_triangles():
        if factor_count(result) >= answer:
            yield result

print get_answer(500).next()
