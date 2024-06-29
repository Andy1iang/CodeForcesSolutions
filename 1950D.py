# https://codeforces.com/contest/1950/problem/D

# using recursion to get all binary numbers under the limit
allBin = set()
def getBin(n):
    if n <= 100000:
        allBin.add(n)
        getBin(int(str(n) + '0'))
        getBin(int(str(n) + '1'))


getBin(1)
allBin.remove(1) # getting rid of 0

# looping through allBin to check if the input can be a product
for _ in range(int(input())):

    n = int(input())

    while n > 1:
        for i in allBin:
            if n % i == 0:
                n = n//i
                break
        else:
            break

    if n == 1:
        print('YES')
    else:
        print('NO')
