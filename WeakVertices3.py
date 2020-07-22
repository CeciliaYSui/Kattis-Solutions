#-------------------------------------
# Edge List Implementation
#-------------------------------------
from sys import stdin, stdout 
n = int(stdin.readline())
while n != -1: 
    edges = [] # edge list --> list of lists of tuples/pairs
    for i in range(n):
        tmp = [(int(i), int(x)) for x,v in enumerate(stdin.readline().split()) if int(v)==1]
        edges.append(tmp)
    for V,E in enumerate(edges):
        flag = False
        for i,a in enumerate(E):
            for j,b in enumerate(E[i+1:]):
                if (a[1], b[1]) in edges[a[1]]:
                    flag = True
                    break
            if flag:
                break
        stdout.write(str(V)+ " ") if not flag else None
    stdout.write("\n")
    n = int(stdin.readline())