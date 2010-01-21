def reverse(num, base):
    result = 0
    while num > 0:
        result = (result*base) + (num % base)
        num  /= base
    return result

def is_palindrome(n):
  return (n == reverse(n, 2) and n == reverse(n,10))

print sum(n for n in xrange(1000000) if is_palindrome(n))
