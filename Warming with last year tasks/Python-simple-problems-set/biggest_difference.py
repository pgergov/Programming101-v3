def biggest_difference(arr):
    lowest = arr[0]
    biggest = arr[0]
    for numb in arr:
        if numb > biggest:
            biggest = numb
        elif numb < lowest:
            lowest = numb
    return lowest - biggest

print(biggest_difference(range(100)))
            
            
