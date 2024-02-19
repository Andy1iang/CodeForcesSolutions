# https://codeforces.com/contest/677/problem/A

friends, height = list(map(int,input().split()))
people = list(map(int, input().split()))

total = 0
for i in people: 
    if i > height:
        total += 2
    else:
        total += 1

print(total)
