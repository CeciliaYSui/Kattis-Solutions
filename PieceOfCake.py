s = input().split()
n = int(s[0])
h = int(s[1])
v = int(s[2])

mid = n/2 

if h < mid: 
    h = n-h
if v < mid: 
    v = n-v
print(h * v * 4)