# https://codeforces.com/contest/1999/problem/B

for _ in range(int(input())):

    a, b, c, d = map(int, input().split())
    res = 0

    # simulating the match-ups

    if a < c:
        pass
    elif a == c:
        if b > d:
            res += 1
    else:
        if b >= d:
            res += 1

    if b < c:
        pass
    elif b == c:
        if a > d:
            res += 1
    else:
        if a >= d:
            res += 1

    # times two because we can either choose A or B first
    print(res*2)
