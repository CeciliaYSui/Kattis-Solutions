n = int(input())
arr = [False] * 365 
for i in range(n):
    l = input().split()
    a,b = int(l[0]), int(l[1])
    for j in range(a-1,b):
        arr[j] = True
print(sum(arr))