N = int(input())
tmp = 2
for i in range(N): 
    tmp = tmp + (tmp -1)
print(tmp**2)