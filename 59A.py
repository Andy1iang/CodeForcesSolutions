#https://codeforces.com/contest/59/problem/A

word = input()
count = 0

for i in word:
    if i.isupper():
        count += 1
    else:
        count-=1
if count > 0:
    print(word.upper())
else:
    print(word.lower())