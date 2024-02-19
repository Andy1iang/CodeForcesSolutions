#https://codeforces.com/contest/1914/problem/B

for _ in range(int(input())):
    
    length:int
    excited:int
    length, excited = list(map(int,input().split()))
    
    numList:list[int] = list(range(1,length+1))
    ansList:list[int] = []
    for i in range(excited):
        ansList.append(numList.pop())
        
    ansList += numList
    ansList.reverse()

    print(' '.join(list(map(str,ansList))))
    
    


    