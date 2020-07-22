s = input().split()
n, t = int(s[0]), int(s[1])
s = input().split()
l = [int(i) for i in s]
sum, cnt = 0, 0
for i in range(n):
    sum += l[i]
    if sum > t: 
        break
    cnt += 1
print(cnt)