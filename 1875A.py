# https://codeforces.com/contest/1875/problem/A

for _ in range(int(input())):

    a, b, n = list(map(int, input().split()))
    tools = list(map(int, input().split()))

    # keep using a tool whenever the timer hits 1
    total = b
    for t in tools:
        # a-1 because the timer ticks after the tool is used
        total += min(t, a-1)

    print(total)
