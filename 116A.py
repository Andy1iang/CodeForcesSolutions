#https://codeforces.com/contest/116/problem/A

max = 0
total = 0

for i in range(int(input())):
    off, on = input().split()
    off, on = int(off),int(on)
    
    total = total + on - off
    if total > max:
        max = total
        
print(max)