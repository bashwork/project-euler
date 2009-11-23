def is_palindrome(input):
    z = str(input)
    return z == z[::-1]

def find_largest():
    a,b,m = 0,0,0
    for i in xrange(999, 100, -1):
        for j in xrange(i, 100, -1):
            x = i * j
            if is_palindrome(x) and x > m:
                a,b,m = i,j,x
    return (a, b, m)

print find_largest()

