# https://codeforces.com/contest/1950/problem/E

# getting all possible divisors of a number
def getDivs(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return sorted(divs)

# checking all possible substrings
# returning the results if case matched
for _ in range(int(input())):

    n = int(input())
    s = input()
    divs = getDivs(n)

    found = False

    for i in divs:
        for j in range(0, i+1, i):
            word = s[j:j+i]*(n//i)
            if sum(word[i] != s[i] for i in range(len(word))) <= 1:
                print(i)
                found = True
                break

        if found:
            break
