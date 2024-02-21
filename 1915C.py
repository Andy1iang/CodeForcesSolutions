# https://codeforces.com/contest/1915/problem/C

for i in range(int(input())):

    input()  # unnecessary input

    blocks: int = sum(list(map(int, input().split())))  # getting sum of all blocks

    # checking if the number of blocks is a perfect square
    if int((blocks**0.5))**2 == blocks:
        print('YES')
    else:
        print('NO')
