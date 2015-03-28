def groupby(func, seq):
    result = {}
    for numb in seq:
        if func(numb) not in result:
            result.setdefault(func(numb), [])
            result[func(numb)].append(numb)
        else:
            result[func(numb)].append(numb)
    return result
print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
