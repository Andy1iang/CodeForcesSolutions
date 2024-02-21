# https://codeforces.com/contest/1916/problem/B

import math

for _ in range(int(input())):

    a, b = list(map(int, input().split()))

    # finding least common multiple
    res = int(math.lcm(a, b))

    # if result is the same as b, then manipulate the result
    if res == b:
        res *= (b/a)

    print(int(res))
