from collections import defaultdict, Counter
from timeit import timeit

def calc_change(amount):
    print(f'Greedy method: {find_coins_greedy(amount)}')
    print(f'Dynamic method: {find_min_coins(amount)}')
    print(f'Greedy method time: {timeit(lambda: find_coins_greedy(amount), number=10000)}')
    print(f'Dynamic method time: {timeit(lambda: find_min_coins(amount), number=10000)}')


def find_coins_greedy(amount):
    coins = [1,2,5,10,25,50]
    return_coins = defaultdict(lambda: 0)

    while amount > 0:
        if amount >= coins[-1]:
            return_coins[coins[-1]] += 1
            amount -= coins[-1]
        else:
            coins.remove(coins[-1])

    return dict(return_coins)

def find_min_coins(amount, return_coins = None):
    coins = [1,2,5,10,25,50]
    if return_coins is None:
        return_coins = defaultdict(lambda: 0)

    while len(coins) > 0:
        coin = coins.pop()
        if coin <= amount:
            return_coins[coin] += 1
            find_min_coins(amount - coin, return_coins)
            break

    return dict(return_coins)


if __name__ == "__main__":
    calc_change(int(input('Enter needed sum in cents: ')))
