# https://codeforces.com/problemset/problem/58/A

chat = input()

letterOrder = ['h', 'e', 'l', 'l', 'o']
for letter in chat:
    if letter == letterOrder[0]:
        # checks the next letter needed, pops it off it matched
        letterOrder.pop(0)
        if len(letterOrder) == 0:  # true if all letters are popped in order
            print('YES')
            break
else:  # runs if loops ends naturally
    print('NO')
