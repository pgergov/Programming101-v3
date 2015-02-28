def list_to_number(digits):
    number = 0
    for digit in digits:
        number = number*10 + digit
    return number

