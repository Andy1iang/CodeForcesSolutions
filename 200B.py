# https://codeforces.com/problemset/problem/200/B

# disgusting one-liner made possible by Python
print(1/(int(input())/(lambda x: x if x > 0 else 1E-9)(sum(list(map(int, input().split()))))))
