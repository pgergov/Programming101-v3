def prepare_meal(number):
    result = ""
    initial_number = number
    count3 = 0
    count5 = 0
    i = 2
    if number % 5 == 0:
            count5 = 1
    while True:
        if number % 3 == 0:
            number /= 3
            count3 += 1
        else:
            break
        if number == 1:
            break
    if count3 >= 1:
        result += "spam"
        while i <= count3:
            result += " spam"
            i += 1
    if count5 != 0:
        if count3 != 0:
            result += " and eggs"
        else:
            result += "eggs"
    return result
print(prepare_meal(45))
