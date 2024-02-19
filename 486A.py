# https://codeforces.com/problemset/problem/486/A

num = int(input())

print(num//2 if num % 2 == 0 else -1*(num//2+1))
