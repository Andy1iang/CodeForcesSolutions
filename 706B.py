#https://codeforces.com/problemset/problem/706/B

'''
Learned:
Dynamic Programming: Prefix Sum
Calculating value and values of indexes before it, so each index does not need to be calculated each time
This problem could also be done with binary search (tweak a little to accommodate for x between 2 values)
'''

#taking input
shops = int(input())
prices = list(map(int,input().split()))
days = int(input())

#creating an array where each index represents the amount of shops at that price point
shopIdx = [0] * max(prices)
for i in prices:
    shopIdx[i-1] += 1

#creating an array where each index represents the amount of shops at that price or less
totalIdx = [0] * len(shopIdx)
totalIdx[0] = shopIdx[0]
for i in range(1,len(totalIdx)):
    totalIdx[i] = totalIdx[i-1] + shopIdx[i] #adding amount of shops for current price & amount of shops of all previous prices

#printing results for each input
for i in range(days):
    budget = int(input())-1
    if budget >= len(totalIdx): #if budget is larger than most expensive shop
        print(shops)
    else:     
        print(totalIdx[budget])