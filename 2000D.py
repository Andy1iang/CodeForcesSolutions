# https://codeforces.com/contest/2000/problem/D

for _ in range(int(input())):

    length = int(input())
    vals = list(map(int, input().split()))
    letters = input()

    # finding the first and last L and R
    # if not present, print 0 and continue

    for i in range(length):
        if letters[i] == 'L':
            l = i
            break
    else:
        print(0)
        continue

    for i in range(length - 1, -1, -1):
        if letters[i] == 'R':
            r = i
            break
    else:
        print(0)
        continue

    if l > r:
        print(0)
        continue

    # getting the total between first L and last R
    # then subtracting the subtractions of all the L and R in between

    total = sum(vals[l:r+1])
    full = total
    sub = 0

    # while we can still have values between L and R
    while l < r:

        # adding values to subtract (values we should not have added)
        sub += vals[l] + vals[r]

        # finding the next L and R
        # if conditions not met, break

        i = l+1
        while i < r and letters[i] != 'L':
            sub += vals[i]
            i += 1

        if i == r:
            break

        j = r-1
        while j > l and letters[j] != 'R':
            sub += vals[j]
            j -= 1

        if j == l:
            break

        if i >= j:
            break

        # if conditions met
        # add the next total and update L and R
        total = (total + full) - sub
        l, r = i, j

    print(total)
