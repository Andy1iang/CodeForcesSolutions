# https://codeforces.com/contest/2000/problem/A

for _ in range(int(input())):

    num = input()

    # checking if the first two letters match
    if num[0:2] != '10':
        print('NO')

    # checking if there's more numbers
    elif len(num) <= 2:
        print('NO')

    # checking if there's a leading zero
    elif num[2] == '0':
        print('NO')

    # checking if the rest of the numbers are > 1
    elif int(num[2::]) <= 1:
        print('NO')

    # if all conditions pass
    else:
        print('YES')
