n = int(input())
for i in range(n):
    maze, parent = [], []
    cnt = 0
    w, h = [int(x) for x in input().split()]
    [maze.append(list(input())) for j in range(h)]
    for b in range(h):
        if maze[b][0] == ".":
            parent.append([(b,0)])
            cnt += 1
            maze[b][0] = cnt
            break
    if not cnt:
        print("impossible")
        continue
    while parent:
        p = parent.pop(0)
        cnt += 1
        nodes = []
        while p:
            child = []
            loc = p.pop(0)
            child.append((loc[0], loc[1]+1))
            child.append((loc[0], loc[1]-1))
            child.append((loc[0]+1, loc[1]))
            child.append((loc[0]-1, loc[1]))
            for c in child:
                if 0<=c[0]<h and 0<=c[1]<w:
                    if isinstance(maze[c[0]][c[1]], int):
                        continue
                    if maze[c[0]][c[1]] == ".":
                        maze[c[0]][c[1]] = cnt
                        nodes.append((c[0],c[1]))
                    elif maze[c[0]][c[1]].islower():
                        nodes.append((c[0],c[1]))
                        letter = maze[c[0]][c[1]]
                        maze[c[0]][c[1]] = cnt
                        for ii in range(h):
                            for jj in range(w):
                                if maze[ii][jj] == letter:
                                    maze[ii][jj] = cnt
                                    nodes.append((ii, jj))
        if nodes:
            parent.append(nodes)
    flag = True
    for b in range(h):
        if isinstance(maze[b][w-1], int):
            print(maze[b][w-1])
            flag = False
            break
    if flag:
        print("impossible")