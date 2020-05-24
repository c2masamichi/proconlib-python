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


def count_div(x, mod):
    cnt = 0
    r = 0
    while r == 0:
        x, r = divmod(x, mod)
        if r == 0:
            cnt += 1

    return cnt
