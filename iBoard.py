flag = True
while True: 
    try: 
        s = input()
        cnt0, cnt1 = True, True
        for i in range (len(s)):
            tmp = "{:07b}".format(ord(s[i]))
            for bit in tmp: 
                if bit == '0':
                    cnt0 = not cnt0
                else:
                    cnt1 = not cnt1
        print("free" if (cnt0&cnt1) else "trapped")
    except EOFError:
        break; 