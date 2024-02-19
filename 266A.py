# https://codeforces.com/contest/266/problem/A

i = 0
stoneLen = int(input())
stones = input()

# counting occurrences of consecutive stones
count = 0
for i in range(1, stoneLen):
    if stones[i] == stones[i-1]:
        count += 1

print(count)
