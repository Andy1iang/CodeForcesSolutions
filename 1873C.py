# https://codeforces.com/contest/1873/problem/C

# manually created point chart
pointChart = [[1]*10, [1]+[2]*8+[1], [1]+[2]+[3]*6+[2]+[1],
              [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]]
pointChart = pointChart + pointChart[::-1]

for _ in range(int(input())):

    points = 0

    arrows = [list(input()) for _ in range(10)]

    for i in range(10):
        for j in range(10):

            if arrows[i][j] == 'X':
                points += pointChart[i][j]

    print(points)
