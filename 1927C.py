# https://codeforces.com/contest/1927/problem/C

for _ in range(int(input())):
    
    n, m ,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a = set(filter(lambda x: x<=k, a))
    b = set(filter(lambda x: x<=k, b))
    
    dupes = a.intersection(b)
    dupeLen = len(dupes)
    aUnique = len(a) - dupeLen
    bUnique = len(b) - dupeLen
    aDupe = k/2 - aUnique
    bDupe = k/2 - bUnique
    
    if aUnique <= k/2 and bUnique <= k/2 and aUnique + bUnique + dupeLen >= k and aDupe+bDupe <= dupeLen:
        print("YES")
    else:
        print("NO")
    
    