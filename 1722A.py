#https://codeforces.com/contest/1722/problem/A

'''
Learned:
else statement after for-loop only executes if for-loop naturally ended (not broken out of)
'''

spelling = ['T','i','m','u','r']

for i in range(int(input())):
    
    if input() != '5':
        input()
        print('NO')
        continue

    name = input()
    
    for letter in spelling:
        if letter not in name:
            print('NO')
            break
    else:
        print('YES')