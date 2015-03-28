def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxz"
    counter = 0
    for char in string.lower():
        if char in consonants:
            counter += 1
    return counter
print(count_consonants("A nice day to code!"))
