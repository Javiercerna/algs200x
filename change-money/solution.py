def changeMoney(money):
    coin_denominations = [1, 5, 10]
    total_coins = 0
    
    while coin_denominations:
        coin = coin_denominations.pop()
        total_coins += money / coin
        money = money % coin

    return total_coins

if __name__ == '__main__':
    m = int(raw_input())
    print changeMoney(m)
