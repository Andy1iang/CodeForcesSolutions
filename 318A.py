# https://codeforces.com/contest/318/problem/A

import math
limit, idx = list(map(int, input().split()))

# testing out one line if statements
print(2*(idx - math.ceil(limit/2)) if idx > math.ceil(limit/2) else (2*idx)-1)
