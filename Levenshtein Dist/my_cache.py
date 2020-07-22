def dist(i, j):
    if cache[i][j] >= 0:
        return cache[i][j]
    if a[i] == "\0":
        cache[i][j] = len(b)-j-1
    elif b[j] == "\0":
        cache[i][j] = len(a)-i-1
    elif a[i] == b[j]:
        cache[i][j] = dist(i+1, j+1)
    else: 
        cache[i][j] = 1 + min(dist(i,j+1), dist(i+1,j), dist(i+1,j+1))
    return cache[i][j]

a = input("String a: ") + "\0"
b = input("String b: ") + "\0"
cache = [[-1 for i in range(100)] for j in range(100)]
print(dist(0, 0))