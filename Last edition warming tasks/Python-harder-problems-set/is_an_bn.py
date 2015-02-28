def is_an_bn(word):
    count_a = 0
    count_b = 0
    for i, char in enumerate(word):
        if char == "a":
            count_a += 1
        if char == "b":
            while i + 1 < len(word) and word[i+1] == "b":
                count_b += 1
                i += 1
            else:
                count_b += 1
                if i+1 == len(word):
                    break
                else:
                    return False
    if count_a == count_b:
        return True
    else:
        return False
print(is_an_bn("aaaaabbbbb"))
