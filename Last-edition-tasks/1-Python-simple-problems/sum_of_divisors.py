def sum_of_divisors(n):
    i = 1
    s = 0
    while i <= n:
        if n % i == 0:
            s += i
        i += 1
    return s

