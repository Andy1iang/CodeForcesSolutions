# https://codeforces.com/contest/1921/problem/D

for _ in range(int(input())):
    
    n,m = list(map(int,input().split()))
    nList = sorted(list(map(int,input().split())))
    mList = sorted(list(map(int,input().split())))
    nLPoint = 0
    nRPoint = -1
    mLPoint = 0
    mRPoint = -1
    
    diff = 0
    for i in range(n):
        if abs(nList[nLPoint] - mList[mRPoint]) > abs(nList[nRPoint] - mList[mLPoint]):
            diff += abs(nList[nLPoint] - mList[mRPoint])
            nLPoint += 1
            mRPoint -= 1
        else:
            diff += abs(nList[nRPoint] - mList[mLPoint])
            mLPoint += 1
            nRPoint -= 1
            
    print(diff)