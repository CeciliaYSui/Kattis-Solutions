n = input().split()
n = sorted(list(map(int, n)))
s = input()
print(n[ord(s[0])-65], n[ord(s[1])-65], n[ord(s[2])-65])