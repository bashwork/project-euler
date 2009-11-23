def gcd(input, start=2):
    while input != start:
        while input % start == 0:
            input /= start
        if input == 1: break
        start += 1
    return start

print gcd(600851475143)
