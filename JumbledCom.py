n = int(input())
s = [int(i) for i in input().split()]
for i in s: 
    n = i
    x0 = n & 1
    x1 = x0<<1 ^ n & 2
    x2 = x1<<1 ^ n & 4
    x3 = x2<<1 ^ n & 8
    x4 = x3<<1 ^ n & 16
    x5 = x4<<1 ^ n & 32
    x6 = x5<<1 ^ n & 64
    x7 = x6<<1 ^ n & 128
    print(x0+x1+x2+x3+x4+x5+x6+x7, end = " ")