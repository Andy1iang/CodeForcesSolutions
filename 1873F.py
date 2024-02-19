# https://codeforces.com/contest/1873/problem/F

for _ in range(int(input())):
    
    trees , k = list(map(int,input().split()))
    fruits = list(map(int,input().split()))
    heights = list(map(int,input().split()))
    
    streaks = [0]
    for i in range(trees-2,-1,-1):
        if heights[i] % heights[i+1] == 0:
            streaks.append(streaks[-1]+1)
        else:
            streaks.append(0)     
    streaks.reverse()
    
    totFruits = [fruits[0]]
    for i in range(1,trees):
        totFruits.append(fruits[i]+totFruits[-1])

    maxStreak = 0
    
    for i in range(trees):
        
        l, r, ans = i, i+streaks[i], 0
        
        while l <= r:
            mid = (l+r)//2
            if i != 0:
                if totFruits[mid] - totFruits[i-1] <= k:
                    ans = mid - i + 1
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                
                if totFruits[mid] <= k:
                    ans = mid - i + 1
                    l = mid + 1
                else:
                    r = mid - 1
                
        
        maxStreak = max(maxStreak,ans)

    print(maxStreak)
        
    