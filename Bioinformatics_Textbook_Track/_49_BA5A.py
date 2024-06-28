from util import get_data


def find_min_n_coins_to_change(money, coins):
    money_list_min_coins = [float('inf')]*(money + 1)
    index = money
    money_list_min_coins[money] = 0

    while index > 0:
        for coin in coins:
            if index-coin >= 0:
                money_list_min_coins[index-coin] = min(money_list_min_coins[index-coin], money_list_min_coins[index] + 1)

        index -= 1
        while money_list_min_coins[index] == 0:
            index -= 1

    return money_list_min_coins[0]


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''40
# 1,5,10,20,25,50'''

    money, coins = data.split("\n")
    coins = list(map(int, coins.split(",")))

    min_n_coins = find_min_n_coins_to_change(int(money), coins)

    print(min_n_coins)    
