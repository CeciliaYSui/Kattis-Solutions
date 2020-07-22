n = int(input())

for i in range(n):
    s = input().split()
    r = int(s[0])
    e = int(s[1])
    c = int(s[2])
    tmp = e-c
    if tmp == r:
        print("does not matter")
    elif tmp < r: 
        print("do not advertise")
    else:
        print("advertise")