# https://codeforces.com/contest/1971/problem/A

# I <3 Python
for _ in range(int(input())):

    a, b = list(map(int, input().split()))

    print(f'{min(a, b)} {max(a, b)}')
