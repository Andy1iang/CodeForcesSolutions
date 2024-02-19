#https://codeforces.com/contest/1907/problem/D

for _ in range(int(input())):
    
    leng = int(input())
    segments = []
    for x in range(leng):
        segments.append(list(map(int,input().split())))
    
    left, right = 0, int(1E10)
    #binary search
    while left <= right:
        mid = (left + right)//2
        lEnd, rEnd = 0, mid #setting the right end to 'k' value
        able = True
        
        #each segment of the array
        for seg in segments:
            if rEnd < seg[0] or lEnd > seg[1]: #if not able to make the jump
                able = False
                break
              
            lEnd = max(lEnd,seg[0]) 
            rEnd = min(rEnd,seg[1])
            
            lEnd = max(lEnd-mid,0)
            rEnd = rEnd + mid
        
        if able is True:
            right = mid-1
        else:
            left = mid+1
    
    print(left)
            