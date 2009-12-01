f = lambda a: 1 if a == 0 else a * f(a-1)
c = lambda a,b: f(a) / (f(b) * f(a-b))
print c(20 + 20, 20)
