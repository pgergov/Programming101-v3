def factorial(n):
    factorial(0) = 1
    return n*factorial(n-1)
print(factorial(2))

def nth_fibonacci(n):
    result = []
    a = 1
    b = 1
    while len(result) < n:
        result.append(a)
        next_fib = a + b
        a = b
        b = next_fib
    return result

def sum_of_digits(n):
    return sum(to_digits(n))

# !!! list comprehension !!!
# a = "123"
# [x for x in a]
# за всяко х, където х е във а

def to_digits(n):
    return [int(x) for x in str(n)]

def factorial_digits(n):
    return sum([factorial(x) for x in to_digits(n)])

def palindrome(obj):
    return str(obj)[::-1] == str(obj)

def digit_count(n):
    return sum([1 for x in to_digits(n)])

def to_number(digits):
    result = 0
    for digit in digits:
        digits_count = digit_count(digit)
        result = result*(10 ** digits_count) + digit
    return result

def fib_number(n):
    return to_number(nth_fibonacci(n))

# !!!!! Dict comprehension !!!!!
def char_histogram(string):
    return {key: string.count(key) for key in string}

def p_score(n):
    if palindrome(n):
        return 1
    s = n + int(str(n)[::-1])
    return 1 + p_score(s)

def even(n):
    return n % 2 == 0

def odd(n):
    return not even(n)

def is_hack(n):
    binary_n = bin(n)[2:]
    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count('1'))
    return is_palindrome and has_odd_ones

def next_hack(n):
    n += 1
    while not is_hack(n):
        n += 1
    return n