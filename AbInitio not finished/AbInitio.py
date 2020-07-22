from sys import stdin, stdout
import numpy as np
M = 1000000007
matrix = np.full((4000,4000), False)

v, e, q = [int(i) for i in stdin.readline().split()]
for i in range(e):
    a,b = [int(i) for i in stdin.readline().split()]
    matrix[a][b] = 1 # src -> dest
for query in range(q):
    l = [int(i) for i in stdin.readline().split()]
    if l[0] == 1: 
        v += 1
    elif l[0] == 2: 
        matrix[l[1]][l[2]] = True
    elif l[0] == 3: 
        matrix[l[1],:] = False
        matrix[:,l[1]] = False
    elif l[0] == 4: 
        matrix[l[1]][l[2]] = False
    elif l[0] == 5: 
        matrix = matrix.transpose()
        for i in range(v):
            matrix[i][i] = False
    else:
        matrix = np.invert(matrix)
        for i in range(v):
            matrix[i][i] = False
matrix = matrix[:v,:][:,:v]
# print(matrix)
stdout.write(str(v)+ "\n")
for i in range(v):
    tmp = matrix[i]
    # stdout.write(str(np.sum(tmp) + " "))
    print(np.sum(tmp), end = " ")
    h = np.argwhere(tmp == True)
    h = [int(j) for j in h][::-1]
    if not h: 
        print(0)
        continue
    hash = h[0]
    for j in range(1,len(h)):
        val = 7 * hash + h[j]
        hash = val % M
    print(hash)
    # stdout.write(" " + str(hash) + "\n")