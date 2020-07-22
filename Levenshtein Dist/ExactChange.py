# recursive implementation
def num_coins(amt, i):
    if amt == 0:  
        return 0
    if amt < 0:
        return 10000
    if i >= n:
        return 10000
    return min(num_coins(amt, i+1), num_coins(amt-coins[i], i+1)+1)
    
t = int(input())
for case in range(t):
    goal = int(input())
    n = int(input())
    coins = []
    for denom in range(n):
        coins.append(int(input()))
    loop = num_coins(goal, 0)
    while loop == 10000:
        # change inc to speed up when applicable 
        loop = num_coins(goal+100,0)
    print(goal+100, loop)