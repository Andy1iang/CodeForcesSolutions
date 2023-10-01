#https://codeforces.com/contest/118/problem/A

word = input().lower()
res = ''

for letter in word:
    if letter not in 'aeiouy':
        res += f'.{letter}'
        
print(res)