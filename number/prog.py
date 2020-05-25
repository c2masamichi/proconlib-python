def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def make_factors(x, mod):
    cnt = 0
    r = 0
    while r == 0:
        x, r = divmod(x, mod)
        if r == 0:
            cnt += 1

    return cnt


def make_divisors(x):
    divisor = [1, x]
    i = 2
    while i * i <= x:
        q, r = divmod(x, i)
        if r == 0:
            divisor.append(i)
            divisor.append(q)
        i += 1
    return sorted(divisor)
