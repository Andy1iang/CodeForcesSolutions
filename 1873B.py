# https://codeforces.com/contest/1873/problem/B

for i in range(int(input())):

    input()  # unnecessary input
    nums = list(map(int, input().split()))
    les = min(nums)  # lowest number
    nums[nums.index(les)] = les+1

    total = 1
    for k in nums:
        total *= k

    print(total)
