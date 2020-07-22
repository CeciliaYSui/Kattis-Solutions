import math
M = 1000000007

sum = 0
for i in range(80):
    sum += (7**i) * i
# print(sum)
print(sum % M)
# h val working 
hashes = [i for i in range(0,80)][::-1]
# print(hashes)
h = hashes[0]
for j in range(1, len(hashes)):
    h = (7 * h) % M + hashes[j]
print(h)
