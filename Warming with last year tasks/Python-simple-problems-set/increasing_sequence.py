def is_increasing(seq):
    i = 0
    while i < len(seq) - 1:
        if seq[i] >= seq[i+1]:
            return False
        i += 1
    return True

print(is_increasing([1,2,3,3]))
