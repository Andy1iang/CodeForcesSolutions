# https://codeforces.com/contest/1928/problem/A

for _ in range(int(input())):

    # mathing it out ;)
    
    a, b = list(map(int, input().split()))
    
    if a == 1 or b == 1:
        
        if (a <= 2 and b <= 2) or (a%2 != 0 and b%2 != 0):
            print('NO')
            
        else:
            print('YES')
            
    elif a == 2 or b == 2:
        print('YES')
        
    else:
        if a%2 != 0 and b%2 != 0:
            print('NO')
            
        elif a%2 != 0:
            if b//2 == a:
                print('NO')
            else:
                print('YES')
                
        elif b%2 != 0:
            if a//2 == b:
                print('NO')
            else:
                print('YES')
            
        else:
            print('YES')