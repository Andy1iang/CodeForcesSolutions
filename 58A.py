#https://codeforces.com/problemset/problem/58/A

chat = input()

letterOrder = ['h','e','l','l','o']
for letter in chat:
    if letter == letterOrder[0]:
        letterOrder.pop(0)
        if len(letterOrder) == 0:
            print('YES')
            exit()

print('NO')