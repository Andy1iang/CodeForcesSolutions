# https://codeforces.com/contest/1928/problem/B

for _ in range(int(input())):

    n = int(input())
    arr = sorted(list(map(int, set(input().split()))))

    left = 0
    maxLeng = 0

    for i in range(len(arr)):

        while arr[i] - arr[left] >= n:

            left += 1

        if i-left+1 > maxLeng:
            maxLeng = (i-left)+1

    print(maxLeng)
