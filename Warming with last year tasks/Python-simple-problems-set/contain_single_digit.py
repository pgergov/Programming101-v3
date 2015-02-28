def contains_digit(number, digit):
    while number // 10 != 0:
        if number % 10 == digit:
            return True
        number = number // 10
    else:
        if number == digit:
            return True
        else:
            return False

print(contains_digit(42,2))
