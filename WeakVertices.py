#-------------------------------------
# Adjacency Matrix Implementation
#-------------------------------------
from sys import stdin, stdout 
n = int(stdin.readline())
while (n != -1):
    matrix = []
    [matrix.append([int(i) for i in stdin.readline().split()]) for i in range(n)]
    for i in range(n):
        if matrix[i].count(1) <= 1 :
            stdout.write(str(i) + " ")
            continue
        vertices = []
        flag = False
        for j in range(n):
            if flag: 
                break
            if matrix[i][j] == 0: 
                continue
            if not vertices:
                vertices.append(j)
            else:
                for k in range(len(vertices)):
                    if matrix[j][vertices[k]] == 1:
                        flag = True
                        break
                vertices.append(j)
        if not flag: 
            stdout.write(str(i) + " ")
    stdout.write("\n")
    n = int(stdin.readline())