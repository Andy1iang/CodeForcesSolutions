# https://codeforces.com/contest/1873/problem/D

for _ in range(int(input())):

    leng, skip = list(map(int, input().split()))
    cells = input()

    # at each new mark, erase the longest length possible
    i = 0
    count = 0
    while i < leng:
        if cells[i] == 'B':
            count += 1
            i += skip
        else:
            i += 1

    print(count)
