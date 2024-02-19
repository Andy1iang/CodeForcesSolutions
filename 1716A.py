# https://codeforces.com/contest/1716/problem/A

import math

for _ in range(int(input())):
    
    coord = abs(int(input()))
    
    if coord == 1:
        print(2)
        continue
    
    else:
        print(math.ceil(coord/3))