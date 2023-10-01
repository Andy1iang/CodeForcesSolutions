#https://codeforces.com/contest/1/problem/A

import math
l , w , s = input().split()
l , w, s = int(l), int(w), int(s) #l = length ; w = width ; s = side length of stone

total = math.ceil(l/s) * math.ceil(w/s)

print(total if total>1 else 1)