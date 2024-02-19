# https://codeforces.com/problemset/problem/466/A

import math

rides, bundleTix, singleTixCost, bundleTixCost = list(map(int, input().split()))

# checking if single ticket costs less than cost per ride for bundles
if singleTixCost <= bundleTixCost/bundleTix:
    print(singleTixCost*rides)

else:
    # buying as many bundle tickets as possible, then spend minimum on the last tickets
    print((rides//bundleTix)*bundleTixCost +
          min(bundleTixCost, (rides % bundleTix)*singleTixCost))
