#https://codeforces.com/contest/1919/problem/B

from collections import Counter

for _ in range(int(input())):
    
    leng = int(input())
    
    chars = input()
    
    a = chars.count('-')
    b = chars.count('+')
    
    print(abs(a-b))
        