n = int(input())
for i in range(n):
    a,b = [int(x) for x in input().split()]
    x = (a//1350) * (b//1350)
    print(x, end=" ")
    if x == 1:
        print("grimble")
    else:
        print("grimbles")