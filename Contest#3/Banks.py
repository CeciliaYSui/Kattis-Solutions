data = int(input())
for i in range(data):
    n = int(input()) # < 10,000
    matrix = [[0 for a in range(n)] for b in range(n)]
    # build matrix
    for j in range(n):
        l = [int(x) for x in input().split()]
        matrix[j][j] = l[0]
        c = 2
        for k in range(l[1]):
            matrix[j][l[c]-1] = True 
            matrix[l[c]-1][j] = True
            c += 1
        c = 2
        for k in range(l[1]-1):
            matrix[l[c]-1][l[c+1]-1] = True
            matrix[l[c+1]-1][l[c]-1] = True
            c += 1
    # compute
    for j in range(n):
        if matrix[j][j] >= 0:
            continue
        trust = matrix[j]
        flag = False
        for k in range(n):
            if flag:
                break
            if trust[k] and matrix[k][k] > 0: 
                # borrow 
                if matrix[k][k] >= abs(matrix[j][j]):
                    matrix[k][k] += matrix[j][j]
                    matrix[j][j] = 0
                    flag = True
                else:
                    matrix[k][k] = 0
                    matrix[j][j] += matrix[k][k]
    flag = False
    for j in range(n):
        if matrix[j][j] < 0:
            flag = True
    print("insolvent" if flag else "solvent")
