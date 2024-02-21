# https://codeforces.com/contest/1915/problem/B

for i in range(int(input())):  # taking 3 lines of input

    # trying out type hinting
    line1: str = input()
    line2: str = input()
    line3: str = input()

    # checking which line the question mark is in, then check which letter is missing
    if '?' in line1:
        if 'A' not in line1:
            print('A')
        elif 'B' not in line1:
            print('B')
        elif 'C' not in line1:
            print('C')

    elif '?' in line2:
        if 'A' not in line2:
            print('A')
        elif 'B' not in line2:
            print('B')
        elif 'C' not in line2:
            print('C')

    elif '?' in line3:
        if 'A' not in line3:
            print('A')
        elif 'B' not in line3:
            print('B')
        elif 'C' not in line3:
            print('C')
