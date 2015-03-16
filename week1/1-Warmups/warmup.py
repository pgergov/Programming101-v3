def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def nth_fibonacci(n):
    fib = [1, 1]
    s = 0
    i = 1
    if n == 1:
        return [1]
    elif n > 2:
        while i < n -1:
            s = fib[i-1] + fib[i]
            fib.append(s)
            i += 1
    return fib

def sum_of_digits(n):
    n = abs(n)
    s = 0
    while n // 10 != 0:
        s += n % 10
        n = n // 10
    else:
        s += n
    return s

def fact_digits(n):
    n = abs(n)
    s = 0
    while n // 10 != 0:
        s += factorial(n % 10)
        n = n // 10
    else:
        s += factorial(n)
    return s

def palindrome(obj):
    obj = str(obj)
    if obj == obj[::-1]:
        return True
    return False

def to_digits(n):
    numbs = []
    while n // 10 != 0:
        numbs.append(n % 10)
        n = n // 10
    else:
        numbs.append(n)
    return numbs[::-1]

def to_number(digits):
    number = 0
    for digit in digits:
        number = number*10 + digit
    return number

def fib_number(n):
    result = ""
    for numb in nth_fibonacci(10):
        result += str(numb)
    return int(result)

def count_vowels(string):
    vowels = "aeiouy"
    counter = 0
    for char in string.lower():
        if char in vowels:
            counter += 1
    return counter

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxz"
    counter = 0
    for char in string.lower():
        if char in consonants:
            counter += 1
    return counter

def char_histogram(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def p_score(n):
    result = 1
    while not palindrome(n):
        result += 1
        n = n + int(str(n)[::-1])
    return result

def is_increasing(seq):
    current_numb = seq[0]
    for i in range(1,len(seq)):
        if seq[i] > current_numb:
            current_numb = seq[i]
        else:
            return False
    return True

def is_decreasing(seq):
    current_numb = seq[0]
    for i in range(1,len(seq)):
        if seq[i] < current_numb:
            current_numb = seq[i]
        else:
            return False
    return True

def next_hack(n):
    i = n + 1
    while True:
        counter = 0
        if palindrome(int(bin(i)[2:])):
            for numb in bin(i)[2:]:
                if numb == '1':
                    counter += 1
        if counter > 0 and counter % 2 != 0:
            break
        i += 1
    return i

print(next_hack(8031))