#https://codeforces.com/contest/231/problem/A

count = 0

for i in range(int(input())):
    if input().count('0') <= 1:
        count +=1
        
print(count)