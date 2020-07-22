from collections import deque
from sys import stdin, stdout 
n = int(stdin.readline())
df, db = deque(), deque()

for i in range(n):
    act, no = stdin.readline().split()
    no = int(no)
    if act[0] == "p":
        if act[5] == "b":
            db.append(no)   #O(1)
        elif act[5] == "f":
            df.appendleft(no)   #O(1)
        else: 
            df.append(no)   #O(1)
        if len(df) > len(db) + 1: 
            db.appendleft(df.pop()) #O(1)
        elif len(db) > len(df): 
            df.append(db.popleft()) #O(1)
    else: 
        if no < len(df):
            stdout.write(str(df[no]) + "\n")
        else: 
            stdout.write(str(db[no-len(df)]) + "\n")