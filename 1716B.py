# https://codeforces.com/contest/1716/problem/B

for _ in range(int(input())):
    
    leng = int(input())
    print(leng)
    
    # starting with the ordered chain
    lst = list(range(1,leng+1))
    print(' '.join(list(map(str,lst)))) 
    
    # moving each number over in each iterations
    # the last iteration should result in [2, 3, 4, ..., 1]
    for i in range(leng-1):
        
        lst[i],lst[i+1] = lst[i+1],lst[i]
        
        print(' '.join(list(map(str,lst))))