
memo = {}
def sequence(s=1):
    run = lambda n: 3*n + 1 if n & 0x01 else n/2
    while s < 1000000:
        c, a = 0, s
        while a != 1:
            if a in memo: c += memo[a]; break
            c, a = c + 1, run(a)
        yield (c, s)
        memo[s], s = c, s + 1
print max(sequence(), key=lambda a: a[0])
        

