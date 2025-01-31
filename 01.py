import time

# в дз використовуються, судя чи за все, українські монети, то ж робимо константу
COINS_UA = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(rest: int) -> dict:
    # Перевірка на від'ємне або нульове значення
    if rest <= 0:
        print(f"Гроші дали без решти або ж недоплатили...")
        return {}

    rest_in_coins = {}
    for coin in COINS_UA:
        count = rest // coin
        if count > 0:
            rest_in_coins[coin] = count
            rest -= coin * count
    return rest_in_coins


def find_min_coins(rest: int) -> dict:
    # Перевірка на від'ємне або нульове значення
    if rest <= 0:
        print(f"Гроші дали без решти або ж недоплатили...")
        return {}

    # Ініціалізація масивів для динамічного програмування
    min_coins = [float("inf")] * (rest + 1)
    min_coins[0] = 0
    optimal_nominal = [0] * (rest + 1)

    # Заповнення масиву мінімальної кількості монет
    for amount in range(1, rest + 1):
        for coin in COINS_UA:
            if coin <= amount and min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1
                optimal_nominal[amount] = coin

    # Відновлення результату
    result = {}

    while rest > 0:
        current_nominal = optimal_nominal[rest]
        result[current_nominal] = result.get(current_nominal, 0) + 1
        rest -= current_nominal

    return result


def test_with_performance(rest):
    greedy_start = time.time()
    greedy_result = find_coins_greedy(rest)
    greedy_end = time.time()
    greedy_time = greedy_end - greedy_start

    dynp_start = time.time()
    dynp_result = find_min_coins(rest)
    dynp_end = time.time()
    dynp_time = dynp_end - dynp_start

    print(f"\nДля решти {rest}")
    print(f"Жадібний: {greedy_result}, за часом виконання: {greedy_time:.6f} sec")
    print(f"Динамічний: {dynp_result}, за часом виконання: {dynp_time:.6f} sec")


def main():
    rest = [10400, 12332, -5346, 4234, 1204, 5555]
    for i in rest:
        test_with_performance(i)


if __name__ == "__main__":
    main()
