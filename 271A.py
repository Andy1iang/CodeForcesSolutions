# https://codeforces.com/contest/271/problem/A

year = int(input())+1

while len(set(str(year))) < 4:  # checking if all numbers are distinct
    year += 1

print(year)
