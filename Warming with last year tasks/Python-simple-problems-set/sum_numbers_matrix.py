def sum_matrix(m):
    s = 0
    for item in m:
        for num in item:
            s += num
    return s
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
