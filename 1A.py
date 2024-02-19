# https://codeforces.com/contest/1/problem/A

import math
l, w, s = list(map(int,input().split()))
# l = length ; w = width ; s = side length of stone

#extra side length has to be used (for each side)
total = math.ceil(l/s) * math.ceil(w/s)

print(total)
