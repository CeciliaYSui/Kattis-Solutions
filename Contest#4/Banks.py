def DFS(tmp, v, visited):
    visited[v] = True
    tmp.append(v)
    for i in adj[v]:
        if visited[i] == False:
            tmp = DFS(tmp, i, visited)
    return tmp

cc = []
adj = [[] for i in range(5)]

adj[1].append(0)
adj[0].append(1)
adj[1].append(2)
adj[2].append(1)
adj[3].append(4)
adj[4].append(3)
adj[4].append(1)
adj[1].append(4)
visited = [ False for i in range(5)]
for v in range(5):
    if visited[v] == False:
        a = []
        cc.append(DFS(tmp, v, visited))
print(len(cc))