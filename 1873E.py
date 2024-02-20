# https://codeforces.com/contest/1873/problem/E

for _ in range(int(input())):

    columns, water = list(map(int, input().split()))
    corals = list(map(int, input().split()))

    #doing binary search on optimal height of water
    lo, hi = 0, int(1E12)
    while lo <= hi:

        target = (hi+lo)//2

        #finding how much water can fit
        sum = 0
        for coral in corals:
            sum += int(max(target-coral, 0))

        if sum == water:
            print(target)
            break

        elif sum < water:
            lo = target + 1

        elif sum > water:
            hi = target - 1

    else:
        print(hi)
