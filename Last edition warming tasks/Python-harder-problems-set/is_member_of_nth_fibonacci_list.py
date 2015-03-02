def member_of_nth_fib_lists(listA, listB, needle):
    result = listA + listB
    result += listB + result
    is_true = False
    for i in range(0, len(result)):
        if result[i] == needle[0]:
            for j in range(0, len(needle)):
                if i + j < len(result) and result[i + j] == needle[j]:
                    is_true = True
                else:
                    is_true = False
                    break
            break  
    return is_true

print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))
