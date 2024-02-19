# https://codeforces.com/contest/266/problem/B

spots, time = list(map(int, input().split()))
line = list(input())  # unpacking into list

for i in range(time):

    changed = False

    for j in range(spots-1):

        if changed == True:  # checking if the boy had just switched
            changed = False
            continue

        else:
            if line[j] == "B" and line[j+1] == "G":
                changed = True
                # switching spots if case is true
                line[j], line[j+1] = 'G', 'B'

print(''.join(line))
