m = int(input())
for i in range(m):
    edges, d, components = [], {}, []
    n = int(input())
    for j in range(n):
        l = [int(x) for x in input().split()]
        edges.append(l)
        d[l[0]] = d[l[0]] + 1 if l[0] in d else 1
        d[l[1]] = d[l[1]] + 1 if l[1] in d else 1
    c = max(d.values())
    for a, b in d.items():
        if b == c:
            components.append(a)
    cnt = 0
    for a, b in edges:
        if a in components or b in components:
            cnt += 1
    print(cnt + len(d))