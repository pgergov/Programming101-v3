def unique_words_count(arr):
    counter = 0
    unique_words = []
    for word in arr:
        if word not in unique_words:
            unique_words.append(word)
            counter += 1
    return counter
print(unique_words_count(["HELLO!"] * 10))
        
