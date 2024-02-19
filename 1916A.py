#https://codeforces.com/contest/1916/problem/A

for _ in range(int(input())):
    
    leng, missing = list(map(int,input().split()))
    
    nums = list(map(int,input().split()))
    product = 1
    for i in nums:
        product *= i
        
    result = 2023/product
    
    if result%1 != 0:
        print('NO')
        continue
    
    ansList = [str(int(result))]
    
    ansList += ['1'] * (missing-1)
    
    print('YES')
    print(' '.join(ansList))