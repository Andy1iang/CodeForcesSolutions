# https://codeforces.com/contest/71/problem/A

for i in range(int(input())):
    x = input()
    if len(x) <= 10:
        print(x)
    else:
        # taking the first letter, length, and last letter
        print(f'{x[0]}{len(x)-2}{x[-1]}')
