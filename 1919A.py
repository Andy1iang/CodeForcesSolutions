# https://codeforces.com/contest/1919/problem/A

for _ in range(int(input())):
    # one liner ;)
    print("Bob" if sum(list(map(int, input().split()))) % 2 == 0 else "Alice")
