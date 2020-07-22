s = input().split()
x = int(s[0])
y = int(s[1])
n = int(s[2])

for i in range(1, n+1):
    if (i % x == 0) & (i % y == 0): 
        print("FizzBuzz")
    elif i % y == 0: 
        print("Buzz")
    elif i % x == 0:
        print("Fizz")
    else: 
        print(i)
