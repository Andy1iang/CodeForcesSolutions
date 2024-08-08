# https://codeforces.com/contest/1999/problem/D

for _ in range(int(input())):
    a = list(input())
    b = input()
    bPtr = 0
    completed = False

    # looping through each character of A
    for i in range(len(a)):

        if a[i] == '?':

            if completed:
                # if completed, replace all remaining '?' with 'x'
                a[i] = 'x'

            else:
                # if not, replace with next unmatched character in B
                a[i] = b[bPtr]
                bPtr += 1
                if bPtr == len(b):
                    completed = True

        # if letter is not '?'
        # and if current letter in A matches next unmatched character in B
        # we increment bPtr
        elif not completed and a[i] == b[bPtr]:
            bPtr += 1
            if bPtr == len(b):
                completed = True

    if completed:
        print('YES')
        print(''.join(a))

    else:
        print('NO')
