def nan_expand(times):
    i = 1
    result = ""
    if times == 0:
        return ""
    while True:
        result += "Not a "
        if i == times:
            result += "NaN"
            break
        i += 1
    return result
print(nan_expand(2))
