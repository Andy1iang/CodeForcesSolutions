# https://codeforces.com/contest/1915/problem/D

for i in range(int(input())):

    leng = int(input())
    word = list(input())
    newWord = []

    # looping through entire word, incrementing by 2 or 3
    j = 0
    while j+3 < leng:

        # checking if the 3rd letter after current letter is a "consonant"
        if word[j+3] == 'b' or word[j+3] == 'c' or word[j+3] == 'd':
            # add 3 letters then a period if true, then increment by 3
            newWord.append(word[j])
            newWord.append(word[j+1])
            newWord.append(word[j+2])
            newWord.append('.')
            j += 3

        else:
            # add 2 letters then a period if false, then increment by 2
            newWord.append(word[j])
            newWord.append(word[j+1])
            newWord.append('.')
            j += 2

    # adding last piece of the word at the end (after the last period)
    while j < leng:
        newWord.append(word[j])
        j += 1

    print(''.join(newWord))
