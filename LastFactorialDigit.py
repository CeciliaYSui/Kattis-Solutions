n = int(input())

for i in range(n):
    t = int(input())
    if (t == 1) | (t == 2) | (t == 4): 
        print(t)
    elif t == 3: 
        print(6)
    else: 
        print(0)