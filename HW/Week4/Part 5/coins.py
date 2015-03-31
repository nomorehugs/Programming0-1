# Used Joker

def calculate_coins(sum):
    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum = round(sum * 100)

    for coin in coins:
        times_to_pay = sum // coin
        result[coin] = times_to_pay
        sum -= times_to_pay * coin
    return result

# For Test 
#print(calculate_coins(8.94))
#print(calculate_coins(0.53))
