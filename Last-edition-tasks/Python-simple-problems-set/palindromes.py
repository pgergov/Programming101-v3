def is_int_palindrome(n):
    initial_n = n
    reverse_n = 0
    if n < 10:
        return True
    while n // 10 != 0:
        reverse_n = reverse_n*10 + n % 10
        n = n // 10
    else:
        reverse_n = reverse_n*10 + n
    if reverse_n == initial_n:
        return True
    else:
        return False