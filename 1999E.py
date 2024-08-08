# https://codeforces.com/contest/1999/problem/E

# all the powers of 3
lst = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441]

for i in range(int(input())):

    l, r = list(map(int, input().split()))
    res = 0

    # finding how many divs of 3 to get to 0
    curr = 0
    for i in range(0, 14):
        if l < lst[i]:
            curr = i
            break

    # adding amount operations to get minimum number to 0
    res += curr

    # add in the rest of the operations needed
    for i in range(curr, 14):

        # if r is less than the cutoff
        # add operations times amount of numbers we have left
        if r < lst[i]:
            res += (i * (r - l + 1))
            break

        # else add amount of numbers in between two powers of 3
        else:
            res += (i * (lst[i] - l))

        # moving our left pointer to the new cutoff
        l = lst[i]

    print(res)
