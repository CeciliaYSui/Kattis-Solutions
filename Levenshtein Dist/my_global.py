def dist(i, j):
    if a[i] == "\0":
        return len(b)-j-1
    if b[j] == "\0":
        return len(a)-i-1
    if a[i] == b[j]:
        return dist(i+1, j+1)
    return 1 + min(dist(i,j+1), dist(i+1,j), dist(i+1,j+1))

a = input("String a: ") + "\0"
b = input("String b: ") + "\0"
print(dist(0, 0))