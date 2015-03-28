def sevens_in_a_row(arr, n):
    counter = 0
    for numb in arr:
        if numb == 7:
            counter += 1
        else:
            if counter == n:
                return True
            counter = 0
    if counter == n:
        return True
    else:
        return False

print(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
