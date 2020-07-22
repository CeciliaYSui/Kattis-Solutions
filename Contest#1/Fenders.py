# Author ------------- Cecilia Y. Sui 
# Course ------------- Competition Programming 
# Program ------------ Sprint Problem #2

n = int(input())
for i in range(n):
    s = [float(i) for i in input().split()]
    cnt = 0
    f, ft = s[0], s[1]
    while (f > 0):
        tmp = 500//ft
        cnt += 1
        f -= tmp
    print(cnt)