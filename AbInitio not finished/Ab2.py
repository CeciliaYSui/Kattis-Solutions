from sys import stdin, stdout
M = 1000000007
matrix = [[False for i in range(4000)] for j in range(4000)]
v, e, q = [int(i) for i in stdin.readline().split()]
for i in range(e):
    a,b = [int(i) for i in stdin.readline().split()]
    matrix[a][b] = True

flag, flip = True, True
# flag # True if edge exisitng 
# flip # True if src -> dest

for query in range(q):
    l = [int(i) for i in stdin.readline().split()]
    if l[0] == 1: 
        v += 1
    elif l[0] == 2: 
        if flip: # src -> dest
            matrix[l[1]][l[2]] = flag
        else: 
            matrix[l[2]][l[1]] = flag
    elif l[0] == 3: 
        for i in range(4000):
            matrix[l[1]][i] = not flag
            matrix[i][l[1]] = not flag
    elif l[0] == 4: 
        if flip: # src -> dest
            matrix[l[1]][l[2]] = not flag
        else: 
            matrix[l[2]][l[1]] = not flag
    elif l[0] == 5: 
        flip = not flip # flip by main diagonal 
    else:
        flag = not flag # reverse values
        # 
        for i in range(4000):
            matrix[i][i] = not flag

stdout.write(str(v)+ "\n")
outdeg = []
if flip: # src -> dest: 
    for i in range(v):
        #print(matrix[i][:v])
        cnt = 0 
        hashes = []
        for j in range(v):
            if (i!=j) and (matrix[i][j] == flag):
                cnt += 1
                hashes.append(j)
        outdeg.append(cnt)
        stdout.write(str(cnt) + " ")
        if not hashes: 
            stdout.write("0\n")
        else:
            hashes = hashes[::-1]
            h = hashes[0]
            for j in range(1, len(hashes)):
                # h = (7 * h + hashes[j]) % M
                h = (7 * h) % M + hashes[j]
            stdout.write(str(h) + "\n")
else: 
    for i in range(v):
        cnt = 0
        hashes = []
        for j in range(v):
            if (i != j) and (matrix[j][i] == flag): 
                cnt += 1
                hashes.append(j)
        outdeg.append(cnt) # outdegree
        stdout.write(str(cnt) + " ")
        if not hashes: 
            stdout.write("0\n")
        else:
            hashes = hashes[::-1]
            h = hashes[0]
            for j in range(1, len(hashes)):
                # h = (7 * h + hashes[j]) % M
                h = (7 * h) % M + hashes[j]
            stdout.write(str(h) + "\n")