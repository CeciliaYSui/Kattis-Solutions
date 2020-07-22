import math

s = input().split()
n = int(s[0])
w = int(s[1])
h = int(s[2])

l = math.sqrt(w**2 + h**2)

for i in range(n):
    val = int(input())
    if val > l:
        print("NE")
    else:
        print("DA")