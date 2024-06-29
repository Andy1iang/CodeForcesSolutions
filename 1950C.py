# https://codeforces.com/contest/1950/problem/C

for _ in range(int(input())):

    h, m = map(int, input().split(":"))

    # account for midnight
    if h == 0:
        print(f'12:{m:02d} AM')

    # no conversion needed
    elif h < 12:
        print(f'{h:02d}:{m:02d} AM')

    # account for noon
    elif h == 12:
        print(f'{h:02d}:{m:02d} PM')

    # account for the afternoon conversion
    else:
        print(f'{h-12:02d}:{m:02d} PM')