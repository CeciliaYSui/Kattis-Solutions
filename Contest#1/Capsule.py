# Author ------------- Cecilia Y. Sui 
# Course ------------- Competition Programming 
# Program ------------ Sprint Problem #1

import math
n = int(input())
p = math.pi
for i in range (n):
    s = [float(i) for i in input().split()]
    r = s[0]/100/2
    l = (s[1] - s[0])/100
    rin = r - 0.005
    Vout = p * (r**2) * l + 4 * p * (r**3) / 3
    Vin = p * (rin**2) * l + 4 * p * (rin**3) / 3
    print("%.7f %.7f" % ((Vout - Vin)*1000, Vin*1000))