# https://codeforces.com/contest/1921/problem/B

for _ in range(int(input())):

    boxes = int(input())
    initial = input()
    final = input()

    # two cases of whether cats need to be taken out or put into boxes

    if initial.count('1') < final.count('1'):
        count = 0
        for top, bottom in zip(initial, final):
            # only considering cases where it needs to be added
            # case of taking out will never happen
            # so moving is considered the right amount of times
            if top == '0' and bottom == '1':
                count += 1

        print(count)

    else:
        count = 0
        for top, bottom in zip(initial, final):
            # same logic as above, but flipped
            if top == '1' and bottom == '0':
                count += 1

        print(count)
