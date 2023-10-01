#https://codeforces.com/contest/1856/problem/B

'''
Lessons:
--Any number can be split (e.g. 3&3 and be 2&4); only 1&1 cannot be split
'''

for i in range(int(input())):
    
    length = int(input()) #length of array
    
    if length == 1: #always bad if length of array is 1
        input()
        print("NO")
        continue
    
    x = input().split() #splitting the array & turning values to ints
    for i in range(length):
        x[i] = int(x[i])
        
    total = sum(x)
    ones = x.count(1)
    
    if total >= ones+length: #bad array when sum is less than number of 1s plus length of array
        print("YES")
    else:
        print("NO")