n = int(input())
for i in range(n):
    l = input().split()
    row, col, s = int(l[0]), int(l[1]), l[2]
    s = [int(a) for a in s]
    lists = [[] for a in range(col)] # lists as cols 
    flag = True  # b's turn 
    for val in s:
        lists[val-1].append(1 if flag else 2)
        flag = not flag
    for l in lists:
        l += [0] * (row - len(l))
    black, red = False, False
    # vertical
    for a in range(row):
        for b in range(col-3):
            print(a,b)
            if lists[a][b]==1 and lists[a+1][b]==1 and lists[a+2][b]==1 and lists[a+3][b]==1:
                black = True
            elif lists[a][b]==2 and lists[a+1][b]==2 and lists[a+2][b]==2 and lists[a+3][b]==2:
                red = True
