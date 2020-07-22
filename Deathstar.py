n = int(input())
x, a = [], []
[x.append([int(n) for n in input().split()]) for i in range(n)]
for i in range(n):
    m = 0 
    for j in range(n):
        m |= x[j][i]
    a.append(m)
[print(i, end=" ") for i in a]