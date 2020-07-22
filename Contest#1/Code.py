# Author ------------- Cecilia Y. Sui 
# Course ------------- Competition Programming 
# Program ------------ Sprint Problem #5

n = int(input())
s = "1234567890-qwertyuiop[asdfghjkl;\'zxcvbnm,./!@#$%^&*()_QWERTYUIOP{ASDFGHJKL:\"ZXCVBNM<>?"
for i in range(n):
    tmp = input()
    out = ""
    for j in range(len(tmp)): 
        loc = s.find(tmp[j])
        out += tmp[j] if (loc<0) else (s[loc-1])
    print(out)