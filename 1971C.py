# https://codeforces.com/contest/1971/problem/C

for _ in range(int(input())):

    a, b, c, d = map(int, input().split())

    # keeping track of which string we've encountered throughout the clock
    first = None
    second = None
    third = None

    for i in range(1, 13):

        if first is None:
            if a == i or b == i:
                first = 'Alice'
            elif c == i or d == i:
                first = 'Bob'

        elif second is None:
            if a == i or b == i:
                second = 'Alice'
            elif c == i or d == i:
                second = 'Bob'

        elif third is None:
            if a == i or b == i:
                third = 'Alice'
                break
            elif c == i or d == i:
                third = 'Bob'
                break

    # they will only intersect if the third one we intersect is the same string as the first
    print('YES' if first == third else 'NO')
