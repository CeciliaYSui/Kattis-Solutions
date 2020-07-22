from sys import stdin, stdout
n = int(stdin.readline())
flag, p = False, True
played = set()
prev = input()
played.add(prev)

for i in range(1,n):
    tmp = prev[-1]
    w = input()
    if (w in played) or (w[0] != tmp): 
        stdout.write("Player 1 lost\n" if flag else "Player 2 lost\n")
        exit()
    else: 
        played.add(w)
    flag = not flag
    prev = w
print("Fair Game")