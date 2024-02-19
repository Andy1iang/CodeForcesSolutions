# https://codeforces.com/contest/1716/problem/B

for _ in range(int(input())):
    
    leng = int(input())
    print(leng)
    
    lst = list(range(1,leng+1))
    print(' '.join(list(map(str,lst))))
    
    for i in range(leng-1):
        
        lst[i],lst[i+1] = lst[i+1],lst[i]
        
        print(' '.join(list(map(str,lst))))