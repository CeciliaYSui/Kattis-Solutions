n = int(input())
for i in range(n):
    a,b,c,d = input().split()
    print(abs(ord(c)-ord(a)) + abs(int(d)-int(b)))