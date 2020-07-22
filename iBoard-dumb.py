flag = True
while True: 
    try: 
        s = input()
        cnt0, cnt1 = 0, 0
        for i in range (len(s)):
            tmp = "{:07b}".format(ord(s[i]))
            cnt0 += tmp.count("0")
            cnt1 += tmp.count("1")
        if (cnt0%2 != 0) | (cnt1%2 != 0):
            print("trapped")
        else: 
            print("free")
    except EOFError:
        break; 