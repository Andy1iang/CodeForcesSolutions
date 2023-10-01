#https://codeforces.com/contest/263/problem/A

'''
Learned:
--int() casting does not work with whitespace between numbers
--int() casting gets rid of leading 0s but not trailing 0s
'''

x = 0
y = 0
for i in range(5):
    line = input().replace(' ','') #getting rid of extra whitespace
    if (int(line)) != 0: #checking the line has a 1 in it
        x = line.index('1')+1 #finding column index of the 1
        y = i+1
        break
 
#x and y differences of index of 1 and the 3rd(middle) row and column
x = abs(3-x) 
y = abs(3-y)
print(x+y)