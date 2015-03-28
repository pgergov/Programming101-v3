def contains_digits(number, digits):
    numbs = []
    is_true = True
    while number // 10 != 0:
        numbs.append(number % 10)
        number = number // 10
    else:
        numbs.append(number)
    for digit in digits:
        if digit in numbs:
            is_true = True
        else:
            is_true = False
    return is_true

print(contains_digits(123456789, [1,2,3,0]))
