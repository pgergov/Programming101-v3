def magic_square(matrix):
    sum_all = []
    forward_diagonal = 0
    backward_diagonal = 0
    is_true = True
    
    for row in matrix:
        s = 0
        for element in row:
            s += element
        sum_all.append(s)
    for i in range(0, len(matrix)):
        s = 0
        for row in matrix:
            s += row[i]
        sum_all.append(s)
    for i in range(0, len(matrix)):
        forward_diagonal += matrix[i][i]
    sum_all.append(forward_diagonal)
    for i in range(len(matrix) - 1, -1, -1):
        backward_diagonal += matrix[i][i]
    sum_all.append(backward_diagonal)

    for i in range(0, len(sum_all)):
        if i + 1 < len(sum_all):
            if sum_all[i] != sum_all[i+1]:
                is_true = False
                break
    return is_true

print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
