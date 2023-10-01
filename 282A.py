#https://codeforces.com/contest/282/problem/A

count = 0
for i in range(int(input())):
    if '+' in input():
        count +=1
    else:
        count -=1
        
print(count)