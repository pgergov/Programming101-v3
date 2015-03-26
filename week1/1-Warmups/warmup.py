def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


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
    n = abs(n)
    return sum([int(ch) for ch in str(n)])


def fact_digits(n):
    return sum([factorial(int(ch)) for ch in str(n)])


def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]


def to_digits(n):
    return [int(ch) for ch in str(n)]


def to_number(digits):
    number = 0
    for digit in digits:
        number = number*10 + digit
    return number


def fib_number(n):
    return int("".join([str(numb) for numb in nth_fibonacci(n)]))


def count_vowels(string):
    return sum([1 for char in string.lower() if char in "aeiouy"])


def count_consonants(string):
    return sum([1 for ch in string.lower() if ch in "bcdfghjklmnpqrstvwxz"])


def char_histogram(string):
    return {key: string.count(key) for key in string}


def p_score(n):
    if palindrome(n):
        return 1
    return 1 + p_score(n + int(str(n)[::-1]))


def is_increasing(seq):
    return all([seq[i] > seq[i-1] for i in range(1, len(seq))])


def is_decreasing(seq):
    return all([seq[i] < seq[i-1] for i in range(1, len(seq))])


def next_hack(n):
    while True:
        if palindrome(bin(n+1)[2:]):
            if sum([1 for numb in bin(n+1)[2:] if numb == '1']) % 2 != 0:
                break
        n += 1
    return n + 1
