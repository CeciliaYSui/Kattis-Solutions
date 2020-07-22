n = int(input())
s = [int(i) for i in input().split()]
pile1, pile2 = [], []
move = 0
[pile1.append(i) for i in s]

while pile1: 
    move += 1
    if not pile2: #  empty pile2 
        pile2.append(pile1.pop())
        continue
    if pile1[-1] == pile2[-1]: # tos equal 
        pile1.pop()
        pile2.pop()
        continue
    pile2.append(pile1.pop())
print(move if not pile2 else "impossible")