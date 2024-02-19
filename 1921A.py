# https://codeforces.com/contest/1921/problem/A

for _ in range(int(input())):
    
    coords = [list(map(int,input().split()))[0] for x in range(4)]
    
    if coords[0] != coords[1]:
        print(abs(coords[0] - coords[1])**2)
        
    elif coords[0] != coords[2]:
        print(abs(coords[0] - coords[2])**2)