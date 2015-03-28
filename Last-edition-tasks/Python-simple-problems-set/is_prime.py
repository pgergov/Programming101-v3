def is_prime(n):
    start = 2
    is_prime = True
    if n == 1 or n < 0:
        is_prime = False
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1   
    return is_prime
