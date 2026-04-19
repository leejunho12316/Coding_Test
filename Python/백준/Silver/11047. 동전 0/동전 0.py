N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins = sorted(coins,reverse=True)

def algorithm(coins, money):
    result = 0

    for coin in coins:
        result += money // coin
        money = money % coin

    return result

print(algorithm(coins, K))