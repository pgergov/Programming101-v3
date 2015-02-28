def is_number_balanced(n):
    numbs = []
    left_sum = 0
    right_sum = 0
    if n < 10:
        return True
    while n // 10 != 0:
        numbs.append(n % 10)
        n = n // 10
    else:
        numbs.append(n)
        
    half = len(numbs) // 2
    right_numbs = numbs[0:half]
    if len(numbs) % 2 == 0:
        left_numbs = numbs[half:]
    elif len(numbs) % 2 != 0:
        left_numbs = numbs[half + 1:]
        
    for i in left_numbs:
        left_sum += i
        
    for j in right_numbs:
        right_sum += j
        
    if left_sum == right_sum:
        return True
    else:
        return False

print(is_number_balanced(1238033))
