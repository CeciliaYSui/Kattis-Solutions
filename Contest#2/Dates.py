import datetime as dt
import itertools as it
n = int(input())
for i in range(n):
    l = [int(x) for x in input().split("/")]
    p = [list(x) for x in (list(set((it.permutations(l)))))]
    dates = []
    for j in p:
        if 0 <= j[0] <= 79:
            j[0] += 2000
        elif 80 <= j[0] <= 99:
            j[0] += 1900
        flag = True
        try:
            dt.datetime(j[0], j[1], j[2])
        except ValueError:
            flag = False
        if flag:
            j = [str(x) for x in j]
            for x in range(len(j)):
                j[x] = "0"+j[x] if len(j[x])==1 else j[x]
            dates.append("-".join(j))
    [print(v, end = " ") for v in sorted(dates)]
    print()