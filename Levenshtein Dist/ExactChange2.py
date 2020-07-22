# dynamic programming implementation    
t = int(input())
for case in range(t):
    goal, n = int(input()), int(input())
    coins = []
    for denom in range(n):
        coins.append(int(input()))
    val = sum(coins)
    num_coins = [[-1 for i in range(n)] for j in range(val+1)]
    i = n-1
    limit = coins[i]
    nc = 1
    num_coins[0][i] = 0
    for amt in range(1,val+1):
        if amt > limit:
            limit += coins[i-1]
            nc += 1
        num_coins[amt][i] = nc

    for i in range(n-2,-1,-1):
        for amt in range(0,sum(coins)+1,1):
            num_coins[amt][i] = min(num_coins[amt][i+1], num_coins[amt-coins[i]][i+1]+1)
        
    print(num_coins[1400][0])