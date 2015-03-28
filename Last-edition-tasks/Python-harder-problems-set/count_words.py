def count_words(arr):
    result = {}
    for word in arr:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result
print(count_words(["python", "python", "python", "ruby"]))
