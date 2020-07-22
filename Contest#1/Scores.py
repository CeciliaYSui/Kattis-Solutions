# Author ------------- Cecilia Y. Sui 
# Course ------------- Competition Programming 
# Program ------------ Sprint Problem #8

n = int(input())
for i in range(n):
    s = sorted([int(i) for i in input().split()])
    print(s[3])