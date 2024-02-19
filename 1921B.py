#https://codeforces.com/contest/1921/problem/B

for _ in range(int(input())):
    
    boxes = int(input())
    initial = input()
    final = input()
    
    if initial.count('1') < final.count('1'):
        count = 0
        for top,bottom in zip(initial, final):
            if top == '0' and bottom == '1':
                count += 1
        
        print(count)
        
    else:
        count = 0
        for top,bottom in zip(initial, final):
            if top == '1' and bottom == '0':
                count += 1
        
        print(count)