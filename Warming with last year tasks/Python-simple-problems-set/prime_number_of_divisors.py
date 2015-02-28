from is_prime import is_prime
def prime_number_of_divisors(n):
    i = 1
    s = 0
    while i <= n:
        if n % i == 0:
            s += 1
        i += 1
    if is_prime(s):
        return True
    else:
        return False
print(prime_number_of_divisors(9))
    
