s = input().split()
a,b = int(s[0]), int(s[1])
l1,l2 = [],[]
for i in range(1,a+1):
    for j in range(1,b+1):
        l1.append(i+j)
for k in range(2,a+b+1):
    l2.append(l1.count(k))
maxval = max(l2)
for m in range(a+b-1):
    if l2[m] == maxval: 
        print(m+2)