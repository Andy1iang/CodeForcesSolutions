#https://codeforces.com/contest/69/problem/A

x,y,z = 0,0,0

for i in range(int(input())):
    dx,dy,dz = list(map(int,input().split())) 
    x += dx
    y += dy
    z += dz
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")