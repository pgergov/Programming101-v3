def sum_of_digits(n):
    s = 0
    while n // 10 != 0:
        s += n % 10
        n = n // 10
    else:
        s += n
    return s
print(sum_of_digits(6))
