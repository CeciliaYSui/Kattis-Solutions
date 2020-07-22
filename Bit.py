n = int(input())
for i in range(n):
    m = input()
    maxval = 0
    for j in range(len(m)):
        cnt = 0
        x = int(m[:len(m)-j])
        while x>0 : 
            cnt = cnt + 1 if x&1 else cnt
            x >>= 1
        maxval = cnt if cnt > maxval else maxval
    print(maxval)