#https://codeforces.com/contest/546/problem/A

k,n,w = input().split() # k = cost of first banana; n = dollars; w = bananas wanted
k,n,w = int(k), int(n), int(w)
total = k*((1+w)*(w/2)) # k times n*(1+n)/2
if total > n:
    print(int(total-n))
else:
    print(0)