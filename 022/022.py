trans = lambda n: sum(ord(a) - 64 for a in n)
names = filter(lambda t: t not in '"', open("names.txt")
        .read()).split(',')
names.sort()
print sum(v*trans(n) for v,n in enumerate(names, 1))
