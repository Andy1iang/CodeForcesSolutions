# https://codeforces.com/contest/1927/problem/C

for _ in range(int(input())):

    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # only letter the letter that meet requirements, and throwing them in a set (only has to be used once)
    a = set(filter(lambda x: x <= k, a))
    b = set(filter(lambda x: x <= k, b))

    # finding how many duplicates there are and how many uniques there are
    dupes = a.intersection(b)
    dupeLen = len(dupes)
    aUnique = len(a) - dupeLen
    bUnique = len(b) - dupeLen
    aDupe = k/2 - aUnique
    bDupe = k/2 - bUnique

    # work if and only if these cases are met
    # enough numbers
    # each one doesn't have too many uniques
    # needed amount of dupes are available
    if aUnique <= k/2 and bUnique <= k/2 and aUnique + bUnique + dupeLen >= k and aDupe+bDupe <= dupeLen:
        print("YES")
    else:
        print("NO")
