# https://codeforces.com/contest/1916/problem/A

for _ in range(int(input())):

    leng, missing = list(map(int, input().split()))

    # getting the product of the given numbers
    nums = list(map(int, input().split()))
    product = 1
    for i in nums:
        product *= i

    # getting a result and checking if 2023 is divisible by it
    result = 2023/product

    # if not
    if result % 1 != 0:
        print('NO')
        continue

    # if yes
    ansList = [str(int(result))]
    ansList += ['1'] * (missing-1)  # pad additional places with 1s

    print('YES')
    print(' '.join(ansList))
