# https://codeforces.com/contest/1914/problem/B

for _ in range(int(input())):

    length, excited = list(map(int, input().split()))

    numList = list(range(1, length+1))
    ansList = []

    # adding a specified amount of problems in order
    for i in range(excited):
        ansList.append(numList.pop())

    # adding the rest of the problems in reverse order
    ansList += numList
    ansList.reverse()

    print(' '.join(list(map(str, ansList))))
