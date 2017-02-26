def r_count(total = 0,i = 0,correct_combinations = 0):
    coin_list = [1,2,5,10,20,50,100,200]
    limit = 200
    for coin in coin_list[i:]:
        if coin + total == limit:
            return 1 + correct_combinations
        elif coin + total > limit:
            return 0 + correct_combinations
        else:
            correct_combinations = r_count(coin+total ,i,correct_combinations)
        i += 1
    return correct_combinations


print(r_count())

