from statistics import mode, median
n, t = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
flag = False
s = sorted(s)
if t == 1:                      # O(nlogn)
    tmp = 0 
    for i in range(len(s)):     # O(n)
        x = 7777 - s[i]
        l = i
        h = len(s)-1
        if s[i] == tmp: 
            continue 
        tmp = s[i] 
        while l <= h:           # O(logn)
            mid = (l+h)//2
            if s[mid] == x: 
                flag = True
                print("Yes")
                break
            elif s[mid] < x: 
                l = mid + 1
            else:  # s[mid] > x: 
                h = mid - 1
        if flag: 
            break
    if not flag: 
        print("No")
elif t == 2: 
    print("Unique" if len(set(s)) == len(s) else "Contains duplicate") 
# Wrong Answer --> 
elif t == 3: 
    if n%2 != 0: 
        val = s[n//2]
        print(val if (s.count(val) > n/2) else -1)
    else: 
        v1 = s[n//2-1]
        v2 = s[n//2]
        if v1 != v2: 
            print(-1)
        else: 
            print(v1 if (s.count(v1) > n/2) else -1)
elif t == 4: 
    if n%2 != 0: 
        print(s[n//2])
    else: 
        print(s[n//2-1], s[n//2])
else: 
    for i in s: 
        if 100 <= i <= 999: 
            print(i, end = " ")
        elif i > 999: 
            break