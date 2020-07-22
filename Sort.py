from collections import Counter 
n, c = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]

# stable sort to preserve original order of inputs 
result = [item for items, c in Counter(s).most_common() for item in [items] * c] 
[print(i, end = " ") for i in result]