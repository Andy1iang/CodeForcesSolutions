#https://codeforces.com/contest/1722/problem/C

for i in range(int(input())):
    words = int(input())
    person1 = input().split()
    person2 = input().split()
    person3 = input().split()
    
    wordCounts = {} #making a counter for each word and its occurrence frequency
    for word in person1+person2+person3:
        try:
            wordCounts[word] +=1
        except:
            wordCounts[word] = 1
        
    person1score, person2score, person3score = 0,0,0
    
    for i in range(words):
        if wordCounts[person1[i]] == 1:
            person1score += 3
        elif wordCounts[person1[i]] == 2:
            person1score += 1
            
        if wordCounts[person2[i]] == 1:
            person2score += 3
        elif wordCounts[person2[i]] == 2:
            person2score += 1
            
        if wordCounts[person3[i]] == 1:
            person3score += 3
        elif wordCounts[person3[i]] == 2:
            person3score += 1

    print (f'{person1score} {person2score} {person3score}')