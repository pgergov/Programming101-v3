def calculate_coins(summ):
    result = {}
    coins = [1,2,100,5,10,50,20]
    coins = sorted(coins, reverse = True)
    the_sum = summ * 100
    counter = 0
    for coin in coins:
        while True:
            if the_sum >= coin:
                the_sum = the_sum - coin
                counter += 1
            else:
                result[coin] = counter
                counter = 0
                break
    return result

print(calculate_coins(0.01))
