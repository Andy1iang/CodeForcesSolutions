# https://codeforces.com/contest/1919/problem/C

for _ in range(int(input())):

    input()  # unnecessary input

    nums = list(map(int, input().split()))

    # starting at very large number
    s = 2E8
    t = 2E8

    count = 0

    for num in nums:

        # make s always smaller or equal to t
        if s > t:
            s, t = t, s

        # choosing the most optimal grouping each time
        if s >= num:
            s = num

        elif t >= num:
            t = num

        else:
            s = num
            count += 1

    print(count)
