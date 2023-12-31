#https://codeforces.com/contest/1915/problem/D

'''
Need to translate into C++ to be within the time limit (1000ms)
Have tried to use the appending to list approach, still exceeds the time limit on test 3
'''

for i in range(int(input())):
    
    leng:int = int(input())
    word:str = input()
    newWord:str = ''
    
    #looping through entire word, incrementing by 2 or 3
    j = 0 
    while j+3 < leng:
        
        #checking if the 3rd letter after current letter is a "consonant"
        if word[j+3] in 'bcd':
            #add 3 letters then a period if true, then increment by 3
            newWord+=(word[j:j+3])
            newWord+='.'
            j+=3
            
        else:
            #add 2 letters then a period if false, then increment by 2
            newWord+=(word[j:j+2])
            newWord+='.'
            j+=2
    
    newWord+=word[j:] #adding last piece of the word at the end (after the last period)
    
    print(newWord)