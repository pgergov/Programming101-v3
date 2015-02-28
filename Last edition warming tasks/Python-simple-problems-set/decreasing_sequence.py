def is_decreasing(seq):
    i = 0
    while i < len(seq) - 1:
        if seq[i] <= seq[i+1]:
            return False
        i += 1
    return True

print(is_decreasing([1,1,1,1]))
