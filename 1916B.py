#https://codeforces.com/contest/1916/problem/B

import math

for _ in range(int(input())):
    
    a,b = list(map(int,input().split()))
    
    res = int(math.lcm(a,b))
    
    if res == b:
        res *= (b/a)
        
    print(int(res))