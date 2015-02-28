def count_vowels(string):
    vowels = "aeiouy"
    counter = 0
    for char in string.lower():
        if char in vowels:
            counter += 1
    return counter

print(count_vowels("A nice day to code!"))
    

