# https://codeforces.com/contest/1030/problem/A

'''
Lesson: 
0 is evaluated to False
'''

input()  # input not needed

if int(input().replace(' ', '')):  # if int is not 0, expression is evaluated to True
    print("HARD")
else:
    print("EASY")
