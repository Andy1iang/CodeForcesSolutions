#https://codeforces.com/contest/318/problem/A

import math
limit, idx = input().split()
limit, idx = int(limit), int(idx)

if idx>math.ceil(limit/2): #starting directly in evens if index is > half of range
    idx -= math.ceil(limit/2)
    print(2*idx)
else:
    print(2*idx-1)