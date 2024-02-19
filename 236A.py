# https://codeforces.com/contest/236/problem/A

if len(set([*input()])) % 2 == 0:  # [*] unpacks input, set() gets rid of duplicates
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
