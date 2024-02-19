# https://codeforces.com/contest/344/problem/A

groups = 0
last = '-1'

for i in range(int(input())):

    new = input()

    if new != last:  # new group if 10 is followed by 01, or vice versa
        groups += 1
        last = new

    # 'last' doesn't need to be updated otherwise because it's the same

print(groups)
