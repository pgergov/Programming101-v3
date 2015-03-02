def nth_fib_lists(listA, listB, n):
    result = []
    fib_list = []
    if n == 1:
        result = listA
    elif n == 2:
        result = listB
    elif n == 3:
        result = listA + listB
    elif n > 3:
        result = [listA] + [listB]
        for i in range(3, n+1):
            result += [result[i-3] + result[i-2]]
        result = result[n-1]
    return result

print(nth_fib_lists([], [1, 2, 3], 4))
