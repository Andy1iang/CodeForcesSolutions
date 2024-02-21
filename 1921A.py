# https://codeforces.com/contest/1921/problem/A

for _ in range(int(input())):

    # getting just the x-coordinate (always a square)
    coords = [list(map(int, input().split()))[0] for x in range(4)]

    # checking with inputs have different x-coordinates, find area
    if coords[0] != coords[1]:
        print(abs(coords[0] - coords[1])**2)

    elif coords[0] != coords[2]:
        print(abs(coords[0] - coords[2])**2)
