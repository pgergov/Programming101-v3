from palindromes import is_int_palindrome
def next_hack(n):
    i = n + 1
    while True:
        counter = 0
        if is_int_palindrome(int(bin(i)[2:])):
            for numb in bin(i)[2:]:
                if numb == '1':
                    counter += 1
        if counter > 0 and counter % 2 != 0:
            break
        i += 1
    return i

print(next_hack(8031))
