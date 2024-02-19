# https://codeforces.com/problemset/problem/122/A

divisors = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 774, 777]

n = int(input())

for number in divisors:
    if n % number == 0:
        print('YES')
        break
else:
    print('NO')
