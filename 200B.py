#https://codeforces.com/problemset/problem/200/B

input() #first input is not needed
sum = 0
drinks = input().split()
for drink in drinks:
    sum += int(drink)

print(sum/len(drinks))