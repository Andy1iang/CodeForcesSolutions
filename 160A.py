#https://codeforces.com/contest/160/problem/A

input()
coins = list(map(int,input().split())) #splitting input into list of ints
total = sum(coins)/2
coins.sort()

count = 0
while total >= 0:
    total-=coins.pop()
    count+=1
    
print(count)