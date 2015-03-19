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
    indexes = [-1, 0, 1]
    for r in indexes:
        for c in indexes:
            if i+r >= 0 and i+r <= len(matrix) - 1 and j+c >= 0 and j+c <= len(row) - 1:
                if not (r == 0 and c == 0):
                    neighbours.append([i+r, j+c])
    return neighbours

def bomb_matrix(matrix,row,i,j):
    bombed_matrix = deepcopy(matrix)
    for element in find_neighbours(matrix, row, i,j):
        if matrix[element[0]][element[1]] - matrix[i][j] >= 0:
            bombed_matrix[element[0]][element[1]] = matrix[element[0]][element[1]] - matrix[i][j]
        else:
            bombed_matrix[element[0]][element[1]] = 0
    return bombed_matrix

def matrix_bombing_plan(matrix):
    result = {}
    for row in matrix:
        i = matrix.index(row)
        for coll in row:
            j = row.index(coll)
            result[(i,j)] = sum_matrix(bomb_matrix(matrix,row,i,j))
    return result

print(matrix_bombing_plan([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))