# https://codeforces.com/contest/1915/problem/A

for i in range(int(input())):

    # taking input (3 numbers in string format)
    nums: list[str] = input().split()

    # printing number that only appears once
    if nums[0] == nums[1]:
        print(nums[2])

    elif nums[1] == nums[2]:
        print(nums[0])

    elif nums[0] == nums[2]:
        print(nums[1])
