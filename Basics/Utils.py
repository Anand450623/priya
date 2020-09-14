def generator():
    i = 0
    for i in range(100):
        yield i
        i += 1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
