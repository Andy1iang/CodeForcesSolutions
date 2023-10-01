#https://codeforces.com/contest/136/problem/A
#Understanding the problem: https://dev.to/rishitc/solving-codeforces-problem-136a-presents-246g

resList = [0]*int(input())

for idx,x in enumerate(input().split()):
    resList[int(x)-1] = str(idx+1)
    
print(' '.join(resList))