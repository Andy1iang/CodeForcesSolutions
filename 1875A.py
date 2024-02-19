# https://codeforces.com/contest/1875/problem/A

for _ in range(int(input())):
    
    a, b, n = list(map(int, input().split()))
    tools = list(map(int, input().split()))
    
    total = b
    for t in tools:
        total += min(t,a-1)
        
    print(total)