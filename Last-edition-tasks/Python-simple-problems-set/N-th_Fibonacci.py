def nth_fibonacci(n):
    fib = [1, 1]
    s = 0
    i = 1
    if n > 2:
        while i < n:
            s = fib[i-1] + fib[i]
            fib.append(s)
            i += 1
    return fib[n-1]

print(nth_fibonacci(10))
