for _ in range(int(input())):
    
    leng = int(input())
    lst = list(map(int,input().split()))
    
    prev = [-1]
    for i in range(1,leng):
        if lst[i] == lst[i-1]:
            if prev[-1] == -1:
                prev.append(-1)
            else:
                prev.append(prev[-1]+1)
        else:
            prev.append(1)
            
    for i in range(int(input())):
        a, b = list(map(int,input().split()))
        if prev[b-1] == -1:
            print("-1 -1")
            continue
        if b - prev[b-1] >= a:
            print(f"{b-prev[b-1]} {b-prev[b-1]+1}")
        else:
            print("-1 -1")