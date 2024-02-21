# https://codeforces.com/contest/1927/problem/B

for _ in range(int(input())):

    leng = int(input())
    trace = list(map(int, input().split()))
    used = [0] * 26
    resStr = []

    # for each letter, if it has been used the right amount of times, add it
    # taking advantage of the fact that letters have ASCII representation
    for i in trace:
        for j in range(26):
            if i == used[j]:
                used[j] += 1
                resStr.append(chr(j+97))
                break

    print(''.join(resStr))
