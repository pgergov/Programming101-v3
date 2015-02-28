def count_substrings(haystack, needle):
    new_word = ""
    counter = 0
    words = haystack.split()
    needle = [needle]
    for word in words:
        i = 0
        new_word = ""
        for char in word:
            new_word += char
            if new_word[i] == needle[0][i]:
                i += 1
                if new_word == needle[0]:
                    new_word = ""
                    i = 0
                    counter += 1
            else:
                new_word = ""
                i = 0
    return counter
print(count_substrings("babababa", "baba"))
print(count_substrings("This is this and that is this", "this"))
