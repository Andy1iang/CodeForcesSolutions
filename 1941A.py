# https://codeforces.com/contest/1941/problem/A

for _ in range(int(input())):

    m, n, k = map(int, input().split())

    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    l = {}
    r = {}

    # making dictionaries of counts of different coins in each pocket
    for i in left:
        if i < k:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1

    for i in right:
        if i < k:
            if i in r:
                r[i] += 1
            else:
                r[i] = 1

    # nested loop to find all combinations that yield the solution
    total = 0
    for coin, cnt in l.items():
        for coin2, cnt2 in r.items():
            if coin + coin2 <= k:
                total += cnt * cnt2

    print(total)