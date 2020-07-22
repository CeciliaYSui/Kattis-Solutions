flag = True
while True: 
    try: 
        s = input().split()
        a,b = int(s[0]), int(s[1])
        print(abs(a-b))
    except EOFError: 
        break; 