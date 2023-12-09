#https://codeforces.com/problemset/problem/131/A

word = input()

if len(word) == 1:
    if word.isupper():
        print(word.lower())
    else:
        print(word.upper())
    
else:
    if word.isupper():
        print(word.lower())
    elif word[1:].isupper():
        print(word[0].upper()+word[1:].lower())
    else:
        print(word)
        