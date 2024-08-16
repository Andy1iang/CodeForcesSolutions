# https://codeforces.com/contest/2000/problem/C

for _ in range(int(input())):

    length = int(input())
    nums = list(map(int, input().split()))

    for i in range(int(input())):
        letters = input()
        lrel = {}  # letter correspondence to numbers
        nrel = {}  # number correspondence to letters

        # goto next iteration if length don't match
        if len(letters) != length:
            print('NO')
            continue

        for j in range(length):

            # if letter is already seen
            if (letters[j] in lrel):
                # if letter corresponds to the current number
                if lrel[letters[j]] != nums[j]:
                    print('NO')
                    break

            # if number is already seen
            elif (nums[j] in nrel):
                # if number corresponds to the current letter
                if nrel[nums[j]] != letters[j]:
                    print('NO')
                    break

            # if number and letter both haven't been seen, add to the dictionaries
            else:
                lrel[letters[j]] = nums[j]
                nrel[nums[j]] = letters[j]

        # if all letters pass
        else:
            print('YES')
