# defective when b has only one character :(
a = input("String a: ") + "\0"
b = input("String b: ") + "\0"
dist = [[-1 for i in range(100)] for j in range(100)]
for i in range(len(a)-1, -1, -1):
    for j in range(len(b)-1, -1, -1):
        if (a[i] == "\0"):
            dist[i][j] = len(b)-j-1
        elif (b[i] == "\0"):
            dist[i][j] = len(a)-i-1
        elif (a[i] == b[j]):
            dist[i][j] = dist[i+1][j+1]
        else:
            dist[i][j] = 1 + min(dist[i][j+1],dist[i+1][j],dist[i+1][j+1])
        j -= 1
    i -= 1
print(dist[0][0])
#  [print(i) for i in cache]