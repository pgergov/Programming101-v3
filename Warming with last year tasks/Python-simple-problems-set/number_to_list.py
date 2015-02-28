def number_to_list(n):
    numbs = []
    while n // 10 != 0:
        numbs.append(n % 10)
        n = n // 10
    else:
        numbs.append(n)
    return numbs[::-1]
