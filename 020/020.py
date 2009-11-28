memoize = {}

def factorial(input):
    if memoize.has_key(input):
        return memoize[input]
    if input == 0: return 1
    memoize[input] = result = factorial(input - 1) * input
    return result

print sum(int(a) for a in str(factorial(100)))
