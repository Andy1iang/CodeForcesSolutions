# https://codeforces.com/contest/110/problem/A

num = input()
total = num.count('4') + num.count('7')

print('YES' if total == 4 or total == 7 else 'NO')