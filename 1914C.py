#https://codeforces.com/contest/1914/problem/C

for _ in range(int(input())):

    available, quests = list(map(int, input().split()))
    firstXP = list(map(int, input().split()))
    repeatXP = list(map(int, input().split()))

    for i in range(1, available):
        firstXP[i] += firstXP[i-1]
        if repeatXP[i-1] > repeatXP[i]:
            repeatXP[i] = repeatXP[i-1]

    maxXP = 0

    for i in range(min(available, quests)):
        XP = firstXP[i] + (repeatXP[i] * (quests-i-1))
        if XP > maxXP:
            maxXP = XP

    print(maxXP)
