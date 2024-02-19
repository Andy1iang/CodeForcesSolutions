# https://codeforces.com/contest/467/problem/A

count = 0
for i in range(int(input())):

    p, q = list(map(int, input().split()))
    if q > p+1:
        count += 1

print(count)
