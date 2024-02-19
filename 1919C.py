#https://codeforces.com/contest/1919/problem/C

for _ in range(int(input())):
    
    input()
    
    nums = list(map(int,input().split()))
    
    #make s always smaller than t
    s = 2E8
    t = 2E8
    
    count = 0
    
    for num in nums:
        
        if s>t:
            s,t = t,s
            
        if s >= num:
            s = num
            
        elif t >= num:
            t = num
            
        else:
            s = num
            count += 1
    
    print(count)