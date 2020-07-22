n = int(input())
for i in range(n):
    m = [int(x) for x in input().split()]
    l = []
    for x in range(1, len(m)):
        tmp = bin(m[x])[2:]
        tmp = "0"*(m[0] - len(tmp)) + tmp
        l.append(tmp)
    row, col = -1, -1
    for j in range(len(l)-1):
        if l[j].count('1') & 1:
            row = j
            break
    if row != -1:
        for a in range(len(l)-1):
            cnt = 0
            for b in range(len(l)):
                if l[b][a] == "1":
                    cnt += 1
            if cnt & 1 == False:
                col = a
                break
        if not (col & 1):
            if l[row][col] == "1":
                l[row] = l[row][:col] + "0" + l[row][col+1:]
            else:
                l[row] = l[row][:col] + "1" + l[row][col+1:]
    for j in range(m[0]-1):
        print(int(l[j],2) >> 1, end = " ")
    print()
    