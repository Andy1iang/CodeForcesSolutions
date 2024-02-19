#https://codeforces.com/contest/1904/problem/A

for _ in range(int(input())):
    
    dx,dy = list(map(int,input().split()))
    kx,ky = list(map(int,input().split()))
    qx,qy = list(map(int,input().split()))
    
    kCells:set = set()
    qCells:set = set()
    
    kCells.add((kx-dx,ky-dy))
    kCells.add((kx-dx,ky+dy))
    kCells.add((kx+dx,ky-dy))
    kCells.add((kx+dx,ky+dy))
    kCells.add((kx-dy,ky-dx))
    kCells.add((kx-dy,ky+dx))
    kCells.add((kx+dy,ky-dx))
    kCells.add((kx+dy,ky+dx))
    
    qCells.add((qx-dx,qy-dy))
    qCells.add((qx-dx,qy+dy))
    qCells.add((qx+dx,qy-dy))
    qCells.add((qx+dx,qy+dy))
    qCells.add((qx-dy,qy-dx))
    qCells.add((qx-dy,qy+dx))
    qCells.add((qx+dy,qy-dx))
    qCells.add((qx+dy,qy+dx))
    
    print(len(qCells.intersection(kCells)))