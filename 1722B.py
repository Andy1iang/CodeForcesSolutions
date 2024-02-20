# https://codeforces.com/contest/1722/problem/B

for i in range(int(input())):
    
    columns = int(input())
    row1 = input()
    row2 = input()
    for column in range(columns):
        if (row1[column] == 'R' and row2[column] == 'R') or (row1[column] != 'R' and row2[column] != 'R'):
            pass
        else:
            print('NO')
            break
    else:
        print('YES')
