# https://codeforces.com/contest/1999/problem/C

for _ in range(int(input())):

    tasks, shower, total = map(int, input().split())

    prev = 0
    found = False

    # going through each time segment to see if we have enough time
    for i in range(tasks):
        start, end = map(int, input().split())

        if not found:
            if (start - prev) >= shower:
                found = True
            prev = end

    if found:
        print('YES')

    else:
        # if we didn't have enough time, check if can shower at the end of the day
        if (total - prev) >= shower:
            print('YES')
        else:
            print('NO')
