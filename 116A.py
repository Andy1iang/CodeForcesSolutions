# https://codeforces.com/contest/116/problem/A

max = 0
total = 0

for i in range(int(input())):
    off, on = list(map(int, input().split()))

    total += (on - off)  # finding the new total number of people on train

    if total > max:
        max = total

print(max)
