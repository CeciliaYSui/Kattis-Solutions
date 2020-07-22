#-------------------------------------
# Adjacency List Implementation (dict)
#-------------------------------------
from sys import stdin, stdout 
n = int(stdin.readline())
while (n != -1):
    d = {x: set() for x in range(n)}
    for i in range(n):
        l = [int(m) for m in stdin.readline().split()]
        [d[i].add(j) if l[j] == 1 else None for j in range(n)]
    for k, v in d.items(): 
        if len(v)<=1: 
            stdout.write(str(k) + " ")
            continue
        flag = False
        for a in v: 
            if flag: 
                break
            for b in v: 
                if b in d[a]:
                    flag = True
                    break
        if not flag: 
            stdout.write(str(k) + " ")
    stdout.write("\n")
    n = int(stdin.readline())