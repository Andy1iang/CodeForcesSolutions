# https://codeforces.com/contest/1928/problem/B

for _ in range(int(input())):

    n = int(input())
    
    # getting rid of the duplicate elements 
    # because they'll never be the same after the addition
    arr = sorted(list(map(int, set(input().split()))))

    left = 0
    maxLeng = 0

    # two pointer method to find the longest streak of numbers within the length requirement
    for i in range(len(arr)):

        while arr[i] - arr[left] >= n:

            left += 1

        if i-left+1 > maxLeng:
            maxLeng = (i-left)+1

    print(maxLeng)
