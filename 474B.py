# https://codeforces.com/contest/474/problem/B

# worms piles and the number of worms piles
n = int(input())
a = list(map(int, input().split()))

# creating prefix sum array
idx = [a[0]]
for i in range(1, len(a)):
    idx.append(a[i]+idx[i-1])

# each test case
j = int(input())
labels = list(map(int, input().split()))

# binary search for each test case
for label in labels:

    left = 0
    right = n
    mid = (left+right)//2

    while left < right:
        
        if label == idx[mid]:
            break
        elif label < idx[mid]:
            right = mid
        elif label > idx[mid]:
            left = mid+1
            
        mid = (left+right)//2
        
    # adding one because indexing starts at 1
    print(mid+1)
