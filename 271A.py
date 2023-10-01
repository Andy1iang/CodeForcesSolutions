#https://codeforces.com/contest/271/problem/A

year = input()
year = str(int(year)+1)

while len(set(year)) < 4: #checking if all numbers are distinct
    year = str(int(year)+1)
print(year)