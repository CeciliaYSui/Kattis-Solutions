t = int(input())
for i in range(t):
    n = int(input())   
    x = sorted([input() for _ in range(n)], key=len, reverse = True)
    pl = set()
    flag = True
    for i in x: 
        if i in pl: 
            flag = False
            break
        [pl.add(i[:j]) for j in range(1, len(i)+1)]
    print("YES" if flag else "NO")    