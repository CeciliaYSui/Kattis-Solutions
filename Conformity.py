from sys import stdin, stdout 
n = int(stdin.readline())
m = {}
for i in range(n):
    tmp = tuple(set(sorted([int(i) for i in stdin.readline().split()])))
    m[tmp] = m[tmp]+1 if tmp in m else 1

p = list(m.values())
maxval = max(p)
maxcnt = p.count(maxval)
print(maxval * maxcnt)