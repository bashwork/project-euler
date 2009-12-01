#--------------------------------------------------------------------#
# manually
#--------------------------------------------------------------------#
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def is_leap(n):
    return (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0)

def harder():
    c, w = 0, 2 # 1/1/01 := tuesday
    for y in xrange(1901, 2001):
        l = is_leap(y)
        for m in xrange(0, 12):
            c += (w == 0) # sunday 
            d  = 28 if m == 1 and l else months[m]
            w  = (w + d) % 7 
    return c

print harder()

##--------------------------------------------------------------------#
# using stdlib
#--------------------------------------------------------------------#
import datetime

print sum(1 for y in xrange(1901, 2001) for m in xrange(1,13)
            if datetime.datetime(y,m,1).weekday() == 6)
