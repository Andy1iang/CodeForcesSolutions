# https://codeforces.com/contest/41/problem/A

ber = input()
bir = input()

# doing it without reversed() or [::-1]
newBir = ''
for i in range(len(bir)):
    newBir += bir[len(bir)-i-1]

print('YES' if newBir == ber else 'NO')
