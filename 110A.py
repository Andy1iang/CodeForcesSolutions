#https://codeforces.com/contest/110/problem/A

num = input()
total = str(num.count('4') + num.count('7'))

#checking if there's any other number than 4 or 7
for x in total:
    if x != '4' and x!='7':
        print('NO')
        exit()
    
print('YES')