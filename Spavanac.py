s = input().split()
h = int(s[0])
m = int(s[1])

if m >= 45: 
    print(h, m-45) # python auto space the print outputs 
elif m == 0: 
    if h == 0: 
        print(23, 15)
    else: 
        print(h-1, 15)
else: 
    if h == 0: 
        print(23, m+60-45)
    else:
        print(h-1, m+60-45)