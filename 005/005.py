def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

print reduce(lcm, range(1,20 + 1))

