from copy import deepcopy

def sum_of_divisors(n):
    return sum([x for x in range(1,n+1) if n % x == 0 ])

def is_prime(n):
    if n == 1 or n < 0:
        return False
    return all([not n % x == 0 for x in range(2,n)])

def prime_number_of_divisors(n):
    return is_prime(sum([1 for x in range(1, n+1) if n % x == 0]))

def contains_digit(number, digit):
    return str(digit) in str(number)

def contain_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
    return True

def is_number_balanced(n):
    numbs = [int(x) for x in str(n)]
    half = len(numbs) // 2
    left_numbs = numbs[0:half]
    if len(numbs) % 2 == 0: right_numbs = numbs[half:]
    else: right_numbs = numbs[half + 1:]

    left_sum = sum(left_numbs)
    right_sum = sum(right_numbs)

    if left_sum == right_sum:
        return True
    return False

def count_substrings(haystack, needle):
    return haystack.count(needle)

def zero_insert(n):
    n = [int(x) for x in str(n)]
    i = 0
    while i < len(n) - 1:
        if n[i] == n[i+1] or (n[i] + n[i+1]) % 10 == 0:
            n.insert(i+1, 0)
        i += 1
    return n

def sum_matrix(n):
    return sum([sum(x) for x in n])

def find_neighbours(matrix,row,i,j):
    neighbours = []
    if i - 1 >= 0:
        if j - 1 >= 0: neighbours.append([i-1,j-1])
        neighbours.append([i-1,j])
        if j + 1 <= len(row) - 1: neighbours.append([i-1,j+1])
    if j - 1 >= 0: neighbours.append([i,j-1])
    if j + 1 <= len(row) - 1: neighbours.append([i,j+1])
    if i + 1 <= len(matrix) - 1:
        if j - 1 >= 0: neighbours.append([i+1,j-1])
        neighbours.append([i+1,j])
        if j + 1 <= len(row) - 1: neighbours.append([i+1,j+1])
    return neighbours

def bomb_matrix(matrix,row,i,j):
    result = deepcopy(matrix)
    for element in find_neighbours(matrix, row, i,j):
        if matrix[element[0]][element[1]] - matrix[i][j] >= 0:
            result[element[0]][element[1]] = matrix[element[0]][element[1]] - matrix[i][j]
        else:
            result[element[0]][element[1]] = 0
    return result

def matrix_bombing_plan(matrix):
    result = {}
    for row in matrix:
        i = matrix.index(row)
        for coll in row:
            j = row.index(coll)
            result[(i,j)] = sum_matrix(bomb_matrix(matrix,row,i,j))
    return result

print(matrix_bombing_plan([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))