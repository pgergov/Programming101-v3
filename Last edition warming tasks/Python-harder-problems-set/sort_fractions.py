def sort_fractions(fractions):
    for i in range(len(fractions)):
        for j in range(len(fractions) - 1, i, -1):
            print(i,j)
            if fractions[j][0] / fractions[j][1] < fractions[j-1][0] / fractions[j-1][1]:
                x = fractions[j]
                fractions[j] = fractions[j-1]
                fractions[j-1] = x
    return fractions

print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
