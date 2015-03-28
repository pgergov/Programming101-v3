from number_to_list import number_to_list
from list_to_number import list_to_number
def zero_insert(n):
    n = number_to_list(n)
    print(n)
    result = n
    i = 0
    while i < len(n) - 1:
        if n[i] == n[i+1] or (n[i] + n[i+1]) % 10 == 0:
            result.insert(i+1, 0)
        i += 1
    return list_to_number(result)

print(zero_insert(114655528555555))