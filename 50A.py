# https://codeforces.com/contest/50/problem/A

size = input().split()
size = int(size[0]) * int(size[1])

print(size//2) # can't be placed if only one space left (odd)
