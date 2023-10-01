#https://codeforces.com/contest/677/problem/A

friends, height = input().split()
friends, height, = int(friends),int(height)
people = list(map(int,input().split()))

total = 0
for i in people:
    if i>height:
        total +=1
    total+=1
    
print(total)