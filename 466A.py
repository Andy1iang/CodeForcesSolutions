#https://codeforces.com/problemset/problem/466/A

import math

rides, bundleTix, singleTixCost, bundleTixCost = input().split()
rides, bundleTix, singleTixCost, bundleTixCost = int(rides), int(bundleTix), int(singleTixCost), int(bundleTixCost)

if singleTixCost <= bundleTixCost/bundleTix: #checking if single ticket costs less than cost per ride for bundles
    print(singleTixCost*rides)
    exit()
    
elif bundleTix >= rides and bundleTixCost < rides*singleTixCost: #checking if tickets can all be bought in bundles
    print(bundleTixCost)
    exit()
    
elif bundleTixCost <= singleTixCost: #checking if single tickets cost more than bundles
    print(math.ceil(rides/bundleTix)*bundleTixCost)
    exit()
    
print( (rides//bundleTix)*bundleTixCost + (rides%bundleTix)*singleTixCost )