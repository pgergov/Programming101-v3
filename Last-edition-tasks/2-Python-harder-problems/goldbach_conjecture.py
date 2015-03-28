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

def goldbach(n):
    prime_list = []
    result = []
    for i in range(2,n):
        if is_prime(i):
            prime_list.append(i)
    for numb1 in prime_list:
        if numb1 < n / 2 + 1:
            for numb2 in prime_list:
                if numb1 + numb2 <= n:
                    if numb1 + numb2 == n:
                        right_combo = (numb1, numb2)
                        result.append(right_combo)
                else:
                    break
    return result

print(goldbach(100))
