m = int(input())
for i in range(m):
    cap, no = [int(x) for x in input().split()] 
    inc = no + 1
    bit1 = bin(inc).count('1')
    while (bit1 > cap):
        inc += 1
        bit1 = bin(inc).count('1')
    print(inc)
