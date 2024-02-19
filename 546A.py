# https://codeforces.com/contest/546/problem/A

k, n, w = list(map(int,input().split()))  # k = cost of first banana; n = dollars; w = bananas wanted
total = int(k*((1+w)*(w/2)))  # k times n*(1+n)/2

if total > n:
    print(total-n)
else:
    print(0)
