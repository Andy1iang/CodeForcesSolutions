# https://codeforces.com/contest/1971/problem/B

for _ in range(int(input())):

    s = input()

    # going through all letters until we find different neighboring letters
    # then swapping them and printing the result
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            print('YES')
            print(f'{s[:i-1:]}{s[i]}{s[i-1]}{s[i+1::]}')
            break

    else:
        print('NO')
