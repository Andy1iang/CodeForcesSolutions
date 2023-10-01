#https://codeforces.com/contest/96/problem/A

lineUp = input()
streak = 0
temp = -1

for i in lineUp:
    if i == temp:
        streak+=1
        if streak == 7:
            print('YES')
            exit()
    else:
        streak = 1
        temp = i
        
print("NO")