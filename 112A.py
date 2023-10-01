#https://codeforces.com/contest/112/problem/A

'''
Learned:
--Strings can directly be compared with operators
'''

first = input().lower()
second = input().lower()
print(-1 if first<second else 1 if first>second else 0)