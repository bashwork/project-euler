def fib():
    a,b,c = 0,1,0
    while c < 4000000:
       c = a + b
       a,b = b,c
       if c % 2 == 0: yield c
print sum(fib()) 
