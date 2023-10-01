#https://codeforces.com/contest/977/problem/A

res,times = list(map(int,input().split())) #splitting input into int types in a list
 
for i in range(times):
    if res%10 == 0:
        res = res // 10
    else:
        res -= 1
        
print(res)