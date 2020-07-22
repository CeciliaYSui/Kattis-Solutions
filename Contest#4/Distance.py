def dist(i, j):
    # print(i,j)
    # print(a[i],b[j])
    # rint(ord(a[i]), ord(b[j]))
    # print(abs(ord(a[i])-ord(b[j])))
    global flag
    if a[i] == "\0":
        return len(b)-j-1
    if b[j] == "\0":
        return len(a)-i-1
    if a[i] == b[j]:
        return dist(i+1, j+1)
    if flag: # even
        c1 = dist(i,j+1) + 3
        flag = not flag
    else:
        c1 = dist(i,j+1)
        flag = not flag
    c2 = dist(i+1,j) + 2
    c3 = dist(i+1,j+1) + abs(ord(a[i]) - ord(b[j]))
    return min(c1,c2,c3)
    # return 1 + min(dist(i,j+1), dist(i+1,j), dist(i+1,j+1))

n = int(input())
for r in range(n):
    a, b = input() + "\0", input() + "\0"
    flag = True # even/odd
    print(dist(0, 0))