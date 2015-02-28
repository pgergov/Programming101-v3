from is_prime import is_prime
def prime_factorization(n):
    primes = []
    i = 2
    while i <= n:
        if is_prime(i):
            primes.append(i)
        i += 1
        
    result = []

    for numb in primes:
        while n % numb == 0:
            result.append(numb)
            n /= numb
                
    return result
print(prime_factorization(1000))
