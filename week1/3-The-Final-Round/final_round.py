import calendar


def count_words(arr):
    return {key: arr.count(key) for key in arr}


def unique_words_count(arr):
    return len(count_words(arr))


def nan_expand(times):
    result = ""
    if times == 0:
        return ""
    for i in range(times):
        result += "Not a "
    result += "NaN"
    return result


def iterations_of_nan_expand(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")
    return False


def is_prime(n):
    if n == 1 or n < 0:
        return False
    return all([n % x != 0 for x in range(2, n)])


def counter(n, prime_number):
    divider_counter = 0
    while n % prime_number == 0:
        divider_counter += 1
        n /= prime_number
    return divider_counter


def prime_factorization(n):
    primes = [x for x in range(2, n+1) if is_prime(x)]
    return [(num, counter(n, num)) for num in primes if counter(n, num) != 0]


def group(lst):
    result = []
    numbs = []
    for i in range(len(lst)):
        if i == 0:
            numbs = [lst[i]]
        else:
            if lst[i] == lst[i-1]:
                numbs.append(lst[i])
            else:
                result.append(numbs)
                numbs = [lst[i]]
    result.append(numbs)
    return result


def max_consecutive(items):
    return max([len(x) for x in group(items)])


def groupby(func, seq):
    result = {}
    for element in seq:
        if func(element) in result:
            result[func(element)].append(element)
        else:
            result[func(element)] = [element]
    return result


def prepare_meal(number):
    result = ""
    count3 = 0
    while number % 3 == 0:
        count3 += 1
        number /= 3
    result += " ".join(["spam" for i in range(count3)])
    if number % 5 == 0:
        result += " ".join(["eggs" if count3 == 0 else " and eggs"])
    return result


def reduce_file_path(path):
    result = "/"
    folders = [word for word in path.split("/") if word != "" and word != "."]
    l = len(folders)
    locations = [folders[i] for i in range(l - 1) if folders[i] != ".." and i + 1 <= l and folders[i  +1] != ".."]
    if l != 0 and folders[l-1] != "..":
        locations.append(folders[l-1])
    result += "/".join(locations)
    return result


def same_characters(letter, string):
    return all([letter == ch for ch in string])


def is_an_bn(word):
    word_length = len(word)
    if word_length % 2 == 0:
        a = word[: word_length // 2]
        b = word[word_length // 2:]
        return same_characters("a", a) and same_characters("b", b)
    return False


def to_digits(n):
    return [int(x) for x in str(n)]


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def is_credit_card_valid(number):
    s = 0
    numbs = to_digits(number)
    if count_digits(number) % 2 != 0:
        for i in range(len(str(number))):
            if i % 2 == 0:
                s += numbs[i]
            else:
                s += sum(to_digits(numbs[i] * 2))
        return s % 10 == 0
    return False


def goldbach(n):
    primes = [x for x in range(2, n+1) if is_prime(x)]
    combos = []
    for n1 in primes:
        if n1 <= n / 2:
            combos.append([(n1, n2) for n2 in primes if n1 + n2 == n])
    return [combo[0] for combo in combos if combo != []]


def magic_square(matrix):
    s = []
# Sum of rows:
    for row in matrix:
        s.append(sum(row))
# Sum of columns:
    for i in range(0, len(matrix)):
        s.append(sum([row[i] for row in matrix]))
# Sum of main diagonal:
    s.append(sum([matrix[i][i] for i in range(len(matrix))]))
# Sum of second diagonal:
    i = 0
    result = 0
    for j in range(len(matrix) - 1, -1, -1):
        result += matrix[i][j]
        i += 1
    s.append(result)
    return all([s[0] == s[i] for i in range(len(s))])


def is_leap_year(year):
    if calendar.isleap(year):
        return {3, 4}
    else:
        return {4}


def friday_years(start, end):
    return sum([1 for elem in[year for year in range(start, end + 1)
                if calendar.weekday(year, 1, 1) in is_leap_year(year)]])
